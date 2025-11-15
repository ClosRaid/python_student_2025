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

#задание 1
#напишите программу, вычисляющую произведение элементов
#списка целых. список передаётся в качестве параметра
#полученный результат возвращается на экран.

# from random import randint
# list1 = []*10
# for i in range(len(list1)):
#     list1[i] = randint(1,10)
# print(f"Вывод списка: {list1}")

# Задание 2
# Напишите программу для нахождения минимума,
# не используя спец. функции, в списке целых,
# список передаётся в качестве параметра.
# полученный результат возвращается на экран.
# аналогично найти максимум.
# аналогично найти сумму.
# аналогично найти произведение всех целых

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

# list = [10,2,9,3,11,7]
# for i in range(len(list)):
#     if list[i] > list[i + 1]:
#         list[i], list[i + 1]=list[i+1],list[i]
# print(list)
import random
# list_booble = []
# N = 10
# for i in range (N):
#     list_booble.append(random.randint(-10,10))
# print(f"Начальный список {list_booble}")
# for i in range(N):
#     for j in range(N - 1 - i):
#         if list_booble[j] > list_booble[j+1]:
#             list_booble[j], list_booble[j+1] = list_booble[j+1], list_booble[j]
#
# print(f"Финальный список {list_booble}")

#необходимо составить список состоящий из случайных чисел в диапазоне от -10 до 10
#где len = 20
#остортировать список следующим способом
#1) левая половина сортировка по убыванию
#2) правая половина сортировка по возрастанию
# list = []
# n = 20
# for i in range (n):
#     list.append(random.randint(-10, 20))
# print(list)
# for i in range(n//2):
#     for j in range(n//2, n-1):
#          if list[j] > list[j+1]:
#              list[j], list[j+1] = list[j+1], list[j]
#             print(f"От меньшего к большему {list}")
#         if list[j] < list[j + 1]:
#             list[j], list[j + 1] = list[j + 1], list[j]
#         print(f"От большего к меньшему {list}")

#Элементы в диапазоне -20 до 20, шде len 45
#отсортировать список следующим образом
#1\3 списка только чётные элементы списка
#2\3 только max и min, которые чередуются
#3\3 только чётные элементы списка
# вывести на экран начальый спислк и результат работы на экран
# list1 = []
# list2 = []
# list3 = []
# n = [0,15]
# r = [15,30]
# d = [30,45]
# for i in range (n):
#     list1.append(random.randint(-20, 20))
# print(f"Начальный список {list}")
# for i in range(n):
#         if list[i] % 2 == 0:
#кортежи tiple - это неизменяемая структура данных, которые по своекму подобию похожа на список.
# list = [1,2,3]
# list.append(2)
# list.pop()
# del list
# tupleB = (4,5,7)
# tupleA = (1, 2, 3)
# print(type(tupleA))
# print(tupleA)
# # tupleA[1] = 20 #type error
# #Удаление кортежей
# # del tupleB
# # print(tupleB)
# #преобразование типа
# list = [1,2,3,4,5]
# print(type(list), list)
# tupl = tuple(list)
# print(type(tupl), tupl)
# #словари - это неупорядоченная структура данных, позволяющая хранить пары "ключ - значение"
# doctionary = {"персона":"человек",
#               "марафон":"гонка бегунов около 26 миль",
#               "противостоять":"оставаться сильным, не смотря на сложости",
#                 "бежать":"двигатьсябыстро"}
# gender_dict = {0: "женский", 1:"мужской"}
# story_count = {"Сто":100, "Девяносто":90, "Десять":10, "Пять":5}
# # dict = {(1,2,3) :"Кортеж можеть быть ключём,",
# #                1: "Целые тоже могут быть ключём",
# #                 "бежать":"строка тоже",
# #                 ['носок',1,2]: "списки не могут",
# #                 1.0 : "Дробый тип не могут"}
# #изменяемые типы данных в качестве ключа выступать не могут(НЕХЕШИРУЮТСЯ)
# int(1) - float(1.0) - True
# #создание словаря
# d = {}
# d = {"dict_key":1, "dictionary":2}
# print(d)
# d = dict(     [(1,1),   (2,1)      ]   )
# d_str = dict( ("ab", "cd") )
# d = dict.fromkeys(['a','b'])
# print(d)
# key_list = ['marvel', 'dc']
# value_list = ['spiderman', 'flash']
# superhero_dict = dict(zip(key_list, value_list))
# print(superhero_dict)
# d = {a : a**2 for a in range(7)}
# print(d)
# #добавление пар
# d['туфля'] = 'обувь'
# #УДАЛЕНИЕ ПАР
# del d['туфля']
# superhero_dict.clear() #очистка словаря
# b = d.copy() #копирование словаря
# print(d.get(1))
# #d.update('ключ':'значение', 'ключНовый': 'значениеНовое')
# #d.values()
# #d.items()
# #d.keys()
# # for keys, value in story_count:
# #     print(key,value)
# for key in story_count.keys():
#     print(key)
# #множества - set
# sets = {0,1,2,3,4}
# fset = frozenset( {2,3,4})
# lists = [1,2,3,4]
# tuple = (7,8,9)
# new_set = sets.union(lists.tuples, fset)

