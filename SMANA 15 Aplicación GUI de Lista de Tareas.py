# Vamos a crear una aplicación GUI simple para gestionar una lista de tareas, como actividades que debe realizar en el
# trabajo como documentos pendientes, documentos despachados, documentos por realizar, permitiendo al usuario
# en este caso William Patricio Zapata que desempeña la función de amanuense de logística
import tkinter as tk
from tkinter import messagebox

# Función para añadir tarea
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor ingrese una tarea.")

# Función para marcar tarea como completada
def mark_completed():
    try:
        selected_task = listbox.curselection()
        if selected_task:
            task = listbox.get(selected_task)
            listbox.delete(selected_task)
            listbox.insert(selected_task, f"{task} (Completada)")
        else:
            messagebox.showwarning("Advertencia", "Por favor seleccione una tarea.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Función para eliminar tarea
def delete_task():
    try:
        selected_task = listbox.curselection()
        if selected_task:
            listbox.delete(selected_task)
        else:
            messagebox.showwarning("Advertencia", "Por favor seleccione una tarea.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas - William Patricio Zapata")

# Crear y ubicar los elementos de la interfaz
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Añadir Tarea", width=20, command=add_task)
add_button.pack(pady=5)

mark_button = tk.Button(root, text="Marcar como Completada", width=20, command=mark_completed)
mark_button.pack(pady=5)

delete_button = tk.Button(root, text="Eliminar Tarea", width=20, command=delete_task)
delete_button.pack(pady=5)

# Lista de tareas
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Vincular la tecla Enter para añadir tarea
root.bind('<Return>', lambda event: add_task())

# Ejecutar la aplicación
root.mainloop()
