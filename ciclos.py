print("DEPARTAENTO DE CONFECCION")
print("1. Ingresar producto")
print("2. Mostrar inventario en fabrica")
print("0. SALIR")
opcion= 100
listaProductos=[]

while opcion != 0:
    opcion=int(input("Digita una opcion: "))
    if opcion ==1:
        producto=input("Digita el producto que ingresa a fabrica: ")
        #Agregar un producto a la lista de producto
        listaProductos.append(producto)
    elif opcion ==2:
        print("Mostrando inventario: ")
        print(listaProductos)
    elif opcion ==0:
        print("Gracias, hasta luego...")
    else:
        print("Opcion invalida...")