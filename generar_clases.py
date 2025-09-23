#!/usr/bin/env python3
"""
Generador de templates LaTeX para el curso de Geoinformática
Semestre 2, 2025 - USACH
"""

import os
from datetime import datetime

# Definición de todas las clases del semestre
CLASES_TEORICAS = [
    {
        "numero": 1,
        "titulo": "Introducción a la Geoinformática",
        "subtitulo": "Fundamentos de Geocomputación y Datos Geoespaciales",
        "contenido": [
            "Presentación del curso",
            "¿Qué es la Geocomputación?",
            "Aplicaciones en el mundo real",
            "Evaluación diagnóstica"
        ]
    },
    {
        "numero": 2,
        "titulo": "Fundamentos de datos geoespaciales",
        "subtitulo": "Tipos y estructuras de datos espaciales",
        "contenido": [
            "Datos vectoriales: puntos, líneas, polígonos",
            "Datos raster: grillas y resolución",
            "Formatos de archivos (Shapefile, GeoJSON, GeoTIFF)",
            "Atributos y geometrías"
        ]
    },
    {
        "numero": 3,
        "titulo": "Sistemas de Referencia de Coordenadas",
        "subtitulo": "CRS y proyecciones cartográficas",
        "contenido": [
            "Coordenadas geográficas vs proyectadas",
            "Proyecciones cartográficas",
            "CRS en Chile (UTM, WGS84)",
            "Transformación de coordenadas"
        ]
    },
    {
        "numero": 4,
        "titulo": "Datos raster y su representación",
        "subtitulo": "Estructura y aplicaciones de datos raster",
        "contenido": [
            "Estructura de datos raster",
            "Álgebra de mapas básica",
            "Modelos digitales de elevación",
            "Imágenes satelitales"
        ]
    },
    {
        "numero": 5,
        "titulo": "Operaciones con atributos",
        "subtitulo": "Manipulación de datos espaciales",
        "contenido": [
            "Selección y filtrado",
            "Uniones espaciales",
            "Agregación de datos",
            "Cálculo de nuevos atributos"
        ]
    },
    {
        "numero": 6,
        "titulo": "Operaciones espaciales vectoriales",
        "subtitulo": "Geoprocesamiento con datos vectoriales",
        "contenido": [
            "Buffer, intersección, unión",
            "Predicados espaciales",
            "Queries espaciales",
            "Operaciones de overlay"
        ]
    },
    {
        "numero": 7,
        "titulo": "Operaciones raster avanzadas",
        "subtitulo": "Análisis y procesamiento de datos raster",
        "contenido": [
            "Álgebra de mapas compleja",
            "Reclasificación",
            "Operaciones focales y zonales",
            "Análisis multicriterio"
        ]
    },
    {
        "numero": 8,
        "titulo": "Interacciones raster-vector",
        "subtitulo": "Integración de diferentes tipos de datos",
        "contenido": [
            "Extracción de valores raster",
            "Rasterización",
            "Vectorización",
            "Casos de uso"
        ]
    },
    {
        "numero": 9,
        "titulo": "Fundamentos de cartografía digital",
        "subtitulo": "Principios de diseño de mapas",
        "contenido": [
            "Elementos de un mapa",
            "Simbolización efectiva",
            "Diseño cartográfico",
            "Introducción a tmap"
        ]
    },
    {
        "numero": 10,
        "titulo": "Visualización interactiva",
        "subtitulo": "Mapas web y dashboards",
        "contenido": [
            "Mapas interactivos con leaflet",
            "Publicación web",
            "Dashboards geoespaciales",
            "Plotly y mapview"
        ]
    },
    {
        "numero": 11,
        "titulo": "Automatización y scripting",
        "subtitulo": "Programación para geoprocesamiento",
        "contenido": [
            "Funciones personalizadas",
            "Automatización de tareas",
            "Buenas prácticas",
            "Manejo de errores"
        ]
    },
    {
        "numero": 12,
        "titulo": "Integración con otros software GIS",
        "subtitulo": "Interoperabilidad y APIs",
        "contenido": [
            "Puentes R/Python - QGIS",
            "GDAL/OGR",
            "APIs geoespaciales",
            "Bases de datos espaciales"
        ]
    },
    {
        "numero": 13,
        "titulo": "Statistical Learning con datos espaciales",
        "subtitulo": "Análisis estadístico espacial",
        "contenido": [
            "Autocorrelación espacial",
            "Modelos de regresión espacial",
            "Clustering espacial",
            "Validación cruzada"
        ]
    },
    {
        "numero": 14,
        "titulo": "Aplicaciones específicas",
        "subtitulo": "Casos de uso en diferentes dominios",
        "contenido": [
            "Geomarketing",
            "Aplicaciones ambientales",
            "Análisis de transporte",
            "Smart Cities"
        ]
    },
    {
        "numero": 15,
        "titulo": "Tendencias y futuro de la Geoinformática",
        "subtitulo": "Tecnologías emergentes",
        "contenido": [
            "Big Data geoespacial",
            "Machine Learning y Deep Learning",
            "Computación en la nube",
            "Gemelos digitales"
        ]
    }
]

