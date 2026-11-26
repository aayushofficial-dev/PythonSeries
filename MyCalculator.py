while True:
    print('Welcome to MyCalculator...')
    print('2. Subtraction')
    print('1. Addition')
    print('3. Multiplicaton')
    print('4. Division')
    print('5. Exit')

    choice = input('Enter your choice(1-5):')

    a = int(input('Enter the first number:'))
    b = int(input('Enter the second number:'))

    if choice == '1':
        print(f'The addition of {a} and {b} is: {a + b}')

    elif choice == '2':
        print(f'The subtraction of {a} and {b} is: {a - b}')

    elif choice == '3':
        print(f'The multiplication of {a} and {b} is: {a * b}')

    elif choice == '4':
        if b == 0:
            print('Number cannot be divided by Zero.')
        else:
            print(f'The division of {a} and {b} is: {a / b}')

    elif choice == '5':
        print('Thank you for using MyCalculator!')
        break

    else:
        print('Invalid syntax!')