#Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz que represente sua soma
#caso as matrizes tenham dimensões iguais. Caso contrário, a função deve devolver False.

def soma_matrizes(m1, m2):
    linhas_m1, colunas_m1 = len(m1), len(m1[0])
    linhas_m2, colunas_m2 = len(m2), len(m2[0])

    if linhas_m1 != linhas_m2 or colunas_m1 != colunas_m2:
        return False

    resultado = []
    for i in range(linhas_m1):
        linha = []
        for j in range(colunas_m1):
            elemento = m1[i][j] + m2[i][j]
            linha.append(elemento)
        resultado.append(linha)

    return resultado
