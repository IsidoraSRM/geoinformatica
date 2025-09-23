#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
from datetime import datetime

# Datos de los estudiantes parseados
estudiantes = [
    {
        "nombre": "Valentina Campos",
        "experiencia": ["todos"],
        "lenguajes": ["SQL"],
        "intereses": ["salud", "transporte", "medioambiente"],
        "idea_proyecto": None
    },
    {
        "nombre": "Branco García",
        "experiencia": ["programado"],
        "lenguajes": ["R", "Python", "Javascript", "SQL"],
        "intereses": ["urbanismo", "negocios", "transporte"],
        "idea_proyecto": "Analizar las zonas urbanas donde se acumula más gente o haya más densidad poblacional, que requiere tener acceso a transporte público rápido."
    },
    {
        "nombre": "Jaime Riquelme",
        "experiencia": ["geojson"],
        "lenguajes": ["R", "Python", "Javascript", "SQL"],
        "intereses": ["urbanismo", "negocios", "transporte"],
        "idea_proyecto": None
    },
    {
        "nombre": "Felipe Baeza Muñoz",
        "experiencia": ["programado"],
        "lenguajes": ["R", "Python", "Javascript", "SQL"],
        "intereses": ["negocios", "salud"],
        "idea_proyecto": None
    },
    {
        "nombre": "Aracely Castro",
        "experiencia": ["sig", "programado"],
        "lenguajes": ["R", "Python", "SQL"],
        "intereses": ["medioambiente"],
        "idea_proyecto": "Algo que pueda recopilar el movimiento de animales dentro de una zona para saber como entran al campo del vecino o donde ponen más las gallinas sus huevos"
    },
    {
        "nombre": "Catalina López",
        "experiencia": ["google_maps"],
        "lenguajes": ["Python", "SQL"],
        "intereses": ["medioambiente"],
        "idea_proyecto": "Un sistema para identificar áreas potenciales para incorporar vegetación acorde al clima, tipo de suelo, entre otros."
    },
    {
        "nombre": "Fabián Ibarra",
        "experiencia": ["nunca"],
        "lenguajes": ["Python", "Javascript", "SQL"],
        "intereses": ["negocios"],
        "idea_proyecto": "Segmentación de clientes"
    },
    {
        "nombre": "Valentina Barría",
        "experiencia": ["google_maps"],
        "lenguajes": ["R", "Python", "Javascript", "SQL"],
        "intereses": ["medioambiente"],
        "idea_proyecto": "Algo relacionado con medio ambiente / agricultura"
    },
    {
        "nombre": "Anael Guzmán",
        "experiencia": ["postgis", "programado"],
        "lenguajes": ["Python", "Javascript", "SQL"],
        "intereses": ["negocios", "transporte", "medioambiente"],
        "idea_proyecto": "Un proyecto enfocado en ayudar el medio ambiente o en mejorar las rutas y medio de transporte"
    },
    {
        "nombre": "Diego Hernández",
        "experiencia": ["postgis"],
        "lenguajes": ["Python", "Javascript", "SQL"],
        "intereses": ["negocios"],
        "idea_proyecto": "Algo relacionado a la minería en el análisis de suelos en busca de yacimientos"
    },
    {
        "nombre": "Isidora Reveco",
        "experiencia": ["programado"],
        "lenguajes": ["Python", "Javascript", "SQL"],
        "intereses": ["negocios", "urbanismo", "medioambiente", "transporte"],
        "idea_proyecto": "Algo relacionado al tema transporte que sea comercial"
    },
    {
        "nombre": "Lucas Contador",
        "experiencia": ["google_earth", "sig", "programado"],
        "lenguajes": ["Python", "Javascript", "SQL"],
        "intereses": ["negocios", "transporte"],
        "idea_proyecto": None
    },
    {
        "nombre": "Bastián Guerrero",
        "experiencia": ["google_maps"],
        "lenguajes": ["R", "Python", "Javascript", "SQL"],
        "intereses": ["medioambiente", "transporte", "urbanismo"],
        "idea_proyecto": None
    },
    {
        "nombre": "Matías Vejar",
        "experiencia": ["google_maps"],
        "lenguajes": ["Python", "Javascript", "SQL"],
        "intereses": ["transporte"],
        "idea_proyecto": "Aplicación para ver recorridos de micros rurales"
    },
    {
        "nombre": "Roberto Galleguillos",
        "experiencia": ["google_maps", "programado"],
        "lenguajes": ["R", "Python", "Javascript", "SQL"],
        "intereses": ["medioambiente", "urbanismo", "transporte"],
        "idea_proyecto": None
    },
    {
        "nombre": "Byron Gracia",
        "experiencia": ["google_maps"],
        "lenguajes": ["Python", "Javascript", "SQL"],
        "intereses": ["urbanismo"],
        "idea_proyecto": "Algo que ayude a la gente"
    },
    {
        "nombre": "John Fernández",
        "experiencia": ["google_maps"],
        "lenguajes": ["R", "Python", "Javascript", "SQL"],
        "intereses": ["negocios"],
        "idea_proyecto": "Un mapa del crimen que permita analizar dónde colocar comisaría"
    }
]

