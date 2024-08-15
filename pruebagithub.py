"""Cree un codigo que pida y muestre 10 número, luego guardarlo en un repositorio local para luego
subirlo a un repositorio remoto en github."""
lista_numeros=[]
for i in range(10):
    numeros=int(input("Ingrese un número: "))
    lista_numeros.append(numeros)
print(lista_numeros)