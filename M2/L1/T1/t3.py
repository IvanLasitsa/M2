'''
Програма повинна обчислювати зріст користувача в папугах. 
Чому не виходить? 
Згадайте, навіщо потрібні функції int () і str ().
'''

r = int(input ("Який у тебе зріст (сантиметрів)? "))
rost_p = 17
p = r / rost_p
answer = "Це" + str(p) + "папуг!"
print (answer)

