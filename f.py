import random
#генерируем 20 чисел
#reader = list(reader)
def numbers():
    numbers = []
    for i in range(20):
        a = random.randint(0,9410)
        numbers.append(a)
    numbers.sort()
    return numbers
print(numbers())

with open('books.csv') as csvfile:
    u = 0
    while u <20:
        table = list(csv.reader(csvfile, delimiter = ';'))
        y = input()
        o = 3
        n =0
        while o != 1:
            n +=1
            o = random.randint(1,2)
            if o == 1:
                print(table[n][3],',',table[n][1], '-', table[n][6])
        u += 1
