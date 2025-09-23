#!/usr/bin/env python3
"""
Script para descargar bandas reales de Sentinel-2 usando PySTAC
Descarga las bandas B4 (Rojo) y B8 (NIR) necesarias para calcular NDVI
"""

import pystac_client
import planetary_computer
import rasterio
from rasterio.plot import show
import numpy as np
from PIL import Image
import os
from datetime import datetime
import requests

def buscar_imagenes_sentinel2(bbox, fecha_inicio="2024-01-01", fecha_fin="2024-12-31"):
    """
    Busca imágenes de Sentinel-2 en el catálogo de Microsoft Planetary Computer
    """
    # Cliente STAC de Planetary Computer
    catalog = pystac_client.Client.open(
        "https://planetarycomputer.microsoft.com/api/stac/v1",
        modifier=planetary_computer.sign_inplace,
    )
    
    # Búsqueda en el catálogo
    search = catalog.search(
        collections=["sentinel-2-l2a"],  # Sentinel-2 Level 2A (corregido atmosféricamente)
        bbox=bbox,
        datetime=f"{fecha_inicio}/{fecha_fin}",
        query={"eo:cloud_cover": {"lt": 20}},  # Menos de 20% de nubes
    )
    
    # Obtener items
    items = list(search.items())
    
    if len(items) == 0:
        print("No se encontraron imágenes para esta zona y fecha")
        return None
    
    # Ordenar por menor cobertura de nubes
    items.sort(key=lambda x: x.properties.get("eo:cloud_cover", 100))
    
    print(f"Se encontraron {len(items)} imágenes")
    
    # Usar la imagen con menos nubes
    item = items[0]
    print(f"Usando imagen del {item.datetime.strftime('%Y-%m-%d')} con {item.properties['eo:cloud_cover']:.1f}% de nubes")
    
    return item

