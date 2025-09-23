# Calendario de Clases - Geoinformática
## Ingeniería Civil en Informática - USACH
## Segundo Semestre 2025 (18 agosto - 20 diciembre)

---

## UNIDAD 1: Fundamentos de Geocomputación y Datos Geoespaciales
### (Semanas 1-5)

### Semana 1
**Martes 19 de agosto - Clase 1: Introducción al curso**
- Presentación del programa del curso
- Introducción a la Geocomputación: ¿Qué es y por qué es relevante?
- Aplicaciones de la geoinformática en el mundo real
- Evaluación diagnóstica

**Jueves 21 de agosto**
- **Clase 2: Fundamentos de Geocomputación** (4 horas teóricas)
  - Historia y evolución de los SIG
  - Componentes de un SIG
  - Software libre vs propietario
  - Introducción a R y Python para geoinformática
  
- **Laboratorio 1: Configuración del ambiente** (2 horas prácticas)
  - Instalación de R y RStudio
  - Instalación de Python y bibliotecas geoespaciales
  - Instalación de paquetes básicos: sf, terra, raster, tmap
  - Primer contacto con datos geoespaciales

### Semana 2
**Martes 26 de agosto - Clase 3: Fundamentos de datos geoespaciales**
- Tipos de datos geoespaciales: vectorial vs raster
- Estructura de datos vectoriales (puntos, líneas, polígonos)
- Estructura de datos raster (grillas, resolución, bandas)
- Formatos de archivos comunes (Shapefile, GeoJSON, GeoTIFF)

**Jueves 28 de agosto**
- **Clase 4: Representación de datos geográficos en R/Python** (4 horas teóricas)
  - Paquete sf (Simple Features) en R
  - GeoPandas en Python
  - Estructuras de datos espaciales
  - Metadatos y atributos
  
- **Laboratorio 2: Manipulación básica de datos vectoriales** (2 horas prácticas)
  - Lectura de archivos shapefile y GeoJSON en R
  - Exploración de datos con sf
  - Operaciones básicas: head(), plot(), summary()
  - Ejercicios prácticos con datos de Chile

### Semana 3
**Martes 2 de septiembre - Clase 5: Sistemas de Referencia de Coordenadas**
- Conceptos de proyección cartográfica
- Sistemas de coordenadas geográficas vs proyectadas
- CRS más utilizados en Chile (UTM, WGS84)
- Importancia del CRS en análisis geoespacial

**Jueves 4 de septiembre**
- **Clase 6: Transformaciones y reproyecciones** (4 horas teóricas)
  - Transformación entre sistemas de coordenadas
  - Distorsiones en proyecciones
  - Selección apropiada de CRS según análisis
  - Errores comunes y cómo evitarlos
  
- **Laboratorio 3: Trabajando con CRS** (2 horas prácticas)
  - Identificación de CRS en datos existentes
  - Transformación y reproyección de datos
  - Ejercicios con datos de diferentes CRS
  - Resolución de problemas comunes de CRS

### Semana 4
**Martes 9 de septiembre - Clase 7: Datos raster y su representación**
- Estructura y propiedades de datos raster
- Álgebra de mapas básica
- Aplicaciones de datos raster (elevación, temperatura, imágenes satelitales)
- Introducción al paquete terra en R

**Jueves 11 de septiembre**
- **Clase 8: Procesamiento de imágenes y datos raster** (4 horas teóricas)
  - Operaciones con bandas
  - Índices espectrales (NDVI, NDWI)
  - Modelos digitales de elevación
  - Análisis multitemporal
  
- **Laboratorio 4: Manipulación de datos raster + Inicio proyecto** (2 horas prácticas)
  - Lectura y visualización de datos raster con terra
  - Operaciones básicas: crop, mask, resample
  - Extracción de valores y estadísticas
  - **PROYECTO:** Formación de grupos y brainstorming de ideas

### Semana 5 (SEMANA DE FIESTAS PATRIAS - NO HAY CLASES)
**15 al 20 de septiembre - Receso**

---

## UNIDAD 2: Operaciones y Visualización de Datos Geoespaciales
### (Semanas 6-11)

### Semana 6
**Martes 23 de septiembre - Clase 9: Operaciones con atributos**
- Selección y filtrado de datos espaciales
- Uniones espaciales (spatial joins)
- Agregación de datos por atributos
- Cálculo de nuevos atributos

