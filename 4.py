string = input("Введите строку с числами: ")

number = {}

for char in string:
    if char.isdigit():
        num = int(char)
        if num in number:
            number[num] += 1
        else:
            number[num] = 1

print("Словарь чисел и их количества:")
for key, value in number.items():
    print(f"{key}: {value}")