# tupleB = (4,5,7)
# tupleA = (1, 2, 3)
# print(type(tupleA))
# print(tupleA)
# tupleA[1] = 20 #type error
#Удаление кортежей
# del tupleB
# print(tupleB)
#преобразование типа
# list = [1,2,3,4,5]
# print(type(list), list)
# tupl = tuple(list)
# print(type(tupl), tupl)
#словари - это неупорядоченная структура данных, позволяющая хранить пары "ключ - значение"
# doctionary = {"персона":"человек",
#               "марафон":"гонка бегунов около 26 миль",
#               "противостоять":"оставаться сильным, не смотря на сложости",
#                 "бежать":"двигатьсябыстро"}
# gender_dict = {0: "женский", 1:"мужской"}
# story_count = {"Сто":100, "Девяносто":90, "Десять":10, "Пять":5}
# # dict = {(1,2,3) :"Кортеж можеть быть ключём,",
# #                1: "Целые тоже могут быть ключём",
# #                 "бежать":"строка тоже",
# #                 ['носок',1,2]: "списки не могут",
# #                 1.0 : "Дробый тип не могут"}
# #изменяемые типы данных в качестве ключа выступать не могут(НЕХЕШИРУЮТСЯ)
# int(1) - float(1.0) - True
# #создание словаря
# d = {}
# d = {"dict_key":1, "dictionary":2}
# print(d)
# d = dict(     [(1,1),   (2,1)      ]   )
# d_str = dict( ("ab", "cd") )
# d = dict.fromkeys(['a','b'])
# print(d)
# key_list = ['marvel', 'dc']
# value_list = ['spiderman', 'flash']
# superhero_dict = dict(zip(key_list, value_list))
# print(superhero_dict)
# d = {a : a**2 for a in range(7)}
# print(d)
#добавление пар
# d['туфля'] = 'обувь'
# #УДАЛЕНИЕ ПАР
# del d['туфля']
# superhero_dict.clear() #очистка словаря
# b = d.copy() #копирование словаря
# print(d.get(1))
# #d.update('ключ':'значение', 'ключНовый': 'значениеНовое')
# #d.values()
# #d.items()
# #d.keys()
# # for keys, value in story_count:
# #     print(key,value)
# for key in story_count.keys():
#     print(key)
# #множества - set
# sets = {0,1,2,3,4}
# fset = frozenset( {2,3,4})
# lists = [1,2,3,4]
# tuple = (7,8,9)
# new_set = sets.union(lists.tuples, fset)

#set.intersection()
#set.difference()
#set.symmetric_difference()
#set.copy()
#set.intersection_update
#set.symmetric_difference_update
#set.add()
#set.remove()
#set.discard()
#set.pop()
#set.clear()


