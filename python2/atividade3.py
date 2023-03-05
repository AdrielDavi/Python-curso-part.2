#Como proposto na primeira vídeo-aula da semana, escreva uma função imprime_matriz(matriz), que recebe uma
#matriz como parâmetro e imprime a matriz, linha por linha. Note que NÃO se deve imprimir espaços após o último elemento de cada linha!




def imprime_matriz(matriz):
    for linha in matriz:
        for i, elemento in enumerate(linha):
            # Imprime o elemento e uma quebra de linha caso seja o último da linha.
            if i == len(linha) - 1:
                print(elemento)
            else:
                print(elemento, end=" ")
