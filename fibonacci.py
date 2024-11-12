#Program to print fibonacci series

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def print_fibonacci_series(n):
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci sequence:")
        for i in range(n):
            print(fibonacci_recursive(i), end=" ")


n_terms = int(input("Enter the number of terms: "))
print_fibonacci_series(n_terms)

"""
output:
Enter the number of terms: 5
0 1 1 2 3
"""