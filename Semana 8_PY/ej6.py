dolar = 3.78
euro = 4.20

while True:
    soles = float(input("ingrese el monto en soles: "))

    def conv_d():
        return round(soles / dolar)

    def conv_e():
        return round(soles/euro)

    print("\nbienvenido al sistema de conversion de moneda")
    print("\n1. dolares")
    print("2. euros")

    opc = int(input("\ningrese una opcion: "))

    if opc in(1,2):
        if opc == 1: print("\nconversion a dolares: ",conv_d())
        else: print("\nconversion a euros: ",conv_e())
    else: print("opcion no valida!")

    conti = input("deseas continuar? presione(y): ")

    if conti != "y":
                print("\nprograma finalizado")
                break