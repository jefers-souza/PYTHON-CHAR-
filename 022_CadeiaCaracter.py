n = str(input('Digite seu nome completo:')).strip()                #Aqui retira os espaçosdo fim e do inicio.
print('MAIUSCULO: {} '.format(n.upper()))
print('minusculo: {}'.format(n.lower()))
print('Qt de letras: {}'.format(len(n)-n.count(' ')))              #Aqui conta as letra sem os espaços entre ela.
print('QT de letras do primeiro nome: {}'.format(n.find(' ')))     #find mostra a possição do primiro espaço que e depois do primeiro nome que mostar a qt de letras
separa = n.split()
print("QT de letras do primeiro nome {}".format(len(separa[0])))