#есть стопка оладий различного радиуса, единственная операция с ними - между двумя оладиями просунуть лопатку и
#поменять порядок оладий над лопаткой на обратный
#необходимо за минимальное кол-во операций таких остортировать снизу вверх по убыванию радиуса
#1. Найти блин с большим радиусом
#2. Перевернуть стопку так, что бы блин с набиольшим радиусом оказался наверху
#3. перевернуть всю стопку, что бы набольший блин оказалася снизу
#4. повтрить сие действие до тех пор пока стопка не будет отсортирована
# pancakes = [3,1,4,5,9,6,4,3,6,2,4,7]
# pancakes2 = []
# n = len(pancakes)
# i = 0
# def sort_blin(pancakes):
#     def find_index_big(pancakes,n):
#         i = 0
#         for j in range(len(pancakes)):
#             if pancakes[j] > pancakes[i]:
#                 i = j
#     pancakes2 = pancakes[:i] [::-1] + pancakes[:1]
#     def flip(pancakes,k):
#         return pancakes[:k][::-1] + pancakes[:k]
#     result = []
#     while n > 1:
#         i = find_index_big(pancakes,n)
#         if i < n-1:
#             pancakes = flip(pancakes, i+1) #перевернуть стопку ещё раз
#             result.append(i+1) #лбавить кол-во шагов(операций)
#             pancakes = flip(pancakes,n) #перевернуть стопку
#             result.append(n) #добавить шаги в список
#         n -= 1 #уменьшаем итерации в стопке
#     return result
# pancakes = [3,1,4,5,9,6,4,3,6,2,4,7]
# oper = sort_blin()
# print(f"блины: {pancakes}")
# print(f"Операции:{oper}")
# pancakes.sort()
# print(pancakes)
# pancakes.sort(reverse=True)
# print(pancakes)


