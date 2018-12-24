print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1
while(rodada <= total_tentativas):
    print("Rodada {} de {}".format(rodada, total_tentativas))
    chute_usuario = int(input("Digite o seu número: "))
    print("Você digitou: ", chute_usuario)

    acertou = chute_usuario == numero_secreto
    maior   = chute_usuario > numero_secreto
    if (acertou):
        print("Você acertou o número!")
        rodada = total_tentativas
    elif (maior):
        print("Você chutou um número maior")
    else:
        print("Você chutou um número menor")
    
    rodada = rodada + 1

print("Fim do jogo")