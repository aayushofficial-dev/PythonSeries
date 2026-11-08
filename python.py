# addition of two numbers

'''using + operators'''
a = 5
b = 7
res = a + b
print(res)

"""
Using sum() function
the sum() function adds all the values present in an iterable like a list or tuple and returns the total 
sum."""

nums = [10,5]
print(sum(nums))


"""
Using operator.add()
The operator module provides the add() function, which performs addition between two values similar 
to the + operator
"""
import operator
print(operator.add(10, 22))

"""
Using math.fsum()
The fsum() function from the math module is used for precise floating-point addition. It helps reduce
rounding errors while adding decimal values"""

import math
x = [0.01, 0.02]
print(math.fsum(x))

# Find the maximum of two numbers in Python

"""Using max()
max() function compares two or more values and returns the largest one. It performs the comparison internally
and eliminates the need to write explicit conditional statements."""

a = 7
b = 4
print(max(a, b))

"""Using Ternary operator
Ternary conditional operator evalutes the condition and return one of two values depending on whether 
the condition is true or false in a single expression"""

a = 7
b = 4

print(a if a > b else b)


"""
Using if-else statements
if-else statement evalutes a condition and executes one of two code blocks based on whether the condition is
true or false. It is used when the logic needs to be written explicitly in separate steps."""

a = 8
b = 7

if a > b:
    print(a)
else:
    print(b)

"""Factorial of a number in python"""

"""using math.factorial()
This method computes the factorial using Python's built-in factorial() function, which performs the
entire calculation internally without requiring loops or recursion in user code."""
import math 
n = 5
print(math.factorial(n))


"""Using NumPy's np.prod()
NumPy performs multiplication through optimized C-level operations. It computes the factorial by multiplying
all numbers from 1 to n in single vectorized step using np.road()"""
import numpy as np
n = 5
if n >= 0:
    print(np.prod(range(1, n + 1)))
else:
    print("Factorial is not defined for negative numbers.")

"""Using For Loop
This method calculates factorial by manually multiplying the numbers from 1 to n inside a for loop."""
n = 5 
if n < 0:
    print("Factorial is not defined for negative numbers.")

else:
    f = 1
    for i in range(1, n+1):
        f *= i
    print(f)



"""Python program to find the largest element in an array.
example:
arr = [20, 10, 20, 30, 100]
output: 100"""

"""Using built-in max() function
Python has an inbuilt method max() which returns the maximum value among the arguements"""

arr = [10, 20, 30, 40, 50]
res = max(arr)
print(res)

"""Using Iteration
This method manually traverse the array and update the largest element when a bigger element is found."""

arr = [10, 324, 45, 90, 9808]
res = arr[0]

for i in range(1, len(arr)):
    if arr[i] > res:
        res = arr[i]
print(res)

"""Using reduce() Function
The reduce() function from functools can find the largest element by applying max cumulatively
across the array."""

from functools import reduce
arr = [10, 324, 45, 90, 9808]
res = reduce(max, arr)
print(res)

"""Using sort() function
Here sort() function is used to sort the array. The largest element will be the last element of the sorted array.
"""

arr = [10, 324, 45, 90, 9808]
arr.sort()
res = arr[-1]
print(res)

"""Using operator.gt()
Use the operator.gt() function to compare elements and find the largest element iteratively."""

import operator
arr = [1, 2, 3, 4, 5]
res = 0

for i in arr:
    if operator.gt(i, res):
        res = i
print(res)


"""Array rotation Without using slicing (using loops)"""

arr = [1, 2, 3, 4, 5]
k = 2

for i in range(k):
    first = arr[0]

    for j in range(len(arr) - 1):
        arr[j] = arr[j + 1]

    arr[-1] = first
print(arr) 

"""Right rotation"""
arr = [1, 2, 3, 4, 5]
k = 2

for i in range(k):
    last = arr[-1]

    for j in range(len(arr) - 1, 0, -1):
        arr[j] = arr[j - 1]

    arr[0] = last

print(arr)

def expanded_form(num):
    num_str = str(num)
    length = len(num_str)
    result = []
    
    for i, digit in enumerate(num_str):
        if digit != '0':
            # Calculate the place value by appending the appropriate number of zeros
            place_value = digit + '0' * (length - i - 1)
            result.append(place_value)
            
    return ' + '.join(result)
print(expanded_form(79))


