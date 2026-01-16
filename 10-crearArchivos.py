from io import open 
import math

lectura=""
texto=open("archivo.txt","r")
lectura= texto.readLines()
print(type(lectura))
print(lectura)

for i in lectura: 
    print(i)
texto.close()
