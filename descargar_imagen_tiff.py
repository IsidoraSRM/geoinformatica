#!/usr/bin/env python3
import requests
import numpy as np
from PIL import Image
import os
from io import BytesIO

def descargar_imagen_satelital_tiff():
    """
    Descarga una imagen satelital y la guarda en formato TIFF
    preservando las 3 bandas RGB sin compresión
    """
    
    print("="*60)
    print("DESCARGA DE IMAGEN SATELITAL EN FORMATO TIFF")
    print("="*60)
    
    # Opción 1: Santiago de Chile (zona urbana/cordillera)
    print("\n1. Descargando imagen de Santiago, Chile...")
    
    # Servicio ESRI World Imagery
    esri_url = "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/export"
    
    params_santiago = {
        'bbox': '-70.75,-33.50,-70.55,-33.35',  # Santiago centro
        'bboxSR': '4326',
        'size': '800,600',
        'imageSR': '4326',
        'format': 'png',  # Descargamos en PNG primero (sin pérdida)
        'f': 'image',
        'transparent': 'false'
    }
    
    try:
        response = requests.get(esri_url, params=params_santiago, timeout=30)
        response.raise_for_status()
        
        # Abrir imagen desde bytes
        img = Image.open(BytesIO(response.content))
        
        # Convertir a RGB si es necesario
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Guardar como TIFF sin compresión
        filename_tiff = "santiago_chile_rgb.tif"
        img.save(filename_tiff, format='TIFF', compression=None)
        
        print(f"✓ Imagen guardada como: {filename_tiff}")
        
        # Verificar el archivo TIFF
        verificar_tiff(filename_tiff)
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    # Opción 2: Valparaíso (zona costera)
    print("\n2. Descargando imagen de Valparaíso, Chile...")
    
    params_valparaiso = {
        'bbox': '-71.65,-33.05,-71.55,-32.95',  # Valparaíso
        'bboxSR': '4326',
        'size': '800,600',
        'imageSR': '4326',
        'format': 'png',
        'f': 'image',
        'transparent': 'false'
    }
    
    try:
        response = requests.get(esri_url, params=params_valparaiso, timeout=30)
        response.raise_for_status()
        
        img = Image.open(BytesIO(response.content))
        
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        filename_tiff = "valparaiso_chile_rgb.tif"
        img.save(filename_tiff, format='TIFF', compression=None)
        
        print(f"✓ Imagen guardada como: {filename_tiff}")
        
        verificar_tiff(filename_tiff)
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Opción 3: Zona con vegetación (La Araucanía)
    print("\n3. Descargando imagen de La Araucanía, Chile...")
    
    params_araucania = {
        'bbox': '-72.65,-38.75,-72.45,-38.60',  # Temuco y alrededores
        'bboxSR': '4326',
        'size': '800,600',
        'imageSR': '4326',
        'format': 'png',
        'f': 'image',
        'transparent': 'false'
    }
    
    try:
        response = requests.get(esri_url, params=params_araucania, timeout=30)
        response.raise_for_status()
        
        img = Image.open(BytesIO(response.content))
        
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        filename_tiff = "araucania_chile_rgb.tif"
        img.save(filename_tiff, format='TIFF', compression=None)
        
        print(f"✓ Imagen guardada como: {filename_tiff}")
        
        verificar_tiff(filename_tiff)
        
    except Exception as e:
        print(f"Error: {e}")

def verificar_tiff(filename):
    """
    Verifica que el archivo TIFF tenga las 3 bandas RGB correctamente
    """
    if not os.path.exists(filename):
        print(f"❌ No se encuentra el archivo {filename}")
        return
    
    # Abrir y verificar
    img = Image.open(filename)
    img_array = np.array(img)
    
    print(f"\n  Verificación de {filename}:")
    print(f"  • Formato: {img.format}")
    print(f"  • Modo: {img.mode}")
    print(f"  • Dimensiones: {img.size[0]}x{img.size[1]} píxeles")
    print(f"  • Tamaño archivo: {os.path.getsize(filename) / 1024:.1f} KB")
    
    # Verificar bandas
    if len(img_array.shape) == 3 and img_array.shape[2] == 3:
        print(f"  ✓ Confirmado: 3 bandas RGB")
        print(f"    - Banda Roja: min={img_array[:,:,0].min()}, max={img_array[:,:,0].max()}")
        print(f"    - Banda Verde: min={img_array[:,:,1].min()}, max={img_array[:,:,1].max()}")
        print(f"    - Banda Azul: min={img_array[:,:,2].min()}, max={img_array[:,:,2].max()}")
    else:
        print(f"  ❌ Problema con las bandas")

