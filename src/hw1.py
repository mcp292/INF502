from math import hypot

# Problem 1
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

'''
**3. Write a function with the following signature:** `grade_calc(grades_in, to_drop)`.

The function accepts a list `grades_in` containing integer grades, drops the `to_drop` lowest grades (so, for to_drop equal to 2, the function should drop the 2 lowest grades), calculates the average of the grades left, and returns the letter grade this average corresponds to according to the letter grade scale for this course.

For example:

```
>>> grade_calc([100, 90, 80, 95], 2)
'A'
```

Present a short (no more than a couple of sentences) description of your solution approach. Then show your source code and the  output of three example runs.
'''

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
