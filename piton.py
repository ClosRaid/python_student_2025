# date = (input("дата рождения"))
# age = input("возраст")
# name = input("имя")
# s_name = input("фамилия")
# print(f"данные: возраст {age} \n"
#       f"данные: имя {name} \n"
#       f"даннык: фамилия {s_name} \n"
#       f"данные: дата {date}")
# \n перенос строки
# \t это 3 пробела (табуляция)
# ctrl + русская точка, комментарий выделенного текста
#from idlelib.debugger_r import restart_subprocess_debugger
#from traceback import print_tb
# print("сегодня жарко", "прям очень", sep = ")", end = '!!')
# print('Да')
# sep команда для разделения аргументов, end команда окончания строки
# ** - возведение в степень
# // - целочисленное деление
# % деление с остатком
# sum() - сумма переданых элементов
# min() - минимальный элемент
# max() - максимальный элемент
# как не делить:
# 1, деление на ноль
# 2. деление целого числа на ноль
# 3. нахождение остатка от деления на ноль
# PEP-8 руководство по коду на python
# value_a = 3
# value_b = 1
# result = (value_a**2 + value_b**2)**0.5
# print(result)



# Задание 1 / Домашнее задание за 05.09
# a = int(input())
# b = int(input())
# c = int(input())
# print (a + b + c)
# print (a * b * c)
# Задание 2
# value = int(input(""))
# num2 = int(input("Месячный платёж по кредиту"))
# num3 = int(input("Задолженность по комуналке"))
# print (value - num2 - num3)
#Задание 3
# first = int(input(""))
# second = int(input(""))
# print(first * second)
# задание 4
# print ("to be \n"
#        "    or not \n"
#        "        to be")
# print ("you're busy  making other plans")
# print("")
# print("\t"*10,"John Lennon")

#Задание 5
# print ("you're busy  making other plans \n",
#        "\n", 
#               "\t"*3,"John Lennon")
#08.09
# age = int(input("возраст"))
# if age < 10 and age > 0: # если выполняется условие
#        print("Ты ещё карапуз")
# elif 10 < age < 20:
#        print("Ты смешарик")
# elif 20 < age < 40:
#        print("Ты взрослый смешарик")
#
#
# else: # иначе
#        print("некорректное значение")
# #кейсовый блок условий
# value_user = int(input("введите ваше меню"))
# #match для работы кейса
# match value_user:
#        case 1:
#               print ("вызвано меню: главное")
#               break
#        case 2:
#               print("вызвано меню: редактировать")
#               break
#        case 3:
#               print("вызвано меню: Вид")
#               break
#        default:
#        print("error")
#задание 1 / Домашнее задание за 08.09
# a = int(input("Введите число "))
# b = int(input("Введите "))
# c = int(input("Enter another number: "))
# d = int(input("вывести сумму трёх чисел или произведение трёх? 1 or 2"))
# if d == 1:
#        print(a+b+c)
# if d == 2:
#        print (a*b*c)
#задание 2
# a = int(input("Введите число "))
# b = int(input("Введите "))
# c = int(input("Enter another number: "))
# d = int(input("вывести сумму максимум трёх чисел? минимум из трёх? или среднее арифметическое этих чисел? 1 or 2 or 3"))
# if d == 1:
#        print(a+b+c)
# if d == 2:
#        print (a*b*c)
# if d == 3:
#print ((a*b*c) // 3)
#Задание 3
# metr = int(input("Введите количество метров"))
# choice = int(input("Перевести метры в мили? дюймы? или ярды?"))
# if choice == 1:
#        print (metr * 0.000621, "милей")
# if choice == 2:
#        print (metr * 39,37, "дюймов")
# if choice == 3:
#        print (metr * 1.09, "ярдов")




#Задание за 09.09 / Задание 1
# num1 = int(input("Введите день недели"))
# if num1 == 1:
#     print("понедельник")
# elif num1 == 2:
#     print("вторник")
# elif num1 == 3:
#     print("среда")
# elif num1 == 4:
#     print("четверг")
# elif num1 == 5:
#     print("пятница")
# elif num1 == 6:
#     print("суббота")
# elif num1 == 7:
#     print("воскресенье")
# else:
#     print("неккоректное значение")

#Задание 2
# month = int(input("Введите месяц 1-12 "))
# match month:
#               case 1:
#                      print("Январь")
#               case 2:
#                      print("Февраль")
#               case 3:
#                      print("Март")
#               case 4:
#                      print("Апрель")
#               case 5:
#                      print("Май")
#               case 6:
#                      print("Июнь")
#               case 7:
#                      print("Июль")
#               case 8:
#                      print("Август")
#               case 9:
#                      print("Сентябрь")
#               case 10:
#                      print("Октябрь")
#               case 11:
#                      print("Ноябрь")
#               case 12:
#                      print("декабрь")
#               case _:
#                      print("неккоректное значение")

#задание 3
# num = int(input("Введите число"))
# if num > 0:
#     print("number is positive")
# elif num == 0:
#     print("number is zero")
# else:
#     print("number is negative")

#задание 4
# num = int(input("Введите число"))
# num2 = int(input("Введите второе число"))
# if num == num2:
#     print("числа равны")
# elif num > num2:
#     print(num2,num)
# elif num < num2:
#     print(num,num2)

metr = int(input("Введите количество метров"))
choice = int(input("Перевести метры в мили? дюймы? или ярды?"))
if choice == 1:
       print (metr * 0.000621, "милей")
if choice == 2:
       print (metr * 39,37, "дюймов")
if choice == 3:
       print (metr * 1.09, "ярдов")