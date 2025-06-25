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
sw == 0
def principal_menu():
    try:
        global sw
        while sw == 1:
            print("MENU PRINCIPAL")
            print("1.Mantencion de maestros")
            print("2.Inventario")
            print("3.Produccion")
            print("4.Ventas")
            print("5.Salir")
            op = int(input("Ingresa una opcion "))

            if op == 1:
                menu_maestros()

            elif op == 2:
                menu_inventario()
                
            elif op == 3:
                menu_produccion()

            elif op == 4:
                menu_ventas()

            elif op == 5:
                sw = 0
            else:
                print("Opcion invalida")
    except ValueError:
        print("Tiene que ingresar numeros, No letras ni otro signo")


#Parte Benjamin
def menu_maestros():
    ok = False
    while ok == False:
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
            ok = True  
        else:
            print("Opción inválida")

def mantener(diccionario, nombre):
    ok = False
    while ok == False:
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
            ok = True
        else:
            print("Opción inválida")


#Parte Vicentedown
def menu_inventario():
    iv = 1
    while iv == 1:
        print("MENU INVENTARIO")
        print("a. Pedidos a proveedores")
        print("b. Recepción de Fármacos e Insumos clínicos")
        print("c. Lista de stock de Fármacos e Insumos clínicos")
        print("d. Reporte de Fármacos e Insumos clínicos a comprar")
        print("e. Volver")
        op = input("Ingresa una opcion: ")

        if op == "a":
            codigo = input("Ingrese el codigo del proveedor: ")
            descripcion = input("Ingrese la descripcion del pedido: ")
            cantidad = int(input("Ingrese la cantidad del pedido: "))
            proveedores[codigo] = {"descripcion": descripcion, "cantidad": cantidad}
            print("Pedido creado exitosamente")
        elif op == "b":
            codigo = input("Ingrese el codigo del fármaco o insumo: ")
            descripcion = input("Ingrese la descripcion del fármaco o insumo: ")
            cantidad = int(input("Ingrese la cantidad recibida: "))
            if op == "fármaco":
                stock_farmacos[codigo] = {"descripcion": descripcion, "cantidad": cantidad}
            elif op == "insumo":
                stock_insumos[codigo] = {"descripcion": descripcion, "cantidad": cantidad}
            print("Recepción registrada exitosamente")    
        elif op == "c":
            print("Lista de stock de Fármacos e Insumos clínicos:")
            print("Fármacos:")
            for k, v in stock_farmacos.items():
                print(f"{k}: {v['descripcion']} - Cantidad: {v['cantidad']}")
            print("Insumos Clínicos:")
            for k, v in stock_insumos.items():
                print(f"{k}: {v['descripcion']} - Cantidad: {v['cantidad']}")    
        elif op == "d":
            print("Reporte de Fármacos e Insumos clínicos a comprar:")
            print("Fármacos:")
            for k, v in stock_farmacos.items():
                if v[cantidad] < 10:
                    print(f"{k}: {v['descripcion']} - Cantidad: {v['cantidad']}")
        elif op == "e":
            iv = 0


#Parte Valentine

def menu_produccion():
    ok = False
    while ok == False:
        print("\n--- PRODUCCIÓN ---")
        print("1. Crear Receta de Producto Terminado")
        print("2. Crear Orden de Producción")
        print("3. Ver Stock de Productos Terminados")
        print("4. Volver")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            codigo = input("Código producto terminado: ")
            composicion = {}
            ok2 = False
            while ok2 == False:
                comp = input("Código de insumo o fármaco (vacío para terminar): ")
                if comp == "":
                    ok2 = True
                cant = int(input("Cantidad a usar: "))
                composicion[comp] = cant
            recetas[codigo] = composicion
        elif opcion == "2":
            codigo = input("Producto terminado a fabricar: ")
            cantidad = int(input("Cantidad a fabricar: "))
            if codigo in recetas:
                for insumo, cant in recetas[codigo].items():
                    total = cant * cantidad
                    if insumo in stock_farmacos and stock_farmacos[insumo] >= total:
                        stock_farmacos[insumo] -= total
                    elif insumo in stock_insumos and stock_insumos[insumo] >= total:
                        stock_insumos[insumo] -= total
                    else:
                        print(f"No hay suficiente de {insumo}")
                        return
                stock_productos[codigo] = stock_productos.get(codigo, 0) + cantidad
            else:
                print("No existe receta")
        elif opcion == "3":
            print("Stock Productos Terminados:", stock_productos)
        elif opcion == "4":
            ok = True



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
                        print("peo")
principal_menu()


