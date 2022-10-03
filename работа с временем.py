import datetime
l = '01.02.2018 20:02:09'
#d = format.datetime

d =(datetime.datetime.strptime(l,'%d.%m.%Y %H:%M:%S'))
print(d.year +1)
print(d)