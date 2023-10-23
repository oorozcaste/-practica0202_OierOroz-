genero = input("dime si eres hombre o mujer: ")
nombre = input("introduzca su nombre: ")

nombre = nombre.lower()

if (genero == "hombre" and nombre < "m") or (genero == "mujer" and nombre > "n"):
    print("perteneces a gryffindor")
else:
    print("perteneces a slythering")