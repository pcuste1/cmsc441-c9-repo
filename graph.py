# CMSC 441 Algorithms, Prof. Christopher Marron
# an algorithm to solve the line folding problem

import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import itertools

	
def main():

	print('Line Folding Algorithm')
	
	
	#number of elements searched
	x_algo = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 500, 1000, 1500, 2000])


	#runtime of program with corresponding elements
	y_algo = np.array([0,0.000470161, 0.0021588, 0.0062839, 0.0121300, 0.1786618, 0.19369, 0.22260, 0.12673, 0.98540, 6.22061, 61.8472, 207.8189, 483.3677])


	#plot running time
	
	#Range of generated values
	x = np.arange(0, 5000, 1)
	
	#X^2 and X^3 to compare algorithm to
	y_x2 = x * x * 0.00001
	y_x3 = x * x * x * 0.00001

	#Draw lines
	plt.plot(x,y_x2)
	plt.plot(x,y_x3)
	plt.plot(x_algo,y_algo)

	#axis labels

	axis = plt.gca()
	axis.set_ylim([0,3000])
	axis.set_xlim([0,3000])

	plt.xlabel('n')
	plt.ylabel('seconds')
	
	plt.title('My Runtimes')
	plt.legend(['X^2', 'X^3', 'My Runtime'])

	plt.show()	

	
main()



