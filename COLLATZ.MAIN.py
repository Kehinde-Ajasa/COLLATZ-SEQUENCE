# THIS code is used for the collatz sequence
import itertools

try:
    number = int(input("Enter the number to check the collatz sequence: "))
    print(number)


    def collatz(my_number):
        """function that returns calculations done on the number based on if it is even or odd"""
        if my_number % 2 == 0:
            return my_number // 2
        elif my_number % 2 != 0:
            return (my_number * 3) + 1
    count = itertools.count()
    while number != 1:
        counter = (next(count))
        number = collatz(number)
        print(number)
    print(f'The sequence has  {counter + 2} characters')
    print(collatz(my_number))
except NameError:
    print('')
