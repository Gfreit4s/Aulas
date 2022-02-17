n1 = input('Digite um numero inteiro:')


try:
    n1.isdigit()
    n1 = int(n1)
    print(n1)
except:
    print(f'Não pode converter {n1} para inteiro')

if (n1 % 2) == 0:
    print(f'Seu numero é par:{n1}')
elif n1 % 2 == 1:
    print(f'Seu numero é Impar:{n1}')
else:
    print(f'Seu numero nao e par:{n1}')
