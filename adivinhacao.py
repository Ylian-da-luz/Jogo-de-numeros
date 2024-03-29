import random


print("********************************")
print("Bem vindo ao jogo de adivinhação!")
print("********************************")

numero_secreto = random.randrange(0,101)
total_de_tentativas = 3
pontos = 1000

print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Defina o nível:"))

if(nivel == 1):
    total_de_tentativas = 15
elif(nivel == 2):
    total_de_tentativas = 8
else:
    total_de_tentativas = 5

for rodada in range (1, total_de_tentativas +1):
    print ("tentativa {} de {}" .format(rodada, total_de_tentativas))
    chute = input("Digite um número entre 1 e 100:")
    print("Você digitou", chute)
    chute = int (chute)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou= chute == numero_secreto
    maior  = chute  > numero_secreto
    menor  = chute  < numero_secreto


    if (acertou):
        print("Você acertou e fez {}!".format(pontos))
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim de jogo!")