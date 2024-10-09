import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime  # Para manejar fechas

def guardar_presupuesto(cliente, descripcion, cantidad, precio_unitario, total):
    with open("presupuestos.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        # Guardar la fecha junto con los demás datos
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), cliente, descripcion, cantidad, precio_unitario, total])
    messagebox.showinfo("Éxito", "Presupuesto guardado correctamente")

def agregar_presupuesto():
    cliente = entry_cliente.get()
    descripcion = entry_descripcion.get()
    cantidad = None
    precio_unitario = None

    if not cliente or not descripcion or not cantidad or not precio_unitario:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return
    
    try:
        cantidad = int(cantidad)
        precio_unitario = float(precio_unitario)
        total = cantidad * precio_unitario
    except ValueError:
        messagebox.showerror("Error", "Cantidad y Precio Unitario deben ser números válidos")
        return
    
    guardar_presupuesto(cliente, descripcion, cantidad, precio_unitario, total)

def ventana_presupuesto():
    ventana = tk.Toplevel()
    ventana.title("Agregar Presupuesto")
    ventana.geometry("400x300")

    tk.Label(ventana, text="Cliente:").pack(pady=5)
    global entry_cliente
    entry_cliente = tk.Entry(ventana, width=40)
    entry_cliente.pack(pady=5)

    tk.Label(ventana, text="Descripción:").pack(pady=5)
    global entry_descripcion
    entry_descripcion = tk.Entry(ventana, width=40)
    entry_descripcion.pack(pady=5)