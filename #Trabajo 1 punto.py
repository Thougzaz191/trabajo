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