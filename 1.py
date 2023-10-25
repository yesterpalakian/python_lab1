# Вывести на экран все простые числа в заданном диапазоне (диапазон вводится с клавиатуры).

start = int(input("от "))
end = int(input("до "))

print(f"Простые числа от {start} до {end}:")

for num in range(start, end + 1):
    if num <= 1:
        continue

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            break
    else:
        print(num)