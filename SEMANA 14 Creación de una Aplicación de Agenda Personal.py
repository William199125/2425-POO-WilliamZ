# En esta agenda vamos a tratar de organizar de mejor manera la agenda diaria para mis actividades diarias en mi trabajo como Militar en servicio activo
# Vamos a aplicar GUI utilizando Tkinter en una agenda personal esto nos permitira agregar, ver, y eliminar eventos o tareas programadas
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox

# Crear la ventana principa
root = tk.Tk()
root.title("Agenda Personal - William Zapata")
root.geometry("600x400")

# Frame para la lista de eventos
frame_lista = tk.Frame(root)
frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Árbol para mostrar eventos
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack(fill=tk.BOTH, expand=True)

# Frame para los campos de entrada
frame_entrada = tk.Frame(root)
frame_entrada.pack(fill=tk.X, padx=10, pady=10)

# Campos de entrada y etiquetas
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0)
date_entry = DateEntry(frame_entrada, width=15, background='darkblue', foreground='white', borderwidth=2)
date_entry.grid(row=0, column=1)

tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0)
hora_entry = tk.Entry(frame_entrada, width=15)
hora_entry.grid(row=1, column=1)

tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0)
descripcion_entry = tk.Entry(frame_entrada, width=30)
descripcion_entry.grid(row=2, column=1)

# Función para agregar eventos
def agregar_evento():
    fecha = date_entry.get()
    hora = hora_entry.get()
    descripcion = descripcion_entry.get()

    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        date_entry.delete(0, "end")
        hora_entry.delete(0, "end")
        descripcion_entry.delete(0, "end")
    else:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

# Función para eliminar eventos seleccionados
def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        tree.delete(seleccionado)
    else:
        messagebox.showerror("Error", "Por favor, seleccione un evento para eliminar.")

# Frame para los botones
frame_botones = tk.Frame(root)
frame_botones.pack(fill=tk.X, padx=10, pady=10)

# Botones
btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.pack(side=tk.LEFT, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.pack(side=tk.LEFT, padx=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=root.quit)
btn_salir.pack(side=tk.RIGHT, padx=5)

# Iniciar la aplicación
root.mainloop()
