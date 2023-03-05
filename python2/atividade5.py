#Escreva a função maiusculas(frase) que recebe uma frase (uma string) como parâmetro e devolve uma string 
#com as letras maiúsculas que existem nesta frase, na ordem em que elas aparecem.
def maiusculas(frase):
    maiusculas = ""
    for letra in frase:
        if letra.isupper():
            maiusculas += letra
    return maiusculas
frase = "Ola, Mundo!"
print(maiusculas(frase))