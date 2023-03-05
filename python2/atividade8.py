#escreva a função primeiro_lex(lista) que recebe uma lista de strings como parâmetro e devolve o 
#primeiro string na ordem lexicográfica. Neste exercício, considere letras maiúsculas e minúsculas.

def primeiro_lex(lista):
    primeiro = lista[0]
    for palavra in lista:
        if palavra < primeiro:
            primeiro = palavra
    return primeiro
