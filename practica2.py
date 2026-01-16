import os

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir (a, b):
    return a / b
    

def main():
    opcion=0

    while opcion != 5:
        print("menu")
        print("1- Suma")
        print("2- Resta")
        print("3- Multiplicacion")
        print("4- Division")
        print("5- Salir")

        opcion= int(input("Digite una opcion: "))

        if opcion < 5:
            a= int(input("Ingrese el primer numero: "))
            b= int(input("Ingrese el segundo numero: "))



        if opcion == 1:
            print("Resultado: " + str(suma(a,b)))
            os.system("pause")
        
        elif opcion == 2:
            print("Resultado:", resta(a, b))
            os.system("pause")

        elif opcion == 3:
            print("Resultado:", multiplicar(a, b))
            os.system("pause")

        elif opcion == 4:
            print("Resultado:", dividir(a, b))
            os.system("pause")

        elif opcion == 5:
            print("Saliendo...")
            
        
        else:
            print("Opcion no disponible")

if __name__ == "__main__":
    main()

