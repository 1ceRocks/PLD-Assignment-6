# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

# The module 'random' will be used as a randrage import on this program.
from random import randrange
import math

# GLOBAL VARIABLES LIST
infMax = 1 # Maximum Information (User Item Input) = Store Global Variable
correct_ans = 0 # Correct Answers of a User = Store Global Variable
wrong_ans = 0 # Wrong Answers of a User = Store Global Variable
maxItems = 10 # The Total Items for the Quiz (Fixed Numerical Int)
prog_preface = print("\nWelcome to \33[36;1mVillariza\33[0m \033[32;1mMath Quiz\33[0m! \nThis is a \033[32;1m\x1B[3mten (10) question mathematical addition item\x1B[0m that will probably test your brain between \33[34;1mrandom digits\33[0m ranging from \033[33;1m0-99!\033[0m")
user_name = input("\nBefore we proceed, please enter your \033[31;1mNAME\33[0m down\33[0m below. \n\033[31;1m>>> ")
verReady = input(f"\n\033[0mHi \033[31;1m{user_name.title()}\33[0m!\nAre you ready for the \033[32;1mMath Quiz\33[0m? (Respond: \33[34;1mYes\33[0m or \33[34;1mNo\33[0m)\n\033[32;1m>>>\33[0m\33[34;1m ") # To Verify if the User is Ready or Not.
ready = False

# While Condition Statement is added in able for Python to Communicate on User Lively.
while not ready:
    if verReady.replace(".","",10).title() == "Yes" or verReady.replace("!","",10).title() == "Yes":
        verReady = "Yes"
        ready = True
    while verReady.replace(".","",10).title() != "Yes":
        if verReady.replace(".","",10).title() == "No" or verReady.replace("!","",10).title() == "No":
            verReady = input(f"\n\033[0mSure indeed, I will give you a plenty of time to take a deep breath. 😇\nAre you now ready for the \033[32;1mMath Quiz\33[0m? (Respond: \33[34;1mYes\33[0m or \33[34;1mNo\33[0m)\n\033[32;1m>>>\33[0m\33[34;1m ")
            if verReady.replace(".","",10).title() == "No" or verReady.replace("!","",10).title() == "No":
                verReady = "No"
                break
            elif verReady.replace(".","",10).title() == "Yes" or verReady.replace("!","",10).title() == "Yes":
                verReady = "Yes"
                break
            while verReady.replace(".","",10).title() != "Yes":
                verReady = input(f"\n\033[0mPython 3.0 didn't understand your response, apologies! ☹️\nAre you now ready for the \033[32;1mMath Quiz\33[0m? (Respond: \33[34;1mYes\33[0m or \33[34;1mNo\33[0m)\n\033[32;1m>>>\33[0m\33[34;1m ")
                if verReady.upper() in "BCDFGHJKLMNPQRSTVWXYZAEIOU":
                    verReady = input(f"\n\033[0mPython 3.0 didn't understand your response, apologies! ☹️\nAre you now ready for the \033[32;1mMath Quiz\33[0m? (Respond: \33[34;1mYes\33[0m or \33[34;1mNo\33[0m)\n\033[32;1m>>>\33[0m\33[34;1m ")
                elif verReady.replace(".","",10).title() == "No" or verReady.replace("!","",10).title() == "No":
                    verReady = "No"
                    break
                elif verReady.replace(".","",10).title() == "Yes" or verReady.replace("!","",10).title() == "Yes":
                    verReady = "Yes"
                    break
                else:
                    verReady = "C"
        else:
            verReady = input(f"\n\033[0mPython 3.0 didn't understand your response, apologies! ☹️\nAre you now ready for the \033[32;1mMath Quiz\33[0m? (Respond: \33[34;1mYes\33[0m or \33[34;1mNo\33[0m)\n\033[32;1m>>>\33[0m\33[34;1m ")
            if verReady.upper() in "BCDFGHJKLMNPQRSTVWXYZAEIOU":
                verReady = input(f"\n\033[0mPython 3.0 didn't understand your response, apologies! ☹️\nAre you now ready for the \033[32;1mMath Quiz\33[0m? (Respond: \33[34;1mYes\33[0m or \33[34;1mNo\33[0m)\n\033[32;1m>>>\33[0m\33[34;1m ")
            elif verReady.replace(".","",10).title() == "No" or verReady.replace("!","",10).title() == "No":
                verReady = "No"
                break
            elif verReady.replace(".","",10).title() == "Yes" or verReady.replace("!","",10).title() == "Yes":
                verReady = "Yes"
                break
            else:
                verReady = "C"

print(f"\n\033[0mOkay \033[31;1m{user_name.title()}\033[0m, let us now begin! Always take note that, \n\x1B[3mIf you fail to prepare, you are prepared to fail. - Benjamin Franklin\x1B[0m")

