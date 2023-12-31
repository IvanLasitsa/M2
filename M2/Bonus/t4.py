'''
Тривалість місяця варіюється від 28 до 31 дня. 
У цій вправі ви створите програму, 
яка читає назву місяця від користувача у вигляді рядка. 
Тоді ваша програма повинна відображати кількість днів у цьому місяці.
Відобразіть «28 або 29 днів» для лютого, щоб зверталися до високосних років.

'''

назва_місяця = input("Введіть назву місяця: ")

if назва_місяця.lower() in ["січень", "березень", "травень", "липень", "серпень", "жовтень", "грудень"]:
    кількість_днів = 31
elif назва_місяця.lower() in ["квітень", "червень", "вересень", "листопад"]:
    кількість_днів = 30
elif назва_місяця.lower() == "лютий":
    рік = int(input("Введіть рік: "))
    if (рік % 4 == 0 and рік % 100 != 0) or рік % 400 == 0:
        кількість_днів = "28 або 29 (високосний рік)"
    else:
        кількість_днів = 28
else:
    кількість_днів = "Невідомий місяць"

print(f"У місяці {назва_місяця} {кількість_днів} днів.")
