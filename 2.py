# С клавиатуры вводится текст, определить, сколько в нём гласных, а сколько согласных.
# В случае равенства вывести на экран все гласные буквы. Посчитать количество слов в тексте.

text = input("Введите текст: ")
text = text.lower()

vowels = "аеёиоуыэюя"
consonants = "бвгджзклмнпрстфхцчшщ"

vowel = 0
consonant = 0

vowel_list = []

word = 0

for char in text:
    if char in vowels:
        vowel += 1
        vowel_list.append(char)
    elif char in consonants:
        consonant += 1

words = text.split()
word = len(words)

print(f"Количество гласных букв: {vowel}")
print(f"Количество согласных букв: {consonant}")

if vowel == consonant:
    print("Гласные буквы в тексте:")
    print(" ".join(vowel_list))

print(f"Количество слов в тексте: {word}")