# Definir proyectos por categoría
proyectos_cientificos = {
    "medioambiente": [
        ("Análisis de Islas de Calor Urbanas en Santiago", "Identificar zonas con mayor temperatura usando imágenes satelitales Landsat y correlacionar con cobertura vegetal"),
        ("Monitoreo de Calidad del Aire", "Crear mapas de interpolación de PM2.5 usando datos de estaciones SINCA y predecir zonas de riesgo"),
        ("Detección de Cambios en Humedales", "Analizar la pérdida de humedales urbanos usando series temporales de NDVI"),
        ("Análisis de Riesgo de Incendios Forestales", "Modelar probabilidad de incendios usando variables climáticas, topográficas y de vegetación"),
        ("Seguimiento de Deforestación", "Detectar cambios en cobertura forestal usando clasificación supervisada de imágenes satelitales"),
        ("Modelado de Corredores Biológicos", "Diseñar rutas óptimas para fauna urbana usando análisis de conectividad"),
        ("Predicción de Inundaciones", "Modelar zonas de riesgo usando DEM y datos históricos de precipitación")
    ],
    "salud": [
        ("Accesibilidad a Centros de Salud", "Analizar tiempos de viaje y cobertura de servicios de salud por comuna"),
        ("Epidemiología Espacial de Enfermedades", "Detectar clusters de enfermedades usando estadística espacial (Moran's I, Getis-Ord)"),
        ("Optimización de Ambulancias", "Ubicación óptima de ambulancias usando análisis de demanda y tiempos de respuesta"),
        ("Mapeo de Vulnerabilidad Social", "Identificar poblaciones vulnerables y su acceso a servicios de salud"),
        ("Análisis de Contaminación y Salud Respiratoria", "Correlacionar datos de calidad del aire con admisiones hospitalarias")
    ],
    "transporte": [
        ("Optimización de Rutas de Transporte Público", "Mejorar recorridos usando datos de demanda y análisis de redes"),
        ("Análisis de Congestión Vehicular", "Identificar puntos críticos usando datos de velocidad de Google Maps API"),
        ("Planificación de Ciclovías", "Diseñar red óptima de ciclovías considerando demanda potencial y seguridad"),
        ("Predicción de Demanda de Metro", "Modelar flujos de pasajeros usando machine learning espacial"),
        ("Análisis de Accidentalidad Vial", "Identificar puntos negros y factores de riesgo espaciales"),
        ("Movilidad Sostenible", "Evaluar potencial de modos de transporte alternativos por zona")
    ],
    "urbanismo": [
        ("Detección de Asentamientos Informales", "Usar deep learning en imágenes satelitales para identificar campamentos"),
        ("Análisis de Gentrificación", "Detectar cambios socioeconómicos usando datos de arriendo y censo"),
        ("Planificación de Áreas Verdes", "Optimizar ubicación de parques según déficit y densidad poblacional"),
        ("Modelado 3D de Crecimiento Urbano", "Simular expansión urbana usando autómatas celulares"),
        ("Análisis de Segregación Espacial", "Medir y visualizar patrones de segregación socioeconómica"),
        ("Smart Cities", "Diseñar sistema de monitoreo urbano integrando múltiples fuentes de datos")
    ]
}

