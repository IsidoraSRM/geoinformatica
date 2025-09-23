# Manual del Profesor - Clase 02: Fundamentos de Geocomputación
## Duración: 80 minutos | Jueves (Primera sesión teórica)

---

## 📋 PREPARACIÓN PREVIA (15 minutos antes de clase)

### Checklist de materiales:
- [ ] Presentación PDF cargada y probada
- [ ] Computador con Python y R instalados para demos
- [ ] Conexión a internet estable
- [ ] Pizarra y plumones para diagramas adicionales
- [ ] Links de recursos listos para compartir
- [ ] Verificar proyector/pantalla
- [ ] Tener agua para hidratarse

### Configuración técnica:
```bash
# Terminal 1: Python listo
cd ~/demos_clase02
source geo_env/bin/activate
jupyter notebook

# Terminal 2: R listo  
R
# Pre-cargar bibliotecas para ahorrar tiempo
library(sf)
library(tmap)
```

### Archivos de ejemplo preparados:
- `santiago_comunas.shp` - Shapefile de comunas de Santiago
- `world_data.json` - Datos mundiales para demos
- `demo_script.py` - Script de ejemplo funcionando

---

## 🎯 OBJETIVOS DE APRENDIZAJE

Al finalizar esta clase, los estudiantes serán capaces de:
1. **Comprender** la evolución histórica desde SIG hasta Geocomputación
2. **Identificar** las principales herramientas de software geoespacial
3. **Comparar** las fortalezas de Python vs R para análisis espacial
4. **Ejecutar** un primer script geoespacial básico

---

## 📚 GUIÓN DETALLADO DE LA CLASE

### **[0:00-0:02] INICIO - Slide 1: Portada**

**DECIR:**
"Buenos días a todos. Bienvenidos a nuestra segunda clase de Geoinformática. Hoy vamos a profundizar en los fundamentos de la Geocomputación, su historia, y las herramientas que usaremos durante todo el semestre."

**HACER:**
- Sonreír y hacer contacto visual con los estudiantes
- Verificar que todos pueden ver la presentación

---

### **[0:02-0:03] Slide 2: Agenda**

**DECIR:**
"Tenemos 80 minutos muy bien aprovechados. Vamos a cubrir 4 grandes temas: primero la historia y evolución de la geocomputación, luego el panorama actual del software, después nos enfocaremos en los ecosistemas de Python y R que son nuestras herramientas principales, y terminaremos con ejemplos prácticos que los prepararán para el laboratorio."

**TRANSICIÓN:**
"Pero antes de comenzar, hagamos un breve repaso..."

---

### **[0:03-0:06] Slide 3: Repaso clase anterior**

**DECIR:**
"En nuestra primera clase definimos qué es la Geocomputación. ¿Alguien recuerda la diferencia entre datos vectoriales y raster?"

**ESPERAR RESPUESTA (30 seg)**

**COMPLEMENTAR:**
"Exacto, vectorial son puntos, líneas y polígonos con coordenadas precisas, mientras que raster son grillas de celdas, como píxeles. Esto es fundamental porque cada tipo requiere diferentes herramientas y técnicas."

**PREGUNTA INTERACTIVA:**
"¿Quién ya instaló Python o R? Levanten la mano... Excelente, los que no, recuerden que es urgente para el laboratorio de hoy."

**TRANSICIÓN:**
"Ahora sí, comencemos con nuestra historia..."

---

## 📖 SECCIÓN 1: HISTORIA Y EVOLUCIÓN (20 minutos)

### **[0:06-0:09] Slide 4: Los precursores**

**DECIR:**
"La historia de la Geocomputación no comienza con computadores. Comienza en 1854 con un médico llamado John Snow en Londres."

**NARRAR LA HISTORIA:**
"Londres estaba sufriendo una epidemia de cólera. La teoría predominante era que se transmitía por 'miasmas' o aire contaminado. Pero Snow tenía otra hipótesis. Creó un mapa marcando cada muerte por cólera con un punto. ¿Y qué descubrió? Que todos los casos se agrupaban alrededor de una bomba de agua en Broad Street."

**DIBUJAR EN PIZARRA:**
[Hacer un esquema simple del mapa de Snow con X marcando casos y un círculo para el pozo]

**ENFATIZAR:**
"Este fue el primer análisis espacial documentado. Sin computadores, Snow demostró que el espacio importa. Que la ubicación puede revelar patrones invisibles de otra forma."

**CONEXIÓN ACTUAL:**
"¿Les suena familiar? Es exactamente lo que hicimos con COVID-19 en 2020, pero ahora con millones de datos y en tiempo real."

---

