import random as rnd

x = int(input("Введіть кількість чисел: "))
number = int(input('Шукане число: '))
listOfNumb = []
for i in range(x):
    listOfNumb.append(rnd.randint(1, 100))
print(listOfNumb)

amount = 0

for el in listOfNumb:
    if el == number:
        amount += 1

print(number, " зустрічається ", amount, ' разів')
