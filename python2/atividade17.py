#Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista e devolve o 
#índice correspondente à posição do elemento encontrado. Utilize o algoritmo de busca binária. Nos casos em 
#que o elemento buscado não existir na lista, a função deve devolver o booleano False.
#Além de devolver o índice correspondente à posição do elemento encontrado, sua função deve imprimir cada
#um dos índices testados pelo algoritmo.

def busca(lista, elemento):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        print(meio)
        if elemento == lista[meio]:
            return meio
        elif elemento < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
    return False
