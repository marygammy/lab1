from math import pi
from math import cos
from math import sin
import os
import csv
#цвета
RED = '\u001b[41m'
WHITE = "\u001b[47m"
BLACK='\u001b[24m'
PURPLE = '\u001b[40m'

END = "\u001b[0m"
d = 24
# 1 часть флаг Швейцарии
def Switzerland():
    for i in range(5):
        if i == 0 or i == 4:
            print(RED + " " * d + END)
        elif i == 1 or i == 3:
            print(RED + " " * 10 + END + WHITE + " " * 4 + END + RED + " " * 10 + END)
        else:
            print(RED + " " * 7 + END + WHITE + " " * 10 + END + RED + " " * 7 + END)

# 2 часть    делаем узор
def pattern(R, count):
    #создаём пустой массив
    plot = [[0 for col in range(2*R+1)] for row in range(2*R+1)]
    print(plot)
    c = 0
    #предельное количество ячеек, которые может занимать круг равно периметру квдарата, в крторый он заключён, поэтому рассмотрим такое же количество углов
    for i in range(8*R):
        c += 2 * pi /( 8 * R )
        #заполняем в массиве места, где должна быть окружнсть, единичками
        plot [R + round( R * cos(c))][R + round(R* sin (c))] = 1
    print(plot)
    #рисуем
    s = ''
    for row in plot:
        for u in range(count):
            for i in row:
                if i == 0:
                    print(WHITE + ' '*3 + END, end = '')
                if i == 1:
                    print(BLACK + ' '*3 + END, end = '')
        print('')

# 3 чвсть график
def graffics():
    #записываем оси с измерениями
    def array_init(array_in, st):
        for i in range(10):
            for j in range(10):
                #ось Y нумеруем с учётом шага в обратном порядке (сверху вниз)
                if j == 0:
                    array_in[i][j] = round(st * (8 - i) + st, 1)
                #ось X нумеруем
                if i == 9:
                    array_in[i][j] = round(j, 1)
        return array_in
    #проверяем, что закрашивать
    def array_fill(array_fi, res, st):
        for i in range(9):
            for k in range(10):
                if abs(array_fi[i][0] - res[9 - k]) < st:
                    for j in range(9):
                        if 8 - j == k:
                            array_fi[i][j + 1] = 1
        return array_fi
    #рисуем
    def print_plot(plot):
        for i in range(9):
            line = ''
            for j in range(10):
                if j == 0:
                    line += WHITE + str(plot[i][j])
                if plot[i][j] == 0:
                    line += '  '
                elif plot[i][j] == 1:
                    line += RED + '  ' + WHITE
            line += END
            print(line)
        print(WHITE + '0   1 2 3 4 5 6 7 8 9' + END)
    #создаём пустые массивы для работы
    array_plot = [[0 for col in range(10)] for row in range(10)]
    result = [0 for i in range(10)]
    #заполняем массив значениями функции
    for i in range(10):
        result[i] = i / 3
    print(result)
    #узнаём шаг, с которым будет ось Y
    step = round(abs((result[9] - result[0])) / 9, 1)
    #реализуем
    array_init(array_plot, step)
    array_fill(array_plot, result, step)
    print_plot(array_plot)

# 4 часть    #находим книги для 16 лет в файле books.csv
def four():
    with open('books.csv') as csvfile:
        books = list(csv.reader(csvfile, delimiter = ';'))
        sixteen = 0
        l = len(books) - 1
        print(l)
        for row in books:
            if row[5] == '16':
                sixteen += 1
        percent = round(sixteen/l * 100)
        print(RED + ' ' * percent + END + ' ' + str(percent) + ' % книги для 16-летнего возраста')
        print( PURPLE + ' ' * (100 - percent) + END  + ' ' + str(100-percent) + " % ")