### **[0:09-0:13] Slide 5: La era de los SIG**

**SEÑALAR EL TIMELINE:**
"Miren esta línea de tiempo. 1963 es un año clave: nace CGIS en Canadá, el primer SIG operacional del mundo."

**CONTEXTO HISTÓRICO:**
"¿Por qué Canadá? Tienen el segundo país más grande del mundo. Necesitaban inventariar sus recursos naturales. Imaginen mapear millones de hectáreas de bosque a mano... imposible."

**EXPLICAR CGIS:**
"CGIS podía hacer algo revolucionario: superponer capas de información. Una capa de suelos, otra de vegetación, otra de hidrología, y encontrar las intersecciones. Esto que hoy hacemos en segundos, tomaba horas en mainframes del tamaño de esta sala."

**DATO CURIOSO:**
"El sistema costó 15 millones de dólares de 1960. Ajustado por inflación, serían como 150 millones de hoy. Por eso solo gobiernos y grandes empresas podían tener SIG."

**MENCIONAR ESRI:**
"En 1969, Jack Dangermond funda ESRI en California. Empezó en su garage, hoy es una empresa de 2 billones de dólares. Su producto ArcGIS sigue siendo el estándar de la industria."

---

### **[0:13-0:17] Slide 6: El nacimiento de la Geocomputación**

**CAMBIO DE TONO (más filosófico):**
"Ahora, aquí viene lo interesante. En los 90s, había una sensación de que los SIG se habían estancado. Eran buenos para mapear, pero ¿y para entender procesos? ¿Para predecir? ¿Para simular?"

**LEER LA CITA:**
"Stan Openshaw, un geógrafo británico brillante, lo dijo mejor: 'Geocomputation is about using the various different types of geodata and about developing relevant geo-tools within an intelligent IT framework'."

**EXPLICAR LA DIFERENCIA:**
"Déjenme ponerlo simple:
- **SIG tradicional:** ¿Dónde está el hospital más cercano?
- **Geocomputación:** ¿Dónde debería construir el próximo hospital para optimizar el acceso considerando el crecimiento poblacional proyectado, las rutas de transporte futuras, y minimizando el costo?"

**EJEMPLO CONCRETO:**
"Los SIG te dicen DÓNDE están los incendios forestales. La Geocomputación PREDICE dónde será el próximo y cómo se propagará."

**TÉCNICAS NUEVAS (mencionar rápido):**
- "Autómatas celulares: cada celda evoluciona según sus vecinos"
- "Redes neuronales: el computador aprende patrones espaciales"
- "Algoritmos genéticos: evolución de soluciones óptimas"

---

### **[0:17-0:21] Slide 7: La revolución Web GIS**

**MOMENTO "WOW":**
"El 8 de febrero de 2005 cambió todo. Google lanza Google Maps. De repente, mi abuela podía hacer análisis espacial sin saberlo."

**MOSTRAR CON LAS MANOS:**
"Antes: Necesitabas software de $5000, training de semanas, datos que costaban miles de dólares.
Después: Abres un navegador, gratis, intuitivo, datos incluidos."

**IMPACTO EN CHILE:**
"¿Saben que el terremoto del 27F en 2010 fue uno de los primeros desastres mapeados colaborativamente? Voluntarios de todo el mundo usaron OpenStreetMap para mapear zonas afectadas en tiempo real. El gobierno chileno usó esos mapas para coordinar la ayuda."

**DATO TÉCNICO:**
"La tecnología clave fue AJAX - Asynchronous JavaScript and XML. Permitió cargar tiles de mapas sin recargar toda la página. Parece simple ahora, pero fue revolucionario."

---

### **[0:21-0:26] Slide 8: Era actual - Big Data y AI**

**MOSTRAR EL GRÁFICO:**
"Miren este crecimiento exponencial. En 2010: 0.5 petabytes de datos geoespaciales al año. 2025: 200 petabytes. ¡400 veces más!"

**CONTEXTUALIZAR:**
"¿Qué es un petabyte? Si un gigabyte fuera un segundo, un petabyte serían 31 años."

**FUENTES DE DATOS:**
"¿De dónde vienen estos datos?
- **Sentinel-2:** Fotografía toda la Tierra cada 5 días. 1.5 TB diarios.
- **Smartphones:** 5 billones de dispositivos generando ubicaciones.
- **IoT:** Sensores en todas partes. Santiago tiene 500+ sensores de calidad del aire.
- **Drones:** Un solo vuelo LiDAR puede generar 100 GB."

**EJEMPLO CHILE:**
"La plataforma IDE Chile integra más de 50 servicios. Pueden ver desde mapas geológicos hasta zonas de riesgo de tsunami, todo integrado. Hace 10 años, conseguir estos datos tomaba semanas de papeleo."

