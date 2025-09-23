#!/usr/bin/env python3
import requests
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

def descargar_imagen_sentinel_chile():
    """
    Descarga una imagen Sentinel-2 de Valparaíso, Chile
    usando el servicio WMS de Copernicus
    """
    
    # Coordenadas de Valparaíso, Chile (zona costera representativa)
    # Bbox: longitud_min, latitud_min, longitud_max, latitud_max
    bbox = "-71.70,-33.10,-71.50,-32.95"
    
    # URL del servicio WMS de Sentinel Hub (servicio gratuito limitado)
    base_url = "https://services.sentinel-hub.com/ogc/wms/421e3c-YOUR-INSTANCEID-HERE"
    
    # Alternativa: usar servicio público de EOX
    # Este servicio proporciona imágenes Sentinel-2 cloudless
    eox_url = "https://tiles.maps.eox.at/wms"
    
    # Parámetros para la solicitud WMS
    params = {
        'service': 'WMS',
        'version': '1.3.0',
        'request': 'GetMap',
        'layers': 's2cloudless-2020',  # Capa de Sentinel-2 sin nubes
        'bbox': bbox,
        'width': 800,  # Ancho en píxeles (tamaño moderado)
        'height': 600,  # Alto en píxeles
        'srs': 'EPSG:4326',  # Sistema de coordenadas WGS84
        'format': 'image/jpeg',
        'transparent': 'false'
    }
    
    print("Descargando imagen satelital de Valparaíso, Chile...")
    print(f"Bbox: {bbox}")
    print(f"Tamaño: {params['width']}x{params['height']} píxeles")
    
    try:
        # Realizar la solicitud
        response = requests.get(eox_url, params=params, timeout=30)
        response.raise_for_status()
        
        # Guardar la imagen
        filename = "valparaiso_sentinel2_rgb.jpg"
        with open(filename, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Imagen descargada exitosamente: {filename}")
        
        # Abrir y mostrar información de la imagen
        img = Image.open(filename)
        print(f"✓ Formato: {img.format}")
        print(f"✓ Modo: {img.mode} (RGB = 3 bandas visibles)")
        print(f"✓ Tamaño: {img.size}")
        print(f"✓ Tamaño del archivo: {os.path.getsize(filename) / 1024:.1f} KB")
        
        # Mostrar la imagen
        plt.figure(figsize=(12, 8))
        plt.imshow(img)
        plt.title("Imagen Sentinel-2 RGB - Valparaíso, Chile\n(Bandas: Rojo, Verde, Azul)")
        plt.xlabel("Píxeles (Este-Oeste)")
        plt.ylabel("Píxeles (Norte-Sur)")
        plt.grid(True, alpha=0.3)
        
        # Guardar figura con metadatos
        plt.savefig("valparaiso_sentinel2_rgb_plot.png", dpi=100, bbox_inches='tight')
        print("✓ Figura guardada como: valparaiso_sentinel2_rgb_plot.png")
        
        # Verificar que tiene las 3 bandas RGB
        img_array = np.array(img)
        if len(img_array.shape) == 3 and img_array.shape[2] == 3:
            print("\n✓ CONFIRMADO: La imagen contiene las 3 bandas del espectro visible:")
            print("  - Banda 1: Rojo (R)")
            print("  - Banda 2: Verde (G)")  
            print("  - Banda 3: Azul (B)")
            
            # Estadísticas básicas de cada banda
            print("\nEstadísticas de las bandas:")
            for i, color in enumerate(['Rojo', 'Verde', 'Azul']):
                banda = img_array[:, :, i]
                print(f"  {color}: min={banda.min()}, max={banda.max()}, media={banda.mean():.1f}")
        
        return filename
        
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen: {e}")
        print("\nIntentando con método alternativo...")
        return descargar_alternativa()

def descargar_alternativa():
    """
    Método alternativo usando OpenStreetMap/ESRI como fuente
    """
    # Usar servicio de imágenes satelitales de ESRI
    esri_url = "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/export"
    
    # Coordenadas de Santiago de Chile (zona urbana/cordillera)
    params = {
        'bbox': '-70.75,-33.50,-70.55,-33.35',  # Santiago
        'bboxSR': '4326',
        'size': '800,600',
        'imageSR': '4326',
        'format': 'jpg',
        'f': 'image'
    }
    
    print("\nDescargando imagen alternativa de Santiago, Chile...")
    
    try:
        response = requests.get(esri_url, params=params, timeout=30)
        response.raise_for_status()
        
        filename = "santiago_satelital_rgb.jpg"
        with open(filename, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Imagen descargada: {filename}")
        
        # Verificar la imagen
        img = Image.open(filename)
        print(f"✓ Tamaño: {img.size}")
        print(f"✓ Modo: {img.mode}")
        print(f"✓ Tamaño del archivo: {os.path.getsize(filename) / 1024:.1f} KB")
        
        return filename
        
    except Exception as e:
        print(f"Error en descarga alternativa: {e}")
        return None

if __name__ == "__main__":
    resultado = descargar_imagen_sentinel_chile()
    if resultado:
        print(f"\n✅ Proceso completado. Imagen disponible: {resultado}")
        print("Esta imagen es ideal para tu presentación porque:")
        print("- Contiene las 3 bandas del espectro visible (RGB)")
        print("- Tamaño optimizado para presentaciones (~200-500 KB)")
        print("- Muestra una zona representativa de Chile")
        print("- Resolución adecuada para visualización y análisis")