# Only Mathematical Operator = "+" will be used on this program as the interface of Villariza \033[32;1mMath Quiz\33[0m.
while infMax <= maxItems:
    """
    LOCAL SPECIAL VARIABLE INPUT-STORE STRING FUNCTION.
    """
    quan1 = randrange(0,99) # quan1 (Abbreviated = Quantity 1) < Special Local Variable
    quan2 = randrange(0,99) # quan2 (Abbreviated = Quantity 2) < Special Local Variable
    prog_ans = quan1 + quan2 # prog_ans (Abberviated = ) < Special Local Variable (MATHEMATICAL OPERATOR = ADDITION)
    if infMax < maxItems:
        print(f"\n\033[0mItem No.\033[36;1m{infMax}\033[0m out of \033[34;1m{maxItems}\033[0m. \nWhat's \033[32;1m{quan1}\033[0m + \033[32;1m{quan2}\033[0m?")
    elif infMax == maxItems:
        print(f"\n\033[0mItem No.\033[34;1m{infMax}\033[0m out of \033[34;1m{maxItems}\033[0m. \nWhat's \033[32;1m{quan1}\033[0m + \033[32;1m{quan2}\033[0m?")
    userResponse = input("\nYour Answer \n\033[31;1m>>>\33[0m\033[32m ") # First Issue (User Input as Answer)
    if userResponse.isalpha() == True: # Second Issue (If User Input is Alphabet)
        """
        TOTAL ITEM QUIZ NOT COUNTED IF ANOTHER INPUT IS ENCODED BY A USER (USING IF STATEMENT).
        """
        print("\033[0mThe program says that you should provide a \033[32;1mnumerical input\033[0m. Please try again. \nThat answer \033[31;1m\x1B[3mwould not\x1B[0m be counted as an \033[32;1m\x1B[3mincrement\x1B[0m of your \033[34;1mtotal item quiz\033[0m.")
    elif userResponse.isdigit() == True: # Third Issue (If User Input is Digit)
        """
        LIVE QUIZ PROGRAM CODE (USING IF-ELIF CODE BLOCK(S) IN WHILE STATEMENT).
        """
        if int(userResponse) == prog_ans: # Count Correct Answers
            correct_ans += 1
            infMax += 1
            if correct_ans == 10:
                None
            elif correct_ans >= 8 or correct_ans == 9:
                print(f"\n\033[0mSuperb! \33[32;1mVery consistent\033[0m indeed!")
            elif correct_ans >= 5 or correct_ans == 7:
                print(f"\n\033[0mYou are \33[32;1mstill right!\033[0m Keep it up!")
            elif correct_ans >= 1 or correct_ans == 4:
                print(f"\n\033[0mYou are \33[32;1mcorrect!\033[0m")
        elif int(userResponse) != prog_ans: # Count Wrong Answers
            if wrong_ans == 9:
                print(f"\n\033[0mThe correct answer for Item No.\033[34;1m{infMax}\033[0m is \033[32;1m{prog_ans}\033[0m")
            elif wrong_ans >= 7 or wrong_ans == 8:
                print(f"\n\033[0mYou are \033[31;1mstill wrong\033[0m! Think more! \nThe correct answer for Item No.\033[36;1m{infMax}\033[0m is \033[32;1m{prog_ans}\033[0m")
            elif wrong_ans >= 4 or wrong_ans == 6:
                print(f"\n\033[0mYou are \033[31;1mwrong\033[0m! But you can still do it! \nThe correct answer for Item No.\033[36;1m{infMax}\033[0m is \033[32;1m{prog_ans}\033[0m")
            elif wrong_ans >= 0 or wrong_ans == 3:
                print(f"\n\033[0m\033[31;1mIncorrect 🙁\033[0m\nThe correct answer for Item No.\033[36;1m{infMax}\033[0m is \033[32;1m{prog_ans}\033[0m")
            wrong_ans += 1
            infMax += 1
    elif userResponse.isalnum() == True: # Fourth Issue (If User Input is Alpha-Numeric)
        """
        TOTAL ITEM QUIZ NOT COUNTED IF ANOTHER INPUT IS ENCODED BY A USER (USING ELIF STATEMENT).
        """
        print("\033[0mThe program says that you should provide a \033[32;1mnumerical input\033[0m. Please try again. \nThat answer \033[31;1m\x1B[3mwould not\x1B[0m be counted as an \033[32;1m\x1B[3mincrement\x1B[0m of your \033[34;1mtotal item quiz\033[0m.")
    else:
        """
        TOTAL ITEM QUIZ NOT COUNTED IF ANOTHER INPUT IS ENCODED BY A USER (USING ELIF STATEMENT).
        """
        print("\033[0mThe program says that \033[32mfloat inputs (with . ,)\033[0m or \033[32mintegers with decimals (with . ,)\033[0m are not recognized in this \033[32;1mMath Quiz\33[0m. Please try again. \nThat answer \033[31;1m\x1B[3mwould not\x1B[0m be counted as an \033[32;1m\x1B[3mincrement\x1B[0m of your \033[34;1mtotal item quiz\033[0m.")

# SUMMARY OF SCORES , EVALUATION , AND ADDITIONAL COMMENTS FOR MORE INTERACTIVE RESPONSE.
if correct_ans >= 10 and wrong_ans == 0:
    print(f"\n\033[0mThe \033[34;1msummary of your grades\033[0m would be: \033[32;1m{correct_ans} / {maxItems}\033[0m.\n\x1B[3mYou've got a perfect score!\033[0m\n")
elif correct_ans >= 5 or correct_ans == 9 and wrong_ans >= 1:
    print(f"\n\033[0mThe \033[34;1msummary of your grades\033[0m would be: \033[32;1m{correct_ans} / {maxItems}\033[0m.\n\x1B[3mYou still did your best!\033[0m\n")
elif correct_ans >= 1 or correct_ans == 4 and wrong_ans >= 1:
    print(f"\n\033[0mThe \033[34;1msummary of your grades\033[0m would be: \033[32;1m{correct_ans} / {maxItems}\033[0m.\n\x1B[3mNice try! But you still need to practice more, okay?\033[0m\n")
elif correct_ans == 0 and wrong_ans >= 0:
    print(f"\n\033[0mThe \033[34;1msummary of your grades\033[0m would be: \033[32;1m{correct_ans} / {maxItems}\033[0m.\n\x1B[3mDo not worry, at least you have tried!\033[0m\n")