# Работа с CSV файлом: найти среднее арифметическое для оценок и проверить через pytest с реальной оценкой (должны быть найдены ошибки).

import pytest
import csv

# Получение информации из файла  
def get_file():
    with open('grades.csv') as file:
      list_grades = list(csv.reader(file, delimiter=","))
    return list_grades

GET = get_file()


# Вычисление среднего значения 
def avg_grades():

    mass_total = [] 

    for row in GET[1:]:    

        total = sum(list(map(float,map(str.strip,row[3:6]))))/4

        mass_total.append(total)
    return mass_total

# Получение данных из файла и запись в список 
def end_is():

    mass_total_answer = []
    for row in GET[1:]:

        mass_total_answer.append(row[7])
    return mass_total_answer

# Получение списка со средним значением из файла и полученного 

def concat_total():
    mass_total_answer = end_is()
    mass_total = avg_grades()
    morget_list = [(mass_total_answer[i], mass_total[i]) for i in range(0, len(mass_total_answer))]

    return morget_list

        # count = 0
        # for elem in row[3:6]:
        #     count += elem
        # avg = count / 4

if __name__ == "__main__":
    avg_grades()
    end_is()