def descargar_banda(item, banda_nombre, output_file, bbox=None):
    """
    Descarga una banda específica de un item de Sentinel-2
    """
    # Obtener el asset de la banda
    asset = item.assets[banda_nombre]
    
    # Obtener la URL firmada
    href = asset.href
    
    print(f"  Descargando banda {banda_nombre} desde: {href[:50]}...")
    
    # Si queremos recortar a un bbox específico, usamos rasterio
    with rasterio.open(href) as src:
        if bbox:
            from rasterio.mask import mask
            from shapely.geometry import box
            
            # Crear geometría del bbox
            lon_min, lat_min, lon_max, lat_max = bbox
            geom = box(lon_min, lat_min, lon_max, lat_max)
            
            # Recortar
            out_image, out_transform = mask(src, [geom], crop=True)
            out_meta = src.meta.copy()
            
            # Actualizar metadatos
            out_meta.update({
                "driver": "GTiff",
                "height": out_image.shape[1],
                "width": out_image.shape[2],
                "transform": out_transform,
                "compress": "none"
            })
            
            # Guardar
            with rasterio.open(output_file, "w", **out_meta) as dest:
                dest.write(out_image)
        else:
            # Descargar banda completa (puede ser muy grande)
            # Para este ejercicio, mejor descargar una submuestra
            
            # Leer una ventana más pequeña
            height, width = src.height, src.width
            
            # Calcular ventana de 800x600 centrada
            row_off = max(0, (height - 600) // 2)
            col_off = max(0, (width - 800) // 2)
            
            window = rasterio.windows.Window(col_off, row_off, 
                                            min(800, width), min(600, height))
            
            # Leer datos
            data = src.read(1, window=window)
            
            # Obtener transformación para la ventana
            transform = src.window_transform(window)
            
            # Guardar
            profile = src.profile.copy()
            profile.update({
                'driver': 'GTiff',
                'height': data.shape[0],
                'width': data.shape[1],
                'count': 1,
                'dtype': data.dtype,
                'transform': transform,
                'compress': 'none'
            })
            
            with rasterio.open(output_file, 'w', **profile) as dst:
                dst.write(data, 1)
    
    print(f"  ✓ Banda guardada: {output_file}")
    
    # Verificar el archivo
    with rasterio.open(output_file) as src:
        print(f"    Dimensiones: {src.width}x{src.height}")
        print(f"    CRS: {src.crs}")
        data = src.read(1)
        print(f"    Valores: min={data.min()}, max={data.max()}, mean={data.mean():.1f}")
    
    return output_file

def calcular_ndvi_real(b4_red_file, b8_nir_file, output_ndvi):
    """
    Calcula el NDVI real usando las bandas de Sentinel-2
    """
    print("\nCalculando NDVI con bandas reales...")
    
    # Abrir bandas
    with rasterio.open(b4_red_file) as red_src:
        red = red_src.read(1).astype(float)
        profile = red_src.profile.copy()
        transform = red_src.transform
    
    with rasterio.open(b8_nir_file) as nir_src:
        nir = nir_src.read(1).astype(float)
    
    # Calcular NDVI
    # Evitar división por cero
    denominador = nir + red
    denominador[denominador == 0] = 0.0001
    
    ndvi = (nir - red) / denominador
    
    # Guardar NDVI como float32
    profile.update({
        'dtype': 'float32',
        'count': 1,
        'compress': 'none'
    })
    
    with rasterio.open(output_ndvi, 'w', **profile) as dst:
        dst.write(ndvi.astype('float32'), 1)
    
    print(f"✓ NDVI calculado: {output_ndvi}")
    print(f"  Rango NDVI: [{ndvi.min():.3f}, {ndvi.max():.3f}]")
    print(f"  NDVI promedio: {ndvi.mean():.3f}")
    
    # Interpretación
    print("\n  Interpretación del NDVI:")
    agua = np.sum(ndvi < 0.0) / ndvi.size * 100
    suelo = np.sum((ndvi >= 0.0) & (ndvi < 0.2)) / ndvi.size * 100
    veg_escasa = np.sum((ndvi >= 0.2) & (ndvi < 0.4)) / ndvi.size * 100
    veg_moderada = np.sum((ndvi >= 0.4) & (ndvi < 0.6)) / ndvi.size * 100
    veg_densa = np.sum(ndvi >= 0.6) / ndvi.size * 100
    
    print(f"  • Agua/No vegetado: {agua:.1f}%")
    print(f"  • Suelo desnudo: {suelo:.1f}%")
    print(f"  • Vegetación escasa: {veg_escasa:.1f}%")
    print(f"  • Vegetación moderada: {veg_moderada:.1f}%")
    print(f"  • Vegetación densa: {veg_densa:.1f}%")
    
    # Crear visualización en colores para presentación
    ndvi_visual = np.zeros((ndvi.shape[0], ndvi.shape[1], 3), dtype=np.uint8)
    
    # Colormap: Rojo (sin vegetación) -> Amarillo -> Verde (vegetación densa)
    for i in range(ndvi.shape[0]):
        for j in range(ndvi.shape[1]):
            valor = ndvi[i, j]
            if valor < 0:  # Agua - azul
                ndvi_visual[i, j] = [0, 0, 255]
            elif valor < 0.2:  # Suelo - marrón
                ndvi_visual[i, j] = [139, 90, 43]
            elif valor < 0.4:  # Vegetación escasa - amarillo
                ndvi_visual[i, j] = [255, 255, 0]
            elif valor < 0.6:  # Vegetación moderada - verde claro
                ndvi_visual[i, j] = [124, 252, 0]
            else:  # Vegetación densa - verde oscuro
                ndvi_visual[i, j] = [0, 128, 0]
    
    # Guardar visualización
    visual_file = output_ndvi.replace('.tif', '_visual.tif')
    img_visual = Image.fromarray(ndvi_visual)
    img_visual.save(visual_file)
    print(f"  ✓ Visualización guardada: {visual_file}")
    
    return ndvi

def main():
    print("="*70)
    print("DESCARGA DE BANDAS REALES SENTINEL-2 PARA NDVI")
    print("="*70)
    
    # Definir zonas (mismas que antes)
    zonas = [
        {
            'nombre': 'Santiago',
            'bbox': [-70.75, -33.50, -70.55, -33.35],
            'prefix': 'santiago_real'
        },
        {
            'nombre': 'Valparaíso',
            'bbox': [-71.65, -33.05, -71.55, -32.95],
            'prefix': 'valparaiso_real'
        },
        {
            'nombre': 'La Araucanía',
            'bbox': [-72.65, -38.75, -72.45, -38.60],
            'prefix': 'araucania_real'
        }
    ]
    
    # Procesar cada zona
    for zona in zonas:
        print(f"\n{'='*50}")
        print(f"Procesando: {zona['nombre']}")
        print(f"BBox: {zona['bbox']}")
        print(f"{'='*50}")
        
        try:
            # Buscar imagen
            item = buscar_imagenes_sentinel2(
                zona['bbox'],
                fecha_inicio="2023-01-01",
                fecha_fin="2024-12-31"
            )
            
            if item is None:
                continue
            
            # Descargar banda B4 (Rojo - 665nm)
            b4_file = f"{zona['prefix']}_B04_red.tif"
            print(f"\nDescargando Banda 4 (Rojo - 665nm)...")
            descargar_banda(item, "B04", b4_file)
            
            # Descargar banda B8 (NIR - 842nm)
            b8_file = f"{zona['prefix']}_B08_nir.tif"
            print(f"\nDescargando Banda 8 (NIR - 842nm)...")
            descargar_banda(item, "B08", b8_file)
            
            # Calcular NDVI
            ndvi_file = f"{zona['prefix']}_ndvi.tif"
            calcular_ndvi_real(b4_file, b8_file, ndvi_file)
            
            # También descargar RGB para referencia
            print("\nDescargando bandas RGB para referencia...")
            descargar_banda(item, "B02", f"{zona['prefix']}_B02_blue.tif")  # Azul
            descargar_banda(item, "B03", f"{zona['prefix']}_B03_green.tif")  # Verde
            
        except Exception as e:
            print(f"Error procesando {zona['nombre']}: {e}")
            continue
    
    print("\n" + "="*70)
    print("RESUMEN PARA EL EJERCICIO DE NDVI")
    print("="*70)
    print("\n✓ Bandas descargadas de Sentinel-2 (datos reales):")
    print("  • *_B04_red.tif: Banda 4 - Rojo (665 nm)")
    print("  • *_B08_nir.tif: Banda 8 - NIR (842 nm)")
    print("  • *_ndvi.tif: NDVI calculado")
    print("  • *_ndvi_visual.tif: Visualización en colores")
    
    print("\n✓ Fórmula NDVI para Sentinel-2:")
    print("  NDVI = (B8 - B4) / (B8 + B4)")
    print("  Donde:")
    print("  - B8 = Banda del infrarrojo cercano (842 nm)")
    print("  - B4 = Banda del rojo (665 nm)")
    
    print("\n✓ Todas las bandas están georreferenciadas con CRS correcto")
    print("✓ Datos atmosféricamente corregidos (Level 2A)")

if __name__ == "__main__":
    main()