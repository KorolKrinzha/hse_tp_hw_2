import timeit
import numpy as np
from matplotlib import pyplot as plt
from NumbersOperator import NumbersOperator
plt.xlabel('Число данных')
plt.ylabel('Время исполнения программы')
testfiles = ['./tests_txt/timetest_1.txt','./tests_txt/timetest_2.txt', './tests_txt/timetest_3.txt']
numbers_list = [ NumbersOperator(filename) for filename in testfiles]
numbers_list_size = [operator.getNumberListSize() for operator in numbers_list]


def sum_timetest_0(numbers_list):
    
    numbers_0 = numbers_list[0]
    
    return numbers_0.sum()
    
# print(numbers_list_size)
# print(sum_timetest_0(numbers_list))
# sum_timetest_0(numbers_list)
stmt = ''
setup = """ 
from NumbersOperator import NumbersOperator
testfiles = ['./tests_txt/timetest_1.txt','./tests_txt/timetest_2.txt', './tests_txt/timetest_3.txt']
numbers_list = [ NumbersOperator(filename) for filename in testfiles]
"""
sum_timetest_0=  """
numbers_list[0].sum()
"""
sum_timetest_1=  """
numbers_list[1].sum()
"""
sum_timetest_2=  """
numbers_list[2].sum()
"""


sum_time_0 = timeit.timeit(stmt=sum_timetest_0, setup=setup, number=10000)
sum_time_1 = timeit.timeit(stmt=sum_timetest_1, setup=setup, number=10000)
sum_time_2 = timeit.timeit(stmt=sum_timetest_2, setup=setup, number=10000)
print(sum_time_0, sum_time_1, sum_time_2)
# print(timeit.timeit("[(a, b) for a in (1, 3, 5) for b in (2, 4, 6)]"))
# x = np.linspace(0, 2.0*np.pi, 101)
# y = np.sin(x)                        # sine function


# plt.plot(x, y, color='r', label='sin')
# plt.plot(x, y)
# plt.show()