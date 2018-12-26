import random

def imprime_comeco():
    print("*********************************")
    print("Bem vindo ao jogo da forca!")
    print("*********************************")

def ler_arquivo(caminho):
    lista_palavras = []
    with open(caminho) as arquivo:
        for linha in arquivo:
            lista_palavras.append(linha.strip().upper())
    return lista_palavras

def define_palavra(lista_palavras):
    return lista_palavras[random.randrange(0,len(lista_palavras) - 1)]

def retorna_chute():
    return input("\nDigite uma letra: ").strip().upper()

def preenche_resultado(palavra):
    return ["_" for letra in palavra]

def imprime_palavra(resultado):
    for letra in resultado:
        print(letra, sep=" ", end=" ")
    print("\n")

def resolve_jogo(palavra):
    enforcou = False
    acertou = False
    erros = 0
    resultado = preenche_resultado(palavra)
    imprime_palavra(resultado)
    while (not enforcou and not acertou):
        chute = retorna_chute()
        index = 0
        if (chute in palavra):
            for letra in palavra:
                if (chute == letra):
                    resultado[index] = letra
                index += 1
        else:
            erros += 1
            print("Você errou. Jogadas restantes:{}".format(6 - erros))
        acertou = "_" not in resultado
        enforcou = erros == 6
        imprime_palavra(resultado)
    if (acertou):
        print("Você ganhou!")
    if (enforcou):
        print("Você perdeu!")

def jogar():
    imprime_comeco()
    lista_palavras = ler_arquivo("c:/Users/f0fp559/Documents/alura/Python/jogos/palavras.txt")
    palavra = define_palavra(lista_palavras)
    resolve_jogo(palavra)

if(__name__ == "__main__"):
    jogar()