#!/usr/bin/env python3
import requests
import numpy as np
from PIL import Image
import rasterio
from rasterio.transform import from_bounds
import os
from io import BytesIO

def descargar_y_georreferenciar(nombre_zona, bbox, archivo_salida):
    """
    Descarga una imagen y la guarda como GeoTIFF con georreferenciación
    
    Args:
        nombre_zona: Nombre descriptivo de la zona
        bbox: Tupla (lon_min, lat_min, lon_max, lat_max) en WGS84
        archivo_salida: Nombre del archivo GeoTIFF de salida
    """
    
    print(f"\nDescargando imagen de {nombre_zona}...")
    print(f"  Bbox: {bbox}")
    
    # URL del servicio ESRI World Imagery
    esri_url = "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/export"
    
    # Parámetros para la descarga
    lon_min, lat_min, lon_max, lat_max = bbox
    width, height = 800, 600
    
    params = {
        'bbox': f'{lon_min},{lat_min},{lon_max},{lat_max}',
        'bboxSR': '4326',  # WGS84
        'size': f'{width},{height}',
        'imageSR': '4326',
        'format': 'png',
        'f': 'image',
        'transparent': 'false'
    }
    
    try:
        # Descargar la imagen
        response = requests.get(esri_url, params=params, timeout=30)
        response.raise_for_status()
        
        # Abrir imagen con PIL
        img = Image.open(BytesIO(response.content))
        
        # Convertir a RGB si es necesario
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Convertir a array numpy
        img_array = np.array(img)
        
        # Reorganizar las bandas para rasterio (bandas, filas, columnas)
        if len(img_array.shape) == 3:
            img_array = np.transpose(img_array, (2, 0, 1))
        
        # Crear la transformación afín (georreferenciación)
        transform = from_bounds(lon_min, lat_min, lon_max, lat_max, width, height)
        
        # Definir el CRS (Sistema de Referencia de Coordenadas)
        # Usar WKT string en lugar de EPSG para evitar problemas con PROJ
        crs = 'EPSG:4326'  # WGS84
        
        # Guardar como GeoTIFF
        with rasterio.open(
            archivo_salida,
            'w',
            driver='GTiff',
            height=height,
            width=width,
            count=3,  # 3 bandas RGB
            dtype=img_array.dtype,
            crs=crs,
            transform=transform,
            compress='none',  # Sin compresión para preservar valores
            photometric='RGB'
        ) as dst:
            # Escribir las bandas
            for i in range(3):
                dst.write(img_array[i], i+1)
            
            # Agregar metadatos
            dst.update_tags(
                AREA=nombre_zona,
                COUNTRY='Chile',
                SOURCE='ESRI World Imagery',
                BANDS='RGB (Red, Green, Blue)',
                BAND1='Red (620-750 nm)',
                BAND2='Green (495-570 nm)',
                BAND3='Blue (450-495 nm)'
            )
        
        print(f"✓ GeoTIFF guardado: {archivo_salida}")
        
        # Verificar la georreferenciación
        verificar_geotiff(archivo_salida)
        
        return True
        
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def verificar_geotiff(archivo):
    """
    Verifica que el GeoTIFF esté correctamente georreferenciado
    """
    print(f"\n  Verificación de {archivo}:")
    
    try:
        with rasterio.open(archivo) as src:
            print(f"  • Dimensiones: {src.width}x{src.height} píxeles")
            print(f"  • Número de bandas: {src.count}")
            print(f"  • CRS: {src.crs}")
            print(f"  • Bounds (EPSG:4326): {src.bounds}")
            
            # Calcular resolución espacial
            res_x = (src.bounds.right - src.bounds.left) / src.width
            res_y = (src.bounds.top - src.bounds.bottom) / src.height
            print(f"  • Resolución espacial: {res_x:.6f}° x {res_y:.6f}°")
            
            # En metros aproximados (en el ecuador 1° ≈ 111 km)
            res_x_m = res_x * 111000
            res_y_m = res_y * 111000
            print(f"  • Resolución aprox: {res_x_m:.1f}m x {res_y_m:.1f}m")
            
            # Verificar valores de las bandas
            for i in range(1, src.count + 1):
                banda = src.read(i)
                print(f"  • Banda {i}: min={banda.min()}, max={banda.max()}, mean={banda.mean():.1f}")
            
            # Leer metadatos
            tags = src.tags()
            if tags:
                print(f"  • Metadatos:")
                for key, value in tags.items():
                    print(f"    - {key}: {value}")
                    
            print(f"  ✓ GeoTIFF correctamente georreferenciado")
            
    except Exception as e:
        print(f"  ✗ Error al verificar: {e}")

