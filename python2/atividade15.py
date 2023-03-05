#Escreva a função lista_grande(n), que recebe como parâmetro um número inteiro n e devolve uma 
#lista contendo n números inteiros aleatórios.

import random

def lista_grande(n):
    """
    Cria uma lista contendo n números inteiros aleatórios.
    """
    lista = []
    for i in range(n):
        lista.append(random.randint(1, 100))  # gera um número inteiro aleatório entre 1 e 100
    return lista
