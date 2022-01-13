# from numpy import divide
from . import Expense
import matplotlib.pyplot as plt
import timeit

def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()       
    divided_set_comp = expenses.categorize_set_comphrehension()
    
    if not divided_set_comp == divided_for_loop:
        print("Sets ere not equal by == test")
    
    for a, b in zip(divided_for_loop, divided_set_comp):
        if not (a.issubset(b) and b.issubset(a)):
            print("Sets are not equal by subset test")
            
    print(timeit.timeit(stmt='expenses.categorize_set_comphrehension()',
        setup = 
        '''
from . import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
        ''',
        number=100000,
        globals=globals()
        ))

    fix, ax = plt.subplots()
    labels = ['necessary','Food',"unnecessary"]
    divided_expenses_sum = []
    for category_exps in  divided_set_comp:
        divided_expenses_sum.append(sum(x.amount for x in category_exps))

    ax.pie(divided_expenses_sum, labels = labels, autopct='%1.1f%%')
    plt.show()


if __name__ == "__main__":
    main()

