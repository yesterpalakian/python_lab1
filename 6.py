numbers = (5, 8, -3, 2, -7, 10, -1)

index = None

for i in range(len(numbers)):
    if numbers[i] < 0:
        index = i
        break

if index is not None:
    print(f"Индекс первого отрицательного элемента: {index}")
else:
    print("Отрицательных элементов нет в кортеже.")
