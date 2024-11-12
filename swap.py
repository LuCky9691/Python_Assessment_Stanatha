#Swapping two numbers without using a temporary variable

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

a, b = b, a

print("After swapping: a =", a, ", b =", b)

"""
Output:
Enter the first number: 3
Enter the second number: 5
After swapping: a = 5, b=3
"""