#Este exercício tem duas partes:

#Implemente a função incomodam(n) que devolve uma string contendo "incomodam " 
#(a palavra seguida de um espaço) n vezes. Se n não for um inteiro estritamente positivo, a função deve
# devolver uma string vazia. Essa função deve ser implementada utilizando recursão.

#Utilizando a função acima, implemente a função elefantes(n) que devolve uma string contendo a letra da 
#música "Um elefante incomoda muita gente" de 1 até n elefantes. Se n não for maior que 1, a função deve
# devolver uma string vazia. Essa função também deve ser implementada utilizando recursão.

#Observe que, para um elefante, você deve escrever por extenso e no singular ("Um elefante..."); para os
# demais, utilize números e o plural ("2 elefantes...").
def incomodam(n):
    if n <= 0:
        return ""
    else:
        return "incomodam " + incomodam(n-1)

def elefantes(n):
    if n <= 1:
        return ""
    else:
        verso_atual = str(n) + " elefantes incomodam " + incomodam(n) + "muito mais"
        resto_da_musica = elefantes(n-1)
        if resto_da_musica:
            return "Um elefante incomoda muita gente\n" + verso_atual + "\n" + resto_da_musica + "\n" + str(n) + " elefantes incomodam " + incomodam(n) + "muito mais"
        else:
            return "Um elefante incomoda muita gente\n" + verso_atual