#30.10 задание до 2.11
# def formativ():
#     print("Don't compare your \n"
#           "with anyone in this world... \n"
#           "if you do so, you are insulting your self \n"
#           "\n",
#           "\t"* 3, "Bill Gates" )
# def value():
#     value1 = int(input("введите число"))
#     value2 = int(input("введите второе число"))
#     for i in range(value1,value2):
#         if i % 2 == 0:
#             print(f"{i},Чётные числа в радиусе от {value1} до {value2}")
#         else:
#             print(f"в радиусе от {value1} до {value2} чётных чисел не обнаружено")
# def square():
#         square_value = int(input("введите длину стороны квадрата "))
#         symbol = input("введите символ ")
#         znak = int(input("введите переменную логического типа 1: истина 2: ложь "))
#         if znak >= 3:
#             print("incorrect value")
#         for i in range(square_value):
#             print(symbol * i,symbol * i,sep = '', end = '')
#             print(symbol, "\t", symbol)
#             print(symbol * i,symbol * i,sep = '', end = '')
# square()
#30.10
# import re
# def isCyrillic(text):
#     return bool(re.search('[а-яА-Я]', text))
# def scrabl():
#     point_en = {1:'AEIOULNSTR',
#                     2:'DG',
#                     3:'BCMP',
#                     4:'FHVWY',
#                     5:'K',
#                     8:'JX',
#                     10:'QZ'}
#     point_ru = {1:'АВЕИНОСТ',
#                 2:'ДКЛМПУ',
#                 3:'БГЁЬЯ',
#                 4:'ЙЫ',
#                 5:'ЖЗЧЦЧ',
#                 8:'ШЭЮ',
#                 10:'ФЩЪ'}
#     while True:
#         text_user = input("Для отмены напишите 0. Игрок 1 Введите слово:").upper()
#         if text_user == "0":
#             print("Прощайте")
#             break
#         text_user2 = input("Для отмены напишите 0. Игрок 2 Введите слово:").upper()
#         if text_user2 == "0":
#             print("Прощайте")
#             break
#         player1 = 0
#         player2 = 0
#         if isCyrillic(text_user):
#                 print('Кол-во очков:',sum([key for i in text_user for key, value in point_ru.items() if i in value]))
#                 player1 = player1 + sum([key for i in text_user for key, value in point_ru.items() if i in value])
#                 player2 = player2 + sum([key for i in text_user2 for key, value in point_ru.items() if i in value])
#         else:
#                 print('Кол-во очков:',sum([key for i in text_user for key, value in point_en.items() if i in value]))
#                 player1 = player1 + sum([key for i in text_user for key, value in point_en.items() if i in value])
#                 player2 = player2 + sum([key for i in text_user2 for key, value in point_en.items() if i in value])
#         print(f"кол-во очков первого игрока {player1}, кол-во очков второго игрока {player2} ")
# def camping():
#     backpack = {'Зажигалка': 20, 'Компас': 100, 'Фрукты': 500, 'Рубашка': 300,
#                 'Термос': 1000, 'аптечка': 200, 'Куртка': 600, 'Бинокль': 400,
#                 'Удочка': 1300, 'Салфетки': 40, 'Бутерброды': 800, 'Палатка': 5500,
#                 'Спальный мешок': 2500, 'Изолента': 250, 'Котел': 3000
#                 }
#     human1_massa = int(input("Введите допустимый вес рюкзака первого человека: ")) * 1000
#     human2_massa = int(input("Введите допустимый вес рюкзака первого человека: ")) * 1000
#     print("Могу взять: ")
#     for key, value in backpack.items():
#         if value < human1_massa or value < human2_massa:
#             print(key, value, end=' ')
#             print()
#             print("Не Могу взять: ")
#     for key, value in backpack.items():
#         if value > human1_massa or value > human2_massa:
#             print(key, value, end=' ')
# def contact_list():
#     note_book = {"Маша":
#                      {'tel': '+7922123561', 'vk': 'vk.com/masha321', 'youtube': 'youtube.com/masha321', 'telegram'
#                      : 't.me/masha321'},
#                  "Даша":{'tel': '+79023321293', 'vk': 'vk.com/dashulya1910', 'telegram': '@Egoistik_manyak'},
#                  "Олег":{'tel': '+79522301092', 'vk': 'vk.com/CODStyle', 'youtube': 'youtube.com/CodeSky',
#                          'telegram':'@CODProf'}}
#     user_search = input(f"Введите имя из списка контактов:Маша,Даша,Олег ").capitalize()
#     for key, value in note_book[user_search].values():
#         print(value)
# def basnya():
#     with open("article.txt", 'w+') as question:
#         question.write("Вечерело \n"
#                    "Жужжали мухи \n"
#                    "Кипела вода в чайнике \n"
#                    "Венера зажглась на небе \n"
#                    "Деревья шумели \n"
#                    "Тучи разошлись \n"
#                    "Листва Зеленела \n")
#     with open ("article.txt", 'r') as file:
#         for i in file.readlines():
#             print(i, end='')
# #задание 2
# def rewrite():
#     with open("articleWords.txt", 'w+') as words:
#                 for j in readlines():
#                     if j >= readlines[8]:
#                         words.write(j)
#     with open("articleWords", 'r') as read:
#                 read.readlines()

'''
методы для работы с файлом
file.close()
file.fileno()
file.flush() - метод очистки буфера
file.isatty() - проверка на открытие файла в терминале()прямо сейчас)
file.next() - возвращает след. строку файла
file.read()
file.readline() - чтение строки файла
file.readlines() - чтение всех строк файла
file.seek()
file.seekable() - проверка доступа файла
file.tell() - текущая позиция в строке файла
file.truncate() - уменьшает размер файла на n байт
file.write()
file.writelines(line) - обавление строк в файл
'''
'''
    r = только для чтения
    w = только для записи
    a  добавление данных в файл
    rb = чтение бинарное
    r+ = чтение и запись
    rb+ = чтение и запись бинарное
    w+ = чтение и запись, если файла нет то создаём его
    wb+ = аналогично выше стоящему
    a+ = чтение и добавление, если файла нет то создаём его
    ab = аналогично выше стоящему только бинарное
    ab+ = аналог выше стоящего с созданием файла
'''
#задание 1
def basnya():
    with open("article.txt", 'w+') as question:
        question.write("Вечерело \n"
                   "Жужжали мухи \n"
                   "Кипела вода в чайнике \n"
                   "Венера зажглась на небе \n"
                   "Деревья шумели \n"
                   "Тучи разошлись \n"
                   "Листва Зеленела \n")
    with open ("article.txt", 'r') as file:
        for i in file.readlines():
            print(i, end='')


