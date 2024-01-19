inicio = int(input("Ingrese el codigo"))
limite = int(input("Ingrese el limite"))

for x in range(inicio, limite):
    if(x % 2 == 0):
        print("| ",x)
        