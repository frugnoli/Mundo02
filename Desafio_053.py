# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite sua frase: ')).strip().upper()
segunda_opcao = frase
frase = frase.replace(' ','')
string = frase[::-1]
print('O inverso de {} é {}'.format(frase, string))
if frase == string:
    print('Temos um Palíndromo')
else:
    print('Não é um palíndromo')

# Não usei o for, porque achei mais fácil desse jeito.
