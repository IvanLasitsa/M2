'''
Напишіть програму, яка отримує два числа і віднімає менше від більшого. 
Якщо числа рівні, неважливо, як віднімати, результат має дорівнювати нулю. 
В інших випадках результат повинен бути більше нуля.
'''
a = int(input("Введіть число "))
b = int(input("Введіть число "))
if a > b:
    a = a - b
    print(a)
else:
    b > a 
    b = b - a
    print(b)
