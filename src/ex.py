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

# main()
VALID_CHARS = "AGCT"            # check if .upper() in string

# upload from file
f_seq1 = open("../pa1_input/seq1.txt", "r")
f_seq2 = open("../pa1_input/seq2.txt", "r")
f_seq3 = open("../pa1_input/seq3.txt", "r")
f_seq4 = open("../pa1_input/seq4.txt", "r")
f_seq5 = open("../pa1_input/seq5.txt", "r")

seq1 = f_seq1.read()
seq2 = f_seq2.read()
seq3 = f_seq3.read()
seq4 = f_seq4.read()
seq5 = f_seq5.read()

f_seq1.close()
f_seq2.close()
f_seq3.close()
f_seq4.close()
f_seq5.close()



# user can specify max or choose to let algo decide (5). Try all combos up to number entered.

# Run comparison and show each combo
# Shifts :
# Seq 2  :
# Seq 2  :
# Score  : 

# pretty print include dashes
