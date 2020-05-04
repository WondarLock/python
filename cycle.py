names = []
salarys = []

amount = 0
amount_of_members = input("Введите количество членов семьи: ")
aom = int(amount_of_members)

for i in range(aom):
    names.append(input('Имя ' + str(i + 1) + ' человека:'))

for i in range(aom):
    salarys.append(input('Доход ' + str(i + 1) + ' человека'))

rent = input("введите сумму аренды ")
comunalka = input("введите сумму жкх ")
pay_per_month = (int(rent) + int(comunalka))

print("Платеж за месяц", pay_per_month)

for salary in salarys:
    amount += int(salary)

mean = (amount - pay_per_month)/aom
# mean = mean - pay_per_month
mean = str(mean)
for name in names:
    print(name.title() + " может потратить " + mean)

