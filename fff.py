#import csv
#with open ('books.csv') as csvfile:
    #csv_gen = csv.reader("books.csv")
    #row_count = 0
    #for row in csv_gen:
        #row_count += 1
    #print(f"Row count is {row_count}")
import random
with open ('books.csv') as csvfile:
    def numbers():
        numbers = []
        for i in range(20):
            a = random.randint(0,9410)
            numbers.append(a)
        numbers.sort()
        return numbers
    #def counter():
        #i=1
        #while(i<=10):
            #yield i
            #i+=1
    #for i in counter():
        #print(i)
    def counter():
        i = 0
        road = list(csv.reader('books.csv'))
        while i<= 20:
            p = road[numbers[i]][1]
            yield p
            i += 1
    for i in counter():
        print(p)