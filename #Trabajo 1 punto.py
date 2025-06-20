#trabajo
sw = 1
pacientes = {}
episodio = {}
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









#Parte Valentine










#Parte Gabriel
def menu_ventas():
    try:
        while sw == 1:
            print("Menu Ventas")
            print("1.Crear episodio")
            print("2.Asignar atencion")
            print("3.Calcular precio de antencion")
            print("4.Reporte de ventas")
            print("5.Salir")
            op = int(input("Ingresa una opcion: "))
    except ValueError:
        print("Tiene que ingresar numeros, No letras ni otro signo")

        if op == "1":
            codigo = input("Ingrese el codigo del episodio: ")
            paciente = input("Ingrese el codigo del paciente: ")
            fecha = input("Ingrese la fecha del episodio:")
            episodio[codigo] = {"paciente": paciente, "fecha": fecha, "items": []}
            print("Episodio creado exitosamente")
        elif op == "2":
            if codigo in episodio:
                item = input("Ingres el item de atencion/insumo/farmaco/prestacion:")
                costo = float(input("Ingrese el costo de la atencion: "))
                episodio[codigo]["items"].append({"item": item, "costo": costo})
                print("Atencion asignada exitosamente")
            else:
                print("Codigo no encontrado")
        
        elif op == "3":

            if codigo in episodio:
                total = 0
                for item, cantidad, costo in episodio[codigo]["items"]:

                    if item == "insumo":



