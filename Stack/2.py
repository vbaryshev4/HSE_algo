import sys
from collections import deque

pairs = [
            ['(', ')'],
            ['[',']'], 
            ['{','}'],
        ]



def run(iter_obj):
    stack = deque()
    while len(iter_obj) > 0:
        elem = iter_obj.popleft()
        if elem in ['(', '[', '{']:
            stack.append(elem)
        elif elem in [')', ']', '}'] and len(stack) > 0:
            if [stack[-1], elem] in pairs:
                stack.pop()
        elif elem in [')', ']', '}'] and len(stack) == 0:
            stack.append(elem)
    
    if len(stack) != 0:
        print('no')
    else:
        print('yes')



if 'test' in sys.argv:

    d = deque('()') # yes
    # d = deque('(') # no
    # d = deque(')') # no
    # d = deque('()(({}[()]{})[{}]){}{}()[]') # yes
    # d = deque('))((') # no
    # d = deque('([{}[{}]{})]') # no
    run(d)

else:
    inp = sys.stdin.read()
    inp = inp.strip().split('\n')
    for i in inp:
        i = deque(i)
        run(i)


