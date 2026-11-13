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

# The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).
# For example:
# 1.08 --> 30

def cockroach_speed(s):
    # Good Luck!
    km = 27.7777778
    result = 0
    if s >= 0:
        res = s * km
        result += res
    return int(result)
print(cockroach_speed(1.08))


# Write a function that accepts a non-negative integer n and a string s as parameters, and returns a string of s repeated exactly n times.
# Examples (input -> output)
# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"

def repeat_str(repeat, string):
    return string * repeat
print(repeat_str(6, 'hello'))

# check even or odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(22))


# dna_to_rna conversion
# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').
# Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').
# Create a function which translates a given DNA string into RNA.
# For example:
# "GCAT"  =>  "GCAU"
# The input string can be of arbitrary length - in particular, it may be empty. All input is guaranteed to be valid, i.e. each input string will only ever consist of 'G', 'C', 'A' and/or 'T'.

def dna_to_rna(dna):
    return dna.replace('T', 'U')
print(dna_to_rna('GCAT'))

# another approach
def dna_to_rna(dna):
    rna = ""
    for char in dna:
        if char == 'T':
            rna += 'U'
        else:
            rna += char
    return rna
print(dna_to_rna('GCAT'))

# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# list filtering
def filter_list(l):
    result = []
    for a in l:
        if isinstance(a, int):
            result.append(a)
    return result
print(filter_list([1,2,'a','b']))


# Is the string uppercase?
# Task
# Create a method to see whether the string is ALL CAPS.
# Examples (input -> output)

# "c" -> False
# "C" -> True
# "hello I AM DONALD" -> False
# "HELLO I AM DONALD" -> True
# "ACSKLDFJSgSKLDFJSKLDFJ" -> False
# "ACSKLDFJSGSKLDFJSKLDFJ" -> True
def is_uppercase(inp):
    if inp == inp.upper():
        return True
    else:
        return False
print(is_uppercase('HELLO@'))
# another approach
def is_uppercase(inp):
    return inp == inp.upper()
print(is_uppercase('HELLO@'))

# sort the odd
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
def sort_array(source_array):
    odds = []
    # step 1: collect all odd numbers
    for num in source_array:
        if num % 2 != 0:
            odds.append(num)

    # step 2: sort the odd numbers
    odds.sort()

    # step 3: create a new array and place sorted odds back in
    result = []
    odd_index = 0

    for num in source_array:
        if num % 2 != 0:
            result.append(odds[odd_index])
            odd_index += 1
        else:
            result.append(num)
    return result
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0] ))

# Find the unique number

def find_uniq(xs):
    s = set(xs)
    for x in s:
        if xs.count(x) == 1:
            return x
print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))

# student's final grade
def final_grade(grade, project):
    if grade > 90 or project > 10:
        return 100
    elif grade > 75 and project >= 5:
        return 90
    elif grade > 50 and project >= 2:
        return 75
    else:
        return 0
print(final_grade(100, 12))
    

# welcome
def greet(language):
    # your code here
    lang = [ ("english", "Welcome")
            , ("czech", "Vitejte")
            , ("danish", "Velkomst")
            , ("dutch", "Welkom")
            , ("estonian", "Tere tulemast")
            , ("finnish", "Tervetuloa")
            , ("flemish", "Welgekomen")
            , ("french", "Bienvenue")
            , ("german", "Willkommen")
            , ("irish", "Failte")
            , ("italian", "Benvenuto")
            , ("latvian", "Gaidits")
            , ("lithuanian", "Laukiamas")
            , ("polish", "Witamy")
            , ("spanish", "Bienvenido")
            , ("swedish", "Valkommen")
            , ("welsh", "Croeso")
            ]
    
    for l in lang:
        if l[0] == language:
            return l[1]
    return "Welcome"
print(greet('Welcome'))


# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# For example, the score of abad is 8 (1 + 2 + 1 + 4).
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.

def high(x):
    words = x.split()
    highest_score = 0
    highest_word = ""
    
    for word in words:
        current_score = 0
        for char in word:
            current_score += ord(char) - 96
            
        if current_score > highest_score:
            highest_score = current_score
            highest_word = word
    return highest_score
print(high('abad'))

# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like 
"""Who likes it?"""
def likes(names):
    # your code here
    if not names:
        return "no one likes this"

    like = 0
    for name in names:
        if len(names) == 1:
            return f'{name} likes this'

        elif len(names) == 2:
            return f'{name} and {names[1]} like this'

        elif len(names) == 3:
            return f'{name}, {names[1]} and {names[2]} like this'

        elif len(names) >= 4:
            like += 1
            return f'{name}, {names[1]} and {len(names) -2} others like this'
    # return like
# print(likes(["Peter", 'alex']))
print(likes(["Max", 'John', 'Mark', 'Aayush', 'Rizan']))


def do_this():
    print('Doing this')

def do_that():
    print('Doing that')

match input('Do this or that?'):
    case 'this':
        do_this()
    case 'that':
        do_that()
    case _:
        print('Invalid input!')