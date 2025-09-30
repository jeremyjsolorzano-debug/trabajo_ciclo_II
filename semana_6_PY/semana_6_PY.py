g = input("genere una contraseña: ")

print("\n-----------------------------")
print("|     Valida tu contraseña    |")
print("|   1. ud. tiene 3 intentos   |")
print("-----------------------------\n")

intentos = 3

while(intentos > 0):
    c = input("ingrese la contraseña: ")

    if g == c:
        print("\nAcceso concedido. Bienvenido al sistema.")
        break
    else:
        intentos-=1
        print("contraseña incorreta. Sus intentos restantes son: ",intentos)
       
else: print("Acceso denegado! Cerrando sistema.")