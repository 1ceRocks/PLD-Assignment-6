# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

print("\nIn this \033[34;1mPython\033[0m \033[1m3.0\033[0m \033[33;1mLanguage\033[0m, the program will identify the inputted digits or values from \033[32;1m\x1B[ascending to descending order\x1B[0m between the \033[32;1mfour (4) statements\033[0m enclosed on a square bracket.")
print("\n\033[32;1mFLOAT STRING Numericals\033[0m are supported.")

def top_number(quan1, quan2, quan3, quan4):
    if quan1 > quan2 and quan1 > quan3 and quan1 > quan4:
        if quan2 > quan3 and quan2 > quan4:
            if quan3 > quan4:
                order_num = [quan1, quan2, quan3, quan4]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan4 > quan3:
                order_num = [quan1, quan2, quan4, quan3]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
        elif quan3 > quan2 and quan3 > quan4:
            if quan2 > quan4:
                order_num = [quan1, quan3, quan2, quan4]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan4 > quan2:
                order_num = [quan1, quan3, quan4, quan2]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
        elif quan4 > quan2 and quan4 > quan3:
            if quan3 > quan2:
                order_num = [quan1, quan4, quan3, quan2]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan2 > quan3:
                order_num = [quan1, quan4, quan2, quan3]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
    elif quan2 > quan1 and quan2 > quan3 and quan2 > quan4:
        if quan1 > quan3 and quan1 > quan4:
            if quan3 > quan4:
                order_num = [quan2, quan1, quan3, quan4]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan4 > quan3:
                order_num = [quan2, quan1, quan4, quan3]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
        elif quan3 > quan1 and quan3 > quan4:
            if quan1 > quan4:
                order_num = [quan2, quan3, quan1, quan4]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan4 > quan1:
                order_num = [quan2, quan3, quan4, quan1]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
        elif quan4 > quan1 and quan4 > quan3:
            if quan1 > quan3:
                order_num = [quan2, quan4, quan1, quan3]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan3 > quan1:
                order_num = [quan2, quan4, quan3, quan1]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
    elif quan3 > quan1 and quan3 > quan2 and quan3 > quan4:
        if quan1 > quan2 and quan1 > quan4:
            if quan2 > quan4:
                order_num = [quan3, quan1, quan2, quan4]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan4 > quan2:
                order_num = [quan3, quan1, quan4, quan2]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
        elif quan2 > quan1 and quan2 > quan4:
            if quan1 > quan4:
                order_num = [quan3, quan2, quan1, quan4]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[ascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan4 > quan1:
                order_num = [quan3, quan2, quan4, quan1]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
        elif quan4 > quan1 and quan4 > quan2:
            if quan1 > quan2:
                order_num = [quan3, quan4, quan1, quan2]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan2 > quan1:
                order_num = [quan3, quan4, quan2, quan1]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
    elif quan4 > quan1 and quan4 > quan2 and quan4 > quan3:
        if quan1 > quan2 and quan1 > quan3:
            if quan2 > quan3:
                order_num = [quan4, quan1, quan2, quan3]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan3 > quan2:
                order_num = [quan4, quan1, quan3, quan2]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
        elif quan2 > quan1 and quan2 > quan3:
            if quan1 > quan3:
                order_num = [quan4, quan2, quan1, quan3]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan3 > quan1:
                order_num = [quan4, quan2, quan3, quan1]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
        elif quan3 > quan1 and quan3 > quan2:
            if quan1 > quan2:
                order_num = [quan4, quan3, quan1, quan2]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")
            elif quan2 > quan1:
                order_num = [quan4, quan3, quan2, quan1]
                print(f"\n\033[0mThe following list is in \033[32;1m\x1B[3mascending to descending\x1B[0m order.\n\33[34;1m{order_num}\33[0m\n")         

try:
    num1 = float(input("\nEnter the \33[36;1mFIRST (1ST)\33[0m number here. \n\033[32;1m>>> "))
    num2 = float(input("\n\033[0mEnter the \33[36;1mSECOND (2ND)\33[0m number here. \n\033[32;1m>>> "))
    num3 = float(input("\n\033[0mEnter the \33[36;1mTHIRD (3RD)\33[0m number here. \n\033[32;1m>>> "))
    num4 = float(input("\n\033[0mEnter the \33[36;1mFOURTH (4TH)\33[0m number here. \n\033[32;1m>>> "))
    top_number(num1, num2, num3, num4)
except ValueError as alpha:
    print(f"\n\033[0mInvalid user input. \33[36;1m{alpha}\33[0m\n")