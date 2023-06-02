###
# Python Debugging Exercise
# Author: Nam Jun Lee
# Date: Sept 3nd, 2021
###

# Identify compile or run-time errors and correct them
def main():
    func_a(122, '10')
    func_b('cpts')


# 1. resolve compilation errors on the function
def func_a(a, b):
    x = a
    y = int(b)
    print(x + y)


# 2. Complete the function definition based on the comments
def func_b(s):
    result = s + '_' + '215'
    print(result)

    # concatenate '_' and '215' to variable 's' and assign it to a variable 'result'

    # print 'result' elements separated with a space. It is ok to have a space after the last element.
    c = len(result)
    i = 0
    for x in range(0, c):
        print(result[i], end=' ')
        i = i + 1
    print()


main()
