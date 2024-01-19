promedio_general = 0
total = 0
cantidad = 0 
calificación = 1 
while(calificación !=0): 
    #se permite solamente del 1 al 5 
    #while...if
    calificación = int(input("Ing calif: "))
    total += calificación
    cantidad+=1

#restamos 1 a cantidad por el exceso de calif = 0
cantidad-=1

promedio_general = total / cantidad

print(f"El promedio general es: ", promedio_general)

