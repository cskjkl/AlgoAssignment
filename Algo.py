import time
import matplotlib.pyplot as plt

#Recursion
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

#DP
def fibonacci_dp(n):
    fib = [0] * (n+1)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    #print(fib[n])
    return fib[n]

# Measure execution time for both ways
def measure_execution_time():
    recursive_times = []
    dp_times = []
    for i in range(1, 101):
        start_time = time.time()
        fibonacci_recursive(i)
        recursive_time = time.time() - start_time
        recursive_times.append(recursive_time)

        start_time = time.time()
        fibonacci_dp(i)
        dp_time = time.time() - start_time
        dp_times.append(dp_time)

        print(f"n={i}, Recursive Time: {recursive_time}, DP Time: {dp_time}")

        # Plotting in real-time
        plt.plot(range(1, i + 1), recursive_times, label='Recursive Time', color='blue')
        plt.plot(range(1, i + 1), dp_times, label='DP Time', color='red')
        plt.xlabel('n')
        plt.ylabel('Time (s)')
        plt.title('Execution Time of Fibonacci Calculation')
        plt.legend()
        plt.pause(0.1)
        plt.clf()  # Clear the plot for the next iteration

measure_execution_time()