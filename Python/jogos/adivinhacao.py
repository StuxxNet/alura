print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chute_usuario = int(input("Digite o seu número: "))

print("Você digitou: ", chute_usuario)

if (numero_secreto == chute_usuario):
    print("Você acertou o número!")
else:
    print("Você errou o número!")

print("Fim do jogo")