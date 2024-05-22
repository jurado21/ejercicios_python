#**Ejercicio Trece**
##Vamos a diseñar una calculadora que se enciende y hasta que no tecleamos `SAL` no se apaga.
##Esta calculadora funciona de la siguiente manera:
#
##- Recogemos los datos A y B
##- Si operación es 1 calcula la raíz cuadrada de la suma de A y B
##- Si operación es 2 calcula A / B. Vigilamos que B no sea 0...
##- Si la operación es 3 calculamos la siguiente fórmula: ( A * B ) / 2.5

while True:
    print(f"""
________MENU DE OPCIONES__________
    1.calcula la raiz cuadrada de la suma de A y B.
    2.calcula A/B.
    3.calcula (A*B)/2.5
    para salir escribe 'SAL'
        """)
    condicion=input("escribe CON o SAL:")
    if condicion.upper() == "SAL":
        break
    valor_A=int(input("ingrese el valor de A:"))
    valor_B=int(input("ingrese el valor de B:"))
    menu=input("Ingrese una opcion a realizar:")
    if menu=="1":
        suma=valor_A+valor_B
        print(f"la raiz de {suma} es: {pow(suma,2)}")
    elif menu=="2":
        while True:
            if valor_B == 0:
                valor_B=int(input("ingrese el valor de B:"))
            else:
                break
        divi=valor_A//valor_B
        print(f"la divicion es: {divi}")
    elif menu=="3":
        formula=(valor_A*valor_B)/2.5
        print(f"la formula es: {formula}")

#**Ejercicio Catorce**
##Tenemos la pantalla del móvil bloqueada. Partiendo de un `PIN_SECRETO`, intentaremos desbloquear la pantalla. Tenemos hasta 3 intentos. Simula el proceso con Python. En caso de acceder, lanza al usuario `login correcto`. Sino, `llamando ala policía`.

pantalla_bloqueo=f"""
_______________________________
|                              |       
|                              |
|                              |
|                              |
|   'INGRESE SU PIN SECRETO'   |
|    _____________________     |
|    | * * * * *  * * *  |     |
|    _____________________     |
|                              |
|                              |
|                              |
|                              |
________________________________ 
"""
print(pantalla_bloqueo)
numero_intentos:int=1
pin_correcto=1234
while numero_intentos <=3:
    pin_secreto=int(input("INGRESE EL PIN SECRETO: "))
    if pin_secreto != pin_correcto:
        print(f"""
            numero de intento {numero_intentos} erroneo
            'LLAMANDO A LA POLICIA'
            """)
        numero_intentos+=1
        continue
    else:
        print("login correcto")
        break


#**Ejercicio Quince**
##Crea un algoritmo para la sucesión de Fibonacci. La sucesión de Fibonacci es la siguiente serie:
#
##`0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89`
#
##Pista: Empezando por 0 y 1, el siguiente número es la suma de los dos números últimos.

limite=12
anterior=0
actual=1
siguiente=actual #2 #3 #5
for n in range (12):
    print(siguiente, end=", ")
    #end lo pone en horizontal.
    anterior=actual
    actual=siguiente
    siguiente=anterior+actual