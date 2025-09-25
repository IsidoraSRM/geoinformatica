FROM jupyter/scipy-notebook:latest

USER root

# Instalar dependencias del sistema con mejores opciones de red
RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
    gdal-bin \
    libgdal-dev \
    libspatialindex-dev \
    libproj-dev \
    libgeos-dev \
    postgresql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Configurar GDAL
ENV GDAL_CONFIG=/usr/bin/gdal-config
ENV PROJ_LIB=/usr/share/proj

USER $NB_UID

# Copiar requirements
COPY requirements.txt /tmp/

# Instalar librerías Python con mejor manejo de errores
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --timeout 300 --retries 3 -r /tmp/requirements.txt && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Instalar extensiones de JupyterLab
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager \
    jupyterlab-plotly \
    @jupyterlab/geojson-extension

WORKDIR /home/jovyan/work
