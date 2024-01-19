import fibonacci
import time

def fibonacci_py(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_py(n - 1) + fibonacci_py(n - 2)

n = 40

start_time = time.time()
print(fibonacci_py(n))
end_time = time.time()
print("python:", end_time - start_time, "seconds")

start_time = time.time()
print(fibonacci.fibonacci(n))
end_time = time.time()
print("C:", end_time - start_time, "seconds")