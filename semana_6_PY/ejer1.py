num = int(input("ingrese  un numero positivo: "))
print()

while num <=0:
    num = int(input("error, ingrese un numero positivo: "))

i = 1
while i <=12:
    print(f"{i} x {num} = {i*num}")
    i+=1
