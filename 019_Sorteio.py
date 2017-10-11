from random import choice
n1 = str(input('Digite seu nome:'))
n2 = str(input('Digite outro nome:'))
n3 = str(input('Digite outro nome:'))
n4 = str(input('Digite outro nome:'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('Aluno escolhido:{}'.format(escolhido))
