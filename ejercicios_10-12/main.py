#**Ejercicio Diez**
##Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

numero = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, numero+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

#**Ejercicio Once**
##Escriba un programa que pregunte cuantos números se van a introducir, pida los esos números (que puedan ser decimales) y calcule su suma, mostrar por terminal la suma de los números introducidos.

frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))

#**Ejercicio Doce**
##Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.

def main():
    print("NÚMEROS NEGATIVOS")
    numero = int(input("¿Cuántos valores va a introducir? "))

    if numero < 0:
        print("¡Imposible!")
    else:
        contador = 0
        for i in range(1, numero + 1):
            valor = float(input(f"Escriba el número {i}: "))
            if valor < 0:
                contador = contador + 1
        if contador == 0:
            print("No ha escrito ningún número negativo.")
        elif contador == 1:
            print("Ha escrito 1 número negativo.")
        else:
            print(f"Ha escrito {contador} números negativos.")


if __name__ == "__main__":
    main()