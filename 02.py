def validacao_tabuada(pergunta):
    while True:
        try:
            n = int(input(pergunta).strip())
            if 1 <= n <= 10:
                return n
            else:
                print('Numero invalido, digite um numero de 1 a 10.')
        except ValueError:
                print('valor invalido, digite apenas numeros de 1 a 10.')

nome = input('Ola, qual o seu nome? ')

resultado = validacao_tabuada(f'{nome}, digite um numero e te mostrarei a tabuada dele: ')
print(f'A tabuada de {resultado} é: ')

for i in range(1, 11):
    print(f'{resultado} x {i} = {resultado * i}')


