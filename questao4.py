def soma_elementos(ini, fim, lista):
    soma_lista = sum(lista[ini:fim])
    return soma_lista
lista = [1,2,3,4,5]
print(soma_elementos(0,len(lista),lista))
print(soma_elementos(1,4,lista))
print(soma_elementos(2,2,lista))