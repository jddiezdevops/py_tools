import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import pandas as pd
import json

def convertir_a_excel():
    try:
        archivo_json = filedialog.askopenfilename(filetypes=[('Archivos JSON', '*.json')])
        if archivo_json:
            data = pd.read_json(archivo_json)
            archivo_excel = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[('Archivos Excel', '*.xlsx')])
            if archivo_excel:
                data.to_excel(archivo_excel, index=False)
                messagebox.showinfo("Éxito", f'Se ha convertido {archivo_json} a {archivo_excel}')
    except Exception as e:
        messagebox.showerror("Error", str(e))

def convertir_a_json():
    try:
        archivo_excel = filedialog.askopenfilename(filetypes=[('Archivos Excel', '*.xlsx')])
        if archivo_excel:
            # Utiliza la variable correcta para la ventana principal de tu aplicación Tkinter aquí
            nombre_indice = simpledialog.askstring("Nombre del índice", "Introduce el nombre del índice para Elasticsearch:", parent=app) 
            if nombre_indice:  # Asegúrate de que se haya ingresado un nombre de índice
                data = pd.read_excel(archivo_excel)
                archivo_json = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[('Archivos JSON', '*.json')])
                if archivo_json:
                    with open(archivo_json, 'w', encoding='utf-8') as f:
                        for _, row in data.iterrows():
                            # Crear metadatos para la operación de indexación
                            meta_dict = {"index": {"_index": nombre_indice}}
                            # Convertir la fila del dataframe a JSON y añadir metadatos
                            f.write(json.dumps(meta_dict) + '\n')
                            f.write(row.to_json(force_ascii=False, date_format='iso') + '\n')
                        # Asegurarse de que el archivo termina con un salto de línea
                        f.write('\n')
                    messagebox.showinfo("Éxito", f'Se ha convertido {archivo_excel} a {archivo_json} en formato Bulk')
            else:
                messagebox.showerror("Error", "No se ingresó un nombre de índice.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("Conversor de Archivos")
app.geometry("400x200")

frame = tk.Frame(app)
frame.pack(pady=10)

boton_excel = tk.Button(frame, text="Convertir a Excel", command=convertir_a_excel, bg="#4CAF50", fg="white")
boton_excel.pack(side=tk.LEFT, padx=10)

boton_json = tk.Button(frame, text="Convertir a JSON", command=convertir_a_json, bg="#2196F3", fg="white")
boton_json.pack(side=tk.RIGHT, padx=10)

mensaje = tk.Label(app, text="Seleccione una opción para convertir los archivos.")
mensaje.pack(pady=20)

app.mainloop()
