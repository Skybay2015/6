import random as rnd


x = int(input("Введіть кількість чисел: "))
listOfNumb = []
for i in range(x):
    listOfNumb.append(rnd.randint(1, 100))
print(listOfNumb)


amount = 0

avarageSum = 0

for el in listOfNumb:
    avarageSum += el

avarageSum = avarageSum / len(listOfNumb)


for el in listOfNumb:
    if el < avarageSum:
        amount += 1

print("К-сть елементів масиву: ", amount)
