personas = int(input("Ingrese cuantas personas calcularan su IMC: "))

#Captura de datos personales mientras la cantidad de personas sea positiva
while personas>0:
    
    name = input("Nombre: ")
    lnp = input("Apellido paterno: ")
    lnm = input("Apellido materno: ")
    age = int(input("Edad: "))
    weight = float(input("Peso en Kg: "))
    height = float(input("Estatura: "))
    
    IMC = round((weight/height**2),2)

    if age >= 18:
        print ("Es mayor de edad ")
        print ("Su indice de masa corporal es: "+ str(IMC))
    else:
        print ("Es menor de edad ")
        print ("Su indice de masa corporal es: "+ str(IMC))

    nombreC = str(name+" "+lnp+" "+lnm)
    
    if IMC >= 0 and IMC <= 15.99 :
        print (nombreC + " tiene Delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99 :
        print (nombreC + " tiene Delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print (nombreC + " tiene Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99 :
        print (nombreC + " esta Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print (nombreC + " tiene Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print (nombreC + " tiene obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        print (nombreC + " tiene obesidad media")
    elif IMC >= 40.00:
        print (nombreC + " tiene obesidad morbida")

    personas = personas-1