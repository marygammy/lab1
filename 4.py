#генератор 20 книг
import csv
import random

def gen():
    with open('books.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter = ';')
        num = 0
        for row in reader:
            yesno = random.randint(0,20)
            if yesno == 0:
                num += 1
                yield row[3]+'.'+row[1]+' - '+ row[6]
            if num ==20:
                break
genbooks = open('genbooks.txt',mode = 'x')
s = 0
for r in gen():
    s+=1
    genbooks.write(str(s) +') '+r+'\n')
