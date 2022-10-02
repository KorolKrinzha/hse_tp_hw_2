class NumbersOperator:
    
    # constructor with one private attribute - filename
    # We will use a filename in each method where we work with the file's numbers
    def __init__(self, filename):
        self.__filename= filename
    
    def __str__(self):
        return f"Оператор чисел из локального файла{self.__filename}"
    
    # function to read numbers out of file is made private 
    # It is because user of the class is not required to know the numbers themselves
    # ! It is done according to TA 
    def __getNumbersFromFile(self) -> list:
        numbers_list = []
        try:
            with open(self.__filename) as f:
                numbers_line = f.readline()
                numbers_list = numbers_line.split(' ')
                numbers_list = [int(i) for i in numbers_list]
                return numbers_list 
        except:
            raise TypeError
        return
    
    def getNumberListSize(self):
        numbers_list = self.__getNumbersFromFile()
        return len(numbers_list)
    # find maximum
    def max(self) -> int:
        numbers_list = self.__getNumbersFromFile()
        return max(numbers_list)
    
    # find minimum
    def min(self) -> int:
        numbers_list = self.__getNumbersFromFile()
        return min(numbers_list)
    # add all numbers
    def sum(self) -> int:
        numbers_list = self.__getNumbersFromFile()
        return sum(numbers_list)
    # multiply all numbers
    def mult(self) -> int:
        numbers_list = self.__getNumbersFromFile()
        result = 1
        for n in numbers_list:
            result*=n
        return result
    
        