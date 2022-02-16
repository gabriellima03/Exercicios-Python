primeirotermo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeirotermo
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(termo)
        cont += 1
        termo += razão
    mais = int(input('Quantos termos você quer mostrar a mais? '))
