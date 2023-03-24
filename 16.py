
size = int(input("Введите кол-во элементов в массиве: "))
arr = list(range(1,size + 1))
print(arr)
num = int(input("Введите искомое число: "))
k = 0
i = 0
while i < len(arr):
    if num == arr[i]:
        k += 1
    i += 1
print(f"Искомое число встретилось {k} раз(а).")