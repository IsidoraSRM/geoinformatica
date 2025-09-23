#!/bin/bash
# Script de setup para Clase 04 - Pipeline de Desarrollo Geoespacial
# Autor: Prof. Francisco Parra O.
# Fecha: 2025

set -e  # Exit on error

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}==========================================${NC}"
echo -e "${GREEN}  Setup Clase 04 - Pipeline Geoespacial  ${NC}"
echo -e "${GREEN}==========================================${NC}"

# Función para verificar comandos
check_command() {
    if ! command -v $1 &> /dev/null; then
        echo -e "${RED}❌ $1 no está instalado${NC}"
        return 1
    else
        echo -e "${GREEN}✓ $1 está instalado${NC}"
        return 0
    fi
}

# Función para verificar Python version
check_python_version() {
    python_version=$(python3 --version 2>&1 | grep -Po '(?<=Python )\d+\.\d+')
    required_version="3.9"
    
    if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" = "$required_version" ]; then 
        echo -e "${GREEN}✓ Python $python_version cumple con el requisito (>= 3.9)${NC}"
        return 0
    else
        echo -e "${RED}❌ Python $python_version no cumple con el requisito (>= 3.9)${NC}"
        return 1
    fi
}

# 1. Verificar prerequisitos
echo -e "\n${YELLOW}1. Verificando prerequisitos...${NC}"

check_command python3
check_python_version
check_command pip3
check_command git
check_command docker

# Verificar PostgreSQL/PostGIS
if check_command psql; then
    # Verificar si PostGIS está instalado
    if psql -U postgres -c "SELECT PostGIS_version();" &> /dev/null; then
        echo -e "${GREEN}✓ PostGIS está instalado${NC}"
    else
        echo -e "${YELLOW}⚠ PostgreSQL está instalado pero PostGIS no está habilitado${NC}"
        echo "  Instalando PostGIS..."
        if [[ "$OSTYPE" == "linux-gnu"* ]]; then
            sudo apt-get update
            sudo apt-get install -y postgis postgresql-14-postgis-3
        elif [[ "$OSTYPE" == "darwin"* ]]; then
            brew install postgis
        fi
    fi
else
    echo -e "${YELLOW}⚠ PostgreSQL no está instalado. Se usará Docker${NC}"
fi

# 2. Crear ambiente virtual
echo -e "\n${YELLOW}2. Creando ambiente virtual...${NC}"

if [ -d "geo_env" ]; then
    echo -e "${YELLOW}  Ambiente virtual ya existe, activando...${NC}"
    source geo_env/bin/activate
else
    echo -e "${GREEN}  Creando nuevo ambiente virtual...${NC}"
    python3 -m venv geo_env
    source geo_env/bin/activate
fi

# 3. Actualizar pip
echo -e "\n${YELLOW}3. Actualizando pip...${NC}"
pip install --upgrade pip wheel setuptools

# 4. Instalar GDAL (necesario antes de otras librerías geo)
echo -e "\n${YELLOW}4. Instalando GDAL...${NC}"

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    echo -e "${GREEN}  Sistema Linux detectado${NC}"
    sudo apt-get update
    sudo apt-get install -y gdal-bin libgdal-dev
    export CPLUS_INCLUDE_PATH=/usr/include/gdal
    export C_INCLUDE_PATH=/usr/include/gdal
    pip install GDAL==$(gdal-config --version)
    
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # Mac OSX
    echo -e "${GREEN}  Sistema macOS detectado${NC}"
    if ! check_command brew; then
        echo -e "${RED}Homebrew no está instalado. Instalando...${NC}"
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    brew install gdal
    pip install GDAL==$(gdal-config --version)
    
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Windows
    echo -e "${YELLOW}  Sistema Windows detectado. Usando conda es recomendado${NC}"
    echo "  Instalando con pip (puede fallar)..."
    pip install GDAL
fi

# 5. Instalar dependencias Python
echo -e "\n${YELLOW}5. Instalando dependencias Python...${NC}"

# Instalar en orden para evitar conflictos
pip install numpy
pip install pandas
pip install shapely
pip install fiona pyproj
pip install geopandas

# Instalar resto de requirements
pip install -r ../requirements.txt

# 6. Crear estructura de carpetas del proyecto
echo -e "\n${YELLOW}6. Creando estructura de proyecto...${NC}"

