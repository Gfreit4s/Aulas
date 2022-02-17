nome = input('Digite seu nome:')

qtd_caractere = len (nome)

if qtd_caractere < 4:
    print(f'Seu nome e curto {nome}')
    print(f'Quantidade de carectere {len(nome)}')
elif qtd_caractere <= 6:
    print(f'Seu nome e normal {nome}')
    print(f'Quantidade de carectere {len(nome)}')
else:
    print(f'Seu nome e muito grande {nome}')
    print(f'Quantidade de carectere {len(nome)}')