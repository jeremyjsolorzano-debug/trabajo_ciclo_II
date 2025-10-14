from triangulo import triangulo
t = triangulo()
from cuadrado import cuadrado
c = cuadrado()
def menu1()->None:
    print("Bienvenidos a calculo de areas y perimetros\n")
    print("************* Menu de opciones **************")
    print("*             1. triangulo                  *")
    print("*             2. cuadrado                   *")
    print("*             3. rectangulo                 *")
    print("*             4. trapecio                   *")
    print("*             0. salir                      *")
    print("*********************************************\n")

def menu2()->int:
        print("***** selecciones calculo *****")
        print("*         1.area              *")
        print("*         2.perimetro         *")
        print("*******************************")

        opcion = int(input("ingrese una opcion: "))
        return opcion
while True:
    menu1()
    while True:     
        opcion = int(input("ingrese opcion: "))

        if opcion in (0,1,2,3,4): break
        else: print("error. Opcion no valida.\n")

    match opcion:
        case 0: exit()#para salir exit()
        case 1:
            opc = menu2()

            match opc:
                case 1: t.area()
                case 2: t.perimetro()
        case 2:
             opc = menu2()
             l=  int(input("ingrese lado: "))
             match opc:
                 case 1: c.area(l);               
                 case 2: c.perimetro(l);
        case 3: print()
        case 4: print()

    while True:
        conti = input("quieres continuar? (s/n): ")
        if conti in("s","n"): break
        else: print("error, solo 's' o 'n'. ")
    
    if conti == "n": break        
    