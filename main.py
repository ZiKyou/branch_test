first_num = int(input("Введите перове число: "))
znak = input("Выберите действие + / - / * / /  : ")
second_num = int(input("Введите второе число: "))

if znak == "+":
    print("Ваш ответ: ", first_num + second_num)

elif znak == "-":
    print("Ваш ответ: ", first_num - second_num)

elif znak == "*":
    print("Ваш ответ: ", first_num * second_num)

elif znak == "/":
    print("Ваш ответ: ", first_num / second_num)

else:
    print("error")