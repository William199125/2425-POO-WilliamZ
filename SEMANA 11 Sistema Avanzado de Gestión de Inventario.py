# Esta clase tiene como obejetico crear un Sistema Avanzado de Gestión de Inventario, el cual vamos aplicar en la tienda que creamos para la tienda mi mi Mamá.
# aqui podra gestionar de mejor manera el inventario de su tienda

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos para obtener y establecer atributos
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


# Clase Inventario
class Inventario:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, producto):
        self.inventario[producto.get_id()] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.inventario:
            del self.inventario[id_producto]

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.inventario:
            producto = self.inventario[id_producto]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)

    def buscar_producto_por_nombre(self, nombre):
        return [producto for producto in self.inventario.values() if nombre.lower() in producto.get_nombre().lower()]

    def mostrar_inventario(self):
        for producto in self.inventario.values():
            print(
                f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")

    # Funciones de almacenamiento en archivo
    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            # Serializar los productos del inventario a JSON
            json.dump({producto.get_id(): {'nombre': producto.get_nombre(), 'cantidad': producto.get_cantidad(),
                                           'precio': producto.get_precio()} for producto in self.inventario.values()},
                      f)

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
                for id_producto, datos in data.items():
                    producto = Producto(id_producto, datos['nombre'], datos['cantidad'], datos['precio'])
                    self.agregar_producto(producto)
        except FileNotFoundError:
            print("No se encontró el archivo, creando uno nuevo.")


# Función de menú interactivo
def menu():
    inventario = Inventario()
    inventario.cargar_inventario('inventario.json')

    while True:
        print("\n---- Menú de Gestión de Inventario ----")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
            print(f"Producto {nombre} añadido.")

        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
            print(f"Producto con ID {id_producto} eliminado.")

        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = int(input("Nueva cantidad (dejar en blanco para no cambiar): ") or 0)
            precio = float(input("Nuevo precio (dejar en blanco para no cambiar): ") or 0.0)
            inventario.actualizar_producto(id_producto, cantidad, precio)
            print(f"Producto con ID {id_producto} actualizado.")

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre)
            for producto in resultados:
                print(
                    f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            inventario.guardar_inventario('inventario.json')
            print("Inventario guardado.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


# Llamar al menú para ejecutar el programa
if __name__ == "__main__":
    menu()
