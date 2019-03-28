# Karimn Daniel Hernández Castorena
# Programa que divide, encuentra el numero mayor y termina las acciones.

def dividir(divi, divisor):
    numDivi = divi
    co = 0

    while divi >= divisor:
        divi = divi - divisor
        co += 1

    print(numDivi, "/", divisor, "=", co, ", sobra", divi)
    print()


def encontrarMayor():
    num = 0
    numMayor = 0

    print("Teclea una serie de números para encontrar el mayor.")
    num = int(input("Teclea el número [-1 para salir]: "))

    if num != -1:
        while num != -1:
            if num >= 0:
                if num >= numMayor:
                    numMayor = num
            num = int(input("Teclea el número [-1 para salir]: "))
        print("El número mayor es:", numMayor)
        print()
    else:
        print("No hay número mayor")
        print()


def main():
    print("Misión 07. Ciclos while")
    print("Autor: Karimn Daniel Hernández Castorena")
    print("Matrícula: A01379038")
    print()
    print("1. Calcular divisiones")
    print("2. Encontrar el número mayor")
    print("3. Terminar")
    print()
    opcion = int(input("Teclea tu opción: "))
    print()

    while opcion != 3:
        if opcion == 1:
            divi = int(input("Dividiendo: "))
            divisor = int(input("Divisor: "))
            dividir(divi, divisor)

        elif opcion == 2:
            encontrarMayor()

        elif opcion < 0 or opcion > 3:
            print("ERROR, teclea 1, 2 o 3")
            print()
        opcion = int(input("""Misión 07. Ciclos while
Autor: Karimn Daniel Hernández Castorena
Matrícula: A01379038
                      
1. Calcular divisiones
2. Encontrar el mayor
3. Salir"
                           
Teclea tu opción: """))
        print()

    print("Gracias por usar este programa, regresa pronto!! :)")


main()
