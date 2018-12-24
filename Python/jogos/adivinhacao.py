print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chute_usuario = int(input("Digite o seu número: "))

print("Você digitou: ", chute_usuario)

acertou = chute_usuario == numero_secreto
maior   = chute_usuario > numero_secreto

if (acertou):
    print("Você acertou o número!")
elif (maior):
    print("Você chutou um número maior")
else:
    print("Você chutou um número menor")
    
print("Fim do jogo")