**PROVOCAR REFLEXIÓN:**
"La pregunta ya no es '¿dónde consigo datos?' sino '¿cómo proceso tanta información?' Y ahí es donde entran las herramientas que veremos ahora..."

---

## 💻 SECCIÓN 2: SOFTWARE PARA ANÁLISIS (20 minutos)

### **[0:26-0:29] Slide 9: Panorama del software**

**EXPLICAR EL DIAGRAMA:**
"Este diagrama es clave. En el eje X tenemos facilidad de uso, en el Y capacidad analítica."

**SEÑALAR CADA SOFTWARE:**
- "Google Earth: Fácil, pero limitado. Perfecto para exploración."
- "QGIS: Buen balance. Por eso lo usaremos."
- "Python/R: Difícil al principio, pero poder ilimitado."
- "PostGIS: Para los valientes. Máximo poder, máxima complejidad."

**ANALOGÍA:**
"Es como herramientas de un mecánico:
- Google Earth = Destornillador básico
- QGIS = Caja de herramientas completa
- Python/R = Taller profesional
- PostGIS = Fábrica de herramientas"

---

### **[0:29-0:33] Slide 10: Software Desktop GIS**

**COMENZAR CON PREGUNTA:**
"¿Quién ha escuchado de QGIS? ¿Y de ArcGIS?"

**HISTORIA DE QGIS:**
"QGIS nació en 2002 como 'Quantum GIS'. Un desarrollador, Gary Sherman, estaba frustrado con el costo de ArcGIS. Decidió crear una alternativa libre. Hoy tiene millones de usuarios."

**VENTAJAS QGIS:**
"¿Por qué QGIS para el curso?
1. **Gratis:** No hay excusa para no practicar en casa
2. **Multiplataforma:** Windows, Mac, Linux, da igual
3. **Plugins:** Más de 1000. Hay un plugin para TODO
4. **Python integration:** Pueden automatizar cualquier cosa"

**SOBRE ARCGIS:**
"No voy a mentirles. ArcGIS Pro es más pulido, más estable, mejor documentado. Pero cuesta $700/año para estudiantes, $3000/año profesional. Y solo funciona en Windows."

**CONSEJO PROFESIONAL:**
"En mi experiencia, 95% de los análisis se pueden hacer igual en QGIS. El 5% restante... probablemente no lo necesiten hasta ser especialistas."

---

### **[0:33-0:36] Slide 11: Comparación QGIS vs ArcGIS**

**REPASAR LA TABLA:**
"Veamos la comparación punto por punto..."

**ANÉCDOTA PERSONAL:**
"Yo trabajé años con ArcGIS. Cuando cambié a QGIS, esperaba limitaciones graves. ¿Saben qué encontré? Que QGIS hace algunas cosas MEJOR. Por ejemplo, maneja formatos open source nativamente, mientras ArcGIS a veces tiene problemas."

**PUNTO IMPORTANTE:**
"'Cloud Integration' - ArcGIS Online es impresionante, lo admito. Pero cuesta. QGIS + GitHub + Leaflet puede lograr resultados similares gratis."

**PREDICCIÓN:**
"Mi predicción: en 5 años, la diferencia será mínima. El open source está cerrando la brecha rápidamente."

---

### **[0:36-0:40] Slide 12: Plataformas Cloud**

**INTRODUCIR CON IMPACTO:**
"Google Earth Engine procesa 40 años de imágenes satelitales en segundos. En mi doctorado, eso hubiera tomado meses."

**EXPLICAR GEE:**
"Earth Engine no es solo almacenamiento. Es procesamiento distribuido. Escribes 10 líneas de JavaScript, y Google moviliza miles de servidores para tu análisis."

**DEMO RÁPIDO (si hay internet):**
[Abrir code.earthengine.google.com]
"Miren, puedo calcular la pérdida de bosque en todo Chile en... 5 segundos."

**MICROSOFT PLANETARY COMPUTER:**
"Microsoft está siendo agresivo. Planetary Computer es su respuesta a GEE. Dato: tienen TODA la constelación Sentinel gratis."

**AWS:**
"Amazon es diferente. No te dan herramientas específicas GIS. Te dan poder computacional crudo. Es como la diferencia entre comprar un auto y comprar las piezas para armarlo."

**PREGUNTA A LA CLASE:**
"¿Cuál creen que es el problema del cloud? [Esperar respuestas] Exacto: dependencia y costos ocultos. Gratis al principio, caro cuando escalas."

---

### **[0:40-0:44] Slide 13: Bases de Datos Espaciales**

