#trabajo
sw = 1
def principal_menu():
    try:
        while sw == 1:
            print("MENU PRINCIPAL")
            print("1.Mantencion de maestros")
            print("2.Inventario")
            print("3.Produccion")
            print("4.Ventas")
            print("5.Salir")
            op = int(input("Ingresa una opcion"))

            if op == "1":
                menu_maestros()

            elif op == "2":
                menu_inventario()
                
            elif op == "3":
                menu_produccion()

            elif op == "4":
                menu_ventas()

            elif op == "5":
                sw = 0
            else:
                print("Opcion invaldia")
    except ValueError:
        print("Tiene que ingresar numeros, No letras ni otro signo")

























#Parte Benjaming










#Parte Vicente
def menu_inventario():
    iv = 1
    while iv == 1:
        print("MENU INVENTARIO")
        print("a. Pedidos a proveedores")
        print("b. Recepción de Fármacos e Insumos clínicos")
        print("c. Lista de stock de Fármacos e Insumos clínicos")
        print("d. Reporte de Fármacos e Insumos clínicos a comprar")
        op = input("Ingresa una opcion: ")

        if op == "a":
            print("Solo registro simulado de pedidos")
        elif op == "b":
            codigo = int(input("Ingrese el codigo del farmaco o insumo: "))
            cantidad = int(input("Ingrese la cantidad recibida:"))
            






#Parte Valentine










#Parte Gabriel