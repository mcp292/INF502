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


# ----
# all in one file for easier grading

# using class like c struct
class seq_c:
    seq_name = None
    seq_num = None
    seq = None


def prompt_user_shifts():
    global MAX_SHIFTS

    shifts = input("Enter max number of shifts to test (no entry = default, default = 5): ")

    # check for default
    if (shifts == ''):
        shifts = MAX_SHIFTS

    return int(shifts)


def prompt_user_first_seq():
    # TODO: in C I would have one prompt function and pass in pointers,
    # how do I do this in python?
    return int(input("First sequence (1-5): "))


def prompt_user_second_seq():
    return int(input("Second sequence (1-5): "))


def prompt_user_seq(seq_c):
    seq_c.seq_num = int(input("{} sequence (1-5): ".format(seq_c.seq_name)))
    

def compare_seq(first_seq, second_seq, shifts):
    # TODO: only print max shift,
    # can have max list and only run prints and scores on those mixes
    
    check_len(first_seq, second_seq)  # chicken?

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
        

def check_len(first_seq, second_seq):
    if (len(first_seq) != len(second_seq)):
        print("Lengths do not match!\n\nTerminating program...\n")
        exit()


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

# "allocate struct"
first_seq = seq_c()
second_seq = seq_c()

first_seq.name = "First"
second_seq.name = "Second"

# prompt user for shifts
shifts = prompt_user_shifts()

# prompt user for filenames
prompt_user_seq(first_seq)
prompt_user_seq(second_seq)

# TODO: consider making file stuff another struct
# create filenames from user input
fn_first_seq = "../pa1_input/seq{}.txt".format(first_seq.seq_num)
fn_second_seq = "../pa1_input/seq{}.txt".format(second_seq.seq_num)
print()

# upload files
# open
try:
    f_first_seq = open(fn_first_seq, "r")
    f_second_seq = open(fn_second_seq, "r")
except FileNotFoundError:
    print("Invalid sequence (file not found)!\n\nTerminating program...\n")
    exit()
    
# read
first_seq.seq = f_first_seq.read().strip()
second_seq.seq = f_second_seq.read().strip()

# compare sequences and print results
compare_seq(first_seq.seq, second_seq.seq, shifts)

# close files
f_first_seq.close()
f_second_seq.close()
