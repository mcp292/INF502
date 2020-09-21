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

def prompt_user():
    global MAX_SHIFTS

    shifts = input("Enter max number of shifts to test (no entry = default, default = 5): ")

    # check for default
    if (shifts == ''):
        shifts = MAX_SHIFTS

    return int(shifts)


def compare_seq(this_seq, that_seq, shifts):
# TODO: refactor to big while loop
# TODO: check if same size or throw execption (pass to func)
    
    # inclusive
    for shift in range(shifts + 1):
        score = 0
        ind = 0
        
        while ind + shift < len(this_seq):
            if (this_seq[ind] == that_seq[ind + shift]):
                # diagnostic
                print(this_seq[ind], that_seq[ind + shift], score, range(len(this_seq)), this_seq[9])
                # diagnostic
                
                score += 1

            # update
            ind += 1

        print(score)        
            


        for ind in range(len(this_seq)):
            if (this_seq[ind + shift] == that_seq[ind]):
                print(this_seq[ind + shift], that_seq[ind], score, range(len(this_seq)), this_seq[9])
                score += 1

        print(score)        

    


# main()
VALID_CHARS = "AGCT"            # check if .upper() in string

MAX_SHIFTS = 5

# upload from file
f_seq1 = open("../pa1_input/seq1.txt", "r")
f_seq2 = open("../pa1_input/seq2.txt", "r")
f_seq3 = open("../pa1_input/seq3.txt", "r")
f_seq4 = open("../pa1_input/seq4.txt", "r")
f_seq5 = open("../pa1_input/seq5.txt", "r")

seq1 = f_seq1.read().strip()
seq2 = f_seq2.read().strip()
seq3 = f_seq3.read().strip()
seq4 = f_seq4.read().strip()
seq5 = f_seq5.read().strip()

# prompt user for shifts
shifts = prompt_user()

#print(shifts)

# compare sequences and print results
compare_seq(shifts)





# Run comparison and show each combo
# Shifts :
# Seq 1  :
# Seq 2  :
# Score  : 

# pretty print include dashes

# close files
f_seq1.close()
f_seq2.close()
f_seq3.close()
f_seq4.close()
f_seq5.close()
