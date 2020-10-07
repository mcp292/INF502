'''
Create a function that receives the dictionary and the name of a mountain, and removes it (please treat the exception triggered when a mountain is not found)

Create a function to list the top 2 mountains

run each func and show result

go back and add exceptions to each prob
'''


def print_data(dict):
    print("List data:")

    for key in dict:
        print("{} is {} m tall!".format(key, dict[key]))

    print("-\n")


def rm_data(dict, key):
    print("Remove {}:".format(key))
    
    try:
        del dict[key]
    except KeyError:
        print("Key not found in dict")
    else:
        print("{} removed!".format(key))

    print("-\n")
    

def list_highest_2(dict):
    print("List tallest two mountains:")
    
    dict_cp = dict.copy() # don't alter data

    for iter in range(2):
        max_key = max(dict_cp)
        print(max_key)

        del dict_cp[max_key]

    print("-\n")
       
    
mount_dict = {"Mount Everest": 8848,
              "K2": 8611,
              "Broad Peak": 8051,
              "Rakaposhi": 7788,
              "Nuptse": 7864}


print_data(mount_dict)

rm_data(mount_dict, "K2")
rm_data(mount_dict, "K4")

print_data(mount_dict)

list_highest_2(mount_dict)
