def print_union(this_list, that_list):
    for num in this_list:
        if num in that_list:
            print(num, end=' ')

    print()


print_union([1, 2, 3, 4,], [3, 4, 5, 6])
    