**COMENZAR CON PROBLEMA:**
"Imaginen que Uber les pide: 'Encuentra el conductor más cercano a este cliente'. Tienen 10,000 conductores activos en Santiago. ¿Calculan la distancia a cada uno? ¡Tomaría segundos! Inaceptable."

**SOLUCIÓN:**
"PostGIS usa índices espaciales R-tree. Divide el espacio en rectángulos jerárquicos. Encuentra al conductor más cercano en milisegundos."

**MOSTRAR QUERY SQL:**
```sql
SELECT nombre, ST_Area(geom)/10000 as hectareas
FROM parcelas
WHERE ST_Within(geom, (SELECT geom FROM comunas WHERE nombre='Santiago'))
```

**EXPLICAR LÍNEA POR LÍNEA:**
- "SELECT: qué quiero"
- "ST_Area: función espacial, calcula área"
- "/10000: conversión a hectáreas"
- "ST_Within: predicado espacial, 'está dentro de'"
- "Subquery: encuentra el polígono de Santiago"

**DATO IMPRESIONANTE:**
"PostGIS puede manejar billones de geometrías. La NASA lo usa para catálogos de estrellas."

---

### **[0:44-0:46] Slide 14: Herramientas CLI**

**INTRODUCCIÓN PRÁCTICA:**
"GDAL es como el cuchillo suizo del GIS. No es bonito, pero es increíblemente poderoso."

**EJEMPLO REAL:**
"El viernes pasado, un colega tenía 500 archivos TIFF que convertir a PNG. En QGIS: 2 horas clicking. Con GDAL:"

```bash
for file in *.tif; do
    gdal_translate -of PNG $file ${file%.tif}.png
done
```
"5 minutos. Incluyendo el café."

**CUÁNDO USAR GDAL:**
- "Conversiones masivas"
- "Reproyecciones batch"
- "Cuando QGIS crashea con archivos grandes"
- "Automatización en servidores"

**TIP PRO:**
"Si trabajan con GIS profesionalmente, GDAL les ahorrará cientos de horas. Garantizado."

---

## 🐍 SECCIÓN 3: ECOSISTEMA PYTHON Y R (25 minutos)

### **[0:46-0:49] Slide 15: ¿Por qué programar GIS?**

**PREGUNTA PROVOCADORA:**
"¿Cuántos clicks hicieron en el último trabajo que entregaron? ¿100? ¿500?"

**EJEMPLO DRAMÁTICO:**
"Caso real de consultoría: Cliente necesitaba análisis mensual de 100 comunas. Manual: 2 días. Script Python: 10 minutos. Después de 3 meses, el script había ahorrado 35 días de trabajo."

**MOSTRAR EL DIAGRAMA:**
"8 horas vs 10 minutos. Pero eso no es lo mejor..."

**LO MEJOR:**
"Reproducibilidad. Cuando el cliente dice 'oops, los datos estaban mal', no lloras. Ejecutas el script de nuevo."

**REGLA DE ORO:**
"Si lo haces más de 3 veces → automatízalo. No es pereza, es eficiencia."

---

### **[0:49-0:54] Slide 16: Ecosistema Python**

**EXPLICAR EL DIAGRAMA:**
"Python es como LEGO. Cada biblioteca es una pieza que encaja perfectamente."

**RECORRER BIBLIOTECAS:**

**GeoPandas (el corazón):**
"GeoPandas es pandas + geografía. Si saben pandas, ya saben 70% de geopandas."

**Ejemplo mental:**
```python
# Pandas normal
df[df['poblacion'] > 100000]

# GeoPandas
gdf[gdf['poblacion'] > 100000].plot()
# ¡Boom! Mapa filtrado
```

**Shapely (la geometría):**
"Shapely maneja geometrías puras. No sabe de proyecciones ni archivos, solo formas."

**Rasterio (los píxeles):**
"Para imágenes satelitales. Nombre gracioso: 'Raster I/O' = rasterio."

**Folium (los mapas web):**
"De Python a mapa web en 3 líneas. En serio, 3 líneas."

**CONSEJO:**
"No intenten aprender todas de una vez. GeoPandas + Folium = 80% de sus necesidades."

---

### **[0:54-0:58] Slide 17: Ejemplo Python**

**PREPARAR:**
"Voy a ejecutar este código en vivo. Si falla, es culpa del WiFi, no de Python."

