#!/bin/bash
# Script para arreglar repositorios y continuar con instalación de PostGIS
# Autor: Prof. Francisco Parra O.

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Arreglando problemas de repositorios...${NC}"

# 1. Eliminar repositorios problemáticos
echo -e "${YELLOW}Removiendo repositorios con errores...${NC}"

# Remover MongoDB 7.0 (obsoleto)
sudo rm -f /etc/apt/sources.list.d/mongodb*.list
sudo rm -f /etc/apt/sources.list.d/qgis*.list

# 2. Actualizar lista de paquetes (ignorando errores)
echo -e "${YELLOW}Actualizando lista de paquetes...${NC}"
sudo apt-get update 2>/dev/null || true

# 3. Instalar PostGIS
echo -e "${GREEN}Instalando PostGIS...${NC}"

# Detectar versión de PostgreSQL instalada
PG_VERSION=$(psql --version | awk '{print $3}' | sed 's/\..*//')

if [ -z "$PG_VERSION" ]; then
    echo -e "${RED}PostgreSQL no detectado. Instalando PostgreSQL 14 con PostGIS...${NC}"
    sudo apt-get install -y postgresql-14 postgresql-14-postgis-3 postgis
else
    echo -e "${GREEN}PostgreSQL versión $PG_VERSION detectado${NC}"
    
    # Instalar PostGIS para la versión detectada
    if [ "$PG_VERSION" -eq "16" ]; then
        sudo apt-get install -y postgresql-16-postgis-3 postgis
    elif [ "$PG_VERSION" -eq "15" ]; then
        sudo apt-get install -y postgresql-15-postgis-3 postgis
    elif [ "$PG_VERSION" -eq "14" ]; then
        sudo apt-get install -y postgresql-14-postgis-3 postgis
    else
        echo -e "${YELLOW}Versión de PostgreSQL no soportada directamente. Intentando instalación genérica...${NC}"
        sudo apt-get install -y postgis postgresql-$PG_VERSION-postgis-3
    fi
fi

# 4. Verificar instalación de PostGIS
echo -e "${YELLOW}Verificando instalación de PostGIS...${NC}"

# Crear extensión PostGIS en la base de datos por defecto
sudo -u postgres psql -c "CREATE EXTENSION IF NOT EXISTS postgis;" 2>/dev/null && \
    echo -e "${GREEN}✓ PostGIS instalado correctamente${NC}" || \
    echo -e "${YELLOW}⚠ PostGIS instalado pero requiere configuración manual${NC}"

# 5. Instalar GDAL y dependencias geoespaciales
echo -e "${GREEN}Instalando GDAL y dependencias geoespaciales...${NC}"

sudo apt-get install -y \
    gdal-bin \
    libgdal-dev \
    libgeos-dev \
    libproj-dev \
    libspatialindex-dev \
    python3-gdal \
    python3-dev \
    build-essential

# 6. Exportar variables de entorno para GDAL
echo -e "${YELLOW}Configurando variables de entorno...${NC}"

export GDAL_CONFIG=/usr/bin/gdal-config
export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal

# Agregar al bashrc para futuras sesiones
echo "# GDAL Configuration" >> ~/.bashrc
echo "export GDAL_CONFIG=/usr/bin/gdal-config" >> ~/.bashrc
echo "export CPLUS_INCLUDE_PATH=/usr/include/gdal" >> ~/.bashrc
echo "export C_INCLUDE_PATH=/usr/include/gdal" >> ~/.bashrc

echo -e "${GREEN}Variables de entorno configuradas${NC}"

# 7. Verificación final
echo -e "\n${YELLOW}=== VERIFICACIÓN FINAL ===${NC}"

# PostgreSQL
if systemctl is-active --quiet postgresql; then
    echo -e "${GREEN}✓ PostgreSQL está activo${NC}"
else
    echo -e "${RED}✗ PostgreSQL no está activo${NC}"
    sudo systemctl start postgresql
fi

# PostGIS
if sudo -u postgres psql -c "SELECT PostGIS_version();" 2>/dev/null | grep -q POSTGIS; then
    POSTGIS_VERSION=$(sudo -u postgres psql -t -c "SELECT PostGIS_version();" 2>/dev/null | head -1)
    echo -e "${GREEN}✓ PostGIS versión: $POSTGIS_VERSION${NC}"
else
    echo -e "${YELLOW}⚠ PostGIS requiere activación manual${NC}"
fi

# GDAL
if command -v gdal-config &> /dev/null; then
    GDAL_VERSION=$(gdal-config --version)
    echo -e "${GREEN}✓ GDAL versión: $GDAL_VERSION${NC}"
else
    echo -e "${RED}✗ GDAL no instalado correctamente${NC}"
fi

echo -e "\n${GREEN}==========================================${NC}"
echo -e "${GREEN}    Configuración completada con éxito    ${NC}"
echo -e "${GREEN}==========================================${NC}"
echo ""
echo -e "${YELLOW}Próximos pasos:${NC}"
echo "1. Continuar con la instalación de Python:"
echo "   cd ../recursos_clase04/scripts"
echo "   bash setup_environment.sh"
echo ""
echo "2. Si PostGIS no se activó automáticamente:"
echo "   sudo -u postgres psql"
echo "   CREATE EXTENSION postgis;"
echo "   \\q"