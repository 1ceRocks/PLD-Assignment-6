# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

from random import randrange

infMax = 1 
correct_ans = 0 
wrong_ans = 0 
maxItems = 10 
prog_preface = print("\nWelcome to Villariza Math Quiz! \nAbout: This is a ten (10) question mathematical addition item that will probably test your brain between random digits ranging from 0-99!")
user_name = input("\nBefore we proceed, please enter your name down below. \n>>> ")
verReady = input(f"\nHi {user_name.title()}!\nAre you ready for the Math Quiz? (Respond: Yes or No)\n>>> ")
ready = False

while not ready:
    if verReady.replace(".","",10).title() == "Yes" or verReady.replace("!","",10).title() == "Yes":
        verReady = "Yes"
        ready = True
    while verReady.replace(".","",10).title() != "Yes":
        if verReady.replace(".","",10).title() or verReady.replace("!","",10).title() == "No":
            verReady = input(f"\nSure indeed, I will give you a plenty of time to take a deep breath. 😇\nAre you now ready for the Math Quiz? (Respond: Yes or No)\n>>> ")
            if verReady.replace(".","",10).title() == "No" or verReady.replace("!","",10).title() == "No":
                verReady = "No"
                break
            elif verReady.replace(".","",10).title() == "Yes" or verReady.replace("!","",10).title() == "Yes":
                verReady = "Yes"
                break
            while verReady.replace(".","",10).title() != "Yes":
                verReady = input(f"\nPython 3.0 didn't understand your response, apologies! ☹️\nAre you now ready for the Math Quiz? (Respond: Yes or No)\n>>> ")
                if verReady.upper() in "BCDFGHJKLMNPQRSTVWXYZAEIOU":
                    verReady = input(f"\nPython 3.0 didn't understand your response, apologies! ☹️\nAre you now ready for the Math Quiz? (Respond: Yes or No)\n>>> ")
                elif verReady.replace(".","",10).title() == "No" or verReady.replace("!","",10).title() == "No":
                    verReady = "No"
                    break
                elif verReady.replace(".","",10).title() == "Yes" or verReady.replace("!","",10).title() == "Yes":
                    verReady = "Yes"
                    break
                else:
                    verReady = "C"
        else:
            verReady = input(f"\nPython 3.0 didn't understand your response, apologies! ☹️\nAre you now ready for the Math Quiz? (Respond: Yes or No)\n>>> ")
            if verReady.upper() in "BCDFGHJKLMNPQRSTVWXYZAEIOU":
                verReady = input(f"\nPython 3.0 didn't understand your response, apologies! ☹️\nAre you now ready for the Math Quiz? (Respond: Yes or No)\n>>> ")
            elif verReady.replace(".","",10).title() == "No" or verReady.replace("!","",10).title() == "No":
                verReady = "No"
                break
            elif verReady.replace(".","",10).title() == "Yes" or verReady.replace("!","",10).title() == "Yes":
                verReady = "Yes"
                break
            else:
                verReady = "C"

print(f"\nOkay {user_name}, let us now begin! Always take note that, \n\x1B[3mIf you fail to prepare, you are prepared to fail. - Benjamin Franklin\x1B[0m")

while infMax <= maxItems:
    quan1 = randrange(0,99)
    quan2 = randrange(0,99)
    prog_ans = quan1 + quan2
    print(f"\nItem No.{infMax} out of {maxItems}. \nWhat's {quan1} + {quan2}?")
    userResponse = input("\nYour Answer \n>>> ")
    if userResponse.isalpha() == True:
        print("The program says that you should provide a numerical input. \nPlease try again. That answer would not be counted as an increment of your total item quiz.")
    elif userResponse.isdigit() == True:
        if int(userResponse) == prog_ans:
            correct_ans += 1
            infMax += 1
            if correct_ans == 10:
                print(f"")
            elif correct_ans >= 8 or correct_ans == 9:
                print(f"\nSuperb! Very consistent indeed!")
            elif correct_ans >= 5 or correct_ans == 7:
                print(f"\nYou are still right! Keep it up!")
            elif correct_ans >= 1 or correct_ans == 4:
                print(f"\nYou are correct!")
        elif int(userResponse) != prog_ans:
            wrong_ans += 1
            infMax += 1
            if wrong_ans == 10:
                print(f"")
            elif wrong_ans >= 8 or wrong_ans == 9:
                print(f"\nYou are still wrong! Think more!")
            elif wrong_ans >= 5 or wrong_ans == 7:
                print(f"\nYou are wrong! But you can still do it!")
            elif wrong_ans >= 1 or wrong_ans == 4:
                print(f"Incorrect 🙁")
    elif userResponse.isalnum() == True:
        print("The program says that you should provide a numerical input. Please try again. \nThat answer would not be counted as an increment of your total item quiz.")

if correct_ans >= 10 and wrong_ans == 0:
    print(f"\nThe summary of your grades would be: {correct_ans} / {maxItems}.\nYou've got a perfect score!\n")
elif correct_ans >= 5 or correct_ans == 9 and wrong_ans >= 1:
    print(f"\nThe summary of your grades would be: {correct_ans} / {maxItems}.\nYou still did your best!\n")
elif correct_ans >= 1 or correct_ans == 4 and wrong_ans >= 1:
    print(f"\nThe summary of your grades would be: {correct_ans} / {maxItems}.\nNice try! But you still need to practice more, okay?\n")
elif correct_ans == 0 and wrong_ans >= 1:
    print(f"\nThe summary of your grades would be: {correct_ans} / {maxItems}.\nDo not worry, at least you have tried!\n")