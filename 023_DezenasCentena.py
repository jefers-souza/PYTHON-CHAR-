n = str(input('Digite um numero:'))
print('Milhar:{}'.format(n[0]))
print('Centenas:{}'.format(n[1]))
print('Dezena:{}'.format(n[2]))
print('Unidade:{}'.format(n[3]))
n1 = int(input('Digite um numero'))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 & 10
m = n1 // 1000 & 10
print("Unidade:{}".format(u))
print("Dezena:{}".format(d))
print("Centena:{}".format(c))
print("Milhar:{}".format(m))
