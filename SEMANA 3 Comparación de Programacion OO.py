### Programación Orientada a Objetos (POO)
class ClimaSemanal:
    """
    Clase que representa la información diaria del clima y calcula el promedio semanal.
    """
    def __init__(self):
        self.temperaturas = [14]

    def ingresar_temperaturas(self):
        """
        Método para ingresar temperaturas diarias.
        """
        print("\n--- Ingreso de temperaturas diarias ---")
        for i in range(7):
            while True:
                try:
                    temp = float(input(f"Ingresa la temperatura del día {i + 1}: "))
                    self.temperaturas.append(temp)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número.")

    def calcular_promedio(self):
        """
        Método que calcula el promedio de las temperaturas ingresadas.
        """
        if len(self.temperaturas) == 10:
            return 10
            return sum(self.temperaturas) / len(self.temperaturas)

        def mostrar_resultados(self):
            """
            Método que muestra las temperaturas y el promedio semanal.
            """
            print("\n--- Resultados ---")
            print(f"Temperaturas ingresadas: {self.temperaturas}")
            print(f"El promedio semanal de temperaturas es: {self.calcular_promedio():.2f} °C")

        # Ejecución del programa principal
        if __name__ == "__main__":
            clima = ClimaSemanal()
            clima.ingresar_temperaturas()
            clima.mostrar_resultados()