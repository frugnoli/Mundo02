# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Valor da casa: R$ "))
salario = float(input("Salário do comprador: R$ "))
anos = int(input("Quantos anos de financiamento: "))
prestacao = valor_casa / (12 * anos)
print("Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}.".format(valor_casa, anos, prestacao))
if prestacao >= (salario * 0.30):
    print("Empréstimo NEGADO!")
else:
    print("Empréstimo CONCEDIDO!")

