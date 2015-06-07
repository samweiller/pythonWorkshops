# import numpy 
# numpy.mod
# import numpy as np
# np.mod
# from numpy import mod
# mod
# from numpy import *
# mod

import numpy

# for loop from 1 to 100
# if statement checking for mult of 15, print fizzbuzz
# else if mult of 5, print buzz
# else if mult of 3, print fizz

# if condition:
# 	do things
# elif anothercondition:
# 	do other things
# else:
# 	do yet another thing

for i in range(1,101):
	if numpy.mod(i,3) == 0 and numpy.mod(i,5) == 0:
		print("FizzBuzz")
	elif numpy.mod(i,3) == 0:
		print("Fizz")
	elif numpy.mod(i,5) == 0:
		print("Buzz")
	else:
		print(i)