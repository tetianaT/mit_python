#ProblemSet0
#by Tetiana Turchyn

"""
Ask the user to enter two numbers: x and y.
Output x to the power y and log2(x)
"""

import numpy

x = int(raw_input("Enter the first number: "))
y = int(raw_input("Enter the second number: "))
print "X =",x,"to the power Y =",y,"is: ", x**y
print "log(x) = ", numpy.log2(x)