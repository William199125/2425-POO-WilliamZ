#Vamos a Ofrecer un menú principal con opciones dinámicas para seleccionar unidades, subcarpetas y scripts.
import os
import subprocess
import json
import logging
from colorama import Fore, Style

# Configuración de logging
logging.basicConfig(filename='dashboard.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def cargar_configuracion(ruta_config):
    """
    Carga la configuración desde un archivo JSON.

    :param ruta_config: Ruta del archivo de configuración
    :return: Diccionario con la configuración cargada
    """
    try:
        with open(ruta_config, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        logging.error(f"Archivo de configuración no encontrado: {ruta_config}")
        print("El archivo de configuración no se encontró.")
        return None
    except json.JSONDecodeError as e:
        logging.error(f"Error al decodificar el archivo de configuración: {e}")
        print("Ocurrió un error al leer la configuración.")
        return None

def mostrar_codigo(ruta_script):
    """
    Lee y muestra el contenido de un archivo Python.

    :param ruta_script: Ruta del script .py a leer
    :return: El contenido del archivo como string o None si ocurre un error
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        logging.error(f"Archivo no encontrado: {ruta_script}")
        print("El archivo no se encontró.")
    except Exception as e:
        logging.error(f"Error leyendo el archivo {ruta_script}: {e}")
        print(f"Ocurrió un error al leer el archivo: {e}")
    return None

def ejecutar_codigo(ruta_script):
    """
    Ejecuta un script Python en una terminal.

    :param ruta_script: Ruta del script .py a ejecutar
    """
    try:
        subprocess.run(['python', ruta_script], check=True)
    except Exception as e:
        logging.error(f"Error ejecutando el script {ruta_script}: {e}")
        print(f"Ocurrió un error al ejecutar el script: {e}")

def imprimir_menu(titulo, opciones):
    """
    Imprime un menú con opciones.

    :param titulo: Título del menú
    :param opciones: Lista de opciones a mostrar
    """
    print(Fore.CYAN + f"\n{titulo}" + Style.RESET_ALL)
    for i, opcion in enumerate(opciones, start=1):
        print(Fore.YELLOW + f"{i} - {opcion}" + Style.RESET_ALL)
    print(Fore.RED + "0 - Salir" + Style.RESET_ALL)

def validar_opcion(opcion, rango):
    """
    Valida si una opción es un entero dentro de un rango válido.

    :param opcion: Opción ingresada por el usuario
    :param rango: Rango de valores válidos
    :return: Entero de la opción válida o None si no es válida
    """
    try:
        opcion_int = int(opcion)
        if opcion_int in rango:
            return opcion_int
    except ValueError:
        pass
    return None

def mostrar_menu_generico(titulo, opciones, accion_seleccion, accion_salir):
    """
    Muestra un menú genérico con opciones dinámicas.

    :param titulo: Título del menú
    :param opciones: Lista de opciones del menú
    :param accion_seleccion: Función a ejecutar al seleccionar una opción válida
    :param accion_salir: Función a ejecutar al salir del menú
    """
    while True:
        imprimir_menu(titulo, opciones)
        eleccion = input("Selecciona una opción: ")
        if eleccion == '0':
            accion_salir()
            break
        else:
            opcion_valida = validar_opcion(eleccion, range(1, len(opciones) + 1))
            if opcion_valida is not None:
                accion_seleccion(opcion_valida - 1)
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_unidades(config):
    """
    Muestra el menú principal de unidades.

    :param config: Configuración cargada desde el archivo JSON
    """
    unidades = config.get("Unidades", {})

    def seleccionar_unidad(indice):
        unidad_nombre = list(unidades.values())[indice]
        ruta_unidad = os.path.join(os.path.dirname(__file__), unidad_nombre)
        mostrar_sub_menu(ruta_unidad)

    mostrar_menu_generico("Menú Principal - Dashboard", list(unidades.values()), seleccionar_unidad, lambda: print("Saliendo del programa."))

def mostrar_sub_menu(ruta_unidad):
    """
    Muestra el submenú de subcarpetas dentro de una unidad.

    :param ruta_unidad: Ruta de la unidad seleccionada
    """
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    def seleccionar_carpeta(indice):
        ruta_carpeta = os.path.join(ruta_unidad, sub_carpetas[indice])
        mostrar_scripts(ruta_carpeta)

    mostrar_menu_generico("Submenú - Selecciona una subcarpeta", sub_carpetas, seleccionar_carpeta, lambda: print("Regresando al menú principal..."))

def mostrar_scripts(ruta_sub_carpeta):
    """
    Muestra los scripts disponibles en una subcarpeta.

    :param ruta_sub_carpeta: Ruta de la subcarpeta seleccionada
    """
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    def seleccionar_script(indice):
        ruta_script = os.path.join(ruta_sub_carpeta, scripts[indice])
        codigo = mostrar_codigo(ruta_script)
        if codigo:
            ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
            if ejecutar == '1':
                ejecutar_codigo(ruta_script)
            elif ejecutar == '0':
                print("No se ejecutó el script.")
            else:
                print("Opción no válida. Regresando al menú de scripts.")
        input("\nPresiona Enter para volver al menú de scripts.")

    mostrar_menu_generico("Scripts - Selecciona un script para ver y ejecutar", scripts, seleccionar_script, lambda: print("Regresando al submenú anterior..."))

if __name__ == "__main__":
    config = cargar_configuracion('config.json')
    if config:
        mostrar_unidades(config)
