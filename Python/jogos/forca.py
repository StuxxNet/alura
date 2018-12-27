import random

def jogar():
    imprime_comeco()
    lista_palavras = ler_arquivo("c:/Users/f0fp559/Documents/alura/Python/jogos/palavras.txt")
    palavra = define_palavra(lista_palavras)
    resolve_jogo(palavra)

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

def imprime_resultado(acertou, enforcou, palavra):
    if (acertou):
        print("Você ganhou!")
    if (enforcou):
        print("Você perdeu! A palavra era{}".format(palavra))

def verifica_acerto(chute, palavra, resultado):
    index = 0
    for letra in palavra:
        if (chute == letra):
            resultado[index] = letra
        index += 1
    return resultado

def verifica_erro(erros):
    erros += 1
    print("Você errou. Jogadas restantes:{}".format(6 - erros))
    return erros

def resolve_jogo(palavra):
    enforcou = acertou = False
    erros = 0
    resultado = preenche_resultado(palavra)
    imprime_palavra(resultado)
    while (not enforcou and not acertou):
        chute = retorna_chute()
        if (chute in palavra):
            resultado = verifica_acerto(chute, palavra, resultado)
        else:
            erros = verifica_erro(erros)
        acertou = "_" not in resultado
        enforcou = erros == 6
        imprime_palavra(resultado)
    imprime_resultado(acertou, enforcou, palavra)

if(__name__ == "__main__"):
    jogar()