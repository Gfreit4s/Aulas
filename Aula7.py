nome ='Guilherme'
idade = 25
altura = 1.77
e_maior = idade > 18
peso = 90

imc = altura*altura/peso

print('Nome:',nome)
print('Idade:',idade)
print('Altura:',altura)
print('+18',e_maior)


print(nome, 'tem',idade,'anos', 'sua altura de ',altura, 'pesa',peso, 'seu IMC é',imc)

print(f'seu imc e{imc:.3f}')

print('{} tem seu imc {}'.format(nome,imc))

