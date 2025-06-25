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
        sw = 1
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
            tipo = input("¿Es fármaco o insumo?: ").lower()
            if tipo == "fármaco":
                stock_farmacos[codigo] = {"descripcion": descripcion, "cantidad": cantidad}
            elif tipo == "insumo":
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
                if v["cantidad"] < 10:
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
        sw = 1
        while sw == 1:
            print("Menu Ventas")
            print("1.Crear episodio")
            print("2.Asignar atencion")
            print("3.Calcular precio de antencion")
            print("4.Reporte de ventas")
            print("5.Salir")
            op = int(input("Ingresa una opcion: "))
   

        if op == "1":
             codigo = input("Ingrese el código del episodio: ")
             paciente = input("Ingrese el código del paciente: ")
             fecha = input("Ingrese la fecha del episodio: ")
             episodios[codigo] = {"paciente": paciente, "fecha": fecha, "items": []}
             print("Episodio creado exitosamente")
        elif op == "2":
            codigo = input("Ingrese el código del episodio: ")
            if codigo in episodios:
                item = input("Ingrese el item de atención (producto/insumo/fármaco/prestación): ")
                costo = float(input("Ingrese el costo del ítem: "))
                cantidad = int(input("Ingrese la cantidad: "))
                episodios[codigo]["items"].append({"item": item, "costo": costo, "cantidad": cantidad})
                print("Atención asignada exitosamente")
            else:
                print("Código de episodio no encontrado")

        elif op == "3":

            if codigo in episodios:
                total = 0
                for item, cantidad, costo in episodios[codigo]["items"]:

                    if item in productos_terminados:
                        precio = costo * 0.60
                    elif item in farmacos:
                        precio = costo * 0.50
                    elif item in insumos:
                        precio = costo * 0.40
                    elif item in prestaciones:
                        precio = costo * 0.55
                    else:
                        precio = costo
                    total += precio * cantidad
                print(f"Total a pagar por atención: ${total:.2f}")
        elif op == "4":
            for codigo, data in episodios.items():
                costo_total = sum(c * cant for _, cant, c in data["items"])
                venta_total = 0
                for item, cant, c in data["items"]:
                    if item in productos_terminados:
                        venta_total += c * 0.60 * cant
                    elif item in farmacos:
                        venta_total += c * 0.50 * cant
                    elif item in insumos:
                        venta_total += c * 0.40 * cant
                    elif item in prestaciones:
                        venta_total += c * 0.55 * cant
                margen = venta_total - costo_total
                print(f"Episodio: {codigo}, Paciente: {data['paciente']}, Costo: {costo_total:.2f}, Venta: {venta_total:.2f}, Margen: {margen:.2f}")
        elif op == "5":
            sw = 0
    except ValueError:
        print("Tiene que ingresar numeros, No letras ni otro signo")

principal_menu()


