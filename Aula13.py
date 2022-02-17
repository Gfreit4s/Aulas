n1 = input('Numero 1:')
n2 = input('Numero 2:')


# isdigit verifica se o numero pode ser convertido
if n1.isdigit() and n2.isdigit():
    n1 = int(n1)
    n2 = int(n2)

    print(n1 + n2)
else:
    print('Não pode converter')