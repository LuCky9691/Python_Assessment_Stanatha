# rectangle_area_calculator.py
import math_operations

def calculate_rectangle_area(length, width):
    return math_operations.multiply(length, width)

#input
length = 5
width = 3
area = calculate_rectangle_area(length, width) #output = 15
print(f"The area of the rectangle is: {area}")
