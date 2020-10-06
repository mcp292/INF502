# all in one file for easier grading

# using class like c struct
class Seq:
    name = None
    num = None
    seq = None


# used to store config that gives highest score    
class MaxScoreConfig:
    first_seq = None
    second_seq = None
    shift_first = None
    num_shifts = None
    score = None

    def __init__(self):
        self.score = 0

        
    def update(self, first_seq, second_seq, shift_first, num_shifts, score):
        self.first_seq = first_seq
        self.second_seq = second_seq
        self.shift_first = shift_first
        self.num_shifts = num_shifts
        self.score = score
    

def prompt_user_mode():
    global DEFAULT_MODE

    mode = input("Enter mode (0 = match, 1 = contiguous, default = match): ")

    # check for default
    if (mode == ''):
        mode = DEFAULT_MODE


    return int(mode)


def prompt_user_max_shifts():
    global DEFAULT_MAX_SHIFTS

    max_shifts = input("Enter max number of shifts to test (no entry = default, default = 5): ")

    # check for default
    if (max_shifts == ''):
        max_shifts = DEFAULT_MAX_SHIFTS

    return int(max_shifts)


def prompt_user_seq(Seq):
    Seq.num = int(input("{} sequence (1-5): ".format(Seq.name)))
    

# TODO: break up both compares into into helper functions and reverse params
def compare_seq_match(first_seq, second_seq, max_shifts):
    max_score_config = MaxScoreConfig()
    
    check_len(first_seq, second_seq)  # chicken?

    # shift first
    shift_first = True
    
    # inclusive
    for num_shifts in range(max_shifts + 1):
        score = 0
        ind = 0
        
        while ind + num_shifts < len(first_seq.seq):
            if (first_seq.seq[ind] == second_seq.seq[ind + num_shifts]):            
                score += 1

                # update max score config
                if (score > max_score_config.score):
                    max_score_config.update(first_seq, second_seq, shift_first,
                                          num_shifts, score)

            # update
            ind += 1

    # shift second
    shift_first = False

    # inclusive
    for num_shifts in range(max_shifts + 1):
        score = 0
        ind = 0
        
        while ind + num_shifts < len(first_seq.seq):
            if (first_seq.seq[ind + num_shifts] == second_seq.seq[ind]):
                score += 1

                # update max score config
                if (score > max_score_config.score):
                    max_score_config.update(first_seq, second_seq, shift_first,
                                          num_shifts, score)

            # update
            ind += 1

    print_result(max_score_config)


def compare_seq_contig(first_seq, second_seq, max_shifts):
    max_score_config = MaxScoreConfig()
    
    check_len(first_seq, second_seq)

    # shift first
    shift_first = True
    
    # inclusive
    for num_shifts in range(max_shifts + 1):
        score = 0
        ind = 0
        
        while ind + num_shifts < len(first_seq.seq):
            if (first_seq.seq[ind] == second_seq.seq[ind + num_shifts]):            
                score += 1
                
                # update max score config
                if (score > max_score_config.score):
                    max_score_config.update(first_seq, second_seq, shift_first,
                                          num_shifts, score)

            else:
                score = 0

            # update
            ind += 1

    # shift second
    shift_first = False
    
    # inclusive
    for num_shifts in range(max_shifts + 1):
        score = 0
        ind = 0
        
        while ind + num_shifts < len(first_seq.seq):
            if (first_seq.seq[ind + num_shifts] == second_seq.seq[ind]):
                score += 1
                
                # update max score config
                if (score > max_score_config.score):
                    max_score_config.update(first_seq, second_seq, shift_first,
                                          num_shifts, score)

            else:
                score = 0
                
            # update
            ind += 1

    print_result(max_score_config)


def check_len(first_seq, second_seq):
    if (len(first_seq.seq) != len(second_seq.seq)):
        print("Lengths do not match!\n\nTerminating program...\n")
        exit()


def print_result(first_seq, second_seq, shift_first, num_shifts, score):
    shift_str = build_shift_str(num_shifts)

    # create title and insert spacers
    if (shift_first):
        title = "Shifting first sequence by {}".format(num_shifts)

        first_output_str = shift_str + first_seq.seq
        second_output_str = second_seq.seq + shift_str
    else:
        title = "Shifting second sequence by {}".format(num_shifts)

        first_output_str = first_seq.seq + shift_str
        second_output_str = shift_str + second_seq.seq

    print(title)
    print("Shifts          : {}".format(num_shifts))
    print("First Sequence  : {}".format(first_output_str))
    print("Second Sequence : {}".format(second_output_str))
    print("Score           : {}".format(score))
    print("-")
    print()

    
def print_result(max_score_config):
    shift_str = build_shift_str(max_score_config.num_shifts)

    # create title and insert spacers
    if (max_score_config.shift_first):
        title = "Shifting first sequence by {}".format(max_score_config.num_shifts)

        first_output_str = shift_str + max_score_config.first_seq.seq
        second_output_str = max_score_config.second_seq.seq + shift_str
    else:
        title = "Shifting second sequence by {}".format(max_score_config.num_shifts)

        first_output_str = max_score_config.first_seq.seq + shift_str
        second_output_str = shift_str + max_score_config.second_seq.seq

    print(title)
    print("Shifts          : {}".format(max_score_config.num_shifts))
    print("First Sequence  : {}".format(first_output_str))
    print("Second Sequence : {}".format(second_output_str))
    print("Score           : {}".format(max_score_config.score))
    print("-")
    print()

    
def build_shift_str(num_shifts):
    output = ""

    for shift in range(num_shifts):
        output += '-'

    return output


def check_valid_chars(str):
    global VALID_CHARS

    for char in str:
        if char not in VALID_CHARS:
            print("Sequence contains invalid chars!\n\nTerminating program...\n")
            exit()
            
        
# main()
VALID_CHARS = "AGCT"            # check if .upper() in string
DEFAULT_MAX_SHIFTS = 5

MODE_MATCH = 0
MODE_CONTIG = 1
DEFAULT_MODE = MODE_MATCH

# "allocate struct"
first_seq = Seq()
second_seq = Seq()

first_seq.name = "First"
second_seq.name = "Second"

try:
    # prompt user for mode 
    mode = prompt_user_mode()

    # prompt user for shifts
    max_shifts = prompt_user_max_shifts()

    # prompt user for filenames
    prompt_user_seq(first_seq)
    prompt_user_seq(second_seq)
except ValueError:
    print("Entry must be a number!\n\nTerminating program...\n")
    exit()

# create filenames from user input
fn_first_seq = "../pa1_input/seq{}.txt".format(first_seq.num)
fn_second_seq = "../pa1_input/seq{}.txt".format(second_seq.num)
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

# check that sequences are valid
check_valid_chars(first_seq.seq)
check_valid_chars(second_seq.seq)

# compare sequences and print results
if (mode == MODE_MATCH):
    compare_seq_match(first_seq, second_seq, max_shifts)
elif (mode == MODE_CONTIG):
    compare_seq_contig(first_seq, second_seq, max_shifts)
else:
    print("Mode not recognized")        

# close files
f_first_seq.close()
f_second_seq.close()
