# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

print("""
IMC                 CLASSIFICAÇÃO   OBESIDADE (GRAU)
MENOR QUE 18,5      MAGREZA             0
ENTRE 18,5 E 24,9   NORMAL              0
ENTRE 25,0 E 29,9   SOBREPESO           I
ENTRE 30,0 E 39,9   OBESIDADE           II
MAIOR QUE 40,0      OBESIDADE GRAVE     III
""")
peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é a sua altura? (m) "))
imc = peso / (altura ** 2)
print("Seu IMC é de {:.2f}".format(imc))
if imc < 18.5:
    print("IMC com Classificação MAGREZA - GRAU 0")
elif imc <= 24.9:
    print("IMC com Classificação NORMAL - GRAU 0")
elif imc <= 29.9:
    print("IMC com Classificação SOBREPESO - GRAU I")
elif imc <= 39.9:
    print("IMC com Classificação OBESIDADE - GRAU II")
else:
    print("IMC com Classificação OBESIDADE GRAVE - GRAU III")