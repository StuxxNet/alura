import adivinhacao
import forca

print("*********************************")
print("Escolha o seu jogo!")
print("*********************************")
print("1 - Adivinhação\n2 - Forca\n3 - Sair")
jogo = int(input("Digite a opção: "))

if (jogo == 1):
    adivinhacao.jogar()
elif (jogo == 2):
    forca.jogar()
else:
    exit()