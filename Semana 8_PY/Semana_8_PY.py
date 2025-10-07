def suma(a,b): print("\nla suma es: ",a+b)
def resta(a,b): print("\nla resta es: ",a-b)
def multi(a,b): print("\nla multi es: ",a*b)
def divi(a,b):
    if b!= 0: print("\nla division es: ",a/b)
    else: print("\n no se pude dividir entre 0")

def operaciones():
    while True:
            print("menu de operaciones")
            print("\n1.suma")
            print("2.resta")
            print("3.multiplicacion")
            print("4.division")

            opc = int(input("\ningrese una opcion: "))

            a = int(input("\ningrese  el primer numero: "))
            b = int(input("\ningrese  el segundo numero: "))

            match opc:
                case 1: suma(a,b)
                case 2: resta(a,b)
                case 3: multi(a,b)
                case 4: divi(a,b)
                case _:  print("opcion no valida") 

            conti = input("deseas continuar? presione (y): ")
            
            if conti != "y":
                print("\nprograma finalizado")
                break

operaciones()