import tkinter as tk
from tkinter import messagebox

class Carrito:

    def __init__(self, root, pedidofinal, preciototal, usuario):
        self.root = root
        self.root.title("Carrito de Compras")
        self.pedidofinal = pedidofinal
        self.preciototal = preciototal
        self.usuario = usuario
        self.envio = tk.BooleanVar

        self.mostrar_pedido()

        self.preguntar_envio()

        # Botón para confirmar pedido
        tk.Button(self.root, text="Confirmar Pedido", command=self.confirmar_pedido).pack()

    def mostrar_pedido(self):
        detalles_pedido = f"Cliente: {self.usuario['nombre']}\n\n"
        detalles_pedido += "Artículos:\n"
        for articulo in self.pedidofinal:
            detalles_pedido += f'- {articulo["nombre"]}: ${articulo["precio"]:.2f}\n'

        detalles_pedido += f"\nPrecio total: ${self.preciototal:.2f}"
        tk.Label(self.root, text=detalles_pedido, justify=tk.LEFT).pack()

    def preguntar_envio(self):
        tk.Checkbutton(self.root, text="¿Enviar a domicilio?", variable=self.envio, command=self.actualizar_precio).pack()

    def actualizar_precio(self):
        if self.envio.get():
            self.preciototal += 1500
        else:
            self.preciototal -= 0
        messagebox.showinfo("Precio Actualizado", f"Precio total con envío: ${self.preciototal:.2f}")

    def confirmar_pedido(self):
        if self.envio.get():
            tiempo_entrega = "30-45 minutos"
            mensaje = f"Su pedido llegará en aproximadamente {tiempo_entrega}. ¡Gracias por su compra!"
        else:
            tiempo_entrega = "15-30 minutos"
            mensaje = f"Su pedido estará listo para retirar en {tiempo_entrega}. ¡Gracias por su compra!"

        messagebox.showinfo("Pedido Confirmado", mensaje)
        self.root.quit()  # Cerrar la aplicación después de confirmar

if __name__ == "__main__":
    # Ejemplo de uso
    root = tk.Tk()

    # Datos de ejemplo
    usuario = {"nombre": "Juan Pérez", "telefono": "12345678"}
    pedidofinal = [
        {"nombre": "Pizza", "precio": 8.0},
        {"nombre": "Refresco", "precio": 2.0}
    ]
    preciototal = sum(articulo["precio"] for articulo in pedidofinal)

    app = Carrito(root, usuario, pedidofinal, preciototal)
    root.mainloop()


'''
        self.horaentrega = horaentrega
        self.confirmar = tk.BooleanVar

    def crear_interfaz(self):
        tk.Checkbutton(self.root, text="Envio a domicilio", variable=self.envio).grid(row=3, columnspan=2)


    def ConfirmarPedido(self):
        confirmar = tk.Button(ventana, text='Confirmar Pedido', font=('Arial', 20))
        confirmar.pack()
'''