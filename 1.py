import random as rnd

x = int(input("Введіть кількість чисел: "))
listOfNumb = []
for i in range(x):
    listOfNumb.append(rnd.randint(1, 100))
print(listOfNumb)

ind = 3

while ind <= len(listOfNumb):
    listOfNumb[ind] = 6
    ind += 4

print(listOfNumb)
