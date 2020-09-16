'''
The Periodic Table of the Elements was developed to organize information about the elements that make up the Universe. Write a terminal application that lets you enter information about each element in the periodic table. Make sure you include the following information:

    symbol, name, atomic number, row, and column

Provide a menu of options for users (inputing numbers) to:

    See all the information that is stored about any element, by entering that element's symbol.
    Choose a property, and see that property for each element in the table.
    Enter a new element
    Change the attributes of an element, by entering the element's symbol.
    Exit the program

You can provide a pre-populated dictionary as part of your program, avoiding the need of typing every time
'''

def prompt_mode():
    print("1. Get info on element")
    print("2. Get property info for all elements")
    print("3. Insert new element")
    print("4. Edit element")
    print()
    print("-9. Exit program")
    print()

    mode = int(input("Enter mode number: "))
    print()
    
    return mode


def mode_1(ptable):
    print("1. Get info on element")
    print()

    print("Elements:")
    for symbol in ptable:
        print(symbol)
    print()

    key = input("Enter element symbol: ").capitalize()
    print()

    info = ptable.get(key)

    if (info != None):
        print("Symbol       : {}".format(key))
        print("Name         : {}".format(info.get("name")))
        print("Atomic Number: {}".format(info.get("atomic number")))
        print("Row          : {}".format(info.get("row")))
        print("Column       : {}".format(info.get("col")))
    else:
        print("Element not found!\nConsider adding it yourself!")


def mode_2(ptable):
    print("2. Get property info for all elements")
    print()

    print("Properties:")
    print("1. Symbol")
    print("2. Name")
    print("3. Atomic number")
    print("4. Row")
    print("5. Column")
    print()

    property = int(input("Enter property number: "))
    print()
    
    if (property == 1):
        print("Symbols:")
        for symbol in ptable:
            print(symbol)
    elif (property == 2):
        print("Names:")
        for key in ptable:
            print(ptable.get(key).get("name"))
    elif (property == 3):
        print("Atomic Numbers:")
        for key in ptable:
            print(ptable.get(key).get("atomic number"))
    elif (property == 4):
        print("Rows:")
        for key in ptable:
            print(ptable.get(key).get("row"))
    elif (property == 5):
        print("Columns:")
        for key in ptable:
            print(ptable.get(key).get("col"))
    else:
        print("Invalid entry")
        

def mode_3(ptable):
    print("3. Insert new element")
    print()

    key = input("Enter symbol: ").capitalize()
    name = input("Enter name: ").capitalize()
    atomic_num = input("Enter atomic number: ")
    row = input("Enter row: ")
    col = input("Enter column: ")
    print()

    ptable[key] = {"name": name,
                   "atomic number": atomic_num,
                   "row": row,
                   "col": col}
    

def mode_4(ptable):
    print("4. Edit element")
    print()

    print("Elements:")
    for symbol in ptable:
        print(symbol)
    print()
    
    key = input("Enter element symbol: ").capitalize()
    print()

    if (key in ptable):
        name = input("Enter new name: ").capitalize()
        atomic_num = input("Enter new atomic number: ")
        row = input("Enter new row: ")
        col = input("Enter new column: ")
        print()

        ptable[key] = {"name": name,
                       "atomic number": atomic_num,
                       "row": row,
                       "col": col}
    else:
        print("Invalid key")


# main()
ptable = {"H":
          {"name": "Hydrogen",
           "atomic number": "1",
           "row": "1",
           "col": "1"},

          "Cs":
          {"name": "Caesium",
           "atomic number": "55",
           "row": "6",
           "col": "1"},

          "Ru":
          {"name": "Ruthenium",
           "atomic number": "44",
           "row": "5",
           "col": "8"}}

mode = 0

while (mode != -9):
    mode = prompt_mode()

    if (mode == 1):
        mode_1(ptable)

    if (mode == 2):
        mode_2(ptable)

    if (mode == 3):
        mode_3(ptable)

    if (mode == 4):
        mode_4(ptable)

    if (mode == 5):
        mode_5(ptable)
    
    print("----")
    print()    
