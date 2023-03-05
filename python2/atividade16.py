#implementação em Python da função ordena que utiliza o algoritmo de ordenação por seleção 
#(selection sort):
def ordena(lista):
    """
    Ordena uma lista de números inteiros em ordem crescente utilizando o algoritmo selection sort.
    """
    tamanho = len(lista)
    for i in range(tamanho):
        indice_menor = i
        for j in range(i+1, tamanho):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
    return lista
