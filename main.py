import time
from tabulate import tabulate
import singelton
class supermercado:
    def __init__(self):
        self.menu()
    def menu(self):

        while True:
            print(" ")
            print("-----------------Menu principal------------")
            print("1. Registrar producto")
            print("2. Registrar cliente")
            print("3. Realizar compra")
            print("4. Reporte de compra")
            print("5. Datos del estudiante")
            print("6. Consultar registros")
            print("7. salir")
            opcion = input("Elija una opción: ")
            print("-------------------------------------------")
            if opcion == "1":
                singelton.referenciaProducto.agregar_producto()
            elif opcion == "2":
                singelton.referenciaCliente.agregar_cliente()
            elif opcion == "3":
                nitCliente=input("Ingrese el nit del cliente ")
                clienteencontrado=singelton.referenciaCliente.buscarCliente(nitCliente)
                if clienteencontrado != None:
                    self.subMenu(clienteencontrado["codigo"],clienteencontrado["nit"])
            elif opcion == "4":
                ccliente=input("Ingrese el NIT del cliente para ver reportes: ")
                singelton.referenciaCarrito.buscarFactura(ccliente)
            elif opcion == "5":
               self.datosEstudiante()
            elif opcion == "6":
                singelton.referenciaCliente.mostrar_clientes()
                singelton.referenciaProducto.mostrar_productos()
            elif opcion == "7":
                print("Saliendo......")
                time.sleep(3)
                print("FUE UN GUSTO SERVIRTE. ¡VUELVE PRONTO!")
                break

    def subMenu(self,codigocliente,nit):
        while True:
            print("*********************Menu de compra****************")
            print("CODIGO DE CLIENTE: ("+str(codigocliente)+")")
            print("1. Agregar Producto")
            print("2. Terminar compra y facturar")
            opSub=input("Elija una opción: ")
            print("***************************************************")
            if opSub=="1":
                if singelton.referenciaProducto.mostrar_productos() == False:
                    pass
                else:
                    while True:
                        codigo_producto = input("Ingrese el código del producto que desea agregar al carrito ('fin' para terminar): ")
                        if codigo_producto.lower() == 'fin':
                            break
                        productoEncontrado=singelton.referenciaProducto.buscar_producto(codigo_producto)
                        if productoEncontrado != None:
                            #producto encontrado
                            cantidad=input("Cantidad de compra: ")
                            singelton.referenciaCarrito.carritoCompras(productoEncontrado["nombre"],productoEncontrado["precioUnitario"],cantidad)
                        else:
                            print("Error")
            elif opSub=="2":
                singelton.referenciaCarrito.factura(nit)

                break


    def datosEstudiante(self):
        datos = [
            ["Nombre", "Apellidos", "Carnet","Curso"],
            ["Edwin Danilo", "Jeronimo Tomas", "202200081","IPC2"]
        ]
        print(tabulate(datos, headers="firstrow", tablefmt="fancy_grid"))
if __name__ == "__main__":
    supermercado()
