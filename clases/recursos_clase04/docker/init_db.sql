-- Script de inicialización de base de datos PostGIS
-- Clase 04 - Pipeline de Desarrollo Geoespacial

-- Crear extensiones espaciales
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;
CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;
CREATE EXTENSION IF NOT EXISTS postgis_tiger_geocoder;

-- Crear schema para organizar tablas
CREATE SCHEMA IF NOT EXISTS geo_chile;
SET search_path TO geo_chile, public;

-- Tabla de regiones
CREATE TABLE IF NOT EXISTS regiones (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(10) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    capital VARCHAR(100),
    poblacion INTEGER,
    superficie_km2 DECIMAL(10,2),
    geom GEOMETRY(MultiPolygon, 4326)
);

-- Tabla de comunas
CREATE TABLE IF NOT EXISTS comunas (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(10) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    provincia VARCHAR(100),
    region_id INTEGER REFERENCES regiones(id),
    poblacion INTEGER,
    superficie_km2 DECIMAL(10,2),
    densidad_hab_km2 DECIMAL(10,2) GENERATED ALWAYS AS (poblacion / NULLIF(superficie_km2, 0)) STORED,
    geom GEOMETRY(MultiPolygon, 4326),
    centroid GEOMETRY(Point, 4326) GENERATED ALWAYS AS (ST_Centroid(geom)) STORED
);

-- Índices espaciales y de búsqueda
CREATE INDEX idx_regiones_geom ON regiones USING GIST(geom);
CREATE INDEX idx_comunas_geom ON comunas USING GIST(geom);
CREATE INDEX idx_comunas_centroid ON comunas USING GIST(centroid);
CREATE INDEX idx_comunas_nombre ON comunas(nombre);
CREATE INDEX idx_comunas_region ON comunas(region_id);

-- Tabla de propiedades (para ejemplos)
CREATE TABLE IF NOT EXISTS propiedades (
    id SERIAL PRIMARY KEY,
    direccion VARCHAR(255),
    comuna_id INTEGER REFERENCES comunas(id),
    tipo VARCHAR(50) CHECK (tipo IN ('casa', 'departamento', 'oficina', 'local', 'terreno')),
    precio_clp BIGINT,
    precio_uf DECIMAL(10,2),
    superficie_m2 DECIMAL(10,2),
    superficie_terreno_m2 DECIMAL(10,2),
    dormitorios INTEGER,
    banos INTEGER,
    estacionamientos INTEGER,
    ano_construccion INTEGER,
    fecha_publicacion DATE DEFAULT CURRENT_DATE,
    activo BOOLEAN DEFAULT TRUE,
    geom GEOMETRY(Point, 4326),
    CONSTRAINT precio_positivo CHECK (precio_clp > 0),
    CONSTRAINT superficie_positiva CHECK (superficie_m2 > 0)
);

-- Índices para propiedades
CREATE INDEX idx_propiedades_geom ON propiedades USING GIST(geom);
CREATE INDEX idx_propiedades_comuna ON propiedades(comuna_id);
CREATE INDEX idx_propiedades_tipo ON propiedades(tipo);
CREATE INDEX idx_propiedades_precio ON propiedades(precio_uf);
CREATE INDEX idx_propiedades_activo ON propiedades(activo) WHERE activo = TRUE;

-- Tabla de amenidades (hospitales, colegios, metro, etc)
CREATE TABLE IF NOT EXISTS amenidades (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255),
    tipo VARCHAR(50),
    subtipo VARCHAR(50),
    direccion VARCHAR(255),
    comuna_id INTEGER REFERENCES comunas(id),
    telefono VARCHAR(20),
    email VARCHAR(100),
    sitio_web VARCHAR(255),
    horario_apertura TIME,
    horario_cierre TIME,
    capacidad INTEGER,
    geom GEOMETRY(Point, 4326)
);

CREATE INDEX idx_amenidades_geom ON amenidades USING GIST(geom);
CREATE INDEX idx_amenidades_tipo ON amenidades(tipo);
CREATE INDEX idx_amenidades_comuna ON amenidades(comuna_id);

-- Tabla de red vial
CREATE TABLE IF NOT EXISTS calles (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255),
    tipo VARCHAR(50),
    velocidad_max INTEGER,
    sentido VARCHAR(20),
    comuna_id INTEGER REFERENCES comunas(id),
    longitud_m DECIMAL(10,2),
    geom GEOMETRY(LineString, 4326)
);

CREATE INDEX idx_calles_geom ON calles USING GIST(geom);
CREATE INDEX idx_calles_nombre ON calles(nombre);
CREATE INDEX idx_calles_comuna ON calles(comuna_id);

-- Vista materializada: Estadísticas por comuna
CREATE MATERIALIZED VIEW IF NOT EXISTS mv_estadisticas_comuna AS
SELECT 
    c.id,
    c.nombre,
    c.poblacion,
    c.superficie_km2,
    c.densidad_hab_km2,
    COUNT(DISTINCT p.id) as total_propiedades,
    AVG(p.precio_uf) as precio_promedio_uf,
    MIN(p.precio_uf) as precio_min_uf,
    MAX(p.precio_uf) as precio_max_uf,
    AVG(p.superficie_m2) as superficie_promedio_m2,
    COUNT(DISTINCT a.id) FILTER (WHERE a.tipo = 'hospital') as hospitales,
    COUNT(DISTINCT a.id) FILTER (WHERE a.tipo = 'colegio') as colegios,
    COUNT(DISTINCT a.id) FILTER (WHERE a.tipo = 'metro') as estaciones_metro
