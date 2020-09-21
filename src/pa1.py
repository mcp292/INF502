# EXCEPTIONS
# FNF
# Invalid char
# Invalid user input
# Invalid length


# TASKS
# Number of matches: Your code must be able to calculate the maximum score and print the shifted strings in the output

# Maximum chain: Your code must be able to calculate the size of the maximum contiguous chain that matches the sequences (score) and the sequences that resulted on that score (shifted)

# User-input: Your program must collect from the user the following information: the maximum shift; the approach to be used (number of matches or maximum chain), the name of the input files (each sequence needs to be provided inside of a file)

# File input: Your code must use file input to read the DNA sequences (one sequence per file)

# Exception handling: Your code must handle all exception types raised, and do so by accounting for specific exception types (in other words, no except: or except Exception: clauses).

# Important: the sequences must have the same length.

# Might need to shift both! dam. Then check high score and config?

# How to keep track of highest config above
# ----

def prompt_user_shifts():
    global MAX_SHIFTS

    shifts = input("Enter max number of shifts to test (no entry = default, default = 5): ")

    # check for default
    if (shifts == ''):
        shifts = MAX_SHIFTS

    return int(shifts)


def prompt_user_first_seq():
    # TODO: error check
    # TODO: should I make boolean and one func?
    return int(input("First sequence (1-5): "))


def prompt_user_second_seq():
    return int(input("Second sequence (1-5): "))


def compare_seq(first_seq, second_seq, shifts):
# TODO: refactor to big while loop
# TODO: check if same size or throw execption (pass to func)
# TODO: bring in here so I can call shift first


    # shift first
    # inclusive
    for shift in range(shifts + 1):
        score = 0
        ind = 0
        
        while ind + shift < len(first_seq):
            if (first_seq[ind] == second_seq[ind + shift]):            
                score += 1

            # update
            ind += 1

        print_result(first_seq, second_seq, True, shift, score)

    # shift second
    # inclusive
    for shift in range(shifts + 1):
        score = 0
        ind = 0
        
        while ind + shift < len(first_seq):
            if (first_seq[ind + shift] == second_seq[ind]):
                score += 1

            # update
            ind += 1

        print_result(first_seq, second_seq, False, shift, score)
        
        
def print_result(first_seq, second_seq, shift_first, shifts, score):
    shift_str = build_shift_str(shifts)

    # create title and insert spacers
    if (shift_first):
        title = "Shifting first sequence by {}".format(shifts)

        first_seq = shift_str + first_seq
        second_seq = second_seq + shift_str
    else:
        title = "Shifting second sequence by {}".format(shifts)
        first_seq = first_seq + shift_str
        second_seq = shift_str + second_seq

    print(title)
    print("Shifts          : {}".format(shifts))
    print("First Sequence  : {}".format(first_seq))
    print("Second Sequence : {}".format(second_seq))
    print("Score           : {}".format(score))
    print("-")
    print()

def build_shift_str(shifts):
    output = ""

    for shift in range(shifts):
        output += '-'

    return output

        
# ----


# main()
VALID_CHARS = "AGCT"            # check if .upper() in string
MAX_SHIFTS = 5

# prompt user for shifts
shifts = prompt_user_shifts()

# prompt user for filenames
fn_first_seq = "../pa1_input/seq{}.txt".format(prompt_user_first_seq())
fn_second_seq = "../pa1_input/seq{}.txt".format(prompt_user_second_seq())
print()

# upload files
# open
f_first_seq = open(fn_first_seq, "r")
f_second_seq = open(fn_second_seq, "r")

# read
first_seq = f_first_seq.read().strip()
second_seq = f_second_seq.read().strip()

# compare sequences and print results
compare_seq(first_seq, second_seq, shifts)

# close files
f_first_seq.close()
f_second_seq.close()
