# Guía de Migración OSMnx 1.x a 2.0

## Cambios Principales en la API

### 1. Configuración
**OSMnx 1.x:**
```python
ox.config(use_cache=True, log_console=True)
```

**OSMnx 2.0:**
```python
ox.settings.use_cache = True
ox.settings.log_console = True
```

### 2. Obtener Geometrías/Features
**OSMnx 1.x:**
```python
pois = ox.geometries_from_place(place, tags)
```

**OSMnx 2.0:**
```python
pois = ox.features_from_place(place, tags)
```

### 3. Utilidades de Grafo
**OSMnx 1.x:**
```python
nodes, edges = ox.utils_graph.graph_to_gdfs(G)
```

**OSMnx 2.0:**
```python
nodes, edges = ox.graph_to_gdfs(G)
```

### 4. Nodos Más Cercanos
**OSMnx 1.x:**
```python
node = ox.distance.nearest_nodes(G, x, y)
```

**OSMnx 2.0:**
```python
node = ox.nearest_nodes(G, x, y)
# Nota: Requiere scikit-learn para grafos no proyectados
```

## Dependencias Adicionales

OSMnx 2.0 requiere scikit-learn para algunas operaciones:
```bash
pip install scikit-learn
```

## Mejores Prácticas

### Proyección de Grafos
Para cálculos de distancia más precisos, proyecta el grafo:
```python
# Proyectar a UTM automáticamente
G_proj = ox.project_graph(G)

# Luego usar el grafo proyectado para cálculos
node = ox.nearest_nodes(G_proj, x, y)
```

### Manejo de Geometrías
OpenStreetMap puede retornar Points, Polygons o MultiPolygons:
```python
# Convertir polígonos a puntos (centroides)
if 'Polygon' in gdf.geometry.type.values:
    gdf['geometry'] = gdf.geometry.centroid
```

## Ejemplo Completo

```python
import osmnx as ox
import networkx as nx

# Configuración
ox.settings.use_cache = True
ox.settings.log_console = True

# Obtener red vial
G = ox.graph_from_place("Las Condes, Santiago, Chile", network_type='drive')

# Convertir a GeoDataFrame
nodes, edges = ox.graph_to_gdfs(G)

# Obtener POIs
pois = ox.features_from_place("Las Condes, Santiago, Chile", 
                              {'amenity': 'hospital'})

# Proyectar para cálculos precisos
G_proj = ox.project_graph(G)

# Encontrar nodo más cercano
node = ox.nearest_nodes(G_proj, lon, lat)

# Análisis de red (isócronas)
subgraph = nx.ego_graph(G_proj, node, radius=1000, distance='length')
```

## Ventajas de OSMnx 2.0

1. **API más consistente**: Funciones principales directamente en el módulo
2. **Mejor rendimiento**: Optimizaciones internas significativas
3. **Mejor manejo de proyecciones**: Soporte mejorado para CRS
4. **Más funcionalidades**: Nuevas herramientas de análisis
5. **Mejor documentación**: API más clara y ejemplos actualizados