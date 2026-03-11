from producto import Producto
from datetime import datetime
import json

class Caja:
    def __init__(self):
        self.carrito = []
        self.total = 0
        self.ventas = self.cargar_ventas()

    def agregar_producto(self):      # Agrega productos
        nombre = input("Nombre del producto: ")
        while True:
            try:
                precio = float(input("Precio del producto: "))
                if precio <= 0:
                    print("El valor del producto debe ser mayor a 0")
                else:
                    break
            except ValueError:
                print("Precio invalido")
        cantidad = int(input("Cantidad de productos: "))
        producto = Producto(nombre,precio, cantidad)
        self.carrito.append(producto)
        print("Producto agregado")


    def mostrar_carrito(self):        #	Muestra productos
        if not self.carrito:
            print("Carrito vacio")
        else:
            self.calcular_total()
            print("\nCarrito:")
            print("Producto\tPrecio\tCantidad\tTotal")
            print("-" * 60)
            for producto in self.carrito:
                total_producto = producto.precio * producto.cantidad
                print(f"{producto.nombre}\t${producto.precio:.2f}\t{producto.cantidad}\t\t${total_producto:.2f}")
            print()
            print()
            print(f'\t\t\t\t  Total:${self.total:.2f}')
            print("-" * 60)


    def calcular_total(self):                 # Suma los precios
        if not self.carrito:
            print("\nCarrito:")
            return 0
        else:
            self.total = sum(producto.precio * producto.cantidad for producto in self.carrito)
            print(f'Total a pagar: ${self.total:.2f}')
            return self.total


    def eliminar_producto(self):
        self.mostrar_carrito()
        indice = int(input("numero de producto a eliminar: ")) -1
        if 0 <= indice < len(self.carrito):
            self.carrito.pop(indice)
            self.calcular_total()
            print("Producto eliminado")


    def venta(self):
        if not self.carrito:
            print("Carrito vacío")
            return

        self.calcular_total()
        monto = float(input("Dinero recibido: "))

        if monto < self.total:
            print(f"La cantidad a cobrar es mayor que el dinero ingresado a caja")
            return
        elif monto > self.total:
            cambio = monto - self.total
            print(f'Cambio:${cambio:.2f}')
        else:
            print("Exacto, no hay cambio")
 
        confirmar = input("¿Confirmar venta? (s/n): ")

        if confirmar.lower() == 's':
            self.guardar_venta()
            self.imprimir_ticket(monto,cambio)
            print("Venta guardada")
            self.carrito.clear()

        else:
            print("Venta cancelada")


    def imprimir_ticket(self, monto, cambio):
        with open("ticket.txt", "w") as f:
            f.write("------ TICKET DE COMPRA ------\n")
            f.write(f"Fecha: {datetime.now().strftime('%Y/%m/%d %H:%M:%S')}\n")
            f.write("------------------------------\n")

            for producto in self.carrito:
                total_producto = producto.precio * producto.cantidad
                f.write(f"{producto.nombre} x{producto.cantidad}  ${total_producto:.2f}\n")

            f.write("------------------------------\n")
            f.write(f"TOTAL: ${self.total:.2f}\n")
            f.write(f"RECIBIDO: ${monto:.2f}\n")
            f.write(f"CAMBIO: ${cambio:.2f}\n")
            f.write("------------------------------\n")
            f.write("Gracias por su compra\n")

    def cargar_ventas(self):
        try:
            with open('ventas.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def guardar_venta(self):
        venta = {
            'fecha' : datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            'productos' : [
                {'nombre' : p.nombre, 'precio' : p.precio, 'cantidad' : p.cantidad} for p in self.carrito
            ],
            'total' : self.total
        }
        self.ventas.append(venta)
        with open('ventas.json', 'w') as f:
            json.dump(self.ventas, f, indent=4)
