#!/usr/bin/python3


def fizz():
     for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif numb % 3 == 0:
            print("Fizz ", end="")
        elif numb % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(numb), end="")
