import time
import matplotlib.pyplot as plt

#Global var for counting F(4)
count_f4 = 0

#Recursion
def fibonacci_recursive_with_count(n):
    global count_f4
    if n <= 1:
        return n
    else:
        if n == 4:
            count_f4 += 1
        return fibonacci_recursive_with_count(n-1) + fibonacci_recursive_with_count(n-2)

#Measure
def measure_execution_time():
    global count_f4
    n_values = list(range(5, 51))
    f4_counts = []

    plt.ion() 

    for n in n_values:
        count_f4 = 0  #Reset F(4) counter
        fibonacci_recursive_with_count(n)
        f4_counts.append(count_f4)

        #Plot
        plt.clf()
        plt.plot(n_values[:len(f4_counts)], f4_counts)
        plt.xlabel('n')
        plt.ylabel('Count of F(4)')
        plt.title('Count of F(4) Calculation')
        plt.draw()
        plt.pause(1)

    plt.ioff()
    plt.show()

measure_execution_time()