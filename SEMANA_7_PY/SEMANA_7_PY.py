p = i = 0

while True:
    num = int(input("ingrese un numero entero (negativo para salir):  "))

    if num < 0:break
    if num %2 == 0: p+=1
    else: i+= 1

print("\ncantidad de pares: ",p)
print("cantidad de pares: ",i)