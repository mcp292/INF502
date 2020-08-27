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


# For example:
# alt way is interesting but hurts my head
# ```
# >>> list_mangler([1, 2, 3, 4])
# [3, 4, 9, 8]
# ```

# Present a short (no more than a couple of sentences) description of your solution approach. Show your source code and the output of three example runs.