FROM comunas c
LEFT JOIN propiedades p ON c.id = p.comuna_id AND p.activo = TRUE
LEFT JOIN amenidades a ON c.id = a.comuna_id
GROUP BY c.id, c.nombre, c.poblacion, c.superficie_km2, c.densidad_hab_km2;

CREATE UNIQUE INDEX idx_mv_estadisticas_comuna_id ON mv_estadisticas_comuna(id);

-- Función: Buscar propiedades cercanas a un punto
CREATE OR REPLACE FUNCTION buscar_propiedades_cercanas(
    lat FLOAT,
    lon FLOAT,
    radio_metros FLOAT DEFAULT 1000,
    limite INTEGER DEFAULT 10,
    tipo_propiedad VARCHAR DEFAULT NULL
)
RETURNS TABLE (
    id INTEGER,
    direccion VARCHAR,
    tipo VARCHAR,
    precio_uf DECIMAL,
    superficie_m2 DECIMAL,
    distancia_metros FLOAT,
    comuna VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        p.id,
        p.direccion,
        p.tipo,
        p.precio_uf,
        p.superficie_m2,
        ST_Distance(
            p.geom::geography,
            ST_SetSRID(ST_MakePoint(lon, lat), 4326)::geography
        ) as distancia_metros,
        c.nombre as comuna
    FROM propiedades p
    JOIN comunas c ON p.comuna_id = c.id
    WHERE p.activo = TRUE
        AND ST_DWithin(
            p.geom::geography,
            ST_SetSRID(ST_MakePoint(lon, lat), 4326)::geography,
            radio_metros
        )
        AND (tipo_propiedad IS NULL OR p.tipo = tipo_propiedad)
    ORDER BY distancia_metros
    LIMIT limite;
END;
$$ LANGUAGE plpgsql;

-- Función: Calcular estadísticas de área de influencia
CREATE OR REPLACE FUNCTION calcular_area_influencia(
    punto_geom GEOMETRY,
    radio_metros FLOAT
)
RETURNS TABLE (
    total_poblacion INTEGER,
    densidad_promedio FLOAT,
    num_propiedades INTEGER,
    precio_promedio_uf FLOAT,
    amenidades_cercanas INTEGER
) AS $$
DECLARE
    buffer_geom GEOMETRY;
BEGIN
    -- Crear buffer
    buffer_geom := ST_Buffer(punto_geom::geography, radio_metros)::geometry;
    
    RETURN QUERY
    SELECT 
        COALESCE(SUM(c.poblacion * ST_Area(ST_Intersection(c.geom, buffer_geom)) / ST_Area(c.geom)), 0)::INTEGER as total_poblacion,
        AVG(c.densidad_hab_km2) as densidad_promedio,
        COUNT(DISTINCT p.id)::INTEGER as num_propiedades,
        AVG(p.precio_uf) as precio_promedio_uf,
        COUNT(DISTINCT a.id)::INTEGER as amenidades_cercanas
    FROM comunas c
    LEFT JOIN propiedades p ON ST_Intersects(p.geom, buffer_geom) AND p.activo = TRUE
    LEFT JOIN amenidades a ON ST_Intersects(a.geom, buffer_geom)
    WHERE ST_Intersects(c.geom, buffer_geom);
END;
$$ LANGUAGE plpgsql;

-- Función: Geocodificar dirección (simplificada)
CREATE OR REPLACE FUNCTION geocodificar_direccion(
    direccion_input VARCHAR,
    comuna_nombre VARCHAR
)
RETURNS GEOMETRY AS $$
DECLARE
    comuna_geom GEOMETRY;
    punto_random GEOMETRY;
BEGIN
    -- Obtener geometría de la comuna
    SELECT geom INTO comuna_geom 
    FROM comunas 
    WHERE LOWER(nombre) = LOWER(comuna_nombre)
    LIMIT 1;
    
    IF comuna_geom IS NULL THEN
        RETURN NULL;
    END IF;
    
    -- Por simplicidad, retornar punto random dentro de la comuna
    -- En producción, usar servicio real de geocoding
    SELECT ST_GeneratePoints(comuna_geom, 1) INTO punto_random;
    
    RETURN ST_GeometryN(punto_random, 1);
END;
$$ LANGUAGE plpgsql;

-- Crear roles y permisos
CREATE ROLE geo_reader;
GRANT USAGE ON SCHEMA geo_chile TO geo_reader;
GRANT SELECT ON ALL TABLES IN SCHEMA geo_chile TO geo_reader;

CREATE ROLE geo_writer;
GRANT USAGE ON SCHEMA geo_chile TO geo_writer;
GRANT ALL ON ALL TABLES IN SCHEMA geo_chile TO geo_writer;
GRANT ALL ON ALL SEQUENCES IN SCHEMA geo_chile TO geo_writer;

-- Asignar permisos al usuario de la aplicación
GRANT geo_writer TO geouser;

-- Mensaje de confirmación
DO $$
BEGIN
    RAISE NOTICE 'Base de datos geoespacial inicializada correctamente';
    RAISE NOTICE 'Esquema: geo_chile';
    RAISE NOTICE 'Tablas creadas: regiones, comunas, propiedades, amenidades, calles';
    RAISE NOTICE 'Funciones disponibles: buscar_propiedades_cercanas, calcular_area_influencia, geocodificar_direccion';
END $$;