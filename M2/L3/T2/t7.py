'''
Придумайте свій діалог з комп'ютером!

Обов'язково придумайте і використовуйте свою власну ідею!

Використовуйте вкладені умовні оператори.
Питання, які задає комп'ютер, повинні змінюватися в залежності 
від попередніх відповідей людини.
'''

print("Привіт! Як я можу допомогти тобі сьогодні?")

is_smart = input("Чи вважаєш ти, що я розумний? (Так/Ні): ").lower()

if is_smart == "так":
    print("Дякую за визнання! Я завжди тут, щоб тобі допомогти.")
else:
    print("Вибач, якщо ти так вважаєш. Я стараюся вдосконалюватися!")

interests = input("Що цікавить тебе найбільше? (Програмування/Мистецтво/Спорт): ").lower()

if interests == "програмування":
    print("Це чудовий вибір! Я можу допомогти з порадами чи прикладами коду.")
elif interests == "мистецтво":
    print("Фантастично! Як ти відносишся до живопису чи музики?")
elif interests == "спорт":
    print("Спорт - це завжди класно! Який вид спорту тобі подобається найбільше?")
else:
    print("Цікавий вибір! Розкажи трошки більше про це.")

print("Дякую за цей чудовий діалог! Якщо у тебе будуть ще питання, не соромся питати.")
