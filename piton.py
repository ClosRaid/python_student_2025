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

# for i in range(0, 10,): условие цикла
#        print ("hi", i)    #выполнение внутреннего кода
#while (условие)
# while True:
#        print("*")
# value_user = int(input("введите число для суммирования"))
# sum_user = 0
# while value_user != 0:
#        value_user = int(input("введите число для суммирования"))
#        sum_user = sum_user + value_user
# print("Сумма чисел пользователя:", sum_user)
# for i in range(0, 6):
#        print('*' * i)
# for i in range(0, 6):
#        for j in range(0, i+1):
#               print("*", end = ' ')
#        print()
#пользователь вводит строку
#Необходимо проверить её на палиндром
# user_str = input("введите строку для проверки на палнидром")
# counter_letter = len(user_str) #функция подсчёта количества элементов
# value_user = True #переменная для проверки палиндрома
# for letter_begin in range (0, counter_letter):
#        for letter_end in (counter_letter, 0, 3):
#               print("проверяется буква:",user_str[letter_begin])
#               print("проверяется буква:",user_str[letter_end])
#               if letter_begin != letter_end:
#                      value_user = False
#                      break
#        if value_user == False:
#               print("не является палиндромом")
#               break
# #строки
# string = "Hello World"
# print(string[0])
# print(len(string))
# print(string*10)
# print(string+"!!!")
# #срез - это подстрока или подмассив
# #извлеченный из основного
# #может состоять из 1-n символов
# #или элементов
# #1 взятие одного символа
# #2. срез с двумя параметрами
# print(string[0:6])
# #[a:b] - интервал символов
# #find and rfind
# #нужны для поиска подстрок в строке
# print(string.find("l")) #Вернёт индекс элемента,
# #если элемента нет, то -1
# print(string.rfind("l"))
# #find - ищет слева направо
# #rfind - ищет справа налево
# #Метод REPLACE - ЗАМЕНА одной строки на другую
# #print(string.replace(_old: 'l',_new: 'l', _count=3))
# #метод Count - считает кол-во вхождений символа в строку
# print(string.count('l')) #3
#список(массив) - последовательность элементов
# #пронумерованных от 0, как символы в строке
# Primes = [2,3,5,7,11,13]
# print(Primes)
# print(Primes[3]) #7
# print(type(Primes)) #list
# rainbow = ['red', 'orange', 'Yellow', 'Green', 'blue']
# print(f'кол-во цветов в радуге: {len(rainbow)}')
# for i in rainbow:
#     print(i, end = ' ')
# print()
#добавления и удаление элементов списка
# my_list = [] #пустой список
# count_list = int(input("Введите кол-во элементов"))
# for i in range(count_list):
#     print(f"введите элемент  {i} ") #счётчик для пользователя
#     new_element = int(input("->: ")) #временная переменная
#     my_list.append(new_element) #добавление нового
# print(my_list)
# print(my_list.pop()) #удаление последнего элемента
#медоты split and join
#1 2 3
# user_str = input() #user_str == '1 2 3'
# user_list = user_str.split() #user_list == ['1', '2', '3']
# print(string.split('l')) #Heo word!
# for i in range(len(user_list)):
#     user_list[i] = int(user_list[i]) #преобразование типа
# print(''.join(rainbow)) #объединение строк
# #генератор списков
# n = 5
#1 способ
# list_gen1 = []
# for i in range(n):
#     list_gen1.append(i*n)
#     print(f'первый способ: {list_gen1}')
# #2 способ
# list_gen2 = [i*n for i in range(0, n)]
# print(f'Второй способ: {list_gen2}')
'''
задание 1
напишите программу, вычисляющую произведение элементов
списка целых. список передаётся в качестве параметра
полученный результат возвращается на экран.
'''
# from random import randint
# list1 = []*10
# for i in range(len(list1)):
#     list1[i] = randint(1,10)
# print(f"Вывод списка: {list1}")
'''
Задание 2
Напишите программу для нахождения минимума,
не используя спец. функции, в списке целых,
список передаётся в качестве параметра.
полученный результат возвращается на экран.
аналогично найти максимум.
аналогично найти сумму.
аналогично найти произведение всех целых
'''
# num = [randint(1,100)]*10
# for i in range(len(num)):
#     if num =
#     print("Минимум", [i])


#Задание за 18.09
#Задание 1
# num1 = int(input("Введите начало диапазона"))
# num2 = int(input("Введите конец диапазона"))
# for i in range(num1, num2):
#     if i % 7 ==0:
#         print(i)
#задание 2
# num1 = int(input("Введите начало диапазона"))
# num2 = int(input("Введите конец диапазона"))
# sum_number = 0
# number_7 = []
# for i in range(num1, num2+1):
#     print(str(i), end = " " )
#     if i % 5 == 0:
#         sum_number += 1
#     elif i % 7 == 0:
#         number_7.append(i)
#
# print("Числа кратные 7", number_7)
# print("кол-во чисел кратных 5:", sum_number)
# print()
#задание 3
# num1 = int(input("Введите начало диапазона"))
# num2 = int(input("Введите конец диапазона"))
# for i in range(num1, num2):
#     if i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 and i % 5 == 0:
#         print("Fizz Buzz")
#     else:
#         print(i)