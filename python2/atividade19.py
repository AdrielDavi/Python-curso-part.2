#Implemente a função insertion_sort(lista), que recebe uma lista com números inteiros como parâmetro e
#devolve esta lista ordenada. Utilize o algoritmo insertion sort.

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = chave
    return lista
