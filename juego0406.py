from curses.ascii import SI
import random

numero_secreto = random.randint(1,100)
cant_intentos = 0
cant_max_intentos = 6
adivinado = False

nombre = input("¿Puedes escribirme cual es tu nombre? =>")
    
print("Hola", nombre,"! Bienvenido al juego de avivinar el numero.")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("¡GAME OVER! No lograste avivinar el numero en", cant_max_intentos, " intentos pero podes volver a intentarlo")    
        break

    entrada = input("Introduce un numero del 1 al 99: ")
    numero = int(entrada)
    
    if numero == numero_secreto:
        print("¡Felicitaciones! Lograste adivinar el numero!")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero es mayor al que ingresaste.")
    else:
        print("El numero es menor al que ingresaste.")

    cant_intentos += 1
