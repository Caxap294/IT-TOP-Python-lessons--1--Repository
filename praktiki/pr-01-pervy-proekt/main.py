##if

temperature = 28

if temperature > 25:
    print("Сегодня жарко ")

print("Проверка завершена ")


##двоеточие и отступ

if balance >= price:
    balance -= price
    print("Покупка оплачена")

print("Текущий баланс:", balance)

##else

age = 17

if age >= 18:
    print("Доступ разрешён")
else:
    print("Доступ закрыт")

##elif

grade = 85

if grade >= 90:
    print("Отлично")
elif grade >= 80:
    print("Хорошо")
elif grade >= 70:
    print("Удовлетворительно")
else:
    print("Нужно повторить тему")



##Порядок проверок

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"


number = 10

if number > 0:
    print("Положительное число")

if number > 5:
    print("Число больше пяти")