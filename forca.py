import random

def jogar():

	imprime_mensagem_abertura()

	palavra_secreta = carrega_palavra_secreta()

	letras_acertadas = ["_" for letra in palavra_secreta]
	print(f"\n{letras_acertadas}\n")

	enforcou = False
	acertou = False
	erros = 0

	while(not enforcou and not acertou):

		chute = pede_chute()
		if(chute in palavra_secreta):
			marcando_letras(chute, palavra_secreta, letras_acertadas)
		else:
			erros += 1
			chances_restantes(erros)
	
		## verifica a quanidade de erros restantes
		enforcou = erros == 7
		acertou = "_" not in letras_acertadas
		print(f"\n{letras_acertadas}\n")
		desenha_forca(erros)

	## imprime voce ganhou ou perdeu
	if(acertou):
		print("Você ganhou!!")
	else:
		print("Você perdeu!!\n")
		print(f'A palavra secreta era {palavra_secreta}')
		
	print("\nFim de jogo")


def imprime_mensagem_abertura():
	print("*************************")
	print("Jogo de Forca")
	print("*************************")


def carrega_palavra_secreta():

	palavras = []

	with open("palavras.txt", "r") as arquivo:
		for linha in arquivo:
			linha = linha.strip()
			palavras.append(linha)

	numero = random.randrange(0, len(palavras))
	palavra_secreta = palavras[numero].upper()
	return palavra_secreta


def pede_chute():
	chute = input("Qual letra?: ")
	chute = chute.strip().upper()
	return chute


def marcando_letras(chute, palavra_secreta, letras_acertadas):
		i = 0
		for letra in palavra_secreta:
			if(chute == letra):
				letras_acertadas[i] = letra
			i = i+1


def chances_restantes(erros):
	print("Ops, você errou! Faltam {} tentativas.".format(6-erros))


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
	

if(__name__=="__main__"):
	jogar()