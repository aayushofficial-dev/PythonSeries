# import keyword
# print('The list of keyword are:')
# print(keyword.kwlist)

a = [1, 2, 3, 4, 5]
a.append(6)
result = []
for i in a:
    total = i ** 2
    result.append(total)
print(result)

# # number guessing game
import random

number = random.randint(1, 21)
guesses = []

for i in range(1, 6):
    usr_input = int(input(f'guess the number. you have left with {i}/5 chances:'))
    guesses.append(usr_input)

    if usr_input > number:
        print('Your guess is too high.Try again!')
    elif usr_input < number:
        print('Your guess is too low.Try again!')
    elif usr_input == number:
        print(f'congratulations! you have guessed the number in {i} attempts.')
else:
    print(f'you are out of chances. The number was {number}')
    print(f'Your guessed number was {guesses}')


i = 'a'
try:
    if i == 1:
        print('hello')
except Exception as e:
    print('error', e)