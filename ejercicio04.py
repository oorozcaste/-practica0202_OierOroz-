edad = int(input("dime tu edad: "))
sueldo = float(input("dime cuanto ganas al mes: "))

if edad > 16 and sueldo >= 1000:
    print("puedes tributar")
else:
    print("no puede tributar")
    