# cython test

cpdef int loop_to(int x):
    cdef float y = 1
    for i in range(1, x+1):
        y *= i

cpdef void run(int count_test, int number):
    for i in range(count_test):
        loop_to(number)
