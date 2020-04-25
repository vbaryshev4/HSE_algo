import sys
from collections import deque

'''
В игре в пьяницу карточная колода раздается поровну двум игрокам. 
Далее они вскрывают по одной верхней карте, и тот, чья карта старше, 
забирает себе обе вскрытые карты, которые кладутся под низ его колоды. 
Тот, кто остается без карт – проигрывает. Для простоты будем считать, 
что все карты различны по номиналу, а также, что самая младшая карта 
побеждает самую старшую карту ("шестерка берет туза"). 

Игрок, который забирает себе карты, сначала кладет под низ своей колоды 
карту первого игрока, затем карту второго игрока 
(то есть карта второго игрока оказывается внизу колоды). Напишите программу, 
которая моделирует игру в пьяницу и определяет, кто выигрывает. 
В игре участвует 10 карт, имеющих значения от 0 до 9, большая карта 
побеждает меньшую, карта со значением 0 побеждает карту 9.

Формат ввода
Программа получает на вход две строки: первая строка содержит 5 чисел, 
разделенных пробелами — номера карт первого игрока, вторая – аналогично 5 карт 
второго игрока. Карты перечислены сверху вниз, то есть каждая строка 
начинается с той карты, которая будет открыта первой.

Формат вывода
Программа должна определить, кто выигрывает при данной раздаче, 
и вывести слово first или second, после чего вывести количество ходов, 
сделанных до выигрыша. Если на протяжении 106 ходов игра не заканчивается, 
программа должна вывести слово botva.
'''

def run(first, second):
    count = 0
    first = deque(first)
    second = deque(second)

    while len(first) > 0 and len(second) > 0:

        f = first.popleft()
        s = second.popleft()

        if f > s:
            if [f, s] == [9, 0]:
                second.extend([f, s])
                count += 1

            else:
                first.extend([f, s])
                count += 1

        else:
            if [f, s] == [0, 9]:
                first.extend([f, s])
                count += 1

            else:
                second.extend([f, s])
                count += 1


    if len(first) > 0:
        print('first', count)
    else:
        print('second', count)



if 'test' in sys.argv:
    # t = '1 3 5 7 9 \n 2 4 6 8 0 \n'
    # t = '2 4 6 8 0 \n 1 3 5 7 9 \n'
    t = '1 7 3 9 4 \n 5 8 0 2 6 \n'
    inp = t.strip().split('\n')
    inp = [list(map(int, i.strip().split(' '))) for i in inp]
    run(inp[0], inp[1])

else:
    inp = sys.stdin.read()
    inp = inp.strip().split('\n')
    inp = [list(map(int, i.strip().split(' '))) for i in inp]
    run(inp[0], inp[1])
