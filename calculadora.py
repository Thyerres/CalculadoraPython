# Calculadora em Python Thyerres
import time

print("CALCULADORA EM PYTHON BY THYERRES!\n"
      "Menu de opções:\n"
      "1 - Soma\n"
      "2 - Subtração\n"
      "3 - Multiplicação\n"
      "4 - Divisão\n"
      "0 - Sair")
print("+=" * 55)
opc = int(input("Digite a sua escolha (Digite ZERO para sair do programa): "))

if opc < 0 or opc > 4:
    while opc < 0 or opc > 4:
        opc = int(input("Opção insválida!\n"
                        "Digite novamente uma opção do menu: "))

while 0 <= opc <= 4:
    if opc == 0:
        break
    elif opc == 1:
        num1 = int(input('Digite o primeiro número da soma: '))
        num2 = int(input('Digite o segundo número da soma: '))
        soma = num1 + num2
        print(f'{num1} + {num2} = {soma}')
    elif opc == 2:
        num1 = int(input('Digite o primeiro número da subtração: '))
        num2 = int(input('Digite o segundo número da subtração: '))
        sub = num1 - num2
        print(f'{num1} - {num2} = {sub}')
    elif opc == 3:
        num1 = int(input('Digite o primeiro número da multiplicação: '))
        num2 = int(input('Digite o segundo número da multiplicação: '))
        mult = num1 * num2
        print(f'{num1} x {num2} = {mult}')
    elif opc == 4:
        num1 = int(input('Digite o primeiro número da divisão: '))
        num2 = int(input('Digite o segundo número da divisão: '))
        div = num1 / num2
        print(f'{num1} / {num2} = {div:_.2f}')

    opc = int(input('Digite uma nova opção, ou ZERO para sair: '))

    if opc < 0 or opc > 4:
        while opc < 0 or opc > 4:
            opc = int(input("Opção inválida!\n"
                            "Digite novamente uma opção do menu: "))

print('Saindo......')
time.sleep(1)
print("+=" * 55)
print('Obrigado por usar a minha calculadora!')
