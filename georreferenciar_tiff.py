#!/usr/bin/env python3
import numpy as np
from PIL import Image
import struct
import os

def crear_world_file(imagen_tiff, lon_min, lat_min, lon_max, lat_max):
    """
    Crea un World File (.tfw) para georreferenciar una imagen TIFF
    
    El World File es un archivo de texto que contiene información de georreferenciación
    y es compatible con la mayoría de software GIS (QGIS, ArcGIS, etc.)
    """
    
    # Abrir la imagen para obtener dimensiones
    img = Image.open(imagen_tiff)
    width, height = img.size
    
    # Calcular el tamaño de píxel
    pixel_width = (lon_max - lon_min) / width
    pixel_height = (lat_max - lat_min) / height
    
    # Nombre del World File (cambiar .tif por .tfw)
    world_file = imagen_tiff.replace('.tif', '.tfw')
    
    # Escribir el World File
    # Formato:
    # Línea 1: tamaño de píxel en dirección X
    # Línea 2: rotación sobre el eje Y (generalmente 0)
    # Línea 3: rotación sobre el eje X (generalmente 0)
    # Línea 4: tamaño de píxel en dirección Y (negativo)
    # Línea 5: coordenada X del centro del píxel superior izquierdo
    # Línea 6: coordenada Y del centro del píxel superior izquierdo
    
    with open(world_file, 'w') as f:
        f.write(f"{pixel_width:.10f}\n")     # Tamaño píxel X
        f.write("0.0000000000\n")             # Rotación Y
        f.write("0.0000000000\n")             # Rotación X
        f.write(f"{-pixel_height:.10f}\n")   # Tamaño píxel Y (negativo)
        f.write(f"{lon_min + pixel_width/2:.10f}\n")   # X centro píxel sup-izq
        f.write(f"{lat_max - pixel_height/2:.10f}\n")  # Y centro píxel sup-izq
    
    print(f"✓ World File creado: {world_file}")
    return world_file

def crear_prj_file(imagen_tiff):
    """
    Crea un archivo .prj con la información del sistema de coordenadas
    """
    prj_file = imagen_tiff.replace('.tif', '.prj')
    
    # WKT (Well Known Text) para WGS84
    wgs84_wkt = """GEOGCS["WGS 84",
    DATUM["WGS_1984",
        SPHEROID["WGS 84",6378137,298.257223563,
            AUTHORITY["EPSG","7030"]],
        AUTHORITY["EPSG","6326"]],
    PRIMEM["Greenwich",0,
        AUTHORITY["EPSG","8901"]],
    UNIT["degree",0.0174532925199433,
        AUTHORITY["EPSG","9122"]],
    AUTHORITY["EPSG","4326"]]"""
    
    with open(prj_file, 'w') as f:
        f.write(wgs84_wkt)
    
    print(f"✓ Archivo PRJ creado: {prj_file}")
    return prj_file

def georreferenciar_imagen_existente(imagen_tiff, bbox, nombre_zona):
    """
    Añade georreferenciación a una imagen TIFF existente
    
    Args:
        imagen_tiff: Ruta al archivo TIFF
        bbox: Tupla (lon_min, lat_min, lon_max, lat_max)
        nombre_zona: Descripción de la zona
    """
    
    print(f"\nGeorreferenciando: {imagen_tiff}")
    print(f"Zona: {nombre_zona}")
    print(f"Bbox: {bbox}")
    
    if not os.path.exists(imagen_tiff):
        print(f"✗ No se encuentra el archivo: {imagen_tiff}")
        return False
    
    lon_min, lat_min, lon_max, lat_max = bbox
    
    # Crear World File
    crear_world_file(imagen_tiff, lon_min, lat_min, lon_max, lat_max)
    
    # Crear archivo PRJ
    crear_prj_file(imagen_tiff)
    
    # Verificar
    img = Image.open(imagen_tiff)
    print(f"✓ Imagen: {img.size[0]}x{img.size[1]} píxeles")
    print(f"✓ Sistema de coordenadas: WGS84 (EPSG:4326)")
    print(f"✓ Coordenadas:")
    print(f"  • Esquina NO: ({lon_min:.4f}, {lat_max:.4f})")
    print(f"  • Esquina SE: ({lon_max:.4f}, {lat_min:.4f})")
    
    # Calcular resolución
    res_x = (lon_max - lon_min) / img.size[0]
    res_y = (lat_max - lat_min) / img.size[1]
    res_x_m = res_x * 111000  # Aproximación en metros
    res_y_m = res_y * 111000
    
    print(f"✓ Resolución: {res_x:.6f}° x {res_y:.6f}°")
    print(f"✓ Resolución aprox: {res_x_m:.1f}m x {res_y_m:.1f}m")
    
    return True

def main():
    print("="*70)
    print("GEORREFERENCIACIÓN DE IMÁGENES TIFF EXISTENTES")
    print("="*70)
    
    # Definir las georreferencias para las imágenes existentes
    imagenes = [
        {
            'archivo': 'santiago_chile_rgb.tif',
            'nombre': 'Santiago Centro y Cordillera',
            'bbox': (-70.75, -33.50, -70.55, -33.35)
        },
        {
            'archivo': 'valparaiso_chile_rgb.tif',
            'nombre': 'Valparaíso Costa',
            'bbox': (-71.65, -33.05, -71.55, -32.95)
        },
        {
            'archivo': 'araucania_chile_rgb.tif',
            'nombre': 'La Araucanía - Temuco',
            'bbox': (-72.65, -38.75, -72.45, -38.60)
        }
    ]
    
    # Georreferenciar cada imagen
    exitosos = []
    for img_info in imagenes:
        if os.path.exists(img_info['archivo']):
            if georreferenciar_imagen_existente(
                img_info['archivo'],
                img_info['bbox'],
                img_info['nombre']
            ):
                exitosos.append(img_info['archivo'])
        else:
            print(f"\n✗ No se encuentra: {img_info['archivo']}")
    
    # Resumen
    print("\n" + "="*70)
    print("RESUMEN DE GEORREFERENCIACIÓN")
    print("="*70)
    
    if exitosos:
        print(f"\n✓ Se georreferenciaron {len(exitosos)} imágenes:")
        for archivo in exitosos:
            base = archivo.replace('.tif', '')
            print(f"\n  {archivo}:")
            print(f"    • {base}.tfw (World File)")
            print(f"    • {base}.prj (Proyección)")
        
        print("\n✓ Las imágenes ahora están georreferenciadas y listas para:")
        print("  • Cargar en QGIS (arrastrar y soltar)")
        print("  • Cargar en ArcGIS")
        print("  • Usar con GDAL")
        print("  • Análisis espacial")
        
        print("\n✓ Para verificar en QGIS:")
        print("  1. Abrir QGIS")
        print("  2. Arrastrar los archivos .tif al canvas")
        print("  3. Las imágenes aparecerán en su ubicación correcta en Chile")
        
        print("\n✓ Archivos auxiliares creados:")
        print("  • .tfw: World File con parámetros de georreferenciación")
        print("  • .prj: Definición del sistema de coordenadas WGS84")
    else:
        print("✗ No se pudo georreferenciar ninguna imagen")

if __name__ == "__main__":
    main()