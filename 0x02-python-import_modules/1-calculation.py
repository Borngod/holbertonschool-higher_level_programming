#!/usr/bin/python3
import calculator_1 as calc

if __name__ == '__main__':
    """

    Prints the result of the addition, substract, multiplication
    and division between two numbers

    """
    a = 10
    b = 5
    print('{:d} + {:d} = {:d}'.format(a, b, calc.add(a, b)))
    print('{:d} - {:d} = {:d}'.format(a, b, calc.sub(a, b)))
    print('{:d} * {:d} = {:d}'.format(a, b, calc.mul(a, b)))
    print('{:d} / {:d} = {:d}'.format(a, b, calc.div(a, b)))