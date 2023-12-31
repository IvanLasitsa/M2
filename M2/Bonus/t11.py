'''
!LOOPS

Напишіть програму, яка відображає таблицю перетворення температури градусів 
Цельсія і градусів Фаренгейта. 
Таблиця повинна включати рядки для всіх температур від 0 до 100 градусів Цельсія, 
кратних 10 градусам Цельсія. Додайте відповідні заголовки до стовпців. 
Формулу перекладу між градусами Цельсія і градусами Фаренгейта можна знайти в 
інтернеті.


'''

print("Температура (°C)\tТемпература (°F)")

for температура_цельсія in range(0, 101, 10):
    температура_фаренгейт = (температура_цельсія * 9/5) + 32
    print(f"{температура_цельсія}°C\t\t\t{температура_фаренгейт}°F")
