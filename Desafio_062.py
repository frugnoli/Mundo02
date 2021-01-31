# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print("=" * 30)
print("GERADOR DE PA")
print("=" * 30)
primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print("{} -> ".format(termo), end = '')
        termo += razao
        contador += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar mais? Digite 0 para sair: "))
print("Progressão finalizada com {} termos mostrados.".format(total))
print("=" * 30)