import timeit
import numpy as np
from matplotlib import pyplot as plt
from NumbersOperator import NumbersOperator

# Amount of files that store numbers for the tests
number_of_files = 7
# because of template names, we store all the names in a list via simple script 
testfiles = ['./tests_txt/timetest_'+str(i)+'.txt' for i in range (1,number_of_files+1)]



# List with NumberOperator objects for each file
numbers_list = [ NumbersOperator(filename) for filename in testfiles] 
# Amount of numbers in each file (Y-AXIS)
numbers_list_size = [operator.getNumberListSize() for operator in numbers_list]



# Thats the way to use timeit module
# It is a setup for a function which we will then measure
setup = """ 
from NumbersOperator import NumbersOperator
number_of_files = 7
testfiles = ['./tests_txt/timetest_'+str(i)+'.txt' for i in range (1,number_of_files+1)]
numbers_list = [ NumbersOperator(filename) for filename in testfiles]
"""


# We will measure time for min function
min_time_list = []
for i in range(len(testfiles)):
    # Measure time for each time we use min() method     
    min_timetest = f"numbers_list[{i}].min()"
    min_time = timeit.timeit(stmt=min_timetest, setup=setup, number=10000)
    # Write down the time to the list (X-AXIS)      
    min_time_list.append(min_time)


# Matplotlib is a popular module for displaying data
# In this case we will use plot type of diagram
plt.plot(min_time_list, numbers_list_size, color='r', label='Функция минимума')
# styling a bit
plt.xlabel('Количество чисел в файле') 
plt.ylabel('Время выполнения программы, сек')
plt.grid()
# show the plot
plt.show()

# The results are
# 10 numbers - 0.9738186000004134 seconds,
# 50 numbers - 1.0879238999996232 seconds,
# 100 numbers - 1.2151348000006692 seconds,
# 1000 numbers - 3.916505799999868 seconds,
# 10000 numbers - 33.50335389999964 seconds,
# 100000 numbers - 301.12019899999996 seconds,
# 500000 numbers - 1666.0187752000002 seconds

# The plot can be seen in imgs pholder
# The prettier version of the code can be seen in Jupyter Notebook file TimeTests