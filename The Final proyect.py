#The Final Proyect
'''
Estudiante: Juan Sebastian Gómez Agudelo
Código: 202259474
Profesor: Andres Felipe Velasco
Grupo: 50 
'''

def menuprincipal():
    a = "------CENTRO DE SERVICIO AUTOMOTRIZ------"
    b = "1) Ver el catalogo"
    c = "2) Adicionar un producto/acceorio o servicio al menú"
    d = "3) Realizar una orden de trabajo"
    e = "0) Cerrar programa"
    salida = f"{a}\n{b}\n{c}\n{d}\n{e}"
    return salida
print(menuprincipal())
#Listas con que corresponden a cada columna 
#Espacios para que quede mas ordenado a la hora de imprimir
menu = input("Digite la opcion que desea realizar: ")
descripcion_productos = ["Producto","llanta  ","Espejo  ","volante ","Palanca ","Bombilla"]
codigo_productos = ["Codigo","320   ","150   ","212   ","304   ","505   "]
valor_productos = ["Valor ","150000","15000 ","200000","165000","35000 "]
codigo_servicios = ["Codigo","188   ","422   ","330   ","109   ","270   "]
descripcion_servicios = ["Servicio           ","Lavado             ","Ajuste de clutch   ","Cambio de aceite   ","Reemplazo de Bujias","Ajuste de frenos   "]
valor_servicios = ["Valor","15000","290000","120000","150000","230000"]
codigo_orden = ["Codigo"]
tipo_orden = ["Tipo    "]
cantidad_orden =["Cantidad"]
valor_orden = ["Valor "]
p = 6
s = 6
o = 1
valorTotal = 0
while menu != "0":
    if menu == "1":
        print()
        print("Productos:")
        print("------------------------------")
        for i in range(0,p):
            print(f"| {codigo_productos[i]} | {descripcion_productos[i]} | {valor_productos[i]} |")
            print("------------------------------")
        print()
        print("Servicios:") 
        print("-----------------------------------------")
        for i in range(0,s):
            print(f"| {codigo_servicios[i]} | {descripcion_servicios[i]} | {valor_servicios[i]} |")
            print("-----------------------------------------")
        back = input("Presiona (4) para volver al menú principal: ")
        if back == "4":
            print(menuprincipal())
            menu = input("Digite la opcion que desea realizar: ")
    elif menu == "2":
        print("¿Que desea adicionar?")
        print("(1) Productos\n(2) Servicios\n\n(4) para volver al menu principal")
        añadir = input("Presiona para añidir: ")  
        while añadir != "4":            
            if añadir == "1":
                codigoNew = input("Digite el codigo del Producto: ")
                productoNew = input("Digite la descripción del producto: ") 
                valorNew = input("Digite el valor del producto: ")
                codigoNew += " "" "" "
                codigo_productos.append(codigoNew)
                descripcion_productos.append(productoNew)
                valor_productos.append(valorNew)
                p+=1
                print()
                print("Su producto se añadió con exito, revise el catalogo para verlo")   
                print()    
            elif añadir == "2":
                codigoNew = input("Digite el codigo del servicio: ")
                productoNew = input("Digite la descripción del servicio: ") 
                valorNew = input("Digite el valor del servicio: ")
                codigoNew += " "" "" "
                codigo_servicios.append(codigoNew)
                descripcion_servicios.append(productoNew)
                valor_servicios.append(valorNew)
                s+=1
                print()
                print("Su producto se añadió con exito, revise el catalogo para verlo") 
                print()
            print("1) Adicionar un producto.\n2) Adicionar un servicio\n3) Volver al menú principal")
            continuar = input("Digite la opcion que desea realizar: ")
            if continuar == "1":
                añadir = "1"
            elif continuar == "2":
                añadir = "2"
            else:
                añadir = "4"
        if añadir == "4":
            print(menuprincipal())
            menu = input("Digite la opcion que desea realizar: ")
    elif menu == "3":
        print("¿Que desea adicionar a la orden de trabajo?")
        print("(1) Productos\n(2) Servicios\n\n(4) para volver al menu principal")
        tipo = input("Digite la opcion que desea realizar: ")
        while tipo != "4":
            if tipo == "1":
                k = "producto"
                ka = "productos"
            elif tipo == "2":
                k = "servicio"
                ka = "servicios"
            codigoOrden = input(f"Digite el codigo del {k}: ")
            codigoOrden += " "" "" "
            cant = int(input(f"Digite la cantidad de {ka} que desea añadir: "))
            if tipo == "1":
                lugar = codigo_productos.index(codigoOrden)
                precio = valor_productos[lugar]
            elif tipo == "2":
                lugar = codigo_servicios.index(codigoOrden)
                precio = valor_servicios[lugar]
            valorINT = cant * int(precio)
            valorTotal += valorINT
            cantSTR = str(cant) + " "" "" "" "" "" "" "
            valorSTR = str(valorINT)
            codigo_orden.append(codigoOrden)
            tipo_orden.append(k)
            cantidad_orden.append(cantSTR)
            valor_orden.append(valorSTR)
            o += 1
            print()
            print("Orden de Trabajo")
            print("-----------------------------------------")
            for i in range(0,o):
                print(f"| {codigo_orden[i]} | {tipo_orden[i]} | {cantidad_orden[i]} | {valor_orden[i]} |")
                print("-----------------------------------------")
            print()
            print(f"1) Añadir un producto.\n2) Añadir un servicio.\n3) Calcular el valor a pagar por la orden de trabajo.\n4) Volver al menú principal")
            continuar = input("Digite la opcion que desea realizar: ")
            if continuar  == "1":
                tipo = "1"
            elif continuar == "2":
                tipo = "2"
            elif continuar == "3":    
                print()
                print(f"El valor correspondiente por la orden de Trabajo es: ${valorTotal}")
                print()
                tipo = "4"
            else:
                tipo = "4"
        if tipo == "4":
            print(menuprincipal())
            menu = input("Digite la opcion que desea realizar: ")
    else:
        print("no corresponde")
        back = input("Presiona (4) para volver al menú principal: ")
        if back == "4":
            print(menuprincipal())
            menu = input("Digite la opcion que desea realizar: ")