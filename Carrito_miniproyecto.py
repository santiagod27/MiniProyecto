import tkinter as tk
from tkinter import messagebox

class Carrito:

    

    def __init__(self, root, pedidofinal, precio, usuario, entrega, confirmar):
        self.root = root
        self.root.title("Carrito de Compras")

        self.pedidofinal = pedidofinal
        self.precio = precio
        self.usuario = usuario
        self.envio = tk.BooleanVar
        self.entrega = entrega
        self.confirmar = confirmar

    def crear_interfaz(self):
        tk.Checkbutton(self.root, text="Envio a domicilio", variable=self.envio).grid(row=3, columnspan=2)


    def ConfirmarPedido(self):
        confirmar = tk.Button(ventana, text='Confirmar Pedido', font=('Arial', 20))
        confirmar.pack()

