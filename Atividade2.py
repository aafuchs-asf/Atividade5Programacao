num = input('Digite um número inteiro: ')

try:
    numInt = int(num)

    if num == 0:
        print('Atenção! O número não pode ser 0.')

    else:    
        div = 10/numInt
        print(f'O resultado de 10 dividido por {num} é: {div}')

except ValueError:
    print(f'{num} não é um número inteiro!')
