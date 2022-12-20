"""This project detects the 'extra' number"""

from itertools import chain
import random

def find_extra(length):
	"""
	Gets length of list, appends list from (1, lenght+1) except for one number,
	detects that 'extra' number and returns it
	"""
	numbers = []
	extra_number = random.randint(1,length+2)
	res = chain(range(1,extra_number), range(extra_number+1,length+2))
	numbers = [i for i in res]
	print(numbers)
	result_extra_number = [i for i in range(1,length+2) if i not in numbers]
	return result_extra_number[0]


if __name__ == '__main__':
	"""You will input the length of list"""
	length = int(input('Length of list: '))
	result = find_extra(length)
	print(result)