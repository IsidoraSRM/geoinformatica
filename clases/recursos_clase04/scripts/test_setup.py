#!/usr/bin/env python3
"""
Script de verificación de ambiente para Clase 04
Verifica que todos los componentes necesarios estén instalados y funcionando
"""

import sys
import os
from pathlib import Path

# Colores para terminal
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
NC = '\033[0m'  # No Color

def print_status(status, message):
    """Imprime mensaje con color según status"""
    if status == "ok":
        print(f"{GREEN}✓ {message}{NC}")
    elif status == "error":
        print(f"{RED}✗ {message}{NC}")
    elif status == "warning":
        print(f"{YELLOW}⚠ {message}{NC}")
    else:
        print(f"  {message}")

def test_python_version():
    """Verifica versión de Python"""
    print("\n1. Verificando Python...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 9:
        print_status("ok", f"Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print_status("error", f"Python {version.major}.{version.minor} (se requiere 3.9+)")
        return False

def test_core_libraries():
    """Verifica librerías core geoespaciales"""
    print("\n2. Verificando librerías geoespaciales core...")
    
    libraries = {
        'numpy': None,
        'pandas': None,
        'geopandas': None,
        'shapely': None,
        'folium': None,
        'fiona': None,
        'pyproj': None,
        'rtree': None
    }
    
    all_ok = True
    for lib_name in libraries:
        try:
            lib = __import__(lib_name)
            version = getattr(lib, '__version__', 'instalado')
            libraries[lib_name] = version
            print_status("ok", f"{lib_name} {version}")
        except ImportError as e:
            print_status("error", f"{lib_name} - No instalado")
            all_ok = False
    
    return all_ok

def test_web_frameworks():
    """Verifica frameworks web"""
    print("\n3. Verificando frameworks web...")
    
    frameworks = ['streamlit', 'fastapi', 'uvicorn']
    all_ok = True
    
    for framework in frameworks:
        try:
            lib = __import__(framework)
            version = getattr(lib, '__version__', 'instalado')
            print_status("ok", f"{framework} {version}")
        except ImportError:
            print_status("error", f"{framework} - No instalado")
            all_ok = False
    
    return all_ok

def test_database_connectivity():
    """Verifica conectividad con bases de datos"""
    print("\n4. Verificando conectividad de bases de datos...")
    
    # Test PostgreSQL
    try:
        import psycopg2
        print_status("ok", "psycopg2 instalado")
        
        # Intentar conexión (puede fallar si no hay servidor)
        try:
            from dotenv import load_dotenv
            load_dotenv()
            
            conn = psycopg2.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                port=os.getenv('DB_PORT', 5432),
                database='postgres',
                user=os.getenv('DB_USER', 'postgres'),
                password=os.getenv('DB_PASSWORD', 'postgres')
            )
            conn.close()
            print_status("ok", "PostgreSQL accesible")
        except Exception as e:
            print_status("warning", f"PostgreSQL no accesible (normal si usará Docker): {str(e)[:50]}...")
    except ImportError:
        print_status("error", "psycopg2 no instalado")
        return False
    
    # Test Redis
    try:
        import redis
        print_status("ok", "redis-py instalado")
        
        try:
            r = redis.Redis(host='localhost', port=6379, decode_responses=True)
            r.ping()
            print_status("ok", "Redis accesible")
        except Exception:
            print_status("warning", "Redis no accesible (normal si usará Docker)")
    except ImportError:
        print_status("error", "redis-py no instalado")
    
    return True

def test_osm_apis():
    """Verifica acceso a APIs de OpenStreetMap"""
    print("\n5. Verificando APIs geoespaciales...")
    
    # Test OSMnx
    try:
        import osmnx as ox
        print_status("ok", f"OSMnx {ox.__version__}")
        
        # Test conexión a Nominatim
        try:
            from geopy.geocoders import Nominatim
            geolocator = Nominatim(user_agent="test_clase04")
            location = geolocator.geocode("Santiago, Chile", timeout=10)
            if location:
                print_status("ok", f"Nominatim accesible - Santiago: ({location.latitude:.2f}, {location.longitude:.2f})")
            else:
                print_status("warning", "Nominatim accesible pero no encontró Santiago")
        except Exception as e:
            print_status("warning", f"No se pudo conectar a Nominatim: {str(e)[:30]}...")
            
    except ImportError:
        print_status("error", "OSMnx no instalado")
        return False
    
    # Test requests para APIs REST
    try:
        import requests
        response = requests.get('https://api.github.com', timeout=5)
        if response.status_code == 200:
            print_status("ok", "Conexión a internet verificada")
        else:
            print_status("warning", "Conexión a internet con problemas")
    except Exception:
        print_status("warning", "No hay conexión a internet")
    
    return True

def test_parallel_processing():
    """Verifica librerías de procesamiento paralelo"""
    print("\n6. Verificando procesamiento paralelo...")
    
    try:
        import dask
        import dask.dataframe as dd
        print_status("ok", f"Dask {dask.__version__}")
        
        try:
            import dask_geopandas
            print_status("ok", "Dask-GeoPandas instalado")
        except ImportError:
            print_status("warning", "Dask-GeoPandas no instalado (opcional)")
            
    except ImportError:
        print_status("warning", "Dask no instalado (opcional pero recomendado)")
    
    return True

def test_project_structure():
    """Verifica estructura del proyecto"""
    print("\n7. Verificando estructura del proyecto...")
    
    required_dirs = [
        'proyecto_geo/data/raw',
        'proyecto_geo/data/processed',
        'proyecto_geo/data/cache',
        'proyecto_geo/src/etl',
        'proyecto_geo/src/analysis',
        'proyecto_geo/src/api',
        'proyecto_geo/src/visualization',
        'proyecto_geo/notebooks',
        'proyecto_geo/tests',
        'proyecto_geo/config',
        'proyecto_geo/docker'
    ]
    
    all_ok = True
    for dir_path in required_dirs:
        if Path(dir_path).exists():
            print_status("ok", f"{dir_path}")
        else:
            print_status("warning", f"{dir_path} - No existe")
            all_ok = False
    
    # Verificar archivos importantes
    required_files = [
        'proyecto_geo/.env',
        'proyecto_geo/.gitignore',
        'proyecto_geo/config/config.yaml'
    ]
    
    for file_path in required_files:
        if Path(file_path).exists():
            print_status("ok", f"{file_path}")
        else:
            print_status("warning", f"{file_path} - No existe")
            all_ok = False
    
    return all_ok

def test_sample_data():
    """Verifica datos de ejemplo"""
    print("\n8. Verificando datos de ejemplo...")
    
    data_files = [
        'proyecto_geo/data/raw/comunas_chile.geojson'
    ]
    
    for file_path in data_files:
        if Path(file_path).exists():
            size = Path(file_path).stat().st_size / 1024 / 1024  # MB
            print_status("ok", f"{file_path} ({size:.2f} MB)")
            
            # Intentar cargar para verificar que es válido
            if file_path.endswith('.geojson'):
                try:
                    import geopandas as gpd
                    gdf = gpd.read_file(file_path)
                    print_status("ok", f"  → {len(gdf)} features cargadas correctamente")
                except Exception as e:
                    print_status("error", f"  → Error al cargar: {str(e)[:50]}...")
        else:
            print_status("warning", f"{file_path} - No existe")
    
    return True

def test_jupyter():
    """Verifica Jupyter"""
    print("\n9. Verificando Jupyter...")
    
    try:
        import jupyter
        import IPython
        print_status("ok", f"Jupyter instalado")
        print_status("ok", f"IPython {IPython.__version__}")
        
        # Verificar kernel
        import subprocess
        result = subprocess.run(['jupyter', 'kernelspec', 'list'], 
                              capture_output=True, text=True)
        if 'python3' in result.stdout:
            print_status("ok", "Kernel Python3 disponible")
        else:
            print_status("warning", "Kernel Python3 no encontrado")
            
    except ImportError:
        print_status("warning", "Jupyter no instalado (opcional)")
    except Exception as e:
        print_status("warning", f"Error verificando Jupyter: {str(e)[:30]}...")
    
    return True

def main():
    """Ejecuta todos los tests"""
    print("=" * 50)
    print("   VERIFICACIÓN DE AMBIENTE - CLASE 04")
    print("=" * 50)
    
    results = {
        'Python': test_python_version(),
        'Librerías Core': test_core_libraries(),
        'Frameworks Web': test_web_frameworks(),
        'Bases de Datos': test_database_connectivity(),
        'APIs': test_osm_apis(),
        'Procesamiento Paralelo': test_parallel_processing(),
        'Estructura Proyecto': test_project_structure(),
        'Datos Ejemplo': test_sample_data(),
        'Jupyter': test_jupyter()
    }
    
    # Resumen
    print("\n" + "=" * 50)
    print("RESUMEN")
    print("=" * 50)
    
    total = len(results)
    passed = sum(results.values())
    
    for component, status in results.items():
        if status:
            print_status("ok", component)
        else:
            print_status("error", component)
    
    print("\n" + "=" * 50)
    if passed == total:
        print_status("ok", f"¡TODO LISTO! ({passed}/{total} componentes OK)")
        print("\nPuedes proceder con la clase.")
    elif passed >= total * 0.7:
        print_status("warning", f"CASI LISTO ({passed}/{total} componentes OK)")
        print("\nRevisa los componentes faltantes pero puedes empezar.")
    else:
        print_status("error", f"FALTAN COMPONENTES ({passed}/{total} componentes OK)")
        print("\nEjecuta setup_environment.sh para completar la instalación.")
    
    # Recomendaciones finales
    print("\n" + "=" * 50)
    print("PRÓXIMOS PASOS:")
    print("=" * 50)
    print("1. Si hay errores, ejecuta: bash setup_environment.sh")
    print("2. Activa el ambiente: source geo_env/bin/activate")
    print("3. Inicia servicios Docker: docker-compose up -d")
    print("4. Abre Jupyter: jupyter notebook")
    print("5. Revisa los notebooks de ejemplo")
    
    return 0 if passed == total else 1

if __name__ == "__main__":
    sys.exit(main())