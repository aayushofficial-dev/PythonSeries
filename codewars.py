# Character Frequency
# Write a Python program that takes a string and counts how many times each character appears.

# user_input = input('Enter the string:')

# result = {}

# for i in user_input:
#     if i in result:
#         result[i] += 1
#     else:
#         result[i] = 1

# print(result)

# Count vowel and consonant
# user_input = input('Enter the string:').lower()

# vowel_letter = 'aeiou'
# vowel = 0
# consonant = 0

# for char in user_input:
#     if char.isalpha():
#         if char in vowel_letter:
#             vowel += 1
#         else:
#             consonant += 1

# print(f'Vowel count: {vowel}')
# print(f'Consonant count: {consonant}')

# First Non-Repeating Character
# Write a Python program that finds the first character that appears only once in a string.
# user_input = input('Enter the string:')

# for char in user_input:
#     if user_input.count(char) == 1:
#         print(f'The first non-repeating character is: {char}')
#         break
# else:
#     print('No non-repeating character is found.')

# Find the Second-Largest Number
# Write a Python program that finds the second-largest unique number in a list without using sort() or sorted().
num = [1, 2, 3, 4, 5]

largest = None
second_largest = None

for n in num:
    if largest is None or n > largest:
        second_largest = largest
        largest = n
    elif n < largest and (second_largest is None or n > second_largest):
        second_largest = n

print(second_largest)

# Sentence smash: this program smash the list into one sentence
def smash(words):
    return ' '.join(words)
print(smash(['this', 'is', 'me', 'aayush']))

def smash(words):
    result = ' '
    for word in words:
        result += word + ' '
    return result.strip()
print(smash(['this', 'is', 'me', 'aayush']))

def smash(words):
    result = ''
    for word in words:
        if result: # checks whether result already contains text.
            result += ' ' # add a space only between words
        result += word
    return result
print(smash(['this', 'is', 'me', 'aayush']))

# opposite : basically this program change the positive number into negative and vice versa
def opposite(number):
    return -number
print(opposite(1))


# reverse
def digitize(n):
    return list(map(int, reversed(str(n))))
print(digitize(12345))

# greet: this function print the famous 'hello world!'
def greet():
    return 'Hello world!'
print(greet())

# invert: this program basically check the list and if there is negative number, it changes into positive and vice versa.
def invert(lst):
    return [-x for x in lst]
print(invert([1, 2, -3, 4, -5]))

# using loop
def invert(lst):
    result = []
    for x in lst:
        result.append(-x)
    return result
print(invert([1, 2, -3, 4, -5]))

# points 
def points(games):
    total_points = 0
    for game in games:
        x, y = map(int, game.split(':'))

        if x > y:
            total_points += 3
        elif x == y:
            total_points += 1
    return total_points
print('Total points you got:', points(['1:3', '3:0', '1:1', '5:4']))


# make negative: yo program le chai positive number lai negative banauxa ra negative lai negative nai rakhxa
def make_negative(number):
    return -abs(number)
print(make_negative(-1))
print(make_negative(1))

# find average
def average(num):
    if len(num) == 0:
        return 0
    return sum(num) / len(num)
print('Average:', average([1, 2, 3, 4, 5]))

# array check
def check(seq, elem):
    return elem in seq
print(check([1, 2, 3, 4, 5], 3))

# slicing in string and list
x = [1, 2, 3, 4, 5]
name = 'ronaldo'
print(x[::2]) # [1, 3, 5]
print(x[::-1]) # [5, 4, 3, 2, 1]
print(name[::-1]) # odlanor
print(x[0]) # 1

# loops: hard
i = 0
result = []
while True:
    i += 1
    if i > 5:
        break
    if i % 2 == 0:
        continue
    result.append(i)
print(result)

# Dragon
def hero(bullets, dragon):
    return bullets >= dragon * 2
print(hero(10, 5))

# Disemvowel Trolls
def disemvowel(string):
    return ''.join(c for c in string if c.lower() not in 'aeiou')
print(disemvowel('Great thing takes time.')) 

# maybe the tuple
t = (10, 20, 30, 40, 50)
print(len(t))
print(t[::-1])

# String
name = 'ronaldo'
print(len(name))
for index, n in enumerate(name):
    print(f'Index: {index}, Value: {n}')

print(name[1:5])

# addition of different data types:
print(7 + 7) # 14
print('7' + '7') # 77
print(True + True) # 2
print(False + False) # 0
print(5 + 5.5) # 10.5



# playing with digits 
def dig_pow(n, p):
    s = 0
    for i, digit in enumerate(str(n)):
        s += int(digit) ** (p + 1)

    if s % n == 0:
        return s // n
    else:
        return -1 
print(dig_pow(8, 9))

# min_max
def min_max(lst):
    min_n = lst[0]
    max_n = lst[0]

    for i in lst:
        if i < min_n:
            min_n = i
        if i > max_n:
            max_n = i

    return [min_n, max_n]
print(min_max([1,2,3,4,5]))

# consecutive string
def longest_consec(strarr, k):
    # condtitons to handle edge cases
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""
    
    longest_string = ""
    
    # Loop to iterate through the list
    for i in range(n - k + 1):
        current_slice = strarr[i : i+k]
        current_string = ''.join(current_slice)
        
        # condition to check if the new string is longer
        if len(current_string) > len(longest_string):
            longest_string = current_string
    
    return longest_string

print(longest_consec(['aayush', 'is', 'the', 'best', 'tech', 'enginerr'], 2))


import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

import json 
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["name"])

a = [1,2,3]
b = [1,2,3]
c = a
print(a == b)
print(a is b)
print(a is c)

a = 'aayushisthebesttechengineerintheworld'
x = lambda func: func.upper()
print(x(a))

def mygenerator():
    yield 1
    yield 2
    yield 3

for value in mygenerator():
    print(value)


print(~(~2))
print(~(~3))
print(~2)

age = 'aayush'

if isinstance(age, int):
    print('it is num')
else:
    print('it is str')


import re

def count_smileys(arr):
    # ^[:;] matches eyes
    # [-~]? matches an optional nose
    # [)D]$ matches the mouth
    pattern = r'^[:;][-~]?[)D]$'
    
    count = 0
    for face in arr:
        if re.match(pattern, face):
            count += 1
            
    return count


def count_smileys(arr):
    eyes = {':', ';'}
    noses = {'-', '~'}
    mouths = {')', 'D'}
    
    count = 0
    for face in arr:
        if len(face) == 2:
            if face[0] in eyes and face[1] in mouths:
                count += 1
            elif len(face) == 3:
                if face[0] in eyes and face[1] in noses and face[2] in mouths:
                    count += 1
    return count
print(count_smileys([';D', ':-(', ':-)', ';~)']))


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