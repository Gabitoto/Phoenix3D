# Aplicación principal
import tkinter as tk
from tkinter import messagebox
from modules.presupuesto import ventana_presupuesto
"""from modules.ganancias import ganancias
from modules.pedidos import pedidios 
from modules.presupuesto import calculo_presupuestario"""

def main():

    def mostrar_presupuestos():
        messagebox.showinfo("Presupuestos", "Funcionalidad de Presupuestos")

    def mostrar_pedidos():
        messagebox.showinfo("Pedidos", "Funcionalidad de Pedidos")

    def mostrar_ganancias():
        messagebox.showinfo("Ganancias", "Funcionalidad de Ganancias")

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Gestión de Finanzas - Impresión 3D")
    root.geometry("300x200")

    # Crear el menú 
    menu_bar = tk.Menu(root)

    # Menú 
    menu_opciones = tk.Menu(menu_bar, tearoff=0)
    menu_opciones.add_command(label="Presupuestos", command=mostrar_presupuestos)
    menu_opciones.add_command(label="Pedidos", command=mostrar_pedidos)
    menu_opciones.add_command(label="Ganancias", command=mostrar_ganancias)
    menu_opciones.add_separator()
    menu_opciones.add_command(label="Salir", command=root.quit)

    menu_bar.add_cascade(label="Opciones", menu=menu_opciones)

    # Mostrar el menú
    root.config(menu=menu_bar)

    # Correr la ventana principal
    root.mainloop()

if __name__ == "__main__":
    main()