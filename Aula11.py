# And e not in

usuario = input('Nome de usuario:')
senha = input('Senha de usuario:')

usuario_bd = 'luiz'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você esta logado !')
else:
    print('Digite a senha novamente:')