proyectos_comerciales = {
    "negocios": [
        ("Geomarketing para Retail", "Identificar ubicaciones óptimas para nuevas tiendas usando análisis de competencia y demografía"),
        ("Segmentación Espacial de Clientes", "Crear perfiles de clientes por zona geográfica para marketing dirigido"),
        ("Análisis de Competencia", "Mapear competidores y analizar áreas de influencia usando polígonos de Voronoi"),
        ("Optimización de Cadena de Suministro", "Diseñar red de distribución minimizando costos de transporte"),
        ("Valorización Inmobiliaria", "Predecir precios de propiedades usando regresión espacial y características del entorno"),
        ("Delivery y Última Milla", "Optimizar rutas de reparto y ubicación de centros de distribución"),
        ("Análisis de Mercado por Zona", "Identificar oportunidades de negocio según características demográficas")
    ],
    "turismo": [
        ("Rutas Turísticas Personalizadas", "Generar itinerarios óptimos según preferencias del usuario"),
        ("Análisis de Flujos Turísticos", "Mapear patrones de movimiento usando datos de redes sociales"),
        ("Recomendación de Destinos", "Sistema de recomendación basado en ubicación y preferencias")
    ],
    "agricultura": [
        ("Agricultura de Precisión", "Optimizar uso de recursos usando índices de vegetación y datos de suelo"),
        ("Predicción de Rendimientos", "Estimar producción usando datos climáticos y satelitales"),
        ("Gestión de Riego", "Optimizar sistemas de riego usando datos de humedad del suelo")
    ],
    "mineria": [
        ("Exploración Mineral", "Identificar zonas con potencial minero usando datos geofísicos y geológicos"),
        ("Optimización de Rutas de Transporte", "Diseñar rutas óptimas para camiones mineros"),
        ("Monitoreo Ambiental", "Seguimiento de impacto ambiental usando imágenes satelitales")
    ]
}

def obtener_nivel_experiencia(exp_list):
    """Determina el nivel de experiencia del estudiante"""
    if "programado" in exp_list or "postgis" in exp_list:
        return "avanzado"
    elif "sig" in exp_list or "geojson" in exp_list:
        return "intermedio"
    elif "google_maps" in exp_list or "google_earth" in exp_list:
        return "basico"
    else:
        return "principiante"

def recomendar_proyectos(estudiante):
    """Genera recomendaciones de proyectos basadas en el perfil del estudiante"""
    recomendaciones_cientificas = []
    recomendaciones_comerciales = []
    
    # Proyectos científicos basados en intereses
    for interes in estudiante["intereses"]:
        if interes in ["medioambiente", "salud", "transporte", "urbanismo"]:
            if interes in proyectos_cientificos:
                # Seleccionar 2-3 proyectos relevantes
                proyectos = proyectos_cientificos[interes]
                for i, (titulo, desc) in enumerate(proyectos[:3]):
                    recomendaciones_cientificas.append((titulo, desc, interes))
    
    # Proyectos comerciales basados en intereses
    for interes in estudiante["intereses"]:
        if interes == "negocios":
            proyectos = proyectos_comerciales["negocios"]
            for i, (titulo, desc) in enumerate(proyectos[:3]):
                recomendaciones_comerciales.append((titulo, desc, "negocios"))
        elif interes == "medioambiente":
            # Agricultura es comercial pero relacionado con medioambiente
            if "agricultura" in proyectos_comerciales:
                proyectos = proyectos_comerciales["agricultura"]
                for titulo, desc in proyectos[:2]:
                    recomendaciones_comerciales.append((titulo, desc, "agricultura"))
    
    # Si no hay suficientes recomendaciones comerciales, agregar genéricas
    if len(recomendaciones_comerciales) < 2:
        recomendaciones_comerciales.extend([
            ("Sistema de Geocoding para E-commerce", "Mejorar precisión de direcciones para entregas", "negocios"),
            ("Dashboard Geoespacial para BI", "Visualización de KPIs con componente espacial", "negocios")
        ])
    
    return recomendaciones_cientificas[:4], recomendaciones_comerciales[:4]

