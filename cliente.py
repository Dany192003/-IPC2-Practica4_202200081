from tabulate import tabulate

class registroCliente:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self):
        codigo = len(self.clientes) + 1
        nombre = input("Nombre del cliente: ")
        correo = input("Correo electrónico: ")
        nit = input("Nit: ")
        cliente = {"codigo": codigo, "nombre": nombre, "correo": correo, "nit": nit}
        self.clientes.append(cliente)
    def mostrar_clientes(self):
        if self.clientes:
            headers = ["Código", "Nombre", "Correo", "Nit"]
            rows = [[cliente["codigo"], cliente["nombre"], cliente["correo"], cliente["nit"]] for cliente in self.clientes]
            print("Lista de clientes:")
            print(tabulate(rows, headers=headers, tablefmt="grid"))
        else:
            print("No hay clientes registrados.")

    def buscarCliente(self,nitbuscar):
        cliente_encontrado = None
        for cliente in self.clientes:
            if cliente["nit"] == nitbuscar:
                cliente_encontrado = cliente
                return cliente_encontrado
                break

        if cliente_encontrado:
            '''print("Cliente encontrado:")
            headers = ["Código", "Nombre", "Correo", "Nit"]
            print(tabulate([[cliente_encontrado["codigo"], cliente_encontrado["nombre"], cliente_encontrado["correo"],
                             cliente_encontrado["nit"]]], headers=headers, tablefmt="grid"))'''
        else:
            print("Cliente con NIT '{}' no encontrado.".format(nitbuscar))

