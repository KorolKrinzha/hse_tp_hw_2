from NumbersOperator import NumbersOperator
def run():
    comparer = NumbersOperator('numbers.txt')
    comparer.max()
    comparer.min()
    comparer.sum()
    print(comparer.mult())
    
    

if __name__ == '__main__':
    run()