def crear_tiff_multiespectral_ejemplo():
    """
    Crea un ejemplo de TIFF con metadatos espectrales
    """
    print("\n" + "="*60)
    print("CREANDO TIFF DE EJEMPLO CON METADATOS")
    print("="*60)
    
    # Crear una imagen sintética de ejemplo con patrones
    width, height = 512, 512
    
    # Crear gradientes para simular una escena
    x = np.linspace(0, 1, width)
    y = np.linspace(0, 1, height)
    xx, yy = np.meshgrid(x, y)
    
    # Simular diferentes respuestas espectrales
    # Banda Roja: más intensa en zonas "urbanas" (esquina superior derecha)
    banda_roja = np.uint8(255 * (0.3 + 0.7 * xx * (1-yy)))
    
    # Banda Verde: más intensa en zonas de "vegetación" (centro)
    dist_centro = np.sqrt((xx - 0.5)**2 + (yy - 0.5)**2)
    banda_verde = np.uint8(255 * (0.2 + 0.8 * np.exp(-5 * dist_centro)))
    
    # Banda Azul: más intensa en zonas de "agua" (esquina inferior izquierda)
    banda_azul = np.uint8(255 * (0.3 + 0.7 * (1-xx) * yy))
    
    # Combinar las bandas
    img_array = np.stack([banda_roja, banda_verde, banda_azul], axis=2)
    
    # Crear imagen PIL
    img = Image.fromarray(img_array, mode='RGB')
    
    # Guardar como TIFF con metadatos
    filename = "ejemplo_multiespectral_rgb.tif"
    
    # Metadatos TIFF
    metadata = {
        'Software': 'Geoinformática UTFSM',
        'DocumentName': 'Imagen Satelital RGB de Ejemplo',
        'ImageDescription': 'Imagen con 3 bandas del espectro visible (R,G,B)',
        'Artist': 'Curso Geoinformática',
        'DateTime': '2024:01:01 12:00:00',
        'XResolution': (100, 1),
        'YResolution': (100, 1),
        'ResolutionUnit': 2  # Inches
    }
    
    img.save(filename, format='TIFF', compression=None, **metadata)
    
    print(f"✓ Imagen de ejemplo creada: {filename}")
    print(f"  • Tamaño: {width}x{height} píxeles")
    print(f"  • Bandas: RGB (simuladas)")
    print(f"  • Sin compresión (preserva valores originales)")
    print(f"  • Tamaño archivo: {os.path.getsize(filename) / 1024:.1f} KB")
    
    # Verificar
    verificar_tiff(filename)

if __name__ == "__main__":
    print("DESCARGADOR DE IMÁGENES SATELITALES - FORMATO TIFF")
    print("Formato TIFF preserva la información espectral sin pérdida")
    print("")
    
    # Descargar imágenes reales
    descargar_imagen_satelital_tiff()
    
    # Crear ejemplo sintético
    crear_tiff_multiespectral_ejemplo()
    
    print("\n" + "="*60)
    print("RESUMEN FINAL")
    print("="*60)
    print("✅ Imágenes disponibles en formato TIFF:")
    
    archivos_tiff = [f for f in os.listdir('.') if f.endswith('.tif')]
    for archivo in archivos_tiff:
        size = os.path.getsize(archivo) / 1024
        print(f"  • {archivo} ({size:.1f} KB)")
    
    print("\nEstas imágenes son ideales para tu presentación porque:")
    print("  • Formato TIFF sin compresión (sin pérdida de información)")
    print("  • Preservan los valores originales de las 3 bandas RGB")
    print("  • Tamaño manejable para presentaciones")
    print("  • Muestran zonas representativas de Chile")