import random

print("***************************************************")
print("   bienvenido al juego adividador kas kas kas      ")
print("                                                   ")
print("1. Ud. tiene que adivinar el numero entre 1 y 20   ")
print("2. tienes 2 intentos                               ")
print("***************************************************")

intentos = 3
secreto = random.randint(1,20)

while intentos > 0:
    num = int(input("\ningrese numero: "))

    if secreto == num:
        print("\ncorrecto! adivinaste el numero.")
        break
    else:
        intentos-=1
        if num > secreto: print(f"pista: El numero es mayor.te quedan {intentos} ")
        else: print(f"\nEl numero es menor.te quedan {intentos} intentalo")
else:print("\nno lograste adivinar el numero: ",secreto)