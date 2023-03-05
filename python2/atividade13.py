#Escreva a função ordenada(lista), que recebe uma lista com números inteiros como parâmetro e 
#devolve o booleano True se a lista estiver ordenada e False se a lista não estiver ordenada.

def ordenada(lista):
    """
    Verifica se a lista está ordenada.
    Retorna True se a lista estiver ordenada e False caso contrário.
    """
    for i in range(len(lista) - 1):
        if lista[i] > lista[i+1]:
            return False
    return True
