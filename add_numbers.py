#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: April 2021
# This program add numbers

def main():
    print("Type two numbers to add:")

    number1 = float(input())
    number2 = float(input())
    result = number1 + number2

    print("\n{0} + {1} = {2}".format(number1, number2, result))
    print("\nDone.")


if __name__ == "__main__":
    main()
