'''
Напишіть програму, яка зчитує ціле число у користувача. 
Потім ваша програма повинна вивести повідомлення про те, 
парне чи непарне ціле число.

'''

введене_число = int(input("Введіть ціле число: "))

if введене_число % 2 == 0:
    print(f"{введене_число} є парним числом.")
else:
    print(f"{введене_число} є непарним числом.")
