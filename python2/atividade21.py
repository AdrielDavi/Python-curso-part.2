#mplemente a função encontra_impares(lista), que recebe como parâmetro uma lista de números inteiros
# e devolve uma outra lista apenas com os números ímpares da lista dada.

#Sua solução deve ser implementada utilizando recursão.


def encontra_impares(lista):
    if not lista: # se a lista estiver vazia
        return []
    else:
        if lista[0] % 2 != 0: # se o primeiro elemento for ímpar
            return [lista[0]] + encontra_impares(lista[1:]) # adiciona o primeiro elemento à lista e chama a função recursivamente com o restante da lista
        else:
            return encontra_impares(lista[1:]) # chama a função recursivamente com o restante da lista
