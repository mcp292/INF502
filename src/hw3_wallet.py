'''
You are requested to request a user of your application to provide 5 numbers representing the value in cash stored in 5 different wallets. Your program should store these five values in a list. When finished, your application should provide the following information:

    "The fattest wallet has $ value in it."
    "The skinniest wallet has $ value in it."
    "All together, these wallets have $ value in them."
    "All together, the total value of these wallets is worth $ dimes"

Please try to think about different functions to complete your work
'''

from math import ceil

def prompt_user(wallets):
    wallets.append(float(input("Money in wallet 1: ")))
    wallets.append(float(input("Money in wallet 2: ")))
    wallets.append(float(input("Money in wallet 3: ")))
    wallets.append(float(input("Money in wallet 4: ")))
    wallets.append(float(input("Money in wallet 5: ")))

    
def get_fattest(wallets):
    return max(wallets)


def get_skinniest(wallets):
    return min(wallets)
    

def get_total(wallets):
    return sum(wallets)


def get_total_dimes(wallets):
    return ceil(get_total(wallets) / 0.10)


def report_fattest(fattest):
    print("The fattest wallet has ${:,.2f} in it.".format(fattest))


def report_skinniest(skinniest):
    print("The skinniest wallet has ${:,.2f} in it.".format(skinniest))


def report_total(total):
    print("All together, these wallets have ${:,.2f} in them.".format(total))


def report_total_dimes(total_dimes):
    print("All together, the total value of these wallets is worth {:,} dimes".format(total_dimes))


def nl():
    print()

    
# main()
wallets = []

# get 5 wallet amounts
prompt_user(wallets)

nl()

# report data
report_fattest(get_fattest(wallets))
report_skinniest(get_skinniest(wallets))

nl()

report_total(get_total(wallets))
report_total_dimes(get_total_dimes(wallets))

nl()
