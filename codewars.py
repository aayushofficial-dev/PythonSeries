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


# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example

# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def count_positives_sum_negatives(arr):
    positive = 0
    negative = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += i
    return [positive, negative]
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))


# Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.

# If no occurrences can be found, a count of 0 should be returned.

# ("Hello", 'o')  =>  1
# ("Hello", 'l')  =>  2
# ("", 'z')       =>  0
def str_count(string, letter):
    # Your code here ;
    result = 0
                                                    # solved
    for s in string:
        if s == letter:
            result += 1
    return result

print(str_count("hello", 'o'))



def evenOdd(x):
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd'

print(evenOdd(13))
print(evenOdd(2))

# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative. If the array is empty, return 0.

# Examples

# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2
def sum_array(a):
    result = 0
    for i in a:
        result += i
    return result
print(sum_array([1, 5.2, 4, 0, -1]))


# Count the number of divisors of a positive integer n.

# Random tests go up to n = 500000, but fixed tests go higher.

# Examples (input --> output)

# 4 --> 3 // we have 3 divisors - 1, 2 and 4
# 5 --> 2 // we have 2 divisors - 1 and 5
def divisors(n):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    return count
print(divisors(12))


# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
# Example
# "abcde" -> 0  # no characters repeats more than once
# "aabbcde" -> 2  # 'a' and 'b'
def duplicate_count(text):
    # Your code goes here
    text = text.lower()
    count = {}
    for t in text:
        if t in count:
            count[t] +=1 
        else:
            count[t] = 1
    duplicate_count = 0
    for key in count:
        if count[key] > 1:
            duplicate_count += 1
    return duplicate_count
print(duplicate_count('abbcc'))


# Your function takes two arguments:

# current father's age (years)
# current age of his son (years)
# Calculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.

def twice_as_old(dad_years_old, son_years_old):
    years = 0
    
#     If the father is currently more than twice as old as the son,
#     we look into the future(or past, depending on perspective)
    if dad_years_old > son_years_old *2:
        while dad_years_old != son_years_old * 2:
            dad_years_old += 1
            son_years_old += 1
            years += 1
            
#     if the father is currently less than twich as old as the son,
#     we look into the past
    elif dad_years_old < son_years_old * 2:
        while dad_years_old != son_years_old * 2:
            dad_years_old -= 1
            son_years_old -= 1
            years += 1
    
    return years
print(twice_as_old(36,7))


def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2 * son_years_old)
print(twice_as_old(36, 7))

# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
def is_pangram(st):
    st = st.lower()
    string = 'abcdefghijklmnopqrstuvwxyz'
    for char in string:
        if char not in st:
            return False
    return True
print(is_pangram('The quick brown fox jumps over the lazy dog'))

# exes and ohs
def xo(s):
    x = 0
    o = 0 
    for a in s:
        if a.lower() == 'x':
            x += 1
        elif a.lower() == 'o':
            o += 1

    if x == o:
        return True
    else:
        return False
    # return x, o
print(xo('xXoo'))


# removing elements
# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

# Example:

# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

def remove_every_other(my_list):
    result = []
    for i, x in enumerate(my_list):
        if i % 2 == 0:
            result.append(x)
    return result
print(remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep"]))


# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.
def get_count(sentence):
    vowel = 'aeiou'
    vowel_count = 0
    for s in sentence:
        if s in vowel:
            vowel_count += 1
    return vowel_count
print(get_count('aayush'))


name = ['aayush', 'rizan', 'ronak', 'ronash']
pos = name.index('ronak')
print(pos * 3)
print(pos)

for i, x in enumerate(name, start=1):
    print(i, x)

a = ['Python', 'Java', 'C++', 'Go']
print(a[:])

li = list(range(100, 110))
print(li.index(105))

a = [10, 20, 30, 40, 50]
b = [1, 2, 3, 4, 5]
res = []

for x, y in zip(a, b):
    res.append(x - y)

print(res)

li = ['a', 'b', 'c', 'd', 'e']
print(li[10:])