def generar_latex(estudiante, rec_cientificas, rec_comerciales):
    """Genera el código LaTeX para el PDF personalizado"""
    
    nivel = obtener_nivel_experiencia(estudiante["experiencia"])
    lenguajes_str = ", ".join(estudiante["lenguajes"])
    intereses_str = ", ".join(estudiante["intereses"])
    
    # Determinar tecnologías recomendadas basadas en lenguajes conocidos
    tech_stack = []
    if "Python" in estudiante["lenguajes"]:
        tech_stack.append("GeoPandas, Folium, Rasterio")
    if "R" in estudiante["lenguajes"]:
        tech_stack.append("sf, terra, tmap")
    if "Javascript" in estudiante["lenguajes"]:
        tech_stack.append("Leaflet, Mapbox, Turf.js")
    if "SQL" in estudiante["lenguajes"]:
        tech_stack.append("PostGIS")
    
    tech_recomendadas = " + ".join(tech_stack) if tech_stack else "Python con GeoPandas (recomendado para principiantes)"
    
    latex_content = r'''\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[spanish]{babel}
\usepackage{geometry}
\geometry{margin=2.5cm}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{tcolorbox}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage{fancyhdr}
\usepackage{fontawesome5}
\usepackage{multicol}

% Colores personalizados
\definecolor{usachblue}{RGB}{0,121,192}
\definecolor{usachred}{RGB}{239,51,64}
\definecolor{darkgreen}{RGB}{0,100,0}
\definecolor{darkorange}{RGB}{255,140,0}

% Configuración de página
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small Geoinformática 2025-2}
\fancyhead[R]{\small USACH}
\fancyfoot[C]{\thepage}

\begin{document}

\begin{center}
    {\Huge \textbf{Recomendaciones de Proyecto}}\\[0.5cm]
    {\Large \textcolor{usachblue}{Geoinformática - Semestre 2, 2025}}\\[0.3cm]
    \rule{\textwidth}{0.5pt}\\[0.3cm]
    {\LARGE \textbf{''' + estudiante["nombre"] + r'''}}\\[0.2cm]
    {\large Fecha: \today}
\end{center}

\vspace{0.5cm}

\section*{\faIcon{user-circle} Perfil del Estudiante}

\begin{tcolorbox}[colback=blue!5,colframe=usachblue,title=Resumen de tu Perfil]
\begin{itemize}[leftmargin=*]
    \item \textbf{Nivel de experiencia:} ''' + nivel.capitalize() + r'''
    \item \textbf{Lenguajes dominados:} ''' + lenguajes_str + r'''
    \item \textbf{Áreas de interés:} ''' + intereses_str.capitalize() + r'''
    \item \textbf{Stack tecnológico recomendado:} ''' + tech_recomendadas + r'''
\end{itemize}
\end{tcolorbox}

'''
    
    # Agregar idea propia si existe
    if estudiante["idea_proyecto"]:
        latex_content += r'''
\section*{\faIcon{lightbulb} Tu Idea de Proyecto}

\begin{tcolorbox}[colback=yellow!10,colframe=darkorange,title=Idea Original]
\textit{"''' + estudiante["idea_proyecto"] + r'''"}

\vspace{0.3cm}
\textbf{Comentario del profesor:} Esta es una excelente idea que puedes desarrollar. Te sugiero considerar los siguientes aspectos técnicos:
\begin{itemize}
    \item Fuentes de datos disponibles (INE, municipalidades, APIs públicas)
    \item Metodología de análisis espacial apropiada
    \item Herramientas específicas de tu stack tecnológico
\end{itemize}
\end{tcolorbox}
'''
    
    # Proyectos Científicos
    latex_content += r'''
\section*{\faIcon{flask} Proyectos Científicos Recomendados}

Basándome en tus intereses y experiencia, estos proyectos científicos serían ideales para ti:

'''
    
    for i, (titulo, desc, area) in enumerate(rec_cientificas, 1):
        latex_content += r'''
\begin{tcolorbox}[colback=green!5,colframe=darkgreen,title={\small Proyecto Científico \#''' + str(i) + r'''}]
\textbf{''' + titulo + r'''}\\[0.2cm]
\textcolor{gray}{\small Área: ''' + area.capitalize() + r'''}\\[0.2cm]
''' + desc + r'''
\end{tcolorbox}

'''
    
    # Proyectos Comerciales
    latex_content += r'''
\section*{\faIcon{building} Proyectos Comerciales Recomendados}

Si te interesa un enfoque más aplicado a la industria, considera estos proyectos:

'''
    
    for i, (titulo, desc, area) in enumerate(rec_comerciales, 1):
        latex_content += r'''
\begin{tcolorbox}[colback=orange!5,colframe=darkorange,title={\small Proyecto Comercial \#''' + str(i) + r'''}]
\textbf{''' + titulo + r'''}\\[0.2cm]
\textcolor{gray}{\small Área: ''' + area.capitalize() + r'''}\\[0.2cm]
''' + desc + r'''
\end{tcolorbox}

'''
    
    # Recursos recomendados
    latex_content += r'''
\section*{\faIcon{graduation-cap} Recursos Recomendados}

\subsection*{Recursos según tu nivel}
'''
    
    if nivel == "principiante":
        latex_content += r'''
\begin{itemize}[leftmargin=*]
    \item Tutorial QGIS básico
    \item Curso Python GeoPandas (Codecademy)
    \item Documentación oficial de Folium
    \item Videos de GeoDelta Labs
\end{itemize}
'''
    elif nivel == "basico":
        latex_content += r'''
\begin{itemize}[leftmargin=*]
    \item Libro: Python for GIS
    \item Curso: Spatial Analysis (Coursera)
    \item Práctica con Jupyter notebooks
    \item Datasets de Natural Earth
\end{itemize}
'''
    else:
        latex_content += r'''
\begin{itemize}[leftmargin=*]
    \item Libro: Geocomputation with Python/R
    \item Paper: Recent advances in GeoAI
    \item Google Earth Engine tutorials
    \item Kaggle competitions geoespaciales
\end{itemize}
'''
    
    latex_content += r'''

\vspace{0.5cm}

\begin{tcolorbox}[colback=gray!10,colframe=gray!50]
\centering
\textbf{Contacto}\\[0.2cm]
\faIcon{envelope} francisco.parra.o@usach.cl
\end{tcolorbox}

\end{document}'''
    
    return latex_content

