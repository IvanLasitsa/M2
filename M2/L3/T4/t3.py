'''
Введіть два цілих числа a і b (при цьому a ≤ b). 
Виведіть в стовпчик всі числа від a до b включно.
'''

a = int(input("Введіть ціле число a: "))
b = int(input("Введіть ціле число b (a ≤ b): "))

if a <= b:
    for i in range(a, b + 1):
        print(i)
else:
    print("Помилка: a більше за b. Будь ласка, введіть a так, щоб a ≤ b.")
