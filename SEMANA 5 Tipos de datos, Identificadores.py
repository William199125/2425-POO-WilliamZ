# Tarea: Cálculo de áreas de figuras geométricas.
# Autor: [William Zapata]
# # Fecha: [10-01-2025]
# Descripción: Este programa permite al usuario calcular el área de tres figuras geométricas:
# rectángulo, círculo y triángulo. Se implementa con tipos de datos como integer, float, string y boolean.
# El programa ofrece un menú de opciones y realiza los cálculos adecuados basándose en la elección del usuario.

import math  # Importamos la librería math para operaciones matemáticas


# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un rectángulo dado su base y altura.

    :param base: La base del rectángulo (float)
    :param altura: La altura del rectángulo (float)
    :return: El área del rectángulo (float)
    """
    return base * altura


# Función para calcular el área de un círculo
def calcular_area_circulo(radio: float) -> float:
    """
    Calcula el área de un círculo dado su radio.

    :param radio: El radio del círculo (float)
    :return: El área del círculo (float)
    """
    return math.pi * radio ** 2  # Usamos pi de la librería math para un valor más preciso


# Función para calcular el área de un triángulo
def calcular_area_triangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un triángulo dado su base y altura.

    :param base: La base del triángulo (float)
    :param altura: La altura del triángulo (float)
    :return: El área del triángulo (float)
    """
    return (base * altura) / 2


# Función que muestra el menú de opciones al usuario
def mostrar_menu():
    """
    Muestra el menú de opciones para que el usuario elija la figura de la cual quiere calcular el área.
    """
    print("\nSeleccione la figura para calcular el área:")
    print("1. Rectángulo")
    print("2. Círculo")
    print("3. Triángulo")
    print("4. Salir")


# Función principal que maneja la lógica del programa
def main():
    """
    Función principal que gestiona la interacción con el usuario y controla el flujo del programa.
    Permite al usuario elegir qué figura calcular y mostrar el resultado.
    """
    continuar = True  # Variable booleana que controla el ciclo del menú

    while continuar:
        mostrar_menu()

        # Solicitamos la elección del usuario
        try:
            opcion = int(input("Ingrese el número de su elección: "))
        except ValueError:
            print("Opción no válida, por favor ingrese un número entero.")
            continue

        if opcion == 1:
            try:
                base = float(input("Ingrese la base del rectángulo: "))
                altura = float(input("Ingrese la altura del rectángulo: "))
                area = calcular_area_rectangulo(base, altura)
                print(f"El área del rectángulo es: {area:.2f} unidades cuadradas.")
            except ValueError:
                print("Por favor ingrese valores numéricos válidos para la base y la altura.")

        elif opcion == 2:
            try:
                radio = float(input("Ingrese el radio del círculo: "))
                area = calcular_area_circulo(radio)
                print(f"El área del círculo es: {area:.2f} unidades cuadradas.")
            except ValueError:
                print("Por favor ingrese un valor numérico válido para el radio.")

        elif opcion == 3:
            try:
                base = float(input("Ingrese la base del triángulo: "))
                altura = float(input("Ingrese la altura del triángulo: "))
                area = calcular_area_triangulo(base, altura)
                print(f"El área del triángulo es: {area:.2f} unidades cuadradas.")
            except ValueError:
                print("Por favor ingrese valores numéricos válidos para la base y la altura.")

        elif opcion == 4:
            print("Gracias por usar el programa. ¡Hasta luego!")
            continuar = False  # Cambia la variable para salir del ciclo

        else:
            print("Opción no válida, intente nuevamente.")


# Llamada a la función principal para iniciar el programa
if __name__ == "__main__":
    main()
