import singelton

class Carritocompras:
    def __init__(self):
        self.items = []
        self.numero_compra = 1
        self.facturas = []

    def carritoCompras(self, nombreProducto, precio, cantidad):
        aux = float(precio) * int(cantidad)
        producto = {'nombre': nombreProducto, 'precio': precio, 'cantidad': cantidad, 'subtotal': aux}
        self.items.append(producto)

    def mostrarCarrito(self):
        for producto in self.items:
            print("Nombre:", producto['nombre'])
            print("Precio:", producto['precio'])
            print("Cantidad:", producto['cantidad'])
            print("Subtotal:", producto['subtotal'])
            print()

    def factura(self, codigo):
        # Calcular el total y el impuesto
        total = sum(producto['subtotal'] for producto in self.items)
        impuesto = total * 0.12

        # Crear el número de factura
        numero_factura = f"NUMERO DE FACTURA ({self.numero_compra})"
        self.numero_compra += 1  # Incrementar el número de compra

        # Obtener la información del cliente
        cliente = singelton.referenciaCliente.buscarCliente(codigo)
        nombre_cliente = cliente['nombre']
        correo_cliente = cliente['correo']
        nit_cliente = cliente['nit']

        # Crear la factura
        factura_data = {
            "numero_factura": numero_factura,
            "codigo_cliente": codigo,
            "cliente": {
                "nombre": nombre_cliente,
                "correo": correo_cliente,
                "nit": nit_cliente
            },
            "productos": self.items.copy(),  # Copiar la lista de productos para evitar modificaciones posteriores
            "total": total,
            "impuesto": impuesto
        }

        # Guardar la factura en la lista de facturas
        self.facturas.append(factura_data)

        # Mostrar la factura
        print("Número de Factura:", numero_factura)
        print("Cliente:")
        print("  Nombre:", nombre_cliente)
        print("  Correo:", correo_cliente)
        print("  Nit:", nit_cliente)
        print("Productos comprados:")
        self.mostrarCarrito()
        print("Total:", total)
        print("Impuesto (12%):", impuesto)

        # Vaciar el carrito al terminar la compra
        self.items = []

    def mostrar(self):
        print(self.facturas)
