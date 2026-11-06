# print('Calculator by Aayush....')
# print('1. Addition')
# print('2. Subraction')
# print('3. Multiplication')
# print('4. Division')
# print('5. Exit')

# while True:
#     a = int(input('enter the first number:'))
#     b = int(input('enter the secone one:'))

#     choice = input('Enter the choice:')

#     if choice == '1':
#         print(f'The addition of {a} and {b} is {a + b}')
#     elif choice == '2':
#         print(f'The subraction of {a} and {b} is {a - b}')
#     elif choice == '3':
#         print(f'The multiplication of {a} and {b} is {a * b}')
#     elif choice == '4':
#         if b == 0:
#             print('number cannot be divided by zero.')
#             break
#         else:
#             print(f'The division of {a} and {b} is {a / b}')
#     elif choice == '5':
#         print('Thank you for using the program')
#         break
#     else:
#         print('Invalid syntax!')


def add():
    return a + b

def sub():
    return a - b

def mul():
    return a * b

def div():
    return a / b

def multiplication():
    num = int(input('Enter the number:'))
    for i in range(1, 11):
        print(f'{num} * {i} = {num * i}')
    return num

print('Calculator by Aayush....')
print('1. Addition')
print('2. Subraction')
print('3. Multiplication')
print('4. Division')
print('5. Multiplication table')
print('6. Exit')

while True:
    a = int(input('Enter the first number:'))
    b = int(input('Enter the second number:'))

    choice = input('Enter your choice:')

    if choice == '1':
        print(add())

    elif choice == '2':
        print(sub())

    elif choice == '3':
        print(mul())

    elif choice == '4':
        if b == 0:
            print('Number cannot be divided by zero.')
            break
        else:
            print(div())

    elif choice == '5':
        print(multiplication())

    elif choice == '6':
        print('Thank you for using the program.')
        break
    else:
        print('Invalid syntax!')