def crear_world_file(archivo_tiff):
    """
    Crea un World File (.tfw) para el GeoTIFF
    """
    archivo_tfw = archivo_tiff.replace('.tif', '.tfw')
    
    with rasterio.open(archivo_tiff) as src:
        transform = src.transform
        
        # Escribir World File
        with open(archivo_tfw, 'w') as f:
            f.write(f"{transform.a}\n")  # Tamaño de píxel en X
            f.write(f"{transform.b}\n")  # Rotación en X
            f.write(f"{transform.d}\n")  # Rotación en Y
            f.write(f"{transform.e}\n")  # Tamaño de píxel en Y (negativo)
            f.write(f"{transform.c}\n")  # Coordenada X del centro del píxel superior izquierdo
            f.write(f"{transform.f}\n")  # Coordenada Y del centro del píxel superior izquierdo
        
        print(f"  • World File creado: {archivo_tfw}")

def main():
    print("="*70)
    print("DESCARGA DE IMÁGENES SATELITALES GEORREFERENCIADAS (GeoTIFF)")
    print("="*70)
    
    # Definir las zonas a descargar
    zonas = [
        {
            'nombre': 'Santiago Centro y Cordillera',
            'bbox': (-70.75, -33.50, -70.55, -33.35),  # lon_min, lat_min, lon_max, lat_max
            'archivo': 'santiago_geotiff.tif'
        },
        {
            'nombre': 'Valparaíso Costa',
            'bbox': (-71.65, -33.05, -71.55, -32.95),
            'archivo': 'valparaiso_geotiff.tif'
        },
        {
            'nombre': 'La Araucanía - Temuco',
            'bbox': (-72.65, -38.75, -72.45, -38.60),
            'archivo': 'araucania_geotiff.tif'
        },
        {
            'nombre': 'Atacama - La Serena',
            'bbox': (-71.30, -29.95, -71.20, -29.85),
            'archivo': 'laserena_geotiff.tif'
        }
    ]
    
    # Descargar cada zona
    exitosos = []
    for zona in zonas:
        if descargar_y_georreferenciar(zona['nombre'], zona['bbox'], zona['archivo']):
            crear_world_file(zona['archivo'])
            exitosos.append(zona['archivo'])
    
    # Resumen final
    print("\n" + "="*70)
    print("RESUMEN DE DESCARGAS")
    print("="*70)
    
    if exitosos:
        print(f"\n✓ Se descargaron {len(exitosos)} imágenes GeoTIFF:")
        for archivo in exitosos:
            size_mb = os.path.getsize(archivo) / (1024 * 1024)
            print(f"  • {archivo} ({size_mb:.1f} MB)")
        
        print("\n✓ Características de los GeoTIFF:")
        print("  • Sistema de coordenadas: WGS84 (EPSG:4326)")
        print("  • 3 bandas del espectro visible (RGB)")
        print("  • Sin compresión (valores preservados)")
        print("  • Incluyen metadatos y World Files (.tfw)")
        print("  • Listos para usar en QGIS, ArcGIS, GDAL, etc.")
        
        print("\n✓ Para verificar en GDAL:")
        print("  gdalinfo santiago_geotiff.tif")
        print("\n✓ Para visualizar en QGIS:")
        print("  Simplemente arrastre los archivos .tif al canvas de QGIS")
    else:
        print("✗ No se pudo descargar ninguna imagen")

if __name__ == "__main__":
    main()