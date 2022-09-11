""" 5. Реализуйте алгоритм перемешивания списка. """

from random import randint
n = int(input('Введите число N - '))
numbers = []
for i in range(n):
    numbers.append(randint(-n, n+1))
print(numbers)

for i in range(n):
    a = randint(0, n)
    b = numbers[i]
    numbers[i] = numbers[a]
    numbers[a] = b
print(numbers)
