from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo:'))
seno = sin(radians(angulo))
print('O angulo de {} tem o seno de {:.2f}'.format(angulo, seno))
cos = cos(radians(angulo))
print('O angulo de {} tem o coseno de {:.2f}'.format(angulo, cos))
tam = tan(radians(angulo))
print('O angulo de {} tem a tagente de {:.2f}'.format(angulo, tam))

