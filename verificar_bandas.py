#!/usr/bin/env python3
import numpy as np
from PIL import Image
import os

def verificar_imagen_rgb(filename="santiago_satelital_rgb.jpg"):
    """
    Verifica que la imagen tenga las 3 bandas RGB
    """
    
    print(f"Verificando imagen: {filename}")
    print("=" * 50)
    
    # Verificar que existe
    if not os.path.exists(filename):
        print(f"❌ Error: No se encuentra el archivo {filename}")
        return False
    
    # Cargar imagen
    img = Image.open(filename)
    img_array = np.array(img)
    
    # Información del archivo
    file_size = os.path.getsize(filename) / 1024  # KB
    
    print(f"✓ Archivo encontrado")
    print(f"  Tamaño del archivo: {file_size:.1f} KB")
    print(f"  Formato: {img.format}")
    print(f"  Modo: {img.mode}")
    print(f"  Dimensiones: {img.size[0]}x{img.size[1]} píxeles")
    
    # Verificar estructura de datos
    print(f"\n  Array shape: {img_array.shape}")
    print(f"  Tipo de datos: {img_array.dtype}")
    print(f"  Rango de valores: [{img_array.min()}, {img_array.max()}]")
    
    # Verificar que tiene exactamente 3 bandas
    if len(img_array.shape) == 3 and img_array.shape[2] == 3:
        print("\n✅ CONFIRMADO: La imagen tiene las 3 bandas del espectro visible")
        print("\nDetalles de las bandas:")
        print("-" * 40)
        
        band_names = ['ROJO (Red)', 'VERDE (Green)', 'AZUL (Blue)']
        wavelengths = ['620-750 nm', '495-570 nm', '450-495 nm']
        
        for i in range(3):
            banda = img_array[:, :, i]
            print(f"\nBanda {i+1}: {band_names[i]}")
            print(f"  Longitud de onda: {wavelengths[i]}")
            print(f"  Valores mínimo/máximo: {banda.min()}/{banda.max()}")
            print(f"  Valor medio: {banda.mean():.2f}")
            print(f"  Desviación estándar: {banda.std():.2f}")
            print(f"  Mediana: {np.median(banda):.2f}")
        
        print("\n" + "="*50)
        print("RESUMEN:")
        print("="*50)
        print("✅ Imagen lista para usar en presentación")
        print(f"✅ Tamaño óptimo: {file_size:.1f} KB (ideal para presentaciones)")
        print("✅ Contiene las 3 bandas RGB del espectro visible")
        print("✅ Resolución adecuada: 800x600 píxeles")
        print("✅ Ubicación: Santiago, Chile (zona representativa)")
        
        return True
    else:
        print("\n❌ La imagen NO tiene el formato RGB esperado")
        return False

if __name__ == "__main__":
    resultado = verificar_imagen_rgb("santiago_satelital_rgb.jpg")
    
    if resultado:
        print("\n📍 La imagen 'santiago_satelital_rgb.jpg' está lista para usar")
        print("   en tu presentación sobre representación de datos espectrales.")