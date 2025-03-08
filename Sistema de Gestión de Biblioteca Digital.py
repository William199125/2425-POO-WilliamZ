# Sistema de Gestión de Biblioteca Digital, en donde vamos a administrar de mejor manera los libros que van a ser prestados
# a los diferentes alumnos o personas

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"'{self.titulo}' de {self.autor}, ISBN: {self.isbn}, Categoría: {self.categoria}"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __repr__(self):
        return f"Usuario {self.nombre} (ID: {self.id_usuario})"

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
        else:
            print(f"El libro '{libro.titulo}' no está en los libros prestados de {self.nombre}.")


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar libros por ISBN
        self.usuarios = set()  # Conjunto para almacenar usuarios únicos

    def registrar_usuario(self, usuario):
        self.usuarios.add(usuario)

    def dar_baja_usuario(self, usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
        else:
            print(f"El usuario {usuario.nombre} no está registrado en la biblioteca.")

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    def prestar_libro(self, usuario, isbn):
        if isbn in self.libros:
            libro = self.libros[isbn]
            usuario.prestar_libro(libro)
            del self.libros[isbn]  # El libro ya no está disponible en la biblioteca
        else:
            print(f"El libro con ISBN {isbn} no está disponible en la biblioteca.")

    def devolver_libro(self, usuario, isbn):
        if isbn not in self.libros:
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    self.libros[isbn] = libro  # El libro regresa a la biblioteca
                    usuario.devolver_libro(libro)
                    break
            else:
                print(f"El libro con ISBN {isbn} no pertenece a {usuario.nombre}.")
        else:
            print(f"El libro con ISBN {isbn} ya está disponible en la biblioteca.")

    def buscar_libro(self, criterio, valor):
        encontrados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.titulo.lower():
                encontrados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.autor.lower():
                encontrados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                encontrados.append(libro)
        return encontrados

    def listar_libros_prestados(self, usuario):
        if usuario.libros_prestados:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print(f"{usuario.nombre} no tiene libros prestados.")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancia de biblioteca
    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("la odisea", "Homero", "Ficción", "1991")
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Ficción", "1605")
    libro3 = Libro("Romeo y Julieta", "William Shakespeare", "Novela", "1597")

    # Añadir libros a la biblioteca
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)

    # Crear usuarios
    usuario1 = Usuario("William Zapata", 1)
    usuario2 = Usuario("Sofia Zapata", 2)

    # Registrar usuarios
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libro
    biblioteca.prestar_libro(usuario1, "1991")
    biblioteca.prestar_libro(usuario2, "1605")

    # Listar libros prestados
    biblioteca.listar_libros_prestados(usuario1)
    biblioteca.listar_libros_prestados(usuario2)

    # Buscar libros
    libros_encontrados = biblioteca.buscar_libro("autor", "Gabriel García Márquez")
    print("Libros encontrados por autor:")
    for libro in libros_encontrados:
        print(libro)

    # Devolver libros
    biblioteca.devolver_libro(usuario1, "1991")
    biblioteca.devolver_libro(usuario2, "1605")

    # Listar libros prestados después de devolver
    biblioteca.listar_libros_prestados(usuario1)
    biblioteca.listar_libros_prestados(usuario2)
