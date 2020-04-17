import sys

# N школьников делят K яблок поровну, 
# неделяющийся остаток остается в корзинке. 
# Сколько яблок достанется каждому школьнику?

def count_apples(schools, apples):
	print(int(apples) // int(schools))

if 'test' in sys.argv:
	count_apples('3', '14')

else:
	s = int(input())
	a  = int(input())
	count_apples(s, a)
