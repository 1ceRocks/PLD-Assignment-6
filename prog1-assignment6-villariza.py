# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

# Program inception for the clarification of this system program.
print("\nIn this \033[34;1mPython\033[0m \033[1m3.0\033[0m \033[33;1mLanguage\033[0m, the program will identify the inputted digits or values from \033[32;1m\x1B[ascending to descending order\x1B[0m between the \033[32;1mfour (4) statements\033[0m enclosed on a square bracket.")

# Informing the user that float string numericals (with decimal places and digits) are supported.
print("\n\033[32;1mFLOAT STRING Numericals\033[0m are supported.")

# Manual if-elif clause conditions are programmed in a named variable in a def function.
def top_number(quan1, quan2, quan3, quan4):
    """
    Statistics and Probability: Number Combinations (4) = 4! (Four Factorial) = 4 x 3 x 2 x 1 = 24 POSSIBLE ANSWERS
    """
    if quan1 >= quan2 and quan1 >= quan3 and quan1 >= quan4:
        if quan2 >= quan3 and quan2 >= quan4:
            if quan3 >= quan4:
                #1 Satisfied = Quan1, Quan2, Quan3, Quan4
                order_num = [quan1, quan2, quan3, quan4]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan4 >= quan3:
                #2 Satisfied = Quan1, Quan2, Quan4, Quan3
                order_num = [quan1, quan2, quan4, quan3]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
        elif quan3 >= quan2 and quan3 >= quan4:
            if quan2 >= quan4:
                #3 Satisfied = Quan1, Quan3, Quan2, Quan4
                order_num = [quan1, quan3, quan2, quan4]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan4 >= quan2:
                #4 Satisfied = Quan1, Quan3, Quan4, Quan2
                order_num = [quan1, quan3, quan4, quan2]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
        elif quan4 >= quan2 and quan4 >= quan3:
            if quan3 >= quan2:
                #5 Satisfied = Quan1, Quan4, Quan3, Quan2
                order_num = [quan1, quan4, quan3, quan2]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan2 >= quan3:
                #6 Satisfied = Quan1, Quan4, Quan2, Quan3
                order_num = [quan1, quan4, quan2, quan3]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
    elif quan2 >= quan1 and quan2 >= quan3 and quan2 >= quan4:
        if quan1 >= quan3 and quan1 >= quan4:
            if quan3 >= quan4:
                #7 Satisfied = Quan2, Quan1, Quan3, Quan4
                order_num = [quan2, quan1, quan3, quan4]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan4 >= quan3:
                #8 Satisfied = Quan2, Quan1, Quan4, Quan3
                order_num = [quan2, quan1, quan4, quan3]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
        elif quan3 >= quan1 and quan3 >= quan4:
            if quan1 >= quan4:
                #9 Satisfied = Quan2, Quan3, Quan1, Quan4
                order_num = [quan2, quan3, quan1, quan4]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan4 >= quan1:
                #10 Satisfied = Quan2, Quan3, Quan4, Quan1
                order_num = [quan2, quan3, quan4, quan1]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
        elif quan4 >= quan1 and quan4 >= quan3:
            if quan1 >= quan3:
                #11 Satisfied = Quan2, Quan4, Quan1, Quan3
                order_num = [quan2, quan4, quan1, quan3]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan3 >= quan1:
                #12 Satisfied = Quan2, Quan4, Quan3, Quan1
                order_num = [quan2, quan4, quan3, quan1]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
    elif quan3 >= quan1 and quan3 >= quan2 and quan3 >= quan4:
        if quan1 >= quan2 and quan1 >= quan4:
            if quan2 >= quan4:
                #13 Satisfied = Quan3, Quan1, Quan2, Quan4
                order_num = [quan3, quan1, quan2, quan4]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan4 >= quan2:
                #14 Satisfied = Quan3, Quan1, Quan4, Quan2
                order_num = [quan3, quan1, quan4, quan2]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
        elif quan2 >= quan1 and quan2 >= quan4:
            if quan1 >= quan4:
                #15 Satisfied = Quan3, Quan2, Quan1, Quan4
                order_num = [quan3, quan2, quan1, quan4]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[ascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan4 >= quan1:
                #16 Satisfied = Quan3, Quan2, Quan4, Quan1
                order_num = [quan3, quan2, quan4, quan1]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
        elif quan4 >= quan1 and quan4 >= quan2:
            if quan1 >= quan2:
                #17 Satisfied = Quan3, Quan4, Quan1, Quan2
                order_num = [quan3, quan4, quan1, quan2]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan2 >= quan1:
                #18 Satisfied = Quan3, Quan4, Quan2, Quan1
                order_num = [quan3, quan4, quan2, quan1]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
    elif quan4 >= quan1 and quan4 >= quan2 and quan4 >= quan3:
        if quan1 >= quan2 and quan1 >= quan3:
            if quan2 >= quan3:
                #19 Satisfied = Quan4, Quan1, Quan2, Quan3
                order_num = [quan4, quan1, quan2, quan3]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan3 >= quan2:
                #20 Satisfied = Quan4, Quan1, Quan3, Quan2
                order_num = [quan4, quan1, quan3, quan2]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
        elif quan2 >= quan1 and quan2 >= quan3:
            if quan1 >= quan3:
                #21 Satisfied = Quan4, Quan2, Quan1, Quan3
                order_num = [quan4, quan2, quan1, quan3]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan3 >= quan1:
                #22 Satisfied = Quan4, Quan2, Quan3, Quan1
                order_num = [quan4, quan2, quan3, quan1]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
        elif quan3 >= quan1 and quan3 >= quan2:
            if quan1 >= quan2:
                #23 Satisfied = Quan4, Quan3, Quan1, Quan2
                order_num = [quan4, quan3, quan1, quan2]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan2 >= quan1:
                #24 Satisfied = Quan4, Quan3, Quan2, Quan1
                order_num = [quan4, quan3, quan2, quan1]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")         

# Included the try and except function for a detailed input of a detected program error.
try:
    """
    Whenever a user inputs an alphabetical/alphanumeric in the string, it will automatically direct into the except function program.
    """
    num1 = float(input("\nEnter the \33[36;1mFIRST (1ST)\33[0m number here. \n\033[32;1m>>> "))
    num2 = float(input("\n\033[0mEnter the \33[36;1mSECOND (2ND)\33[0m number here. \n\033[32;1m>>> "))
    num3 = float(input("\n\033[0mEnter the \33[36;1mTHIRD (3RD)\33[0m number here. \n\033[32;1m>>> "))
    num4 = float(input("\n\033[0mEnter the \33[36;1mFOURTH (4TH)\33[0m number here. \n\033[32;1m>>> "))
    top_number(num1, num2, num3, num4)
# ValueError entails an inappropriate argument value (of correct type) so that it is utilized.
except ValueError as alpha:
    """
    Variable alpha is used to store the ValueError in except function followed by a print statement.
    """
    print(f"\n\033[0mInvalid user input. \33[36;1m{alpha}\33[0m\n")