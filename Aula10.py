nome = input('Qual é seu nome:')
idade = input('Qual sua idade:')

idade = int(idade)
limit = 18
if idade >= limit:
    print(f'{nome} valido para emprestimo')
else:
    print(f'{nome} não pode fazer emprestimo')
