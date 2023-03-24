N = int(input('Введите длину массива: '))
i = 0
arr = list()
print('Введите числа массива:')
while i < N:
    arr.append(int(input()))
    i += 1
print('Вы ввели: ', arr)
num = int(input('Искомое число: '))
print('Ближайшее: ',min(arr, key=lambda a:abs(a-num)))
