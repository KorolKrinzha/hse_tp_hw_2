import timeit
import numpy as np
from matplotlib import pyplot as plt
from NumbersOperator import NumbersOperator
number_of_files = 3
testfiles = ['./tests_txt/timetest_'+str(i)+'.txt' for i in range (1,number_of_files+1)]

numbers_list = [ NumbersOperator(filename) for filename in testfiles]
numbers_list_size = [operator.getNumberListSize() for operator in numbers_list]


    
# print(numbers_list_size)
# print(sum_timetest_0(numbers_list))
# sum_timetest_0(numbers_list)
stmt = ''
setup = """ 
from NumbersOperator import NumbersOperator
testfiles = ['./tests_txt/timetest_1.txt','./tests_txt/timetest_2.txt', './tests_txt/timetest_3.txt']
numbers_list = [ NumbersOperator(filename) for filename in testfiles]
"""

# sum_timetest_0=  """
# numbers_list[0].sum()
# """
# sum_timetest_1=  """
# numbers_list[1].sum()
# """
# sum_timetest_2=  """
# numbers_list[2].sum()
# """
sum_time_list = []
for i in range(len(numbers_list)):
    sum_timetest = f"numbers_list[{i}].sum()"
    sum_time = timeit.timeit(stmt=sum_timetest, setup=setup, number=10000)
    sum_time_list.append(sum_time)

plt.xlabel('Число данных')
plt.ylabel('Время исполнения программы')

plt.plot(sum_time_list, numbers_list_size, color='r', label='Функция суммы')

min_time_list = []
for i in range(len(numbers_list)):
    min_timetest = f"numbers_list[{i}].min()"
    min_time = timeit.timeit(stmt=min_timetest, setup=setup, number=10000)
    min_time_list.append(min_time)
    
plt.plot(min_time_list, numbers_list_size, color='g', label='Функция минимума')

plt.show()

# plt.plot(x, y, color='r', label='sin')
# plt.show()