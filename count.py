import random as rnd

arr = input("Введіть елементи: ").split(' ')
elem = input('Шуканий елемент: ')


amount = 0

for el in arr:
    if el == elem:
        amount += 1

print(elem, " зустрічається ", amount, ' разів')
