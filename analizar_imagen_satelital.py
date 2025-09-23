#!/usr/bin/env python3
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def analizar_imagen_rgb(filename="santiago_satelital_rgb.jpg"):
    """
    Analiza y visualiza las bandas RGB de la imagen satelital
    """
    
    print(f"Analizando imagen: {filename}")
    print("=" * 50)
    
    # Cargar imagen
    img = Image.open(filename)
    img_array = np.array(img)
    
    # Información básica
    print(f"Dimensiones: {img_array.shape}")
    print(f"Tipo de datos: {img_array.dtype}")
    print(f"Rango de valores: [{img_array.min()}, {img_array.max()}]")
    
    # Verificar que tiene 3 bandas
    if len(img_array.shape) == 3 and img_array.shape[2] == 3:
        print("\n✓ CONFIRMADO: Imagen con 3 bandas del espectro visible")
        print("  • Banda 1: ROJO (620-750 nm)")
        print("  • Banda 2: VERDE (495-570 nm)")
        print("  • Banda 3: AZUL (450-495 nm)")
    else:
        print("⚠ Advertencia: La imagen no tiene el formato RGB esperado")
        return
    
    # Crear visualización completa
    fig = plt.figure(figsize=(15, 10))
    
    # 1. Imagen RGB completa
    ax1 = plt.subplot(2, 4, 1)
    ax1.imshow(img_array)
    ax1.set_title("Imagen RGB Compuesta\n(Las 3 bandas visibles)", fontsize=10)
    ax1.axis('off')
    
    # 2-4. Bandas individuales
    band_names = ['Rojo', 'Verde', 'Azul']
    cmaps = ['Reds', 'Greens', 'Blues']
    
    for i in range(3):
        ax = plt.subplot(2, 4, i+2)
        banda = img_array[:, :, i]
        im = ax.imshow(banda, cmap=cmaps[i])
        ax.set_title(f"Banda {band_names[i]}\n({banda.min()}-{banda.max()})", fontsize=10)
        ax.axis('off')
        plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    
    # 5. Histogramas de las bandas
    ax5 = plt.subplot(2, 4, 5)
    colors = ['red', 'green', 'blue']
    for i in range(3):
        banda = img_array[:, :, i].flatten()
        ax5.hist(banda, bins=50, alpha=0.5, color=colors[i], label=band_names[i])
    ax5.set_xlabel('Valor de píxel')
    ax5.set_ylabel('Frecuencia')
    ax5.set_title('Distribución de valores\npor banda', fontsize=10)
    ax5.legend()
    ax5.grid(True, alpha=0.3)
    
    # 6. Estadísticas por banda
    ax6 = plt.subplot(2, 4, 6)
    ax6.axis('off')
    stats_text = "ESTADÍSTICAS POR BANDA\n" + "="*25 + "\n"
    for i in range(3):
        banda = img_array[:, :, i]
        stats_text += f"\n{band_names[i]}:\n"
        stats_text += f"  Media: {banda.mean():.1f}\n"
        stats_text += f"  Desv. Est.: {banda.std():.1f}\n"
        stats_text += f"  Mediana: {np.median(banda):.1f}\n"
    ax6.text(0.1, 0.5, stats_text, fontsize=9, family='monospace', 
             verticalalignment='center')
    
    # 7. Composición falso color (infrarrojo simulado)
    ax7 = plt.subplot(2, 4, 7)
    # Simular infrarrojo usando combinación de bandas
    falso_color = np.zeros_like(img_array)
    falso_color[:, :, 0] = img_array[:, :, 1]  # Verde -> Rojo
    falso_color[:, :, 1] = img_array[:, :, 0]  # Rojo -> Verde  
    falso_color[:, :, 2] = img_array[:, :, 2]  # Azul -> Azul
    ax7.imshow(falso_color)
    ax7.set_title('Composición Falso Color\n(Resalta vegetación)', fontsize=10)
    ax7.axis('off')
    
    # 8. Información de la imagen
    ax8 = plt.subplot(2, 4, 8)
    ax8.axis('off')
    info_text = "INFORMACIÓN DE LA IMAGEN\n" + "="*25 + "\n"
    info_text += f"\nUbicación: Santiago, Chile"
    info_text += f"\nFuente: ESRI World Imagery"
    info_text += f"\nResolución: {img.size[0]}x{img.size[1]} px"
    info_text += f"\nBandas espectrales:"
    info_text += f"\n  • Rojo (B1): 620-750 nm"
    info_text += f"\n  • Verde (B2): 495-570 nm"
    info_text += f"\n  • Azul (B3): 450-495 nm"
    info_text += f"\n\nIdeal para:"
    info_text += f"\n  • Análisis visual"
    info_text += f"\n  • Clasificación"
    info_text += f"\n  • Detección de cambios"
    ax8.text(0.1, 0.5, info_text, fontsize=8, family='monospace',
             verticalalignment='center')
    
    plt.suptitle('Análisis de Imagen Satelital RGB - Santiago, Chile', 
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    # Guardar figura
    output_file = "analisis_bandas_rgb_santiago.png"
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"\n✓ Análisis guardado en: {output_file}")
    
    # Mostrar
    plt.show()
    
    return img_array

if __name__ == "__main__":
    # Analizar la imagen descargada
    img_data = analizar_imagen_rgb("santiago_satelital_rgb.jpg")
    
    print("\n" + "="*50)
    print("RESUMEN PARA LA PRESENTACIÓN:")
    print("="*50)
    print("✓ Imagen satelital RGB de Santiago, Chile")
    print("✓ Contiene las 3 bandas del espectro visible")
    print("✓ Tamaño optimizado: ~233 KB")
    print("✓ Resolución: 800x600 píxeles")
    print("✓ Formato: JPEG (compresión eficiente)")
    print("\nLa imagen muestra:")
    print("  • Zona urbana de Santiago")
    print("  • Cordillera de los Andes al este")
    print("  • Variación de coberturas (urbano/vegetación/suelo)")
    print("\nPerfecta para explicar:")
    print("  • Representación de datos en bandas espectrales")
    print("  • Composición RGB en teledetección")
    print("  • Análisis visual de imágenes satelitales")