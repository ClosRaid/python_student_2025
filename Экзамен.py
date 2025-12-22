#задача 1
'''
radius = int(input("Введите радиус круга: "))
def circle_stats(radius):
    p = 3.14159 #Число пи
    circle_lenght = 2 * p * radius
    area = p * radius**2
    print(f"Длина = {circle_lenght}, Радиус = {area} ")
    return circle_lenght,area
circle_stats(radius)
'''
from collections import Counter

#Задание 2
'''
user_str = input("Введите предложение и узнайте сколько в нём раз использовались гласные: ")
def count_vowels(text):
    vowels = 'аеиоуыэюя'
    text = text.lower()
    vowels_count = {}
    for vowel in vowels:
        count = text.count(vowel)
        if count > 0:
            vowels_count[vowel] = count
            print(f"{vowels_count} <- Итог")
count_vowels(user_str)
'''
#Задание 3
'''
number = int(input("Введите число которое будет концом радиуса: "))

def fizzbuzz_sum(end_range): #перечислить цифры которые не деляться на 3 и 5
    for i in range(1,end_range):
        if i % 3 and 5 != 0:
            print(i)
def fizzbuzz_sum2(end_range): #Посчитать сколько чисел не делится на 3 и 5
    total = 0
    for i in range(1,end_range):
        if i % 3 and 5 != 0:
            total += 1
            print(f"Столько чисел не делятся на 3 и 5 {total}")
fizzbuzz_sum(number)
'''
#задание 4
'''
list_numbers = [3,1,8,9,2,0,2,1]
def remove_duplicates_sorted(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
            new_list.sort()
    print(new_list)
    return new_list
remove_duplicates_sorted(list_numbers)
'''
#задание 5
'''
dict1 = {1:"Один",2:"Два",3:"Три",4:"Четыре"}
dict2 = {3:"Три",6:"Шесть",9:"Девять"}
def merge_dict(dict_1,dict_2): #сложение словарей в один
    all_dict = dict_1 | dict_2
    print(all_dict)
merge_dict(dict1,dict2)
'''
#задание 6
'''
def filter():
    with open("numbers.txt",'r') as firstfile, open("filtered.txt",'w+') as secondfile:
        for line in firstfile:
            if line.strip():
                number = int(line.strip())
                if number > 0 and number % 2 == 0:
                    secondfile.write(str(number))
filter()
'''
#задание 7
def apply_to_list(func, lst):
    result = []
    for item in lst:
        result.append(func(item))

#задание 8
'''
variable_1 = int(input("Введите первое число: "))
variable_2 = int(input("Введите второе число: "))
def safe_divide(number1,number2): #функция деления с проверкой
    if number1 and number2 != 0:
        divide = number1 // number2
        print(f"{number1}:{number2} = {divide}")
    elif number1 or number2 == 0:
        print("Ошибка. Деление на 0 невозможно!")
safe_divide(variable_1,variable_2)
'''
'''
#задание 9
import csv
with open("students.csv",'w+') as csvfile: #создаём файл студентов
    writer = csv.writer(csvfile) #создаём программу для записи
    writer.writerow(["name","score1","score2","score3"]) #в каком порядке записывать
    writer.writerow(["Михаил",5,3,0])
    writer.writerow(["Александр",4,4,2]) 
with open("students.csv",'r') as csvfile, open("result.csv",'w+') as secondfile: #открываем файлы для дальнейшей работы
    reader = csv.reader(csvfile) #команда для чтения первого файла
    writer = csv.writer(secondfile) #команда для записи во второй файл
    for row in reader: #запись
        name = row[0]
        score1 = row[1]
        score2 = row[2]
        score3 = row[3]
        summa = score1 + score2 + score3 
        average_score = int(summa) / 3 #считаем среднюю оценку
    writer.writerow([name,average_score]) #записываем в файл
'''
#задание 10
import re
def text_analyzer(text):
    symbol_count = len(text) #кол-во слов
    words = text.split() #убираем пробелы
    words_count = len(words) #считаем кол-во слов
    predlojenie = len(re.findall(r'[.!?]+', text)) #считаем кол-во предложений
    lower_word = []
    if lower_word:
        word_counter = Counter(lower_word)
        max_count = max(word_counter.values())
    for word in lower_word:
        if word_counter[word] == max_count:
            most_common_word = word
    return {
        "Всего символов":symbol_count,
        "Количество слов":words_count,
        "Количество предложений": predlojenie,
        "Самое часто встречающееся слово":most_common_word
    }