mkdir -p proyecto_geo/{data/{raw,processed,cache},src/{etl,analysis,api,visualization},notebooks,tests,config,docker,docs}

# Crear archivos base
touch proyecto_geo/README.md
touch proyecto_geo/.gitignore
touch proyecto_geo/.env.example
touch proyecto_geo/config/config.yaml

# 7. Configurar .env
echo -e "\n${YELLOW}7. Configurando variables de entorno...${NC}"

cat > proyecto_geo/.env.example << EOF
# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=geodata
DB_USER=geouser
DB_PASSWORD=changeme

# APIs (obtener keys gratuitas)
GOOGLE_API_KEY=your_google_maps_api_key_here
OPENWEATHER_API_KEY=your_openweather_api_key_here
MAPBOX_TOKEN=your_mapbox_token_here

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379

# App
APP_SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_hex(32))')
DEBUG=True
EOF

cp proyecto_geo/.env.example proyecto_geo/.env
echo -e "${GREEN}✓ Archivo .env creado (editar con tus API keys)${NC}"

# 8. Configurar Git
echo -e "\n${YELLOW}8. Configurando Git...${NC}"

cat > proyecto_geo/.gitignore << EOF
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
geo_env/
venv/
.venv

# Data
data/raw/*
data/cache/*
*.gpkg
*.shp
*.tif
*.tiff
!data/raw/.gitkeep
!data/cache/.gitkeep

# Environment
.env
.env.local
config/secrets.yaml

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Logs
*.log
logs/

# Database
*.db
*.sqlite
*.sqlite3

# Docker
.dockerignore
docker-compose.override.yml
EOF

# 9. Verificar instalación
echo -e "\n${YELLOW}9. Verificando instalación...${NC}"

python3 << EOF
import sys
print(f"Python: {sys.version}")

try:
    import geopandas as gpd
    print(f"✓ GeoPandas: {gpd.__version__}")
except ImportError as e:
    print(f"✗ GeoPandas: {e}")

try:
    import folium
    print(f"✓ Folium: {folium.__version__}")
except ImportError as e:
    print(f"✗ Folium: {e}")

try:
    import streamlit as st
    print(f"✓ Streamlit: {st.__version__}")
except ImportError as e:
    print(f"✗ Streamlit: {e}")

try:
    import fastapi
    print(f"✓ FastAPI: {fastapi.__version__}")
except ImportError as e:
    print(f"✗ FastAPI: {e}")

try:
    import osmnx as ox
    print(f"✓ OSMnx: {ox.__version__}")
except ImportError as e:
    print(f"✗ OSMnx: {e}")

try:
    import dask_geopandas
    print(f"✓ Dask-GeoPandas: instalado")
except ImportError as e:
    print(f"✗ Dask-GeoPandas: {e}")

print("\nVerificación completada!")
EOF

# 10. Descargar datos de ejemplo
echo -e "\n${YELLOW}10. Descargando datos de ejemplo...${NC}"

cd proyecto_geo/data/raw

# Comunas de Chile (desde GitHub)
echo "Descargando comunas de Chile..."
curl -L -o comunas_chile.geojson \
    "https://raw.githubusercontent.com/aoguedao/chile-geojson/master/comunas.geojson"

# Crear dataset de prueba
echo "Creando dataset de propiedades de ejemplo..."
cd ../../

# 11. Información final
echo -e "\n${GREEN}==========================================${NC}"
echo -e "${GREEN}       ¡Setup completado con éxito!       ${NC}"
echo -e "${GREEN}==========================================${NC}"
echo ""
echo -e "${YELLOW}Para activar el ambiente virtual:${NC}"
echo "  source geo_env/bin/activate"
echo ""
echo -e "${YELLOW}Para verificar que todo funciona:${NC}"
echo "  python3 ../scripts/test_setup.py"
echo ""
echo -e "${YELLOW}Para iniciar servicios Docker:${NC}"
echo "  docker-compose -f ../docker/docker-compose.yml up -d"
echo ""
echo -e "${YELLOW}Próximos pasos:${NC}"
echo "  1. Editar proyecto_geo/.env con tus API keys"
echo "  2. Iniciar PostgreSQL/PostGIS"
echo "  3. Abrir Jupyter: jupyter notebook"
echo "  4. Revisar notebooks de ejemplo en ../notebooks/"
echo ""
echo -e "${GREEN}¡Listo para la clase!${NC}"