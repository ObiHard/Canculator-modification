a = int(input("Введите первое число: "))
op = input("Введите оператор (+, -, *, /): ")
b = int(input("Введите второе число: "))

if op == '+':
    print("Результат:", a + b)
elif op == '-':
    print("Результат:", a - b)
elif op == '*':
    print("Результат:", a * b)
elif op == '/':
    if b != 0:
        print("Результат:", a / b)
    else:
        print("Деление на ноль невозможно!")
else:
    print("Неизвестный оператор!")

cont = input("Вам ещё нужен канкулятор? Вы будете продолжить? (Да/Нет): ").strip().lower()
if cont == 'да':
    exec(open(__file__).read())
else:
    print("Работа завершена")
