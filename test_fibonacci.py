import fibonacci
import time

def fibonacci_py(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_py(n - 1) + fibonacci_py(n - 2)

n = 10
print()

start_time = time.perf_counter()
print("C result:", fibonacci.fibonacci(n))
end_time = time.perf_counter()
print(f"C: {(end_time - start_time) * 1000: .5f} ms")
print()

start_time = time.perf_counter()
print("python result:", fibonacci_py(n))
end_time = time.perf_counter()
print(f"python: {(end_time - start_time) * 1000: .5f} ms")
