#!/bin/bash

# ================================================
# Script para configurar repositorio en GitHub
# Curso: Geoinformática - USACH
# Autor: Francisco Parra O.
# ================================================

set -e  # Salir si hay errores

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║          CONFIGURACIÓN REPOSITORIO GITHUB - GEOINFORMÁTICA        ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Verificar si estamos en el directorio correcto
if [ ! -d "laboratorio_integrador" ]; then
    echo -e "${RED}❌ Error: No se encuentra la carpeta laboratorio_integrador${NC}"
    echo -e "${YELLOW}📁 Asegúrate de estar en /home/franciscoparrao/proyectos/geoinformatica${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Directorio verificado${NC}"

# Paso 1: Inicializar repositorio Git si no existe
if [ ! -d ".git" ]; then
    echo -e "${YELLOW}📦 Inicializando repositorio Git...${NC}"
    git init
    echo -e "${GREEN}✓ Repositorio Git inicializado${NC}"
else
    echo -e "${GREEN}✓ Repositorio Git ya existe${NC}"
fi

# Paso 2: Crear archivo .gitignore principal
echo -e "${YELLOW}📝 Creando .gitignore principal...${NC}"
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Jupyter Notebooks
.ipynb_checkpoints
*/.ipynb_checkpoints/*

# Environment variables
.env
.env.local
.env.*.local

# Data files (muy pesados para GitHub)
*.csv
*.shp
*.tif
*.tiff
*.geojson
*.gpkg
*.zip
*.tar.gz
data/raw/*
data/processed/*
data/external/*
!data/raw/.gitkeep
!data/processed/.gitkeep
!data/external/.gitkeep

# Model files
*.pkl
*.joblib
*.h5
*.pt
*.pth
outputs/models/*
!outputs/models/.gitkeep

# IDE
.vscode/
.idea/
*.swp
*.swo
.DS_Store

# Docker
docker/jupyter/work/*
docker/postgis/data/*

# Logs
*.log
logs/
*.out

# Temporary files
tmp/
temp/
*.tmp
*.bak
*~

# Large output files
outputs/figures/*.png
outputs/figures/*.jpg
outputs/figures/*.pdf
!outputs/figures/.gitkeep
EOF

echo -e "${GREEN}✓ .gitignore creado${NC}"

# Paso 3: Crear README principal del curso
echo -e "${YELLOW}📚 Creando README principal del curso...${NC}"
cat > README.md << 'EOF'
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
├── 📚 clases/                    # Material de clases
│   ├── teoricas/                 # Presentaciones y material teórico
│   └── practicas/                # Ejercicios y actividades prácticas
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
    ├── bibliografia/
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
EOF

echo -e "${GREEN}✓ README principal creado${NC}"

# Paso 4: Crear archivo LICENSE
echo -e "${YELLOW}📄 Creando archivo LICENSE...${NC}"
cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2024 Francisco Parra O. - Universidad de Santiago de Chile

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

echo -e "${GREEN}✓ LICENSE creado${NC}"

# Paso 5: Crear estructura de carpetas del curso
echo -e "${YELLOW}📁 Creando estructura de carpetas del curso...${NC}"

mkdir -p clases/teoricas
mkdir -p clases/practicas
mkdir -p tareas
mkdir -p proyectos
mkdir -p recursos/bibliografia
mkdir -p recursos/tutoriales
mkdir -p recursos/datasets

# Crear archivos .gitkeep para mantener carpetas vacías
touch clases/teoricas/.gitkeep
touch clases/practicas/.gitkeep
touch tareas/.gitkeep
touch proyectos/.gitkeep
touch recursos/bibliografia/.gitkeep
touch recursos/tutoriales/.gitkeep
touch recursos/datasets/.gitkeep

echo -e "${GREEN}✓ Estructura de carpetas creada${NC}"

# Paso 6: Configurar Git
echo -e "${YELLOW}⚙️ Configurando Git...${NC}"

# Agregar todos los archivos
git add .

# Crear primer commit
git commit -m "🚀 Inicializar repositorio del curso de Geoinformática

- Agregar laboratorio integrador completo
- Crear estructura del curso
- Configurar Docker y ambiente Python
- Agregar documentación y guías
- Incluir scripts de automatización"

echo -e "${GREEN}✓ Commit inicial creado${NC}"

# Paso 7: Instrucciones para GitHub
echo -e "${BLUE}"
echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║                    CONFIGURACIÓN COMPLETADA ✅                     ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

echo -e "${YELLOW}📋 SIGUIENTES PASOS:${NC}"
echo ""
echo -e "${GREEN}1. Crear repositorio en GitHub:${NC}"
echo "   - Ve a: https://github.com/new"
echo "   - Nombre: geoinformatica"
echo "   - Descripción: Curso de Geoinformática - USACH"
echo "   - Visibilidad: Public"
echo "   - NO inicialices con README, .gitignore o LICENSE"
echo ""
echo -e "${GREEN}2. Conectar con GitHub (copia y pega estos comandos):${NC}"
echo -e "${BLUE}"
echo "git remote add origin https://github.com/franciscoparrao/geoinformatica.git"
echo "git branch -M main"
echo "git push -u origin main"
echo -e "${NC}"
echo ""
echo -e "${GREEN}3. Para futuros cambios:${NC}"
echo -e "${BLUE}"
echo "git add ."
echo "git commit -m \"Descripción del cambio\""
echo "git push"
echo -e "${NC}"
echo ""
echo -e "${YELLOW}📌 URLs importantes:${NC}"
echo "   Repositorio: https://github.com/franciscoparrao/geoinformatica"
echo "   Laboratorio: https://github.com/franciscoparrao/geoinformatica/tree/main/laboratorio_integrador"
echo ""
echo -e "${GREEN}✨ ¡Listo! El repositorio está preparado para subir a GitHub${NC}"