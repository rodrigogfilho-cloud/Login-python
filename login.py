#Informações do usuário
usuario_correto = 'Rodrigo'
senha_correta = 'Rodrigo@10'

#Input´s para o usuário 
usuario_digitado = input('Usuário: ')
senha_digitada = input('Senha: ')

if usuario_digitado == usuario_correto and senha_digitada == senha_correta:
    print('Você realmente é o dono dessa conta. Bem-vindo')
else:
    print('Seu malandro, você não irá conseguir entrar.')