import os
resp = 1 
while resp != 0:
    print("Paint (1)")
    print("Calc (2)")
    print("Apagar PC en 2 hora (3)")
    print("Google (4)")
    print("Word 2016 (5)")
    print("Salir (0)")
    resp = int(input("Seleccione: "))
    if(resp == 1):
        os.system("mspaint")
    elif(resp == 2):
        os.system("calc")
    elif(resp == 3):
        os.system("shutdown -s -t 7200")
    elif(resp == 4):
        os.system("start chrome")
    elif(resp == 5):
        os.system("IEXPLORER")
    else:
        print("No entiendo esa orden")

