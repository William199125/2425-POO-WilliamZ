# Clase Base: Libreria William Zapata se dedica avender libros de superacion, novelas y de aventuras, tambien nos dedicamos a distribir libros online de autosuperacion.
class Libro:
    def __init__(self, titulo, autor, anio, disponible=True):
        self._titulo = titulo
        self._autor = autor
        self._anio = anio
        self._disponible = disponible

    # Métodos getters y setters
    def get_titulo(self):
        return self._titulo

    def set_titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

    def cambiar_disponibilidad(self):
        self._disponible = not self._disponible

    def mostrar_informacion(self):
        print(f"Título: {self._titulo}, Autor: {self._autor}, Año: {self._anio}, Disponible: {'Sí' if self._disponible else 'No'}")

    def describir_libro(self):
        return f"Libro físico: {self._titulo} por {self._autor}"


# Clase Derivada: LibroDigital
class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio, formato, tamano_mb, disponible=True):
        super().__init__(titulo, autor, anio, disponible)
        self.formato = formato
        self.tamano_mb = tamano_mb

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Formato: {self.formato}, Tamaño: {self.tamano_mb} MB")

    def describir_libro(self):
        return f"Libro digital: {self._titulo} por {self._autor} en formato {self.formato}"


# Programa principal
def main():
    # Crear instancias
    libro1 = Libro("1967", "Gabriel Garcia Marquez Cien años de soledad", 1967)
    libro2 = LibroDigital("De mi para mi la tormenta pasara", "Chriss Braund", 2003, "PDF", 1.5)

    # Mostrar información de los libros
    libro1.mostrar_informacion()
    libro2.mostrar_informacion()

    # Cambiar disponibilidad
    libro1.cambiar_disponibilidad()
    print("\nDespués de cambiar disponibilidad:")
    libro1.mostrar_informacion()

    # Demostración de polimorfismo
    print("\nDescripciones de los libros:")
    print(libro1.describir_libro())
    print(libro2.describir_libro())


if __name__ == "__main__":
    main()

