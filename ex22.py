'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiusculas 
- O nome com todas as letras maiusculas
- Quantas letras ao todo sem considerar espaços
- Quantas letras tem o primeiro nome'''
nome=str(input('Digite seu nome completo: ')).strip()
print('Analizando seu nome...')
print('Seu nome em letra maiuscula é: {}'.format(nome.upper()))
print('Seu nome em letra minuscula é: {}'.format(nome.lower()))
print('Seu nome tem um total de {} caracteres'.format(len(nome)-nome.count(' ')))
#print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa=nome.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))