LABORATORIOS = [
    {
        "numero": 1,
        "titulo": "Configuración del ambiente",
        "subtitulo": "Instalación y primeros pasos",
        "objetivos": [
            "Instalar R, RStudio y Python",
            "Configurar paquetes básicos",
            "Primer contacto con datos geoespaciales",
            "Verificar instalación"
        ]
    },
    {
        "numero": 2,
        "titulo": "Manipulación básica de datos vectoriales",
        "subtitulo": "Trabajando con sf en R",
        "objetivos": [
            "Lectura de archivos espaciales",
            "Exploración de datos",
            "Operaciones básicas",
            "Visualización simple"
        ]
    },
    {
        "numero": 3,
        "titulo": "Trabajando con CRS",
        "subtitulo": "Proyecciones y transformaciones",
        "objetivos": [
            "Identificar CRS",
            "Transformar coordenadas",
            "Resolver problemas de CRS",
            "Ejercicios prácticos"
        ]
    },
    {
        "numero": 4,
        "titulo": "Manipulación de datos raster + Inicio proyecto",
        "subtitulo": "Terra y formación de grupos",
        "objetivos": [
            "Trabajar con terra",
            "Operaciones básicas raster",
            "Formar grupos de proyecto",
            "Brainstorming inicial"
        ]
    },
    {
        "numero": 5,
        "titulo": "Manipulación de atributos",
        "subtitulo": "dplyr + sf",
        "objetivos": [
            "Filtrado y selección",
            "Joins espaciales",
            "Agregación de datos",
            "Mini-proyecto demográfico"
        ]
    },
    {
        "numero": 6,
        "titulo": "Geoprocesamiento vectorial + Propuesta proyecto",
        "subtitulo": "Análisis espacial y proyecto",
        "objetivos": [
            "Implementar buffers",
            "Análisis de proximidad",
            "Entregar propuesta de proyecto",
            "Overlay de capas"
        ]
    },
    {
        "numero": 7,
        "titulo": "Análisis raster",
        "subtitulo": "Procesamiento avanzado",
        "objetivos": [
            "Cálculo de pendientes",
            "Análisis de visibilidad",
            "Estadísticas zonales",
            "Análisis de riesgo"
        ]
    },
    {
        "numero": 8,
        "titulo": "Integración raster-vector",
        "subtitulo": "Combinando tipos de datos",
        "objetivos": [
            "Extracción de valores",
            "Conversión entre formatos",
            "Análisis combinado",
            "Ejercicio integrador"
        ]
    },
    {
        "numero": 9,
        "titulo": "Creación de mapas + Plan de proyecto",
        "subtitulo": "Cartografía y planificación",
        "objetivos": [
            "Diseño con tmap",
            "Definición formal del proyecto",
            "Personalización de mapas",
            "Revisión de datos"
        ]
    },
    {
        "numero": 10,
        "titulo": "Mapas interactivos",
        "subtitulo": "Visualización web",
        "objetivos": [
            "Crear mapas con leaflet",
            "Añadir interactividad",
            "Publicación web",
            "Popups y controles"
        ]
    },
    {
        "numero": 11,
        "titulo": "Scripts + Primer avance proyecto",
        "subtitulo": "Automatización y revisión",
        "objetivos": [
            "Funciones reutilizables",
            "Procesamiento batch",
            "Primer avance del proyecto",
            "Feedback personalizado"
        ]
    },
    {
        "numero": 12,
        "titulo": "Integración de herramientas",
        "subtitulo": "APIs y servicios",
        "objetivos": [
            "Conexión con WMS/WFS",
            "APIs geoespaciales",
            "PostGIS básico",
            "Interoperabilidad"
        ]
    },
    {
        "numero": 13,
        "titulo": "Análisis estadístico + Segundo avance",
        "subtitulo": "Estadística espacial y proyecto",
        "objetivos": [
            "Autocorrelación espacial",
            "Hotspots",
            "Segundo avance proyecto",
            "Revisión de resultados"
        ]
    },
    {
        "numero": 14,
        "titulo": "Trabajo en proyecto",
        "subtitulo": "Desarrollo intensivo",
        "objetivos": [
            "Desarrollo del proyecto",
            "Resolución de problemas",
            "Análisis avanzados",
            "Visualizaciones finales"
        ]
    },
    {
        "numero": 15,
        "titulo": "Últimos ajustes proyecto",
        "subtitulo": "Preparación final",
        "objetivos": [
            "Ajustes finales",
            "Preparación de presentación",
            "Ensayo opcional",
            "Documentación completa"
        ]
    }
]

