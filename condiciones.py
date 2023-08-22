nombreUsuario=input("Digite su nombre: ")
edadUsuario=int(input("Digite su edad: ")) #Casteo de datos(convertir un dato en otro dato)

if edadUsuario < 18:
    print("Usted es menor de edad, no puede ingresar a la discoteca")
else:
    print("Usted es mayor de edad, puede ingresar a la discoteca")