import random

def jogar():
	print("*************************")
	print("Jogo de Adivinhação")
	print("*************************")

	numero_secreto = round(random.randrange(0, 101))
	tentativas = 0
	pontos = 1000

	print("Escolha um nivel:")
	print("(1)Facil (2)Médio (3)Difícil")

	nivel = int(input("Difina o nivel: "))

	if(nivel == 1):
		tentativas = 20
	elif(nivel == 2):
		tentativas = 10
	else:
		tentativas = 5

	for rodada in range(1,tentativas + 1):
		print("Tentiva: {} de {}".format(rodada, tentativas))

		chute_str = input("Digite um numero entre 1 e 100: ")
		chute = int(chute_str)
		print("Você digitou", chute)

		if(chute < 1 or chute > 100):
			print("Você deve digitar entre 1 e 100!")
			continue

		acertou = numero_secreto == chute
		maior = chute > numero_secreto
		menor = chute < numero_secreto

		if(acertou):
			print("Você Acertou! E fez {} pontos".format(pontos))
			break
		else:
			if(maior):
				print("Você errou! o chute foi maior que o numero secreto")
			elif(menor):
				print("Você errou! o chute foi menor que o numero secreto")
				pontos_perdidos = abs(numero_secreto - chute)
			pontos = pontos - pontos_perdidos

	print("Fim de jogo")
if(__name__=="__main__"):
    jogar()