def generar_template_base():
    """Genera el template base común para todas las clases"""
    return """\\documentclass[10pt]{{beamer}}
\\usetheme{{metropolis}}
\\usepackage{{FiraSans}}
\\usefonttheme{{professionalfonts}}

\\usepackage{{graphicx}}
\\usepackage{{tikz}}
\\usepackage[spanish]{{babel}}
\\usepackage{{tcolorbox}}
\\usepackage{{ragged2e}}
\\usepackage{{pgfplots}}
\\pgfplotsset{{compat=1.18}}
\\usepackage{{listings}}
\\usepackage{{xcolor}}

\\definecolor{{codegreen}}{{rgb}}{{0,0.6,0}}
\\definecolor{{codegray}}{{rgb}}{{0.5,0.5,0.5}}
\\definecolor{{codepurple}}{{rgb}}{{0.58,0,0.82}}
\\definecolor{{backcolour}}{{rgb}}{{0.95,0.95,0.92}}

\\lstdefinestyle{{mystyle}}{{
    backgroundcolor=\\color{{backcolour}},   
    commentstyle=\\color{{codegreen}},
    keywordstyle=\\color{{magenta}},
    numberstyle=\\tiny\\color{{codegray}},
    stringstyle=\\color{{codepurple}},
    basicstyle=\\ttfamily\\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2
}}

\\lstset{{style=mystyle}}

\\newcommand{{\\examplebox}}[2]{{
\\begin{{tcolorbox}}[colframe=darkcardinal,colback=boxgray,title=#1]
#2
\\end{{tcolorbox}}
}}

% Personalización del pie de página
\\setbeamertemplate{{footline}}{{%
  \\begin{{beamercolorbox}}[wd=\\paperwidth,sep=2ex]{{footline}}%
    \\usebeamerfont{{structure}}\\textbf{{Geoinformática - {tipo}}} \\hfill Profesor: Francisco Parra O. \\hfill \\textbf{{Semestre 2, 2025}}
  \\end{{beamercolorbox}}%
}}

\\title{{{titulo}}}
\\subtitle{{{subtitulo}}}
\\author{{Profesor: Francisco Parra O.}}
\\institute{{USACH - Ingeniería Civil en Informática}}
\\date{{\\today}}

\\titlegraphic{{%
  \\begin{{tikzpicture}}[overlay, remember picture]
    \\node[anchor=north east, yshift=0cm] at (current page.north east) {{
      \\includegraphics[width=1.5cm]{{Logo-Color-Usach-Web.jpg}}
    }};
  \\end{{tikzpicture}}
}}

\\begin{{document}}

\\maketitle

\\begin{{frame}}{{Agenda}}
    \\tableofcontents
\\end{{frame}}

{contenido}

\\begin{{frame}}{{Cierre}}
    \\begin{{center}}
        \\Large{{¿Preguntas?}}
        
        \\vspace{{1cm}}
        
        Próxima clase: {proxima}
    \\end{{center}}
\\end{{frame}}

\\end{{document}}"""

