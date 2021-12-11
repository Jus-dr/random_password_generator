import random
import string

#LISTS OF LOWERCASES,UPPERCASES,DIGITS,PUNCTUATIONS#

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
main_list = lower + upper + num + symbols

#RANDOM PASSWORD MAIN CODE#
want_continue = "y"
while want_continue in ["y","Y"]:
    print("-"*100)
    input_difficulty = input("Please enter a difficulty (e/E = Easy , m/M = Medium , h/H = Hard) : ")
    print("-"*100)
    while input_difficulty not in ["e","E","m","M","h","H"]:
        print("Wrong enter please try again")
        print("-"*100)
        input_difficulty = input("Please enter a difficulty (e/E = Easy , m/M = Medium , h/H = Hard) : ")
        print("-"*100)

    if input_difficulty in ["e","E"]:
        print("Easy difficulty selected") #EASY DIFFICULTY'S LONG IS 8#
        print("-"*100)
        password = "".join(random.sample(main_list,8))
        print(f"Your password : {password}")
        print("-"*100)
        
    if input_difficulty in ["m","M"]:
        print("Medium difficulty selected") #MEDIUM DIFFICULTY'S LONG IS 12#
        print("-"*100)
        password = "".join(random.sample(main_list,12))
        print(f"Your password : {password}")
        print("-"*100)

    if input_difficulty in ["h","H"]:
        print("Hard difficulty selected") #HARD DIFFICULTY'S LONG IS 16#
        print("-"*100)
        password = "".join(random.sample(main_list,16))
        print(f"Your password : {password}")
        print("-"*100)

    
    want_continue = input("Do you want continue (y/Y = Yes , n/N = No) : ")
    print("-"*100)
    while want_continue not in ["y","Y","n","N"]:
        print("Wrong enter please try again")
        print("-"*100)
        want_continue = input("Do you want continue (y/Y = Yes , n/N = No) : ")