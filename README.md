# Tarea 1

## Descripción
Este proyecto realiza el procesamiento de un archivo GraphML (`CR_Capital.xml`) para construir un grafo en memoria utilizando la librería SAX de Python. A partir del archivo, se extrae la información de los nodos (con sus latitudes y longitudes) y de las aristas (con las conexiones entre los nodos). Finalmente, se construye una lista de adyacencias que representa el grafo, lo que permite el análisis de rutas y caminos en la localidad de Ciudad Real.

## Estructura del Proyecto
- `CR_Capital.xml`: Archivo GraphML que contiene la representación de la red de nodos y conexiones de la localidad de Ciudad Real.
- `leerxml.py`: Script de Python que procesa el archivo XML, extrae los nodos y aristas, y construye la lista de adyacencias.
- `README.md`: Documentación del proyecto (este archivo).

## Requisitos
- Python 3.11 o superior.
- Conocimientos básicos de manipulación de archivos XML y estructuras de datos en Python.

## Instalación
1. Clonar el repositorio o descargar los archivos.
2. Navegar a la carpeta del proyecto.
3. Asegurarse de tener instalado Python 3.11.
4. Ejecutar el script desde la línea de comandos:
   ```bash
   python3 leerxml.py

