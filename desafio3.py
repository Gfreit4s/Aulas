hora = input('Digite a hora:')

hora = int(hora)


if hora <= 11:
    print('Bom dia Usuario !')
elif hora <= 17:
    print('Boa tarde Usuario !')
else:
    print('Boa noite usuario !')