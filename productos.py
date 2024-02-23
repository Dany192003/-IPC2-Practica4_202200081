from tabulate import tabulate

class registroProductos:
    def __init__(self):
        self.productos = []

    def agregar_producto(self):
        codigo = len(self.productos) + 1
        nombre = input("Nombre del producto: ")
        descripcion = input("Descripción del producto: ")
        precioUnitario = input("Precio unitario: ")
        producto = {"codigo": codigo, "nombre": nombre, "descripcion": descripcion, "precioUnitario": precioUnitario}
        self.productos.append(producto)
    def mostrar_productos(self):
        if self.productos:
            headers = ["Código", "Nombre", "Descripción", "Precio unitario"]
            rows = [[producto["codigo"], producto["nombre"], producto["descripcion"], producto["precioUnitario"]] for producto in self.productos]
            print("Lista de productos:")
            print(tabulate(rows, headers=headers, tablefmt="grid"))
        else:
            print("No hay productos registrados.")
            return False

    def buscar_producto(self,codigo_buscar):
        producto_encontrado = None
        for producto in self.productos:
            if str(producto["codigo"]) == codigo_buscar:
                producto_encontrado = producto
                return producto_encontrado
                break

        if producto_encontrado==False:
            print("Producto con código '{}' no encontrado.".format(codigo_buscar))
