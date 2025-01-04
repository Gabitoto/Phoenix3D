import tkinter as tk
from tkinter import ttk
from modules.pedidos import guardar_pedido

# Crear la ventana principal
root = tk.Tk()
root.title("Phoenix 3D")
root.geometry("600x400")

# Etiquetas y entradas para el formulario
frame_formulario = ttk.Frame(root)
frame_formulario.pack(pady=20)

# Cliente
label_cliente = ttk.Label(frame_formulario, text="Cliente:")
label_cliente.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_cliente = ttk.Entry(frame_formulario, width=30)
entry_cliente.grid(row=0, column=1, padx=5, pady=5)

# Objeto
label_objeto = ttk.Label(frame_formulario, text="Objeto:")
label_objeto.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_objeto = ttk.Entry(frame_formulario, width=30)
entry_objeto.grid(row=1, column=1, padx=5, pady=5)

# Cantidad
label_cantidad = ttk.Label(frame_formulario, text="Cantidad:")
label_cantidad.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_cantidad = ttk.Entry(frame_formulario, width=30)
entry_cantidad.grid(row=2, column=1, padx=5, pady=5)

# Fecha de entrega
label_fecha = ttk.Label(frame_formulario, text="Fecha de entrega:")
label_fecha.grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_fecha = ttk.Entry(frame_formulario, width=30)
entry_fecha.grid(row=3, column=1, padx=5, pady=5)

# Botón para guardar
btn_guardar = ttk.Button(root, text="Guardar Pedido", command=guardar_pedido)
btn_guardar.pack(pady=10)

# Iniciar el loop principal de la interfaz
root.mainloop()