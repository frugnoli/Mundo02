# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import date
nasc = int(input("Ano de Nascimento: "))
ano_atual = date.today().year
idade = ano_atual - nasc
print("O atleta tem {} anos.".format(idade))
if idade <= 9:
   print("Classificação: MIRIM")
elif idade <= 14 and idade > 9:
   print("Classificação: INFANTIL")
elif idade <= 19 and idade > 14:
   print("Classificação: JÚNIOR")
elif idade <= 25 and idade > 19:
   print("Classificação: SÊNIOR")
else:
   print("Classificação: MASTER")