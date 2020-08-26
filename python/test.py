# python test
# loop test

__author__ = 'd4rk3r'

def loop_to(x):
    y = 1.0
    for i in range(1, x+1):
        y *= i

def run(count_test, number):
    for i in range(count_test):
        loop_to(number)
