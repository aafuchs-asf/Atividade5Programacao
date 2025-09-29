y = True

while y:

    num = int(input('Digite um número inteiro: '))

    if num % 2 == 0:
        print(f'O numero {num} é par!')
        y = False

    else:
        x = input(f'O número {num} é ímpar! Deseja tentar novamente?(S/N)').upper()
        if x == 'N':
            y = False
            