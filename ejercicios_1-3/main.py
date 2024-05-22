#**Ejercicio Uno**
##Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 puede entrar gratis, si tiene entre 4 y 18 debe pagar 5 soles, y si es mayor de 18 deberá pagar 10 soles.

edad=int(input("ingrese la edad del cliente"))
if edad <4:
    print("el cliente entra gratis")
elif edad >=4 and edad<18:
    print("cliente debe pagar 5 soles por entrada")
else:
    print("el cliente debe pagar 10 soles por entrada")

#**Ejercicio Dos**
##Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces

oracion:int=input("ingrese su oracion :")
for n in range(10):
    print(oracion)


#**Ejercicio Tres**
##Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero=int(input("ingrese el numero entero psotivo"))
if numero <=0:
    print("el numero no es positivo ingrese de nuevo")
else:
    impares = [str(i)for i in range (1 , numero+1)if i %2!=0]
    print("mostrar los numeros impares :",",".join (impares))
