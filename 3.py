nums = [int(x) for x in input("Введите список чисел через пробел: ").split()]

pair = 0

number = {}

for num in nums:
    if num in number:
        pair += number[num]
        number[num] += 1
    else:
        number[num] = 1

print(f"Количество пар элементов, равных друг другу: {pair}")
