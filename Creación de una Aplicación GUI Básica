import tkinter as tk
from tkinter import ttk

def agregar_dato():
    dato = entrada_texto.get()
    if dato:
        lista_datos.insert("", "end", values=(dato,))
        entrada_texto.delete(0, tk.END)

def limpiar_datos():
    for item in lista_datos.get_children():
        lista_datos.delete(item)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")
ventana.geometry("400x300")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack(pady=5)

# Campo de texto
entrada_texto = tk.Entry(ventana)
entrada_texto.pack(pady=5)

# Botón Agregar
tk.Button(ventana, text="Agregar", command=agregar_dato).pack(pady=5)

# Tabla para mostrar datos
lista_datos = ttk.Treeview(ventana, columns=("Datos",), show="headings")
lista_datos.heading("Datos", text="Datos Ingresados")
lista_datos.pack(pady=5, fill=tk.BOTH, expand=True)

# Botón Limpiar
tk.Button(ventana, text="Limpiar", command=limpiar_datos).pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
