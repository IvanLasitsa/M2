'''
Введіть рядок s і число повторень рядків n. 
Виведіть рядок n раз за допомогою циклу.
'''

s = input("Введіть рядок s: ")
n = int(input("Введіть кількість повторень n: "))

for _ in range(n):
    print(s)
