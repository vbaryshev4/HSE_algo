import sys
import math

'''
Капитан Флинт зарыл клад на Острове сокровищ. 
Он оставил описание, как найти клад. 
Описание состоит из строк вида: "North 5", 
где  слово – одно из "North", "South", "East", "West", – задает направление движения, 
а  число – количество шагов, которое необходимо пройти в этом направлении. 
Напишите программу, которая по описанию пути к кладу определяет точные координаты клада, 
считая, что начало координат находится в начале пути, 
ось OX направлена на восток, ось OY – на север.


Необходимо вывести  координаты клада – два целых числа через пробел. 
Гарантируется, что эти числа не превосходят 10**8.

'''

def count_coord(d, v):
    if d == 'South':
        v = v * (-1)
        return 0, v
    elif d == 'North':
        return 0, v
    if d == 'East':
        return v, 0
    elif d == 'West':
        v = v * (-1)
        return v, 0

def run(iter):
	result_1 = 0
	result_2 = 0
	for i in iter:
		i = i.split()
		d = i[0]
		v = i[1]
		r1, r2 = count_coord(d, int(v))
		result_1 += r1
		result_2 += r2
	print(result_1, result_2)


inp = sys.stdin.read().strip()
inp = inp.split('\n')
run(inp)

# t = 'North 1 \n South 10'
# inp = t.split('\n')
# run(inp)

# t1 = 'South 19'
# inp = t1.split('\n')
# run(inp)


