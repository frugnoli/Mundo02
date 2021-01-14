# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

print("{:=^40}".format(" LOJAS GUANABARA "))
valor = float(input("Preços das compras: R$ "))
print("""
FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão sem juros
[ 4 ] 3x ou mais no cartão com juros""")
pag = str(input("Qual opção: "))
if pag in ["1","2","3","4"]:
    if pag == "1":
        total = valor - (valor * 10/100)
        print("Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.".format(valor, total))
    elif pag == "2":
        total = valor - (valor * 5/100)
        print("Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.".format(valor, total))
    elif pag == "3":
        total = valor
        parcela = total / 2
        print("Sua compra será parcelada em 2x de R$ {:.2f} sem juros.".format(parcela))
        print("Sua compra vai custar R$ {:.2f} no final.".format(total))
    elif pag == "4":
        total = valor + (valor * 20/100)
        total_parcela = int(input("Quantas parcelas: "))
        if total_parcela > 2:
            parcela = total / total_parcela
            print("Sua compra será parcelada em {}x de R$ {:.2f} com juros.".format(total_parcela, parcela))
            print("Sua compra vai custar R$ {:.2f} no final.".format(total))
        else:
            print("Pagamento em 1 ou 2 vezes é na opção [ 3 ]")
else:
    print("Opção Inválida!!!")