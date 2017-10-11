d = int(input('how many days the car was rented ? '))
k = float(input('How Km did you run ? '))
d = d * 60
k = k * 0.15
t = d + k
print('Total amount for rented days, and kilometers rolled: {}'.format(t))