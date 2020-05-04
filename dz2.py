# cars = ['mazda', 'citroen', 'bmw']
# cars.append('jigul')
# cars.remove('jigul')
# cars.sort()
# cars.reverse()
# print(cars)
import random

luckyNumber = random.randint(1, 100)
print(luckyNumber)
difficulty = int(input('Выбери количество попыток: '))

attempts = 1
userNumber = int(input('И ваша цифра: '))

while attempts != difficulty:

    if luckyNumber == (userNumber):
        print('GGWP')
        break
    elif luckyNumber > int(userNumber):
        print('Бери больше')
    else:
        print('Бери меньше')
    userNumber =int(input('И ваша цифра: '))
    attempts += 1
if userNumber != luckyNumber:
    print('Ты проиграл, число было:', luckyNumber, '\nПопробуй еще')