**EJECUTAR LÍNEA POR LÍNEA:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
```

**EXPLICAR:**
"Importamos las herramientas. Como sacar las herramientas del cajón."

```python
comunas = gpd.read_file('santiago_comunas.shp')
```

**MOSTRAR:**
"Un shapefile, directamente a un DataFrame. Miren:"

```python
print(comunas.head())
print(f"CRS: {comunas.crs}")
```

**CREAR HOSPITALES:**
```python
hospitales = gpd.GeoDataFrame(
    {'nombre': ['Hospital 1', 'Hospital 2'],
     'geometry': [Point(-70.65, -33.45), 
                  Point(-70.60, -33.42)]},
    crs='EPSG:4326')
```

**EXPLICAR:**
"Creamos datos desde cero. EPSG:4326 = WGS84, el sistema de GPS."

**BUFFER Y ANÁLISIS:**
```python
areas_servicio = hospitales.buffer(0.02)  # ~2km
comunas_servidas = comunas[comunas.intersects(areas_servicio.unary_union)]
```

**RESULTADO:**
"¡Miren! Identificamos qué comunas tienen cobertura hospitalaria en 2 líneas."

**SI HAY TIEMPO:**
"¿Quieren ver el mapa?" [Generar visualización]

---

### **[0:58-1:03] Slide 18: Ecosistema R**

**TRANSICIÓN:**
"Ahora R. R es diferente. Fue creado por estadísticos, para estadísticos."

**FILOSOFÍA DE R:**
"R trata todo como datos para analizar. Python trata todo como objetos para procesar. Sutil pero importante diferencia."

**SF (Simple Features):**
"'sf' revolucionó R spatial. Antes era un desastre con 'sp'. Ahora es elegante."

**Diferencia clave:**
"En R, los datos espaciales son data frames normales con una columna especial 'geometry'. Genial para análisis estadístico."

**Terra vs Raster:**
"'terra' reemplazó a 'raster'. Es 10x más rápido. Si ven tutoriales con 'raster', búsquenlos con 'terra'."

**Tmap (la joya):**
"'tmap' es increíble para mapas temáticos. Hace mapas nivel publicación con código mínimo."

---

### **[1:03-1:07] Slide 19: Ejemplo R**

**EJECUTAR EN R:**

```r
library(sf)
library(tmap)
library(dplyr)
```

**COMPARAR CON PYTHON:**
"Noten algo: R usa <- para asignación, Python usa =. Pequeñas diferencias."

```r
comunas <- st_read("santiago_comunas.shp")
```

**PIPE OPERATOR:**
```r
comunas %>%
  filter(poblacion > 100000) %>%
  select(nombre, poblacion)
```

**EXPLICAR:**
"El %>% (pipe) es mágico. Lee el código como una receta: toma comunas, LUEGO filtra, LUEGO selecciona."

**VISUALIZACIÓN:**
```r
tm_shape(comunas) + 
  tm_polygons("poblacion", palette = "Blues") +
  tm_layout(title = "Población por Comuna")
