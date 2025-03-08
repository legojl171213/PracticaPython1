personas = int(input("Ingrese cuantas personas calcularan su IMC: "))

#Captura de datos personales mientras la cantidad de personas sea positiva
while personas>0: #Ciclo while dependiendo la cantidad de personas ingresadas debe ser un número mayor a 0 o no ejecutara el programa
    
    name = input("Nombre: ")
    lnp = input("Apellido paterno: ")
    lnm = input("Apellido materno: ")
    age = int(input("Edad: "))
    weight = float(input("Peso en Kg: "))
    height = float(input("Estatura: "))
    #Calculo del indice de masa corporal con la formula y con la funcion round ocupar solo 2 digitos después del punto decimal en el resultado
    IMC = round((weight/height**2),2)
    #Condicional para distinguir si se trata de un mayor de edad o un menor
    if age >= 18:
        print ("Es mayor de edad ")
        print ("Su indice de masa corporal es: "+ str(IMC))
    else:
        print ("Es menor de edad ")
        print ("Su indice de masa corporal es: "+ str(IMC))
    #Unión del nombre en una sola variable para usarla en un futuro
    nombreC = str(name+" "+lnp+" "+lnm)
    
    #Condicional para todas las opciones que se le darán al usuario dependiento el resultado de su IMC agregando su nombre completo en el resultado
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
    #Se declara personas -1 para terminar el ciclo while y no haya un loop
    personas = personas-1