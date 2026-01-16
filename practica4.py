x = 0
lista1 = []

while x != 20:
    d = int(input("Numero " + str(x + 1) + ": "))
    lista1.append(d)
    x += 1

lista1.sort()
print(lista1)

repetidos = {}

for num in lista1:
    if num in repetidos:
        repetidos[num] += 1
    else:
        repetidos[num] = 1

for num, veces in repetidos.items():
    print(str(num) + "-" + str(veces))

pares = []
impares = []

for num in lista1:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(pares)
print(impares)
