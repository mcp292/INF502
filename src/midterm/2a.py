'''
Approach: I knew I had to run a for loop it range of the entered number to print 
the asterisks. The hard part was converting user input to a list of integers. 
I found out a good use for list comprehension, which made the code a one liner.
'''

nums = input("Enter 5 comma separated numbers between 1 and 20: ").split(",")

# convert list of strings to list of ints
try:
    nums = [int(num) for num in nums] # list comprehension
except ValueError:
    print("\nEntry must be a number!\nTerminating program...\n")
    exit()

for num in nums:
    if (num <= 20):              
        for iter in range(num):
            print("*", end='')

        print()

    else:
        print("Number out of range! {}".format(num))
