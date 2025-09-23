#!/usr/bin/env python3
"""
Script para crear datos de ejemplo para la Clase 04
"""

import json
import os

# Crear datos GeoJSON de ejemplo con comunas de Santiago
comunas_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "nombre": "Las Condes",
                "poblacion": 294838,
                "superficie_km2": 99.4
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-70.5827, -33.4167]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "nombre": "Providencia",
                "poblacion": 157749,
                "superficie_km2": 14.4
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-70.6087, -33.4372]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "nombre": "Santiago",
                "poblacion": 404495,
                "superficie_km2": 22.4
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-70.6483, -33.4489]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "nombre": "Vitacura",
                "poblacion": 96774,
                "superficie_km2": 28.3
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-70.5977, -33.3817]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "nombre": "La Reina",
                "poblacion": 100252,
                "superficie_km2": 23.4
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-70.5447, -33.4522]
            }
        }
    ]
}

# Crear directorio si no existe
os.makedirs("../proyecto_geo/data/raw", exist_ok=True)

# Guardar archivo
output_path = "../proyecto_geo/data/raw/comunas_chile.geojson"
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(comunas_data, f, indent=2, ensure_ascii=False)

print(f"✓ Archivo de datos de ejemplo creado en: {output_path}")
print(f"  - {len(comunas_data['features'])} comunas incluidas")
print(f"  - Formato: GeoJSON")
print(f"  - Geometría: Points (centroides)")