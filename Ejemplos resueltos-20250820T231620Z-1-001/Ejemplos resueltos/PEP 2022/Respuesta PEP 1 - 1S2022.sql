-- 1) Espacializar y unir información de estaciones
-- 1.1) Georreferenciar estaciones de monitoreo
ALTER TABLE "Estaciones_concentracion" ADD COLUMN geom geometry(Point, 32719);
UPDATE "Estaciones_concentracion" SET geom = ST_MakePoint("Lon", "Lat");

-- crear índice espacial
SELECT AddGeometryColumn('Estaciones_concentracion', 'geom',32719, 'POINT', 'XY');
SELECT CreateSpatialIndex('Estaciones_concentracion', 'geom');


-- 1.2) Unir información de estaciones
create table estaciones as
select concentracion."AlxCan" as alxcan, 
		concentracion."PseudAus" as pseudaus,
		concentracion.geom as geom,
		celulas."AlxCan" as cual_alxcan,
		celulas."PseudAus" as cual_pseudaus
from "Estaciones_concentracion" as concentracion
inner join "Estaciones_celulas" as celulas
on concentracion. "Id_est" = celulas."Id_est";

-- crear índice espacial
SELECT AddGeometryColumn('estaciones', 'geom',32719, 'POINT', 'XY');
SELECT CreateSpatialIndex('estaciones', 'geom');

-- 2) Unir información de estaciones a consesiones

create table con_toxinas as
select con."Id_con", ST_MakePolygon(con."Geom") as geom, est.alxcan, est.pseudaus, est.cual_alxcan, est.pseudaus
from consesiones as con
join estaciones as est
on ST_Intersects(ST_MakePolygon(con."Geom"),est.geom);

-- crear índice espacial
SELECT AddGeometryColumn('con_toxinas', 'geom',32719, 'POLYGON', 'XY');
SELECT CreateSpatialIndex('con_toxinas', 'geom');

-- 3) Determinar estado de alerta
-- 3.1) Análisis cuantitativo y cualitativo
create table estado_alerta as
select con."Id_con", con.geom,
CASE
 	WHEN ((con.alxcan < 80 and con.alxcan > 30) and (con.pseudaus > 20) and (con.cual_alxcan > 15 or con.cual_pseudaus >50)) THEN 'VPM - VAM - AR'
 	WHEN ((con.alxcan < 80 and con.alxcan > 30) and (con.cual_alxcan > 15 or con.cual_pseudaus >50)) THEN 'VPM - AR'
 	WHEN ((con.pseudaus > 20) and (con.cual_alxcan > 15 or con.cual_pseudaus >50)) THEN 'AM - AR'
 	WHEN ((con.alxcan < 80 and con.alxcan > 30) and (con.pseudaus > 20)) THEN 'VPM - VAM'
 	WHEN (con.cual_alxcan > 15 or con.cual_pseudaus >50) THEN 'AR'
 	WHEN ((con.alxcan < 80 and con.alxcan > 30)) THEN 'VPM'
 	ELSE 'Sin Alerta'
END as alerta
from con_toxinas as con;

-- 3.2) Unir y pivotear produccion según tipo de producto para generar tabla maestra
-- suponiendo que existen tipos de moluscos [a y b] y bivalvos [c y d]
create table tabla_maestra as
select estal."Id_con" as id_con, estal.geom as geom,
		sum(mol."Ton_Mol") filter(where mol."Moluscos" = a) as ton_a,
		sum(mol."Ton_Mol") filter(where mol."Moluscos" = b) as ton_b,
		sum(biv."Ton_Biv") filter(where biv."Bivalvos" = c) as ton_c,
		sum(biv."Ton_Biv") filter(where biv."Bivalvos" = d) as ton_d,
		sum(sal."Ton_Sal") as ton_sal
from estado_alerta as estal 
inner join "Produccion_mol" as mol
on estal."Id_con" = mol."Id_con"
inner join "Produccion_biv" as biv
on estal."Id_con" = biv."Id_con"
inner join "Produccion_sal" as sal
on estal."Id_con" = sal."Id_con"
group by estal."Id_con"
where not estal.alerta = 'Sin Alerta';

-- crear índice espacial
SELECT AddGeometryColumn('tabla_maestra', 'geom',32719, 'POLYGON', 'XY');
SELECT CreateSpatialIndex('tabla_maestra', 'geom');

-- 4) Generar area de cierre donde se encuentre alerta
-- 4.1) Generar tabla auxiliar que contiene las geometrias
create table pol_dissolve as
select st_unaryunion(st_collect(tbl.geom)) as geom
from tabla_maestra as tbl;

-- crear índice espacial
SELECT AddGeometryColumn('pol_dissolve', 'geom',32719, 'POLYGON', 'XY');
SELECT CreateSpatialIndex('pol_dissolve', 'geom');

-- 4.2) Obtener coordenadas de extensión basado en X e Y min/max
create table area_cierre as
select ST_GeomFromText(concat('POLYGON((',aux.x_min,' ',aux.y_min,',',
						aux.x_max,' ',aux.y_min,',',
						aux.x_max,' ',aux.y_max,',',
						aux.x_min,' ',aux.y_max,',',
						aux.x_min,' ',aux.y_min,'))')) as geom -- otra forma es con "text" || "text"
from (SELECT st_xmax(geom) as x_max, 
				st_xmin(geom) as x_min, 
				st_ymax(geom) as y_max, 
				st_ymin(geom) as y_min
		from pol_dissolve as geom) 
		as aux;

-- crear índice espacial
SELECT AddGeometryColumn('area_cierre', 'geom',32719, 'POLYGON', 'XY');
SELECT CreateSpatialIndex('area_cierre', 'geom');

-- 4.3) Generar un buffer de 1.8 km
create table cierre_extent as
select ST_BUFFER(ac.geom, 1.8) as geom
from area_cierre as ac;

-- crear índice espacial
SELECT AddGeometryColumn('cierre_extent', 'geom',32719, 'POLYGON', 'XY');
SELECT CreateSpatialIndex('cierre_extent', 'geom');

-- 5) Intersectar area de cierre con concesiones y obtener datos de contingencia
create table resultado as
select *
from cierre_extent as extent
join tabla_maestra as tbl
on ST_Intersects(extent.geom,tbl.geom);

-- crear índice espacial
SELECT AddGeometryColumn('resultado', 'geom',32719, 'POLYGON', 'XY');
SELECT CreateSpatialIndex('resultado', 'geom');

/*
 La tabla Final se verá como
 
 id_con | geom | ton_a | ton_b | ton_c | ton_d | ton_sal
 1		| POL  |	123	|	23	|	43	|	5	| 0
 2		| POL  |	13	|	2	|	6	|	5	| 0
 3		| POL  |	0	|	0	|	0	|	0	| 0
 ..		| POL  |	..	|	..	|	..	|	..	| ..
 N		| POL  |	..	|	..	|	..	|	..	| ..
 */


-- 6) Limpiar resultados intermedios
DROP TABLE IF EXISTS estaciones;
DROP TABLE IF EXISTS con_toxinas;
DROP TABLE IF EXISTS estado_alerta;
DROP TABLE IF EXISTS tabla_maestra;
DROP TABLE IF EXISTS area_cierre;