def generar_clase_teorica(clase, numero):
    """Genera el contenido específico para una clase teórica"""
    contenido = ""
    
    # Generar secciones basadas en el contenido
    for item in clase["contenido"]:
        contenido += f"""
\\section{{{item}}}

\\begin{{frame}}{{{item}}}
    % Contenido a desarrollar
    \\begin{{itemize}}
        \\item Punto 1
        \\item Punto 2
        \\item Punto 3
    \\end{{itemize}}
\\end{{frame}}
"""
    
    # Información de próxima clase
    if numero < 15:
        proxima = f"Laboratorio {numero}"
    else:
        proxima = "Presentaciones finales"
    
    template = generar_template_base()
    return template.format(
        tipo=f"Clase {numero}",
        titulo=f"Clase {numero:02d}: {clase['titulo']}",
        subtitulo=clase["subtitulo"],
        contenido=contenido,
        proxima=proxima
    )

def generar_laboratorio(lab, numero):
    """Genera el contenido específico para un laboratorio"""
    contenido = ""
    
    # Sección de objetivos
    contenido += """
\\section{Objetivos del laboratorio}

\\begin{frame}{Objetivos}
    \\begin{itemize}
"""
    for obj in lab["objetivos"]:
        contenido += f"        \\item {obj}\n"
    
    contenido += """    \\end{itemize}
\\end{frame}
"""
    
    # Secciones de práctica
    contenido += """
\\section{Actividades prácticas}

\\begin{frame}{Ejercicio 1}
    % Descripción del ejercicio
    \\begin{itemize}
        \\item Instrucción 1
        \\item Instrucción 2
        \\item Resultado esperado
    \\end{itemize}
\\end{frame}

\\begin{frame}[fragile]{Código de ejemplo}
    \\begin{lstlisting}[language=R]
# Código R de ejemplo
library(sf)
# Más código aquí
    \\end{lstlisting}
\\end{frame}

\\section{Tarea}

\\begin{frame}{Para la próxima clase}
    \\begin{itemize}
        \\item Completar ejercicios
        \\item Revisar material complementario
        \\item Preparar preguntas
    \\end{itemize}
\\end{frame}
"""
    
    # Información de próxima clase
    if numero < 15:
        proxima = f"Clase teórica {numero + 1}"
    else:
        proxima = "Presentaciones de proyectos"
    
    template = generar_template_base()
    return template.format(
        tipo=f"Laboratorio {numero}",
        titulo=f"Laboratorio {numero:02d}: {lab['titulo']}",
        subtitulo=lab["subtitulo"],
        contenido=contenido,
        proxima=proxima
    )

def main():
    """Función principal para generar todos los archivos"""
    
    # Crear directorios si no existen
    os.makedirs("clases/teoricas", exist_ok=True)
    os.makedirs("clases/laboratorios", exist_ok=True)
    
    # Generar clases teóricas
    print("Generando clases teóricas...")
    for i, clase in enumerate(CLASES_TEORICAS, 1):
        contenido = generar_clase_teorica(clase, i)
        filename = f"clases/teoricas/clase{i:02d}_{clase['titulo'].lower().replace(' ', '_')[:20]}.tex"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(contenido)
        print(f"  ✓ Clase {i:02d}: {clase['titulo']}")
    
    # Generar laboratorios
    print("\nGenerando laboratorios...")
    for i, lab in enumerate(LABORATORIOS, 1):
        contenido = generar_laboratorio(lab, i)
        filename = f"clases/laboratorios/lab{i:02d}_{lab['titulo'].lower().replace(' ', '_')[:20]}.tex"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(contenido)
        print(f"  ✓ Laboratorio {i:02d}: {lab['titulo']}")
    
    print("\n✅ Todos los archivos han sido generados exitosamente!")
    print(f"Total: {len(CLASES_TEORICAS)} clases teóricas y {len(LABORATORIOS)} laboratorios")

if __name__ == "__main__":
    main()