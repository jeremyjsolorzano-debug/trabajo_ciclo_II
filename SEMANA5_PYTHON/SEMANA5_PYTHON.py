#Profesor Yordan :)
def Ejercicio1():
    edad = int(input("Buen día. Ingrese su edad: "))
    
    if (edad >= 18):
        print("Usted puede votar.")

        if edad >= 25:
            print("Usted es candidato para un cargo político")
        else: 
            print("Usted NO es candidato para un cargo político")
    else:
        print("Usted no puede votar.")
        print("Usted no puede ejercer un cargo político.")

def Ejercicio2():
    num1 = float(input("Buen día. Ingrese el primer número: ")) # el profesor lo puso como lado
    num2 = float(input("Buen día. Ingrese el segundo número: "))
    num3 = float(input("Buen día. Ingrese el tercero número: "))

    if (num1 == num2 == num3):
        print("El triángulo es Equilátero")
    
    elif (num1 == num2 or num1 == num3):
        print("El triángulo Isósceles")
    else:
        print("El triángulo Escaleno")

def ejercicio3():
    n = int(input("Ingrese un numero: "))
    suma = 0

    print()

    for i in range(1,n+1):
        print(i)

        if i % 2 == 0:
            suma += i
    print("\nSuma de pares: ", suma)

def ejercicio4():
    cant = int(input("ingrese la cantidad de numeros a ingresar: "))
    ceros = pares = impares = 0
    print()
    for i in range(1, cant+1):
        num = int(input(f"ingrese el numero  {i}: "))

        if num == 0:
            ceros+=1
        elif num % 2==0:
            pares += 1
        else:
            impares += 1

    print("\n# ceros: ",ceros)
    print("# pares: ",pares)
    print("# impares: ",impares)



ejercicio4()