def task2():
    """Задание 2: Создать файл со словами из 7+ букв из басни"""
    try:
        with open('vorona_i_lisitsa.txt', 'r') as file:
            content = file.read()

        words = content.split()
        long_words = [word for word in words if len(word.strip('.,!?;:"')) >= 7]

        with open('long_words.txt', 'w') as output_file:
            for word in long_words:
                output_file.write(word + '\n')

        print(f"Задание 2 выполнено! Найдено {len(long_words)} слов из 7+ букв.")
        print("Результат записан в файл 'long_words.txt'")

    except FileNotFoundError:
        print("Ошибка: Файл 'vorona_i_lisitsa.txt' не найден!")
        print("Создайте файл с басней или измените имя файла.")

def task3():
    try:
        with open('file1.txt', 'r') as file1:
            lines = file1.readlines()

        with open('file2.txt', 'w') as file2:
            for line in lines:
                file2.write(line)

        print("файлы переписаны, хорошего дня!")

    except FileNotFoundError:
        print("Ошибка: Файл 'file1.txt' не найден!")


def task4():
    try:
        with open('file1.txt', 'r', encoding='utf-8') as file1:
            lines = file1.readlines()

        with open('file2_reversed.txt', 'w', encoding='utf-8') as file2:
            for line in reversed(lines):
                file2.write(line)

        print("Задание 4 выполнено! Строки переписаны в обратном порядке в 'file2_reversed.txt'")

    except FileNotFoundError:
        print("Ошибка: Файл 'file1.txt' не найден!")


def task5():
    try:
        with open('text_file.txt', 'r') as file:
            lines = file.readlines()

        last_no_comma_index = -1
        for i, line in enumerate(lines):
            if ',' not in line:
                last_no_comma_index = i

        if last_no_comma_index != -1:
            lines.insert(last_no_comma_index + 1, '*' * 12 + '\n')
        else:
            lines.append('*' * 12 + '\n')

        with open('text_file.txt', 'w') as file:
            file.writelines(lines)

        print("Задача выполнена!")

    except FileNotFoundError:
        print("Ошибка: Файл 'text_file.txt' не найден!")


def task6():
    try:
        char = input("Введите символ для поиска: ").strip()
        if len(char) != 1:
            print("Ошибка: нужно ввести один символ!")
            return

        with open('text_file.txt', 'r') as file:
            content = file.read()

        words = content.split()
        count = 0
        matching_words = []

        for word in words:
            clean_word = word.strip('.,!?;:"').lower()
            if clean_word and clean_word[0] == char.lower():
                count += 1
                matching_words.append(word)

        print(f"Найдено {count} слов, начинающихся с символа '{char}':")
        for word in matching_words[:10]:  # Показываем первые 10 слов
            print(f"  {word}")
        if len(matching_words) > 10:
            print(f"  ... и еще {len(matching_words) - 10} слов")

    except FileNotFoundError:
        print("Ошибка: Файл 'text_file.txt' не найден!")


def task7():
    try:
        with open('file_with_stars.txt', 'r', encoding='utf-8') as file1:
            lines = file1.readlines()

        modified_lines = [line.replace('*', '&') for line in lines]

        with open('file_with_ampersands.txt', 'w', encoding='utf-8') as file2:
            file2.writelines(modified_lines)

        print("Задача выполнена! Символы * заменены на & в новом файле.")

    except FileNotFoundError:
        print("Ошибка: Файл 'file_with_stars.txt' не найден!")


