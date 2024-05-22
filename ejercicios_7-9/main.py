#**Ejercicio Siete**
##Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))

#**Ejercicio Ocho**
##Escribir un programa que pida al usuario una palabra y luego muestre por pantalla la primera letra la letra que se encuentra en medio y la ultima letra separadas por comas(,).


#**Ejercicio Nueve**
##Escriba un programa que pregunte cuántos números se van a introducir, luego pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el anterior.