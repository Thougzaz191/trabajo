#trabajo
sw = 1
pacientes = {}
episodio = {}
pacientes = {}
farmacos = {}
insumos = {}
productos_terminados = {}
prestaciones = {}
proveedores = {}

stock_farmacos = {}
stock_insumos = {}
stock_productos = {}
costos = {}

recetas = {}
episodios = {}

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

























#Parte Benjamin
def menu_maestros():
    while True:
        print("\n--- MANTENCIÓN DE MAESTROS ---")
        print("1. Pacientes")
        print("2. Fármacos")
        print("3. Insumos Clínicos")
        print("4. Productos Terminados")
        print("5. Prestaciones Médicas")
        print("6. Proveedores")
        print("7. Volver")
        opcion = input("Seleccione entidad: ")

        if opcion == "1":
            mantener(pacientes, "Paciente")
        elif opcion == "2":
            mantener(farmacos, "Fármaco")
        elif opcion == "3":
            mantener(insumos, "Insumo Clínico")
        elif opcion == "4":
            mantener(productos_terminados, "Producto Terminado")
        elif opcion == "5":
            mantener(prestaciones, "Prestación Médica")
        elif opcion == "6":
            mantener(proveedores, "Proveedor")
        elif opcion == "7":
            break
        else:
            print("Opción inválida")

def mantener(diccionario, nombre):
    while True:
        print(f"\n-- {nombre.upper()} --")
        print("1. Crear")
        print("2. Modificar")
        print("3. Bloquear")
        print("4. Mostrar")
        print("5. Volver")
        opcion = input("Seleccione acción: ")

        if opcion == "1":
            codigo = input("Código: ")
            descripcion = input("Descripción: ")
            diccionario[codigo] = {"descripcion": descripcion, "activo": True}
        elif opcion == "2":
            codigo = input("Código a modificar: ")
            if codigo in diccionario:
                nueva = input("Nueva descripción: ")
                diccionario[codigo]["descripcion"] = nueva
            else:
                print("No existe")
        elif opcion == "3":
            codigo = input("Código a bloquear: ")
            if codigo in diccionario:
                diccionario[codigo]["activo"] = False
        elif opcion == "4":
            for k, v in diccionario.items():
                estado = "Activo" if v["activo"] else "Bloqueado"
                print(f"{k}: {v['descripcion']} ({estado})")
        elif opcion == "5":
            break
        else:
            print("Opción inválida")








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



