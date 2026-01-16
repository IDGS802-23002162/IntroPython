import os
i=1
x=1

while x!= 0:
    
    print("TABLAS")
    x= int(input("Digite el numero o use 0 para salir: "))
    
    rango=x*11

    for i in range (x,rango, x):
        print(i)
    os.system("pause")
    os.system("cls")