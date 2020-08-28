# Problem 1
from math import hypot

def pythagoreanTheorem(length_a, length_b):
    return hypot(length_a, length_b)


print("Problem 1")
print(pythagoreanTheorem(2, 2))
print(pythagoreanTheorem(3, 2))
print(pythagoreanTheorem(2, 4))


# Problem 2
def list_mangler(list_in):
    list_out = []
    
    for item in list_in:
        # even
        if (item % 2 == 0):            
            list_out.append(item * 2)
        # odd
        else:
            list_out.append(item * 3)

    return list_out
    

print("\nProblem 2")
print(list_mangler([1, 2, 3, 4]))
print(list_mangler([5, 6, 7, 8]))
print(list_mangler([9, 10, 11, 110, 111]))


# Problem 3
from statistics import mean

def grade_calc(grades_in, to_drop):
    # leave original list unmodified
    grades_out = grades_in.copy()
    
    # sort and drop lowest `to_drop`
    grades_out.sort()
    
    for iter in range(to_drop):
        grades_out.pop(0)

    # calc avg of modified list
    avg = mean(grades_out)
    
    # give letter grade 
    if (100 >= avg >= 90):
        return 'A'
    
    elif (89 >= avg >= 80):
        return 'B'

    elif (79 >= avg >= 70):
        return 'C'

    elif (69 >= avg >= 60):
        return 'D'

    else:
        return 'F'

    
print("\nProblem 3")
print(grade_calc([100, 90, 80, 95], 2))
print(grade_calc([0, 90, 80, 95], 2))
print(grade_calc([70, 100, 60, 50], 2))


# Problem 4
def odd_even_filter(numbers):
    # separate odd and even
    even = []
    odd = []

    for num in numbers:
        if (num % 2 == 0):
            even.append(num)
            
        else:
            odd.append(num)

    return [even, odd]


print("\nProblem 4")
print(odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(odd_even_filter([3, 9, 43, 7]))
print(odd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56]))