def crear_directorio_salida():
    """Crea el directorio para los PDFs si no existe"""
    output_dir = "/home/franciscoparrao/proyectos/geoinformatica/recomendaciones_estudiantes"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def generar_pdf(estudiante, latex_content, output_dir):
    """Genera el PDF a partir del código LaTeX"""
    # Limpiar nombre para usar como archivo
    nombre_archivo = estudiante["nombre"].replace(" ", "_").lower()
    
    # Escribir archivo .tex
    tex_file = os.path.join(output_dir, f"{nombre_archivo}.tex")
    with open(tex_file, 'w', encoding='utf-8') as f:
        f.write(latex_content)
    
    # Compilar a PDF
    try:
        # Cambiar al directorio de salida para que los archivos auxiliares se generen ahí
        original_dir = os.getcwd()
        os.chdir(output_dir)
        
        # Compilar dos veces para referencias
        subprocess.run(['pdflatex', '-interaction=nonstopmode', f"{nombre_archivo}.tex"], 
                      capture_output=True, text=True)
        subprocess.run(['pdflatex', '-interaction=nonstopmode', f"{nombre_archivo}.tex"], 
                      capture_output=True, text=True)
        
        # Volver al directorio original
        os.chdir(original_dir)
        
        # Limpiar archivos auxiliares
        for ext in ['.aux', '.log', '.out', '.toc']:
            aux_file = os.path.join(output_dir, f"{nombre_archivo}{ext}")
            if os.path.exists(aux_file):
                os.remove(aux_file)
        
        print(f"✓ PDF generado para {estudiante['nombre']}")
        return True
    except Exception as e:
        print(f"✗ Error generando PDF para {estudiante['nombre']}: {e}")
        return False

def main():
    """Función principal"""
    print("="*60)
    print("GENERADOR DE RECOMENDACIONES DE PROYECTO")
    print("Geoinformática - USACH 2025-2")
    print("="*60)
    print()
    
    # Crear directorio de salida
    output_dir = crear_directorio_salida()
    print(f"Directorio de salida: {output_dir}")
    print()
    
    # Procesar cada estudiante
    exitosos = 0
    fallidos = 0
    
    for i, estudiante in enumerate(estudiantes, 1):
        print(f"[{i}/{len(estudiantes)}] Procesando: {estudiante['nombre']}...")
        
        # Obtener recomendaciones
        rec_cientificas, rec_comerciales = recomendar_proyectos(estudiante)
        
        # Generar LaTeX
        latex_content = generar_latex(estudiante, rec_cientificas, rec_comerciales)
        
        # Generar PDF
        if generar_pdf(estudiante, latex_content, output_dir):
            exitosos += 1
        else:
            fallidos += 1
    
    print()
    print("="*60)
    print(f"RESUMEN: {exitosos} PDFs generados exitosamente, {fallidos} fallos")
    print(f"Los archivos se encuentran en: {output_dir}")
    print("="*60)

if __name__ == "__main__":
    main()