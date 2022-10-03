import csv
import random
with open('books.csv') as csvfile:
    u = 0
    table = list(csv.reader(csvfile, delimiter=';'))
    while u <20:

        y = input()
        o = 3
        n =0
        while o != 1:
            n +=1
            o = random.randint(1,2)
            if o == 1:
                print(table[n][3],',',table[n][1], '-', table[n][6])
                print(u)
        u += 1