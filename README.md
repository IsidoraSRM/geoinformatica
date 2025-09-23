# 🌍 Geoinformática - USACH

[![Universidad](https://img.shields.io/badge/Universidad-USACH-blue)](https://www.usach.cl)
[![Profesor](https://img.shields.io/badge/Profesor-Francisco%20Parra%20O.-green)](https://github.com/franciscoparrao)
[![Semestre](https://img.shields.io/badge/Semestre-2024--1-yellow)](https://github.com/franciscoparrao/geoinformatica)

## 📋 Descripción del Curso

Repositorio oficial del curso de **Geoinformática** de la Universidad de Santiago de Chile (USACH). Este curso integra tecnologías de análisis espacial, programación en Python, y sistemas de información geográfica para resolver problemas territoriales complejos.

## 🗂️ Estructura del Repositorio

```
geoinformatica/
│
├── 🔬 laboratorio_integrador/    # Proyecto integrador del curso
│   ├── docs/                     # Documentación del laboratorio
│   ├── data/                     # Datos para análisis
│   ├── notebooks/                # Notebooks Jupyter
│   ├── scripts/                  # Scripts Python
│   ├── app/                      # Aplicación web
│   └── README.md                 # Guía del laboratorio
│
├── 📝 tareas/                    # Tareas individuales
│   ├── tarea_01/
│   ├── tarea_02/
│   └── ...
│
├── 🎯 proyectos/                 # Proyectos especiales
│
└── 📖 recursos/                  # Material complementario
    ├── tutoriales/
    └── datasets/
```

## 🚀 Laboratorio Integrador

El **[Laboratorio Integrador](./laboratorio_integrador/)** es el proyecto principal del curso donde los estudiantes aplican todas las tecnologías aprendidas:

- 🗺️ Análisis espacial con GeoPandas y PySAL
- 🛰️ Procesamiento de imágenes satelitales
- 📊 Geoestadística y análisis exploratorio (ESDA)
- 🤖 Machine Learning geoespacial
- 🌐 Desarrollo de aplicaciones web interactivas
- 🐳 Containerización con Docker

[**→ Ir al Laboratorio Integrador**](./laboratorio_integrador/)

## 📚 Contenidos del Curso

### Módulo 1: Fundamentos
- Introducción a la Geoinformática
- Python para análisis espacial
- Sistemas de coordenadas y proyecciones

### Módulo 2: Análisis Vectorial
- GeoPandas y operaciones espaciales
- OpenStreetMap y OSMnx
- Análisis de redes

### Módulo 3: Análisis Raster
- Procesamiento de DEMs
- Imágenes satelitales (Sentinel, Landsat)
- Google Earth Engine

### Módulo 4: Geoestadística
- Análisis exploratorio de datos espaciales (ESDA)
- Autocorrelación espacial
- Interpolación (Kriging, IDW)

### Módulo 5: Machine Learning
- Feature engineering espacial
- Modelos predictivos geoespaciales
- Validación espacial

### Módulo 6: Aplicaciones
- Desarrollo web con Streamlit
- Visualización interactiva
- Deployment con Docker

## 🛠️ Tecnologías Utilizadas

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-20.10%2B-blue?logo=docker)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15%2B-blue?logo=postgresql)
![Jupyter](https://img.shields.io/badge/Jupyter-Lab-orange?logo=jupyter)

### Stack Principal
- **Lenguaje:** Python 3.10+
- **Geoespacial:** GeoPandas, Shapely, Rasterio, OSMnx
- **ML/DL:** Scikit-learn, XGBoost, TensorFlow
- **Visualización:** Matplotlib, Plotly, Folium, Streamlit
- **Base de datos:** PostGIS
- **Containerización:** Docker & Docker Compose

## 💻 Instalación Rápida

### Opción 1: Docker (Recomendado)
```bash
# Clonar repositorio
git clone https://github.com/franciscoparrao/geoinformatica.git
cd geoinformatica/laboratorio_integrador

# Configurar y ejecutar
./setup.sh
docker-compose up -d
```

### Opción 2: Ambiente Local
```bash
# Crear ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r laboratorio_integrador/requirements.txt
```

## 📖 Recursos Adicionales

### Documentación Recomendada
- [GeoPandas Documentation](https://geopandas.org)
- [PySAL - Python Spatial Analysis Library](https://pysal.org)
- [OSMnx Documentation](https://osmnx.readthedocs.io)
- [PostGIS Documentation](https://postgis.net/docs/)

### Datasets Públicos
- [IDE Chile](https://www.ide.cl)
- [Instituto Nacional de Estadísticas](https://www.ine.cl)
- [OpenStreetMap](https://www.openstreetmap.org)
- [Google Earth Engine Catalog](https://developers.google.com/earth-engine/datasets)

## 👥 Contribuciones

Los estudiantes pueden contribuir al repositorio mediante:
1. Fork del repositorio
2. Crear una rama para su contribución
3. Hacer commit de los cambios
4. Crear un Pull Request

## 📧 Contacto

- **Profesor:** Francisco Parra O.
- **GitHub:** [@franciscoparrao](https://github.com/franciscoparrao)
- **Email:** francisco.parra@usach.cl

## 📄 Licencia

Este material educativo está disponible bajo licencia [MIT](LICENSE).

---

**Universidad de Santiago de Chile - USACH**
*Departamento de Ingeniería Geográfica*
*2024*
