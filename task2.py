# семинар 2 зад 1
n = input('Введите вещественное число: ')
sum = sum(map(int, n.replace('.', '')))
print (sum)