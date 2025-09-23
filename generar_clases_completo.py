#!/usr/bin/env python3
"""
Generador de templates LaTeX para el curso de Geoinformática
Semestre 2, 2025 - USACH
Estructura: Martes (teórica) + Jueves (teórica + laboratorio)
"""

import os
from datetime import datetime

# Definición de todas las clases del semestre (30 clases teóricas: 2 por semana)
CLASES_TEORICAS = [
    # SEMANA 1
    {
        "numero": 1,
        "dia": "martes",
        "titulo": "Introducción al curso",
        "subtitulo": "Presentación y contexto de la Geoinformática",
        "contenido": [
            "Presentación del programa del curso",
            "Introducción a la Geocomputación",
            "Aplicaciones en el mundo real",
            "Evaluación diagnóstica"
        ]
    },
    {
        "numero": 2,
        "dia": "jueves",
        "titulo": "Fundamentos de Geocomputación",
        "subtitulo": "Conceptos básicos y herramientas",
        "contenido": [
            "Historia y evolución de la Geocomputación",
            "Software para análisis geoespacial",
            "Ecosistema R y Python para geodatos",
            "Primeros ejemplos prácticos"
        ]
    },
    # SEMANA 2
    {
        "numero": 3,
        "dia": "martes",
        "titulo": "Fundamentos de datos geoespaciales",
        "subtitulo": "Tipos y estructuras de datos espaciales",
        "contenido": [
            "Datos vectoriales: puntos, líneas, polígonos",
            "Datos raster: grillas y resolución",
            "Formatos de archivos comunes",
            "Atributos y geometrías"
        ]
    },
    {
        "numero": 4,
        "dia": "jueves",
        "titulo": "Representación de datos geográficos",
        "subtitulo": "Trabajando con R y Python",
        "contenido": [
            "Paquete sf en R",
            "GeoPandas en Python",
            "Importación y exportación de datos",
            "Estructuras de datos espaciales"
        ]
    },
    # SEMANA 3
    {
        "numero": 5,
        "dia": "martes",
        "titulo": "Sistemas de Referencia de Coordenadas",
        "subtitulo": "CRS y proyecciones cartográficas",
        "contenido": [
            "Coordenadas geográficas vs proyectadas",
            "Proyecciones cartográficas",
            "CRS en Chile (UTM, WGS84)",
            "Importancia del CRS"
        ]
    },
    {
        "numero": 6,
        "dia": "jueves",
        "titulo": "Transformación y reproyección",
        "subtitulo": "Manejo práctico de CRS",
        "contenido": [
            "Identificación de CRS en datos",
            "Transformación de coordenadas",
            "Problemas comunes y soluciones",
            "Mejores prácticas"
        ]
    },
    # SEMANA 4
    {
        "numero": 7,
        "dia": "martes",
        "titulo": "Datos raster y su representación",
        "subtitulo": "Estructura y propiedades",
        "contenido": [
            "Estructura de datos raster",
            "Resolución espacial y espectral",
            "Bandas y multicapas",
            "Formatos raster comunes"
        ]
    },
    {
        "numero": 8,
        "dia": "jueves",
        "titulo": "Trabajando con raster",
        "subtitulo": "Paquete terra y rasterio",
        "contenido": [
            "Introducción a terra en R",
            "Rasterio en Python",
            "Lectura y escritura de raster",
            "Visualización básica"
        ]
    },
    # SEMANA 5 - FIESTAS PATRIAS (NO HAY CLASES)
    
    # SEMANA 6
    {
        "numero": 9,
        "dia": "martes",
        "titulo": "Operaciones con atributos",
        "subtitulo": "Manipulación de datos espaciales",
        "contenido": [
            "Selección y filtrado",
            "Uniones espaciales (spatial joins)",
            "Agregación de datos",
            "Cálculo de nuevos atributos"
        ]
    },
    {
        "numero": 10,
        "dia": "jueves",
        "titulo": "Análisis de atributos avanzado",
        "subtitulo": "Integración con dplyr y pandas",
        "contenido": [
            "Pipeline de procesamiento",
            "Operaciones grupales",
            "Estadísticas espaciales",
            "Optimización de consultas"
        ]
    },
    # SEMANA 7
    {
        "numero": 11,
        "dia": "martes",
        "titulo": "Operaciones espaciales vectoriales",
        "subtitulo": "Geoprocesamiento fundamental",
        "contenido": [
            "Buffer, intersección, unión",
            "Diferencia y diferencia simétrica",
            "Predicados espaciales",
            "Relaciones topológicas"
        ]
    },
    {
        "numero": 12,
        "dia": "jueves",
        "titulo": "Geoprocesamiento avanzado",
        "subtitulo": "Queries y análisis complejos",
        "contenido": [
            "Queries espaciales complejas",
            "Operaciones de overlay",
            "Análisis de proximidad",
            "Casos de uso prácticos"
        ]
    },
    # SEMANA 8
    {
        "numero": 13,
        "dia": "martes",
        "titulo": "Operaciones raster básicas",
        "subtitulo": "Álgebra de mapas",
        "contenido": [
            "Operaciones aritméticas",
            "Operaciones lógicas",
            "Reclasificación",
            "Estadísticas raster"
        ]
    },
    {
        "numero": 14,
        "dia": "jueves",
        "titulo": "Operaciones raster avanzadas",
        "subtitulo": "Análisis focal, zonal y global",
        "contenido": [
            "Operaciones focales (vecindad)",
            "Operaciones zonales",
            "Operaciones globales",
            "Análisis multicriterio"
        ]
    },
    # SEMANA 9
    {
        "numero": 15,
        "dia": "martes",
        "titulo": "Interacciones raster-vector",
        "subtitulo": "Integración de tipos de datos",
        "contenido": [
            "Extracción de valores raster",
            "Estadísticas por polígono",
            "Máscaras y recortes",
            "Sampling de puntos"
        ]
    },
    {
        "numero": 16,
        "dia": "jueves",
        "titulo": "Conversión entre formatos",
        "subtitulo": "Rasterización y vectorización",
        "contenido": [
            "Rasterización de vectores",
            "Vectorización de raster",
            "Parámetros de conversión",
            "Preservación de información"
        ]
    },
    # SEMANA 10
    {
        "numero": 17,
        "dia": "martes",
        "titulo": "Fundamentos de cartografía digital",
        "subtitulo": "Principios de diseño de mapas",
        "contenido": [
            "Elementos de un mapa",
            "Teoría del color",
            "Simbolización efectiva",
            "Jerarquía visual"
        ]
    },
    {
        "numero": 18,
        "dia": "jueves",
        "titulo": "Creación de mapas con tmap",
        "subtitulo": "Mapas estáticos profesionales",
        "contenido": [
            "Sintaxis de tmap",
            "Layouts y composición",
            "Mapas temáticos",
            "Exportación de alta calidad"
        ]
    },
    # SEMANA 11
    {
        "numero": 19,
        "dia": "martes",
        "titulo": "Visualización interactiva",
        "subtitulo": "Mapas web y dashboards",
        "contenido": [
            "Introducción a leaflet",
            "Mapview y plotly",
            "Controles interactivos",
            "Publicación web"
        ]
    },
    {
        "numero": 20,
        "dia": "jueves",
        "titulo": "Dashboards geoespaciales",
        "subtitulo": "Shiny y Streamlit",
        "contenido": [
            "Arquitectura de aplicaciones web",
            "Componentes interactivos",
            "Integración de mapas",
            "Deployment básico"
        ]
    },
    # SEMANA 12
    {
        "numero": 21,
        "dia": "martes",
        "titulo": "Automatización y scripting",
        "subtitulo": "Programación para geoprocesamiento",
        "contenido": [
            "Funciones personalizadas",
            "Manejo de errores",
            "Logging y debugging",
            "Buenas prácticas"
        ]
    },
    {
        "numero": 22,
        "dia": "jueves",
        "titulo": "Pipelines de procesamiento",
        "subtitulo": "Automatización de flujos de trabajo",
        "contenido": [
            "Procesamiento batch",
            "Paralelización",
            "Optimización de código",
            "Generación de reportes"
        ]
    },
    # SEMANA 13
    {
        "numero": 23,
        "dia": "martes",
        "titulo": "Integración con otros software GIS",
        "subtitulo": "Interoperabilidad",
        "contenido": [
            "GDAL/OGR",
            "Puentes R-Python-QGIS",
            "Formatos de intercambio",
            "APIs geoespaciales"
        ]
    },
    {
        "numero": 24,
        "dia": "jueves",
        "titulo": "Bases de datos espaciales",
        "subtitulo": "PostGIS y servicios web",
        "contenido": [
            "Introducción a PostGIS",
            "Consultas espaciales SQL",
            "Servicios WMS/WFS",
            "APIs REST geoespaciales"
        ]
    },
    # SEMANA 14
    {
        "numero": 25,
        "dia": "martes",
        "titulo": "Statistical Learning espacial",
        "subtitulo": "Fundamentos de análisis estadístico",
        "contenido": [
            "Autocorrelación espacial",
            "Índice de Moran",
            "LISA y hotspots",
            "Dependencia espacial"
        ]
    },
    {
        "numero": 26,
        "dia": "jueves",
        "titulo": "Modelos predictivos espaciales",
        "subtitulo": "Machine Learning geoespacial",
        "contenido": [
            "Regresión espacial",
            "Random Forest espacial",
            "Validación cruzada espacial",
            "Feature engineering geoespacial"
        ]
    },
    # SEMANA 15
    {
        "numero": 27,
        "dia": "martes",
        "titulo": "Aplicaciones específicas",
        "subtitulo": "Casos de uso por dominio",
        "contenido": [
            "Geomarketing y retail",
            "Análisis ambiental",
            "Planificación urbana",
            "Gestión de emergencias"
        ]
    },
    {
        "numero": 28,
        "dia": "jueves",
        "titulo": "Casos de estudio Chile",
        "subtitulo": "Aplicaciones locales",
        "contenido": [
            "Análisis de movilidad Santiago",
            "Gestión de recursos hídricos",
            "Monitoreo de incendios",
            "Planificación territorial"
        ]
    },
    # SEMANA 16
    {
        "numero": 29,
        "dia": "martes",
        "titulo": "Tendencias actuales",
        "subtitulo": "Estado del arte en Geoinformática",
        "contenido": [
            "Big Data geoespacial",
            "Cloud computing (GEE)",
            "Deep Learning para imágenes",
            "IoT y sensores"
        ]
    },
    {
        "numero": 30,
        "dia": "jueves",
        "titulo": "Futuro de la Geoinformática",
        "subtitulo": "Tecnologías emergentes",
        "contenido": [
            "Gemelos digitales",
            "Realidad aumentada",
            "Computación cuántica",
            "Ética y privacidad"
        ]
    }
]