```

**MOSTRAR RESULTADO:**
"Miren la calidad del mapa. Listo para publicación."

---

### **[1:07-1:11] Slide 20: Python vs R**

**PREGUNTA CLAVE:**
"La pregunta del millón: ¿Python o R?"

**RESPUESTA HONESTA:**
"Depende. Y no es respuesta diplomática."

**CUÁNDO PYTHON:**
- "Integración con aplicaciones web"
- "Deep Learning (TensorFlow, PyTorch)"
- "Cuando ya saben Python"
- "Pipelines de producción"

**CUÁNDO R:**
- "Análisis estadístico espacial complejo"
- "Visualización para publicaciones"
- "Investigación académica"
- "Cuando trabajan con estadísticos"

**MI RECOMENDACIÓN:**
"Aprendan ambos, pero empiecen con el que les sea más natural. En este curso, 60% Python porque es más versátil para ingeniería."

**SECRETO:**
"Los profesionales usan ambos. Python para producción, R para exploración."

---

## 🚀 SECCIÓN 4: EJEMPLOS PRÁCTICOS (15 minutos)

### **[1:11-1:14] Slide 21: Flujo de trabajo típico**

**EXPLICAR EL DIAGRAMA:**
"Este es el flujo que seguirán en CADA proyecto."

**PASO 1 - DATOS:**
"APIs, web scraping, archivos. Ejemplo: Datos COVID del MINSAL, tienen API REST."

**PASO 2 - LIMPIEZA:**
"80% del tiempo. Datos sucios = análisis basura. Fechas mal formateadas, coordenadas en sistema incorrecto, valores null..."

**PASO 3 - ANÁLISIS:**
"La parte divertida. Aquí aplican geocomputación."

**PASO 4 - VISUALIZACIÓN:**
"Un mapa vale más que mil tablas."

**PASO 5 - MODELADO:**
"Predicción, optimización, simulación."

**PASO 6 - COMPARTIR:**
"GitHub, web app, reporte. Código sin documentación es inútil."

---

### **[1:14-1:19] Slide 22: Caso COVID-19**

**CONTEXTUALIZAR:**
"Marzo 2020. Primer caso COVID en Chile. Necesitamos entender la propagación."

**DATOS:**
"MINSAL publicaba datos diarios. Problema: por comuna, no georeferenciados."

**SOLUCIÓN PASO A PASO:**

1. **"Join espacial:** Unir datos COVID con shapefile comunas"
2. **"Normalización:** Casos/población * 100,000 = tasa incidencia"
3. **"Autocorrelación:** Moran's I = 0.7, alta correlación espacial"
4. **"Clusters:** Las Condes, Vitacura, Providencia = primer cluster"
5. **"Predicción:** Modelo SIR espacial predijo expansión a Ñuñoa"

**RESULTADO:**
"El modelo predijo correctamente 8 de 10 comunas siguientes. Información crucial para asignar recursos."

**LECCIÓN:**
"Geocomputación puede salvar vidas. Literalmente."

---

### **[1:19-1:22] Slide 23: Demo configuración**

**ACCIÓN:**
"Abramos terminal. Voy a mostrar exactamente lo que haremos en el lab."

**VERIFICAR PYTHON:**
```bash
python --version
# Python 3.9.7 ✓
```

**CREAR AMBIENTE:**
```bash
python -m venv geo_env
source geo_env/bin/activate
```

**EXPLICAR:**
"Ambiente virtual = carpeta aislada. No contamina su Python sistema."

**INSTALAR:**
```bash
pip install geopandas folium matplotlib jupyter
```

**SI FALLA:**
"En Windows, a veces fiona da problemas. Solución: usar conda en lugar de pip."

---

### **[1:22-1:26] Slide 24: Primer script completo**

**COPIAR SCRIPT:**
"Les voy a compartir este script. Es su plantilla base."

**EJECUTAR Y EXPLICAR:**
[Ejecutar el script línea por línea, mostrando resultados intermedios]

**DESTACAR:**
- "get_path('naturalearth_lowres') - datos de ejemplo incluidos"
- "figsize=(15,8) - tamaño en pulgadas"
- "cmap='YlOrRd' - Yellow-Orange-Red, paleta secuencial"
- "tight_layout() - evita que se corten labels"

**RESULTADO:**
[Mostrar los dos mapas generados]

**TAREA MENTAL:**
"¿Qué patterns ven? ¿Por qué Brasil tiene tanto PIB pero no per cápita?"

---

## 🎯 PREPARACIÓN Y CIERRE (10 minutos)

### **[1:26-1:29] Slide 25: Laboratorio 1**

**EXPECTATIVAS:**
"El laboratorio es hands-on. Traigan paciencia, las instalaciones pueden ser frustrantes."

**PROBLEMAS COMUNES:**
1. "Windows: Permisos de admin"
2. "Mac: Xcode tools necesarios"
3. "Linux: Generalmente sin problemas"

**ESTRATEGIA:**
"Trabajen en parejas. Si uno tiene problemas, el otro puede ayudar."

**META:**
"Todos salen del lab con un mapa de Chile funcionando."

---

### **[1:29-1:32] Slide 26: Recursos**

**LIBROS:**
"Geocomputation with Python es GRATIS y EXCELENTE. Capítulo 1 para la próxima semana."

**COMUNIDADES:**
"Stack Overflow tag 'gis' tiene 50,000+ preguntas respondidas."

**YOUTUBE:**
"GeoDelta Labs - canal mexicano, excelente contenido en español."

**CONSEJO:**
"No intenten aprender todo de una vez. Un concepto por día."

---

### **[1:32-1:34] Slide 27: Proyecto - Ideas**

**MOTIVACIÓN:**
"El mejor proyecto es el que les apasiona. ¿Qué problema les gustaría resolver?"

**IDEAS COMERCIALES:**
"Piensen en problemas reales de empresas. Rappi optimizando rutas, inmobiliarias buscando terrenos..."

**IDEAS CIENTÍFICAS:**
"¿Qué les preocupa de Chile? Sequía, contaminación, segregación urbana..."

**FORMAR GRUPOS:**
"Hablen con sus compañeros. Intereses comunes = mejor equipo."

---

### **[1:34-1:36] Slide 28: Resumen**

**REPASAR RÁPIDO:**
"Hoy cubrimos 60+ años de historia en 80 minutos. Desde mapas en papel hasta IA."

**CONCEPTOS CLAVE:**
- "Geocomputación > SIG tradicional"
- "Open source es viable y poderoso"
- "Python/R son complementarios"
- "La práctica es esencial"

---

### **[1:36-1:37] Slide 29: Tarea**

**URGENTE:**
"Instalación ANTES del lab. No durante. ANTES."

**LECTURA:**
"Capítulo 1 de Geocomputation with Python. 30 minutos máximo."

**REFLEXIÓN:**
"Piensen en un problema espacial que les interese. Anótenlo."

---

### **[1:37-1:40] Slide 30: Cierre**

**PREGUNTAS:**
"¿Dudas? ¿Preguntas? ¿Comentarios?"

[Responder 2-3 preguntas]

**MOTIVACIÓN FINAL:**
"En 4 meses, estarán haciendo análisis que hoy parecen magia. Confíen en el proceso."

**LOGÍSTICA:**
"10 minutos de break. Vayan por café. Nos vemos aquí mismo para el laboratorio."

**ÚLTIMO RECORDATORIO:**
"Si no han instalado nada, usen el break para al menos descargar los instaladores."

---

## 📝 PREGUNTAS FRECUENTES Y RESPUESTAS

### P1: "¿Es mejor aprender Python o R primero?"
**R:** "Si vienen de programación, Python será más natural. Si vienen de estadística o no programan, R puede ser más intuitivo para análisis. Mi consejo: empiecen con Python porque es más versátil."

### P2: "¿Necesito una GPU para el curso?"
**R:** "No. Todo lo que haremos funciona en cualquier laptop de los últimos 5 años. GPU ayuda para deep learning con imágenes satelitales, pero eso es opcional/avanzado."

### P3: "¿Por qué no usamos ArcGIS si es el estándar de la industria?"
**R:** "Tres razones: 1) Costo - no todos pueden pagarlo después. 2) Multiplataforma - ArcGIS solo Windows. 3) Filosofía - quiero que entiendan QUÉ hacen, no solo hacer clicks. El que sabe programar GIS puede aprender ArcGIS en una semana."

### P4: "¿Los datos de Chile son fáciles de conseguir?"
**R:** "Sí y no. IDE Chile tiene mucho, pero disperso. Les compartiré un repositorio con datos limpios y listos. Pro tip: el INE tiene shapefiles actualizados de todas las comunas."

### P5: "¿Cuánto Python/R necesito saber antes?"
**R:** "Lo básico: variables, loops, funciones. Si pueden hacer un FizzBuzz, están listos. Si no, Khan Academy tiene un curso Python gratuito excelente."

### P6: "¿El proyecto puede ser sobre mi comuna/región?"
**R:** "¡Absolutamente! De hecho, lo incentivo. Conocen el contexto, tienen interés personal, y pueden conseguir datos locales únicos."

### P7: "¿Vamos a trabajar con imágenes satelitales?"
**R:** "Sí, en la unidad 2. Usaremos Sentinel-2 (10m resolución, gratis) y Landsat (30m, histórico desde 1972). Si hay interés, podemos ver Planet (3m, pago) en proyecto."

### P8: "¿Qué tan difícil es PostGIS?"
**R:** "Requiere saber SQL primero. Es opcional para el curso. Si les interesa, puedo dar una clase extra. Es MUY poderoso para proyectos grandes."

### P9: "¿Sirve para conseguir trabajo?"
**R:** "Absolutamente. Demanda altísima, poca oferta. Un junior Python + GIS parte en 1.2M CLP. Con experiencia, 2-3M. Startups de delivery, inmobiliarias, consultoras ambientales, todos buscan."

### P10: "¿Podemos usar ChatGPT/Copilot?"
**R:** "Sí, pero... úsenlo para aprender, no para copiar. Si no entienden el código que genera, no sirve. En el proyecto, deben poder explicar cada línea."

---

## 🎭 ACTIVIDADES INTERACTIVAS

### Actividad 1: "Encuentra el patrón" [Slide 4]
**Tiempo:** 2 minutos
**Instrucción:** "Miren este mapa de puntos. ¿Qué patrón ven? ¿Dónde pondrían una X para el próximo caso?"
**Objetivo:** Demostrar análisis espacial intuitivo

### Actividad 2: "Software Speed Dating" [Slide 9]
**Tiempo:** 3 minutos
**Instrucción:** "En parejas, uno defiende QGIS, otro ArcGIS. 1 minuto cada uno. ¡Cambio!"
**Objetivo:** Reflexionar sobre trade-offs

### Actividad 3: "Pseudo-código" [Slide 21]
**Tiempo:** 3 minutos
**Instrucción:** "Sin programar, escriban en español los pasos para encontrar el restaurant más cercano a su casa"
**Objetivo:** Pensar algorítmicamente

### Actividad 4: "Pitch tu proyecto" [Slide 27]
**Tiempo:** 2 minutos
**Instrucción:** "30 segundos. Pitch una idea de proyecto a tu compañero de al lado"
**Objetivo:** Empezar a pensar en proyectos

---

## 🔧 TROUBLESHOOTING COMÚN

### Problema: "ImportError: No module named geopandas"
**Solución:** 
```bash
# Windows
conda install -c conda-forge geopandas
# Mac/Linux
pip install --upgrade pip
pip install geopandas
```

### Problema: "Proyector no muestra colores correctamente"
**Solución:** Tener versión alternativa con alto contraste lista

### Problema: "Internet lento/caído"
**Solución:** Tener demos pre-grabados como GIF animados

### Problema: "Estudiante dice 'no entiendo nada'"
**Solución:** "Normal. Es mucha información. En el lab practicamos paso a paso. ¿Qué parte específica te perdió?"

### Problema: "Se acaba el tiempo"
**Priorizar:** Slides 1-20 son esenciales. 21-30 pueden ser rápidos o para lectura posterior.

---

## 📊 EVALUACIÓN DE COMPRENSIÓN

### Checkpoints durante la clase:
- [ ] Minuto 15: ¿Entienden diferencia SIG vs Geocomputación?
- [ ] Minuto 30: ¿Ven valor en open source?
- [ ] Minuto 45: ¿Comprenden ecosistema Python/R?
- [ ] Minuto 60: ¿Pueden seguir el código ejemplo?
- [ ] Minuto 75: ¿Tienen claro qué hacer para el lab?

### Señales de alerta:
- Más de 3 estudiantes en el celular → Cambiar ritmo
- Silencio absoluto en preguntas → Muy difícil o muy fácil
- Confusión en caras → Parar y preguntar

---

## 💡 TIPS PARA EL PROFESOR

1. **Energía:** El jueves primera hora puede ser pesado. Mantén energía alta.

2. **Historias:** Las anécdotas personales enganchan. Úsalas.

3. **Humor:** Un chiste malo sobre Python (serpiente) rompe el hielo.

4. **Pausas:** Si ves cansancio, 30 segundos de "estiren brazos" ayuda.

5. **Nombres:** Intenta aprender 3-5 nombres por clase.

6. **Preguntas:** "¿Quién ha usado...?" mejor que "¿Entienden?"

7. **Demostración:** Si algo falla en vivo, es oportunidad de enseñar debugging.

8. **Tiempo:** Ten un reloj visible. Slides 15-20 pueden comprimirse si es necesario.

9. **Participación:** Ofrece puntos extra por preguntas interesantes.

10. **Cierre:** Siempre termina con algo inspirador, no con detalles administrativos.

---

## 📚 MATERIAL ADICIONAL PARA PROFUNDIZAR

### Si sobra tiempo:
- Historia de ESRI y Jack Dangermond
- Caso Waze: Crowdsourcing geoespacial
- Diferencias entre Docker y ambientes virtuales
- WebAssembly y el futuro del GIS en browser

### Si hay mucho interés en un tema:
- **Historia:** Libro "The Esri Story" gratis online
- **Python:** "Automating GIS Processes" curso online University of Helsinki
- **R:** "Spatial Data Science" by Edzer Pebesma
- **Cloud:** Google Earth Engine guides oficiales

### Para estudiantes avanzados:
- Sugerir explorar Rust + GeoRust
- WebGL para visualización 3D (deck.gl)
- Apache Sedona para big data espacial
- STAC (SpatioTemporal Asset Catalogs)

---

## ✅ CHECKLIST POST-CLASE

- [ ] Subir slides al repositorio del curso
- [ ] Compartir links de recursos en el foro
- [ ] Preparar datos para el laboratorio
- [ ] Revisar que laboratorio tenga computadores funcionando
- [ ] Responder emails/consultas pendientes
- [ ] Anotar qué funcionó bien y qué mejorar
- [ ] Preparar material extra para estudiantes rápidos en lab
- [ ] Verificar que todos tengan acceso a los materiales

---

## 🎯 OBJETIVO CUMPLIDO

Si al final de la clase los estudiantes pueden:
1. Explicar qué es Geocomputación vs SIG tradicional ✓
2. Nombrar 3 herramientas de software geoespacial ✓
3. Escribir un "Hola Mundo" geoespacial ✓
4. Sentirse emocionados por el curso ✓

**¡MISIÓN CUMPLIDA!**

---

*Última actualización: Agosto 2025*
*Duración total estimada: 80 minutos*
*Preparación recomendada: 30 minutos*