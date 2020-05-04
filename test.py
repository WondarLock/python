import datetime
print("Привет я программа которая посчитает сколько тебе будет лет в таком то году")
age = int(input("Сколько тебе лет? \n"))
# сколько тебе будет лет в таком то году?
# Программа,  которая спрашивает сколько тебе лет, потом ты вбиваешь год. Программа отвечает сколько тебе лет.
# yearnow = datetime.datetime.now()
# print(yearnow)
newyear = int(input("Введи год в котором хочешь узнать свой возраст (в формате ГГГГ): \n"))
month = int(input("Введи номер месяца своего рождения (в формате (ММ): \n"))
todayYear = datetime.datetime.now().year
todayMonth = datetime.datetime.now().month

if age < 0:
   print("ты еще не родился")
elif age > 50:
   print("Слишком большая цифра")
if todayMonth > month:
   print(newyear - todayYear + age -1)
else:
   print(newyear - todayYear +age)