**Jueves 25 de septiembre**
- **Clase 10: Análisis de atributos avanzado** (4 horas teóricas)
  - Joins complejos y relacionales
  - Operaciones grupales y resúmenes
  - Integración con dplyr/pandas
  - Optimización de consultas
  
- **Laboratorio 5: Manipulación de atributos** (2 horas prácticas)
  - Práctica con dplyr y sf
  - Ejercicios de filtrado y selección
  - Joins espaciales con datos reales
  - Mini-proyecto: análisis de datos demográficos por comuna

### Semana 7
**Martes 30 de septiembre - Clase 11: Operaciones espaciales vectoriales**
- Operaciones geométricas: buffer, intersección, unión
- Predicados espaciales (within, contains, intersects)
- Queries espaciales complejas
- Operaciones de overlay

**Jueves 2 de octubre**
- **Clase 12: Análisis espacial avanzado** (4 horas teóricas)
  - Análisis de redes
  - Polígonos de Voronoi y triangulación
  - Análisis de proximidad y accesibilidad
  - Modelado de áreas de servicio
  
- **Laboratorio 6: Geoprocesamiento vectorial + Propuesta proyecto** (2 horas prácticas)
  - Implementación de buffers y áreas de influencia
  - Análisis de proximidad
  - Overlay de capas vectoriales
  - **PROYECTO:** Entrega de propuesta preliminar (1 página)

### Semana 8
**Martes 7 de octubre - Clase 13: Operaciones raster básicas**
- Álgebra de mapas compleja
- Reclasificación de valores
- Operaciones focales, zonales y globales
- Análisis multicriterio con raster

**Jueves 9 de octubre**
- **Clase 14: Análisis raster avanzado** (4 horas teóricas)
  - Análisis de terreno (pendiente, orientación, curvatura)
  - Análisis hidrológico
  - Visibilidad y línea de vista
  - Modelado de superficies
  
- **Laboratorio 7: Análisis raster** (2 horas prácticas)
  - Cálculo de pendientes y orientaciones
  - Análisis de visibilidad
  - Estadísticas zonales
  - Proyecto: análisis de riesgo usando múltiples capas raster

### Semana 9
**Martes 14 de octubre - Clase 15: Interacciones raster-vector**
- Extracción de valores raster a puntos
- Rasterización de datos vectoriales
- Vectorización de datos raster
- Casos de uso y mejores prácticas

**Jueves 16 de octubre**
- **Clase 16: Integración de datos heterogéneos** (4 horas teóricas)
  - Fusión de datos de múltiples fuentes
  - Manejo de diferentes resoluciones
  - Interpolación espacial
  - Validación cruzada
  
- **Laboratorio 8: Integración raster-vector** (2 horas prácticas)
  - Extracción de valores de elevación a puntos de muestreo
  - Conversión entre formatos
  - Análisis combinado raster-vector
  - Ejercicio integrador con datos ambientales

### Semana 10
**Martes 21 de octubre - Clase 17: Fundamentos de cartografía digital**
- Principios de diseño cartográfico
- Elementos de un mapa
- Simbolización efectiva
- Introducción a tmap y ggplot2 para mapas

**Jueves 23 de octubre**
- **Clase 18: Cartografía temática y composición** (4 horas teóricas)
  - Tipos de mapas temáticos
  - Clasificación de datos
  - Escalas y generalización
  - Composición y layout
  
- **Laboratorio 9: Creación de mapas + Plan de proyecto** (2 horas prácticas)
  - Diseño de mapas temáticos con tmap
  - Personalización de símbolos y colores
  - **PROYECTO:** Definición formal del proyecto y plan de trabajo
  - Revisión de fuentes de datos disponibles

### Semana 11
**Martes 28 de octubre - Clase 19: Visualización interactiva**
- Mapas web interactivos con leaflet
- Publicación de mapas online
- Dashboards geoespaciales
- Introducción a mapview y plotly

**Jueves 30 de octubre**
- **Clase 20: Aplicaciones web geoespaciales** (4 horas teóricas)
  - Arquitectura de aplicaciones web GIS
  - Shiny para R
  - Streamlit para Python
  - Deployment y hosting
  
- **Laboratorio 10: Mapas interactivos** (2 horas prácticas)
  - Creación de mapas con leaflet en R
  - Añadir capas y controles
  - Popups y etiquetas interactivas
  - Publicación de mapas web simples

---

## UNIDAD 3: Extensiones y Aplicaciones de Geoinformática
### (Semanas 12-16)

