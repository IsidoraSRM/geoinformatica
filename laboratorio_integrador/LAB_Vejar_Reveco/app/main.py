import streamlit as st
import geopandas as gpd
from sqlalchemy import create_engine
from streamlit_folium import st_folium
import folium

st.set_page_config(layout="wide", page_title="Análisis San Bernardo")

st.title("Dashboard San Bernardo - Demo")

# Ejemplo simple: leer GeoPackage local
st.sidebar.header("Controles")
if st.sidebar.button("Mostrar mapa ejemplo"):
    # si tienes un geopackage local
    try:
        gdf = gpd.read_file("data/processed/sanbernardo_manzanas.gpkg")
        m = folium.Map(location=[-33.58, -70.67], zoom_start=12)
        folium.GeoJson(gdf.to_crs(epsg=4326)).add_to(m)
        st_folium(m, width=900)
    except Exception as e:
        st.error(f"No se pudo cargar el GeoDataFrame: {e}")