class triangulo:
    def area(self)->None:
        b = int(input("\ningrese la base: "))
        h = int(input("ingrese la altura: "))
        print("\nArea: ",(b * h)/2)

    def perimetro(self)->None:
        l1 = int(input("\ningrese lado 1:"))
        l2 = int(input("ingrese lado 2:"))
        l3 = int(input("ingrese lado 3:"))
        print("el perimetro es: ",l1 + l2 + l3)