### Semana 12
**Martes 4 de noviembre - Clase 21: Automatización y scripting**
- Creación de funciones personalizadas para geoprocesamiento
- Automatización de tareas repetitivas
- Buenas prácticas en programación geoespacial
- Manejo de errores y debugging

**Jueves 6 de noviembre**
- **Clase 22: Pipelines de procesamiento geoespacial** (4 horas teóricas)
  - Diseño de flujos de trabajo
  - Procesamiento por lotes (batch)
  - Paralelización de procesos
  - Optimización de rendimiento
  
- **Laboratorio 11: Scripts + Primer avance proyecto** (2 horas prácticas)
  - Creación de funciones reutilizables
  - Procesamiento batch de múltiples archivos
  - **PROYECTO:** Primer avance - Revisión de datos y metodología
  - Feedback personalizado por grupo

### Semana 13
**Martes 11 de noviembre - Clase 23: Integración con otros software GIS**
- Puentes entre R/Python y QGIS
- Uso de GDAL/OGR
- Interoperabilidad de datos
- APIs de servicios geoespaciales

**Jueves 13 de noviembre**
- **Clase 24: Bases de datos espaciales y servicios web** (4 horas teóricas)
  - PostGIS y consultas espaciales SQL
  - Servicios WMS/WFS/WCS
  - APIs REST geoespaciales
  - GeoServer y MapServer
  
- **Laboratorio 12: Integración de herramientas** (2 horas prácticas)
  - Conexión con servicios WMS/WFS
  - Uso de APIs geoespaciales (OpenStreetMap, Google Earth Engine)
  - Importación/exportación entre diferentes plataformas
  - Trabajo con bases de datos espaciales (PostGIS)

### Semana 14
**Martes 18 de noviembre - Clase 25: Statistical Learning con datos espaciales**
- Introducción al análisis espacial estadístico
- Autocorrelación espacial
- Modelos de regresión espacial
- Clustering espacial

**Jueves 20 de noviembre**
- **Clase 26: Machine Learning geoespacial** (4 horas teóricas)
  - Clasificación de imágenes satelitales
  - Random Forest y SVM espacial
  - Deep Learning para datos geoespaciales
  - Validación de modelos espaciales
  
