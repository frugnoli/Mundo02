# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
print("Sou seu computador... Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
palpite = int(input("Qual o seu palpite? "))
tentativa = 1
computador = randint(0, 10)
while palpite != computador:
    if palpite < computador:
        palpite = int(input("Mais... Tente outra vez: "))
        tentativa += 1
    else:
        palpite = int(input("Menos... Tente outra vez: "))
        tentativa += 1
print('Acertou com {} tentativas. Parabéns!'.format(tentativa))

