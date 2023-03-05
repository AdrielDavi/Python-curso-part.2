#Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e imprime as dimensões da 
#matriz recebida, no formato iXj.
minha_matriz = [[1], [2], [3]]

def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    print(f"{linhas}X{colunas}")

dimensoes(minha_matriz)