- **Laboratorio 13: Análisis estadístico + Segundo avance** (2 horas prácticas)
  - Cálculo de índices de autocorrelación (Moran's I)
  - Detección de hotspots
  - **PROYECTO:** Segundo avance - Resultados preliminares
  - Revisión de visualizaciones y mapas del proyecto

### Semana 15
**Martes 25 de noviembre - Clase 27: Aplicaciones específicas**
- Geomarketing: análisis de mercado y localización
- Aplicaciones ambientales y ecológicas
- Análisis de redes de transporte
- Smart Cities y planificación urbana

**Jueves 27 de noviembre**
- **Clase 28: Casos de estudio en Chile** (4 horas teóricas)
  - Gestión de desastres naturales
  - Monitoreo de recursos naturales
  - Planificación territorial
  - Análisis de movilidad urbana
  
- **Laboratorio 14: Trabajo en proyecto** (2 horas prácticas)
  - Sesión dedicada al desarrollo del proyecto final
  - Resolución de problemas técnicos específicos
  - Apoyo en análisis avanzados
  - Preparación de visualizaciones finales

### Semana 16
**Martes 2 de diciembre - Clase 29: Tendencias actuales en Geoinformática**
- Big Data geoespacial
- Machine Learning y Deep Learning en geoinformática
- Computación en la nube para análisis geoespacial
- Google Earth Engine y plataformas similares

**Jueves 4 de diciembre**
- **Clase 30: Futuro de la Geoinformática** (4 horas teóricas)
  - Gemelos digitales y ciudades inteligentes
  - Realidad aumentada y visualización 3D
  - Internet de las Cosas (IoT) y sensores
  - Consideraciones éticas y privacidad
  
- **Laboratorio 15: Últimos ajustes proyecto** (2 horas prácticas)
  - Trabajo supervisado en proyectos finales
  - Últimos ajustes y mejoras
  - Preparación de presentaciones
  - Ensayo de presentaciones (opcional)

### Semana 17
**Martes 9 de diciembre - Presentaciones de proyectos (Parte 1)**
- Presentación de proyectos finales por grupos
- Evaluación entre pares
- Retroalimentación

**Jueves 11 de diciembre - Presentaciones de proyectos (Parte 2)**
- Continuación de presentaciones
- Discusión de resultados
- Cierre del curso

### Semana 18
**Martes 16 de diciembre - Evaluación recuperativa (si corresponde)**
- Evaluación recuperativa para quienes lo requieran

**Jueves 18 de diciembre - Cierre administrativo**
- Entrega de notas finales
- Retroalimentación general del curso

---

## Resumen de contenidos

### Total de sesiones:
- **30 clases teóricas** (16 martes + 14 jueves, excluyendo presentaciones)
- **16 laboratorios prácticos** (todos los jueves)
- **Total: 46 sesiones**

### Distribución por unidades:
- **Unidad 1** (Semanas 1-4): Fundamentos - 8 clases teóricas + 4 laboratorios
- **Unidad 2** (Semanas 6-11): Operaciones y Visualización - 12 clases teóricas + 6 laboratorios
- **Unidad 3** (Semanas 12-16): Aplicaciones - 10 clases teóricas + 5 laboratorios
- **Semanas 17-18**: Presentaciones y cierre

---

## Evaluación del Curso: Proyecto Semestral

### Modalidad de Evaluación
La evaluación del curso se basará en el desarrollo de **UN PROYECTO SEMESTRAL** que integrará todos los conocimientos adquiridos durante el curso. Los estudiantes podrán elegir entre dos enfoques:

#### 1. Proyecto de Carácter Comercial
- Desarrollo de una solución geoinformática para un problema de negocio real
- Ejemplos:
  - Sistema de análisis de localización óptima para retail
  - Plataforma de geomarketing para análisis de mercado
  - Aplicación de logística y optimización de rutas
  - Dashboard geoespacial para toma de decisiones empresariales
  - Análisis inmobiliario con datos geoespaciales

#### 2. Proyecto de Carácter Científico
- Investigación aplicada usando técnicas de geocomputación
- Ejemplos:
  - Modelado de fenómenos ambientales o climáticos
  - Análisis de distribución de especies y biodiversidad
  - Estudios de cambio de uso de suelo
  - Análisis de riesgos naturales (inundaciones, incendios, etc.)
  - Investigación en salud pública con componente espacial

### Hitos del Proyecto

1. **Semana 4** (11 de septiembre): Formación de grupos y brainstorming inicial
2. **Semana 7** (2 de octubre): Entrega de propuesta preliminar (1 página)
3. **Semana 10** (23 de octubre): Definición formal del proyecto y plan de trabajo
4. **Semana 12** (6 de noviembre): Primer avance - Revisión de datos y metodología
5. **Semana 14** (20 de noviembre): Segundo avance - Resultados preliminares
6. **Semana 16** (4 de diciembre): Trabajo supervisado y últimos ajustes
7. **Semana 17** (9-11 de diciembre): Presentaciones finales

### Entregables del Proyecto

1. **Código fuente** (R/Python) documentado y reproducible
2. **Informe técnico** (máx. 20 páginas) que incluya:
   - Introducción y objetivos
   - Descripción de datos utilizados
   - Metodología implementada
   - Resultados y visualizaciones
   - Conclusiones y trabajo futuro
3. **Presentación oral** (15 minutos + 5 de preguntas)
4. **Repositorio GitHub** con toda la documentación

### Criterios de Evaluación (100%)

- **Calidad técnica** (40%): Correcta implementación de técnicas geoespaciales
- **Innovación/Originalidad** (20%): Creatividad en la solución propuesta
- **Visualización y cartografía** (20%): Calidad de mapas y visualizaciones
- **Documentación** (10%): Código comentado, informe claro y completo
- **Presentación** (10%): Claridad en la comunicación de resultados

### Trabajo en Grupos
- Grupos de 1 a 3 personas máximo
- La complejidad del proyecto debe ser proporcional al tamaño del grupo
- Evaluación incluirá autoevaluación y coevaluación entre pares

## Recursos adicionales

- Libro base online: [Geocomputation with R](https://r.geocompx.org/)
- Repositorio del curso con datos y ejemplos
- Foro de consultas en plataforma institucional
- Horario de consultas: A definir con el profesor

## Notas importantes

- Los laboratorios son de asistencia obligatoria (mínimo 75%)
- Se espera participación activa en clases y laboratorios
- Los proyectos pueden ser individuales o en grupos de máximo 3 personas
- Todos los códigos deben estar documentados y ser reproducibles