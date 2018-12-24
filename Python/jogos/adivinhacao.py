import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = int(random.randrange(1,101))
total_tentativas = 3

for rodada in range(1, total_tentativas + 1):
    print("Rodada {} de {}".format(rodada, total_tentativas))
    chute_usuario = int(input("Digite um número entre 1 e 100: "))
    if (chute_usuario < 1 or chute_usuario > 100):
        print("O chute não deve ser menor do que 1 nem maior do que 100")
        continue
    print("Você digitou: ", chute_usuario)
    acertou = chute_usuario == numero_secreto
    maior   = chute_usuario > numero_secreto
    if (acertou):
        print("Você acertou o número!")
        break
    elif (maior):
        print("Você chutou um número maior")
    else:
        print("Você chutou um número menor")

if (not acertou):
    print("O número gerado foi {}".format(numero_secreto))

print("Fim do jogo")