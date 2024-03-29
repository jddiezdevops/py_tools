import json
import subprocess
import tkinter as tk
from tkinter import Label, Entry, Button, filedialog, Menu, messagebox, Frame

def habilitar_campos():
    url_entry.config(state='normal')
    indice_entry.config(state='normal')
    usuario_entry.config(state='normal')
    password_entry.config(state='normal')
    enviar_button.config(state='normal')

def seleccionar_archivo():
    # Abre un cuadro de diálogo para seleccionar el archivo JSON
    archivo_json = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.json")])

    if archivo_json:
        habilitar_campos()
        archivo_seleccionado.set(archivo_json)  # Actualiza la etiqueta con el archivo seleccionado
    else:
        messagebox.showerror("Error", "Debes seleccionar un archivo JSON.")

def cargar_datos():
    archivo_json = archivo_seleccionado.get()  # Obtiene el archivo seleccionado
    if not archivo_json:
        messagebox.showerror("Error", "Debes seleccionar un archivo JSON.")
        return

    # Obtiene los valores de los campos de entrada
    url_opensearch = url_entry.get()
    nombre_indice = indice_entry.get()
    usuario = usuario_entry.get()
    password = password_entry.get()

    # Construir el comando curl para usar la API Bulk
    comando_curl = [
        "curl",
        "-k",
        "-u", f"{usuario}:{password}",
        "-X", "POST",
        f"{url_opensearch}/_bulk",
        "-H", "Content-Type: application/x-ndjson",
        "--data-binary", f"@{archivo_json}"
    ]
    resultado = subprocess.run(comando_curl, capture_output=True, text=True)
    print(resultado.stdout)  # Imprime la salida de curl

    if resultado.returncode == 0:
        messagebox.showinfo("Información", "Datos enviados a OpenSearch correctamente.")
    else:
        messagebox.showerror("Error", resultado.stderr)

# Crear la ventana principal
root = tk.Tk()
root.title("Cargar datos a OpenSearch")

# Crear un menú "Archivo" con la opción "Selección de fichero JSON"
menu = Menu(root)
root.config(menu=menu)

archivo_menu = Menu(menu, tearoff=0)  # Eliminar el separador
menu.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Selección de fichero JSON", command=seleccionar_archivo)

# Crear un contenedor para los campos de entrada
input_frame = Frame(root)
input_frame.pack(pady=10)

# Etiquetas y campos de entrada
url_label = Label(input_frame, text="URL de OpenSearch:")
url_label.grid(row=0, column=0, padx=5, pady=5)
url_entry = Entry(input_frame, state='disabled')
url_entry.grid(row=0, column=1, padx=5, pady=5)

indice_label = Label(input_frame, text="Nombre del índice:")
indice_label.grid(row=1, column=0, padx=5, pady=5)
indice_entry = Entry(input_frame, state='disabled')
indice_entry.grid(row=1, column=1, padx=5, pady=5)

usuario_label = Label(input_frame, text="Usuario:")
usuario_label.grid(row=2, column=0, padx=5, pady=5)
usuario_entry = Entry(input_frame, state='disabled')
usuario_entry.grid(row=2, column=1, padx=5, pady=5)

password_label = Label(input_frame, text="Contraseña:")
password_label.grid(row=3, column=0, padx=5, pady=5)
password_entry = Entry(input_frame, show="*", state='disabled')
password_entry.grid(row=3, column=1, padx=5, pady=5)

# Etiqueta para mostrar el archivo seleccionado
archivo_seleccionado = tk.StringVar()
archivo_seleccionado_label = Label(root, textvariable=archivo_seleccionado)
archivo_seleccionado_label.pack(pady=10)

# Crear un botón para enviar los datos (inicialmente deshabilitado)
enviar_button = Button(root, text="Enviar Datos", command=cargar_datos, state='disabled')
enviar_button.pack()

# Ejecutar la aplicación
root.mainloop()

