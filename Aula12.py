usuario = input('Nome de usuario:')
qtd_caractere = len (usuario)

#len le a quantidade de caractere

if qtd_caractere < 6:
    print('digite acima de 6 caracteres')
else:
    print('Cadastrado')

print(usuario, qtd_caractere, type(qtd_caractere))