def task8():
    strings = [
        "Первая строка",
        "Вторая строка",
        "Третья строка",
        "Четвертая строка",
        "Пятая строка"
    ]

    print("Массив для записи:")
    for i, string in enumerate(strings, 1):
        print(f"{i}. {string}")

    with open('array_output.txt', 'w') as file:
        for string in strings:
            file.write(string + '\n')

    print("Задача выполнена! Массив записан в файл 'array_output.txt'")


def task9():
    try:
        filename = input("Введите имя файла (по умолчанию 'text_file.txt'): ").strip()
        if not filename:
            filename = 'text_file.txt'

        with open(filename, 'r') as file:
            content = file.read()

        char_count = len(content)
        print(f"Файл '{filename}' содержит {char_count} символов.")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден!")


def task10():
    try:
        filename = input("Введите имя файла (по умолчанию 'text_file.txt'): ").strip()
        if not filename:
            filename = 'text_file.txt'

        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        line_count = len(lines)
        print(f"Файл '{filename}' содержит {line_count} строк.")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден!")

def main():
    while True:
        print("\n" + "=" * 50)
        print("Меню: \n"
                    "1. Создать примеры файлов для демонстрации \n"
                    "2. Задание 2 - Слова из 7+ букв из басни \n"
                    "3. Задание 3 - Переписать строки с сохранением порядка \n"
                    "4. Задание 4 - Переписать строки в обратном порядке \n"
                    "5. Задание 5 - Добавить строку из звездочек \n"
                    "6. Задание 6 - Подсчитать слова по первой букве \n"
                    "7. Задание 7 - Заменить * на & \n"
                    "8. Задание 8 - Записать массив в файл \n"
                    "9. Задание 9 - Подсчитать символы в файле \n"
                    "10. Задание 10 - Подсчитать строки в файле \n"
                    "0. Выход")

        choice = input("Выберите задание (0-10): ").strip()

        if choice == '0':
            print("Выход из программы.")
            break
        elif choice == '1':
            basnya()
        elif choice == '2':
            task2()
        elif choice == '3':
            task3()
        elif choice == '4':
            task4()
        elif choice == '5':
            task5()
        elif choice == '6':
            task6()
        elif choice == '7':
            task7()
        elif choice == '8':
            task8()
        elif choice == '9':
            task9()
        elif choice == '10':
            task10()
        else:
            print("Неверный выбор! Попробуйте снова.")

        input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()

#лабораторная работа по файлам
import math
import numpy as np


def y1(x):
    """y1(x) = 20 + (1 + x) * ∛(1 + x²)"""
    return 20 + (1 + x) * np.cbrt(1 + x ** 2)


def y2(x):
    """y2(x) = -x + 2e^(-2x)"""
    return -x + 2 * math.exp(-2 * x)


# Параметры
n0 = -5  # начальное значение x
nk = 5  # конечное значение x
h = 0.5  # шаг

# Генерация массивов
x_values = np.arange(n0, nk + h, h)
y1_values = []
y2_values = []

# Вычисление значений функций
for x in x_values:
    y1_values.append(y1(x))
    y2_values.append(y2(x))

# Запись в файл
with open('data.txt', 'w') as file:
    file.write("Результаты вычислений функций y1 и y2\n")
    file.write(f"Диапазон x: от {n0} до {nk} с шагом {h}\n")
    file.write("№\t x\t\t y1(x)\t\t y2(x)\n")

    for i, (x, y1_val, y2_val) in enumerate(zip(x_values, y1_values, y2_values), 1):
        file.write(f"{i}\t {x:.2f}\t {y1_val:.4f}\t {y2_val:.4f}\n")

    file.write(f"Формулы:\n")
    file.write(f"y1(x) = 20 + (1 + x) * ∛(1 + x²)\n")
    file.write(f"y2(x) = -x + 2e^(-2x)\n")

print("Результаты успешно записаны в файл 'data.txt'")

# Дополнительно выводим первые несколько значений для проверки
print("\nПервые 5 значений для проверки:")
print("x\t y1(x)\t\t y2(x)")
for i in range(min(5, len(x_values))):
    print(f"{x_values[i]:.2f}\t {y1_values[i]:.4f}\t {y2_values[i]:.4f}")