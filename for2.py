promedio_general = 0
total = 0
cantidad = 0 
calificación = 1 
while(calificación !=0): 
    #se permite solamente del 1 al 5 
    #while...if
    calificación = int(input("Ing calif: "))
    if(calificación >=1 and calificación <=5):
        total += calificación
        cantidad+=1
    elif(calificación == 0):
        print("-----")
        continue
    else:
        print("Ingrese del 1 al 5")       

promedio_general = total / cantidad

print(f"El promedio general es {promedio_general}")

