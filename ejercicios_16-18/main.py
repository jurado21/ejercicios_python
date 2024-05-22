#**Ejercicio Dieciséis**
##Desarrolla un programa en Python que permita gestionar una lista de tareas pendientes. El programa debe cumplir con los siguientes requisitos:
#
##- Debe permitir agregar nuevas tareas a la lista.
##- Debe permitir marcar tareas como completadas, lo que las eliminará de la lista de tareas pendientes.
##- Debe mostrar la lista actual de tareas pendientes.
##- Debe proporcionar un menú interactivo que permita al usuario seleccionar entre las opciones anteriores y salir del programa.
##El menú debe presentar las siguientes opciones:
#
##- Agregar tarea
##- Marcar tarea como completada
##- Mostrar tareas
##- Salir

tareas:list=[] #creando una lista vacia
menu=f"""
        ________MENU DE OPCIONES_________
        1.Agregar Tarea
        2.Marcar Tarea completa
        3.Mostrar Tarea
        4.Salir
        """
while True:
    print(menu)
    opcion=input("Ingresa la opcion que deseas realizar :")
    if opcion == "4":
        break
    elif opcion == "1":
        tarea=input("Ingrese una tarea: ")
        tareas.append(tarea)
        print(f"tarea {tarea} fue ingresada con exito!")
    elif opcion == "2":
        print(tareas)
        eliminar=input("escribe la tarea que deseas eliminar: ")
        el_eliminado=""
        for i,l in enumerate(tareas):
            if l == eliminar:
                el_eliminado=tareas.pop(i)
        print(f"la tarea {el_eliminado} fue eliminado de pendientes")
    elif opcion == "3":
        print(tareas)
        print(f"tines {len(tareas)} tareas pendientes")

#**Ejercicio Diecisiete**
##Crea un programa en Python que simule el funcionamiento de un cajero automático. El programa debe permitir al usuario realizar las siguientes operaciones:
#
##- Verificar el saldo de su cuenta.
##- Depositar dinero en su cuenta.
##- Retirar dinero de su cuenta.
##- Salir del programa.
##El programa debe iniciar con un saldo inicial predeterminado y mostrar un menú con las siguientes opciones:
#
##- Verificar saldo
##- Depositar dinero
##- Retirar dinero
##- Salir

saldo:int=100
mensaje=f"""
_________________MENU DE OPCIONES_________________
1.Verificar saldo
2.Depositar dinero
3.Retirar dinero
4.Salir
"""

while True:
    print(mensaje)
    opcion=input("Ingreser la accion que desea realizar: ")
    if opcion == "1":
        print(f"el saldo en su cuenta es de: {saldo}")
    elif opcion == "2":
        cantidad=int(input("ingresa la cantidad a suma: "))
        print(f"se agrego {cantidad} asu saldo actual de {saldo}")
        saldo+=cantidad
    elif opcion == "3":
        cantidad=int(input("ingresa la cantidad a retira: "))
        print(f"se retiro {cantidad} as u saldo de {saldo}")
        saldo-=cantidad
    elif opcion == "4":
        break

#**Ejercicio Dieciocho**
##Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan.
password="hola"
pide_password=input("ingrese su contra: ")
while password!=pide_password:
    print("contra incorrecta")
    pide_password=input("ingrese su contra: ")
print("contra correcta bienvenido al sistem")