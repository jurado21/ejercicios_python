#**Ejercicio Cuatro**
##Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

# for i in range(1, 11):
#     for j in range(1, 11):
        
#         print(f"{i}*{j}")
                       
#     print(i*j)

#**Ejercicio Cinco**
##Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

# palabra = input("Introduce una palabra: ")

# for i in range(len(palabra)-1, -1, -1):
#     print(palabra[i])

#**Ejercicio Seis**

##Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo.

numero=int(input("ingreses el numero"))

for i in range(1, numero+1):
    print ("* i")

    for i in range(numero ):
        print("*"*numero)
  