# 15 Laboratorios (uno cada jueves después de la clase teórica)
LABORATORIOS = [
    {
        "numero": 1,
        "titulo": "Configuración del ambiente",
        "subtitulo": "Instalación y primeros pasos",
        "objetivos": [
            "Instalar R, RStudio y Python",
            "Configurar paquetes básicos",
            "Primer contacto con datos geoespaciales",
            "Verificar instalación correcta"
        ]
    },
    {
        "numero": 2,
        "titulo": "Manipulación básica de datos vectoriales",
        "subtitulo": "Trabajando con sf en R",
        "objetivos": [
            "Lectura de archivos espaciales",
            "Exploración de datos con sf",
            "Operaciones básicas",
            "Visualización simple"
        ]
    },
    {
        "numero": 3,
        "titulo": "Trabajando con CRS",
        "subtitulo": "Proyecciones y transformaciones",
        "objetivos": [
            "Identificar CRS en datos",
            "Transformar coordenadas",
            "Resolver problemas de CRS",
            "Ejercicios con datos de Chile"
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
            "Filtrado y selección avanzada",
            "Joins espaciales complejos",
            "Agregación de datos",
            "Mini-proyecto demográfico"
        ]
    },
    {
        "numero": 6,
        "titulo": "Geoprocesamiento vectorial + Propuesta proyecto",
        "subtitulo": "Análisis espacial y proyecto",
        "objetivos": [
            "Implementar buffers y análisis",
            "Overlay de capas",
            "Entregar propuesta de proyecto",
            "Casos de uso reales"
        ]
    },
    {
        "numero": 7,
        "titulo": "Análisis raster",
        "subtitulo": "Procesamiento avanzado",
        "objetivos": [
            "Cálculo de pendientes y orientación",
            "Análisis de visibilidad",
            "Estadísticas zonales",
            "Proyecto: análisis de riesgo"
        ]
    },
    {
        "numero": 8,
        "titulo": "Integración raster-vector",
        "subtitulo": "Combinando tipos de datos",
        "objetivos": [
            "Extracción de valores a puntos",
            "Conversión entre formatos",
            "Análisis combinado",
            "Ejercicio con datos ambientales"
        ]
    },
    {
        "numero": 9,
        "titulo": "Creación de mapas + Plan de proyecto",
        "subtitulo": "Cartografía y planificación",
        "objetivos": [
            "Diseño de mapas con tmap",
            "Definición formal del proyecto",
            "Personalización avanzada",
            "Revisión de fuentes de datos"
        ]
    },
    {
        "numero": 10,
        "titulo": "Mapas interactivos",
        "subtitulo": "Visualización web",
        "objetivos": [
            "Crear mapas con leaflet",
            "Añadir interactividad",
            "Publicación web básica",
            "Dashboard simple"
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
            "Conexión con servicios web",
            "APIs (OSM, Google Earth Engine)",
            "PostGIS básico",
            "Interoperabilidad"
        ]
    },
    {
        "numero": 13,
        "titulo": "Análisis estadístico + Segundo avance",
        "subtitulo": "Estadística espacial y proyecto",
        "objetivos": [
            "Implementar Moran's I",
            "Detectar hotspots",
            "Segundo avance proyecto",
            "Revisión de resultados"
        ]
    },
    {
        "numero": 14,
        "titulo": "Trabajo en proyecto",
        "subtitulo": "Desarrollo intensivo",
        "objetivos": [
            "Desarrollo del proyecto final",
            "Resolución de problemas técnicos",
            "Análisis avanzados",
            "Preparación de visualizaciones"
        ]
    },
    {
        "numero": 15,
        "titulo": "Últimos ajustes proyecto",
        "subtitulo": "Preparación final",
        "objetivos": [
            "Ajustes finales al código",
            "Preparación de presentación",
            "Ensayo de presentaciones",
            "Documentación completa"
        ]
    }
]

