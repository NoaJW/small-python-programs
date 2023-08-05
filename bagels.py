# Qns: https://inventwithpython.com/bigbookpython/project1.html

import random 

def main(): 
    print("I am thinking of a 3-digit number. Try to guess what it is.")
    print("Here are some clues:")
    print("When I say:    That means")
    print("  Pico         One digit is correct but in the wrong position.")
    print("  Fermi        One digit is correct and in the right position.")
    print("  Bagels       No digit is correct.")
    print("I have thought up a number.")
    print(" You have 10 guesses to get it.")

    tries = 1
    com_num = random.randint(100, 999)
    com_num_str = str(com_num)

    while tries < 11: 
        user_num = input("Guess {} ".format(tries))
        # Validate user input is number and consists of 3 digits
        if not user_num.isdigit() or len(user_num) != 3:
            print("Invalid input. Please enter a three-digit number.")
            continue

        user_num_str = str(user_num)
        fermi_counter = 0
        check = ""

        # Iterate through user num and check against com num
        for index in range(len(user_num_str)): 
        # Check if digit is correct and in correct position
            if user_num_str[index] == com_num_str[index]:
                check += "Fermi "
                fermi_counter += 1
            # Check if digit is correct but in wrong position
            elif user_num_str[index] in com_num_str: 
                check += "Pico "
        
        if check == "":                 # Bagels 
            print("Bagels")
        elif fermi_counter != 3:        # Partially correct answer 
            print(check)
        else:                           # Correct answer on 3 fermi  
            print("You got it!")
            # Replay
            replay = input("Do you want to play again? (yes or no) ")
            if replay.strip() == "yes" or replay.strip() == "y":
                tries = 1
                com_num = random.randint(100, 999)
                com_num_str = str(com_num)
                continue
            else: 
                print("Thanks for playing!")
                break
            
        tries += 1


if __name__ == '__main__':
    main()