"""When provided with a number between 0-9, return it in words. Note that the input is guaranteed 
to be within the range of 0-9.

Input: 1
Output: "One".
"""
def switch_it_up(number):
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    result = ""
    for i, value in enumerate(num):
        if number >= 0 and number <= 9:
            if i == number:
                result = value
    return result.capitalize()
print(switch_it_up(2))


num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for i, value in enumerate(num):
    print(i, value)

"""
def get_volume_of_cuboid(length, width, height):
    volume = length * width * height
    return volume
print(get_volume_of_cuboid(10, 20, 30))
"""


def reverse_seq(n):
    result = []
    for i in range(n, 0, -1):
        result.append(i)
    return result
print(reverse_seq(5))

def human_years_cat_years_dog_years(human_years):
    # Your code here
    initialhumanage = 1
    initialcatage = 15
    initialdogage = 15
    if human_years == 1:
        return [initialhumanage,initialcatage,initialdogage]
    elif human_years == 2:
        return [initialhumanage + 1, initialcatage + 9, initialdogage + 9]
    else:
        return [human_years, 24 + (human_years -2) * 4, 24 + (human_years - 2) * 5]

print(human_years_cat_years_dog_years(1))

def double_char(s):
    result = ""
    for i in s:
        result += i * 2
    return result
print(double_char('string'))

# altERnaTIng cAsE <=> ALTerNAtiNG CaSe
def to_alternating_case(string):
    result = ""
    for s in string:
        if s.islower():
            result += s.upper()
        else:
            result += s.lower()
    return result
print(to_alternating_case('hello Aayush'))

a = b = c = 100
del a
print(b + c )

a = 10
b = a
print(b)
b <<= a
print(b)


def two_sum(numbers, target):
    result = {}
    for i, n in enumerate(numbers):
        complement = target - n
        if complement in result:
            return [result[complement], i]
        result[n] = i
    return []

print(two_sum([1,2,3], 4))


def count_by(x, n):
    result = []
    for i in range(x, (x*n) + 1, x):
        result.append(i)
    return result
print(count_by(3, 10))


def order(sentence):
    result = sentence.split()
    return result
print(order("is2 Thi1s T4est 3a"))


def order(sentence):
    if not sentence:
        return ""
    
    words = sentence.split()
    result = []
    
    for i in range(1, 10):
        for word in words:
            if str(i) in word:
                result.append(word)
    return " ".join(result)
print(order("is2 Thi1s T4est 3a"))

# sum of odd numbers:
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

# 1 -->  1
# 2 --> 3 + 5 = 8


def row_sum_odd_numbers(n):
    total = 0
    result = []
    for i in range(1, n):
        if i % 2 == 1:
            result.append(i)

    for x, y in enumerate(result, start=1):
        if x == y:
            total += i
    return total
print(row_sum_odd_numbers(2))

def row_sum_odd_numbers(n):
    # The first number in the nth row
    start = n * (n - 1) + 1
    total = 0
    
    for i in range(n):
        current_number = start + (i * 2)
        # Condition to check if the number is odd (which it always will be)
        if current_number % 2 != 0:
            total += current_number
            
    return total
print(row_sum_odd_numbers(2))

# Mexican wave
def wave(people):
    # Code here
    result = []
    for i in range(len(people)):
        if people[i].isalpha():
            wave_str = people[:i] + people[i].upper() + people[i+ 1:]
            result.append(wave_str)
    return result
print(wave('hello'))

age = 25

if age <= 12:
    print('child')
elif age <= 19:
    print('teenager')
elif age <= 35:
    print('young adult')
else:
    print('adult')


def between(a,b):
    # good luck
    result = []
    if a < b:
        for i in range(a, b+1):
            result.append(i)
    return result
print(between(1, 4))

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    # your code here
    result = []
    for i in range(a, b+1):
        total  = 0
        for index, digit in enumerate(str(i),start=1):
            total += int(digit) ** index
        if total == i:
            result.append(i)
    return result
print(sum_dig_pow(1, 100))

def fun():
    print('Hello aayush')
fun()


# Your task is to create a function that does four basic mathematical operations.
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

# Examples(Operator, value1, value2) --> output

# ('+', 4, 7) --> 11
# ('-', 15, 18) --> -3
# ('*', 5, 5) --> 25
# ('/', 49, 7) --> 7
def basic_op(operator, value1, value2):
    #your code here
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
print(basic_op('+', 5, 5))


a = 256
b = 256
print(a is b)

x = 257
y = 257

print(x is y)


print(bool([]))
print(bool([0]))
print(bool(""))
print(bool(" "))


for i in range(5):
    if i == 3:
        continue
    else:
        print(i)