def generar_template_base(tipo_clase):
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
        
        {proxima}
    \\end{{center}}
\\end{{frame}}

\\end{{document}}"""

def generar_clase_teorica(clase, numero):
    """Genera el contenido específico para una clase teórica"""
    contenido = ""
    
    # Generar secciones basadas en el contenido
    for i, item in enumerate(clase["contenido"], 1):
        contenido += f"""
\\section{{{item}}}

\\begin{{frame}}{{{item}}}
    % Contenido a desarrollar en clase
    \\begin{{itemize}}
        \\item Concepto clave 1
        \\item Concepto clave 2
        \\item Concepto clave 3
        \\item Ejemplo práctico
    \\end{{itemize}}
\\end{{frame}}

\\begin{{frame}}{{Profundización}}
    % Detalles adicionales del tema
    \\begin{{itemize}}
        \\item Aspecto detallado 1
        \\item Aspecto detallado 2
        \\item Consideraciones importantes
    \\end{{itemize}}
\\end{{frame}}
"""
    
    # Determinar próxima actividad
    if clase["dia"] == "martes":
        proxima = "Próxima clase: Jueves (teórica + laboratorio)"
    else:
        if numero < 30:
            proxima = "A continuación: Laboratorio práctico"
        else:
            proxima = "Próxima semana: Presentaciones de proyectos"
    
    template = generar_template_base(f"Clase {numero}")
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

\\begin{frame}{Objetivos de hoy}
    \\begin{itemize}
"""
    for obj in lab["objetivos"]:
        contenido += f"        \\item {obj}\n"
    
    contenido += """    \\end{itemize}
\\end{frame}
"""
    
    # Secciones de práctica
    contenido += """
\\section{Configuración inicial}

\\begin{frame}{Preparación del entorno}
    \\begin{itemize}
        \\item Cargar librerías necesarias
        \\item Configurar directorio de trabajo
        \\item Descargar datos de ejemplo
        \\item Verificar instalaciones
    \\end{itemize}
\\end{frame}

\\begin{frame}[fragile]{Código inicial}
    \\begin{lstlisting}[language=R]
# Cargar librerías
library(sf)
library(terra)
library(tmap)
library(tidyverse)

# Configurar directorio
setwd("~/geoinformatica/lab""" + str(numero) + """")

# Verificar
sf::sf_extSoftVersion()
    \\end{lstlisting}
\\end{frame}

\\section{Ejercicios prácticos}

\\begin{frame}{Ejercicio 1}
    \\textbf{Objetivo:} Aplicar conceptos de la clase teórica
    
    \\begin{enumerate}
        \\item Paso 1: Preparación de datos
        \\item Paso 2: Aplicación de técnicas
        \\item Paso 3: Análisis de resultados
        \\item Paso 4: Visualización
    \\end{enumerate}
\\end{frame}

\\begin{frame}[fragile]{Implementación}
    \\begin{lstlisting}[language=R]
# Código del ejercicio
# A completar durante el laboratorio
    \\end{lstlisting}
\\end{frame}

\\begin{frame}{Ejercicio 2}
    \\textbf{Objetivo:} Práctica avanzada
    
    \\begin{itemize}
        \\item Descripción del problema
        \\item Datos disponibles
        \\item Resultado esperado
        \\item Criterios de evaluación
    \\end{itemize}
\\end{frame}

\\section{Proyecto semestral}

\\begin{frame}{Trabajo en proyecto}
    \\textbf{Tiempo dedicado al proyecto:} 30 minutos
    
    \\begin{itemize}
        \\item Aplicar lo aprendido al proyecto
        \\item Consultas con el profesor
        \\item Trabajo en equipo
        \\item Avance incremental
    \\end{itemize}
\\end{frame}

\\section{Cierre y tareas}

\\begin{frame}{Para la próxima clase}
    \\begin{itemize}
        \\item Completar ejercicios pendientes
        \\item Revisar material complementario
        \\item Avanzar en el proyecto según calendario
        \\item Preparar dudas para consultar
    \\end{itemize}
\\end{frame}
"""
    
    # Información de próxima clase
    if numero < 15:
        proxima = f"Próxima semana: Clase teórica {numero*2 + 1}"
    else:
        proxima = "Próxima semana: Presentaciones finales de proyectos"
    
    template = generar_template_base(f"Laboratorio {numero}")
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
    
    print("="*60)
    print("GENERADOR DE CLASES - GEOINFORMÁTICA USACH")
    print("="*60)
    print("\nEstructura del curso:")
    print("- Martes: 1 clase teórica")
    print("- Jueves: 1 clase teórica + 1 laboratorio")
    print("- Total: 30 clases teóricas + 15 laboratorios")
    print("="*60)
    
    # Generar clases teóricas
    print("\nGenerando clases teóricas...")
    for i, clase in enumerate(CLASES_TEORICAS, 1):
        contenido = generar_clase_teorica(clase, i)
        # Nombrar archivos con día de la semana para claridad
        dia = clase["dia"]
        filename = f"clases/teoricas/clase{i:02d}_{dia}_{clase['titulo'].lower().replace(' ', '_')[:20]}.tex"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(contenido)
        print(f"  ✓ Clase {i:02d} ({dia}): {clase['titulo']}")
    
    # Generar laboratorios
    print("\nGenerando laboratorios (todos los jueves)...")
    for i, lab in enumerate(LABORATORIOS, 1):
        contenido = generar_laboratorio(lab, i)
        filename = f"clases/laboratorios/lab{i:02d}_jueves_{lab['titulo'].lower().replace(' ', '_')[:20]}.tex"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(contenido)
        print(f"  ✓ Laboratorio {i:02d}: {lab['titulo']}")
    
    print("\n" + "="*60)
    print("✅ GENERACIÓN COMPLETADA")
    print(f"Total: {len(CLASES_TEORICAS)} clases teóricas")
    print(f"Total: {len(LABORATORIOS)} laboratorios")
    print("="*60)
    
    # Crear archivo README con el calendario
    print("\nGenerando archivo README con calendario...")
    with open("clases/README.md", 'w', encoding='utf-8') as f:
        f.write("# Clases de Geoinformática - Semestre 2, 2025\n\n")
        f.write("## Estructura semanal\n")
        f.write("- **Martes**: Clase teórica\n")
        f.write("- **Jueves**: Clase teórica + Laboratorio\n\n")
        f.write("## Calendario\n\n")
        
        semana = 1
        for i in range(0, 30, 2):
            if i < len(CLASES_TEORICAS):
                f.write(f"### Semana {semana}\n")
                if semana == 5:
                    f.write("*RECESO - FIESTAS PATRIAS*\n\n")
                    semana += 1
                    continue
                f.write(f"- **Martes**: Clase {i+1:02d} - {CLASES_TEORICAS[i]['titulo']}\n")
                if i+1 < len(CLASES_TEORICAS):
                    f.write(f"- **Jueves**: Clase {i+2:02d} - {CLASES_TEORICAS[i+1]['titulo']}")
                    if semana <= 15:
                        lab_num = semana if semana < 5 else semana - 1
                        if lab_num <= len(LABORATORIOS):
                            f.write(f" + Lab {lab_num:02d} - {LABORATORIOS[lab_num-1]['titulo']}")
                f.write("\n\n")
                semana += 1
    
    print("✓ README.md creado con el calendario completo")

if __name__ == "__main__":
    main()