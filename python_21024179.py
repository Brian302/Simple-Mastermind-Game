import random
import os

cont, correct_order = 'Y', 0 #Initialization of values
hidden, q = False, False
Ans, Error, User = [], [], []
Order = ['first','second','third','fourth']
Selection = ['red','pink','blue','orange','yellow','green']

def input_validate(User): #User-defined function for validating input
    Selection = ['red','pink','blue','orange','yellow','green']
    User_checklist = [0,0,0,0]
    for x in range(4): #Outputs True or False for each element in list
        for y in range(6):
            if (len(User[x]) == 1 and User[x][0].upper() == Selection[y][0].upper()) or User[x].upper() == Selection[y].upper():
                User_checklist[x] = True
                break
            else:
                User_checklist[x] = False 
    return User_checklist

def check_ans(User,Ans): #User-defined function for checking answer
    copy_User = User.copy() #Copying both lists to manipulate the elements without changing the original lists
    copy_Ans = Ans.copy()
    c, w = 0, 0   
    for i in range(4): #Firstly look for the correct colors in the correct place
        if copy_User[i][0].lower() == copy_Ans[i][0]:
            c += 1
            copy_User[i] = '1_User1' #Replace used elements to prevent overlapping, use numbers to start naming to not interfere with the logic of comparing the initial letter in the next steps
            copy_Ans[i] = '2_Ans1'               
    for j in range(4): #Secondly look for the correct colors but in the wrong place
        for k in range(4):
            if copy_User[j][0].lower() == copy_Ans[k][0]:
                w += 1
                copy_User[j] = '3_User2' #Replace used elements to prevent overlapping, use numbers to start naming to not interfere with the logic of comparing the initial letter in the next steps
                copy_Ans[k] = '4_Ans2'
    return c,w

while cont.upper() == 'Y': #Introduction
    print('--------------------------------------------------------------------------------') #Introduction of the game
    print('This is an on-screen version of the board game Master Mind!')
    print('This is a game where you need to guess the code, which is a random sequence of\nfour colors!')
    print('--------------------------------------------------------------------------------')
    
    while True: #Some information and input system before starting game
        user = input('[1] Rules\n[2] Gameplay\n[3] Start game\n[4] Quit game\nSelect 1/2/3/4:')
        if user == '1': #Rules
            os.system('cls')
            print('--------------------------------------------------------------------------------')
            print('Rules:')
            print('The selections of colors will be red, pink, blue, orange, yellow and green.')
            print('You can only input colors within the provided list.')
            print('You can either type its initial letter or the entire word. Ex: r / red.')
            print('Duplicate colors in the code is possible! But no blank spaces.')
            print("*Note that the inputs aren't case sensitive!")
            print('--------------------------------------------------------------------------------')
        elif user == '2': #Gameplay
            os.system('cls')
            print('--------------------------------------------------------------------------------')
            print('Gameplay:')
            print('The answer to the code will be randomized at the start.')
            print('For each guess, you need to input the four colors in order.')
            print('After each guess, the game will return two numbers, which are\n[Correct color in the correct place] and [Correct color but in the wrong place].')
            print('You need to continue guessing according to the hints until you get the final\nanswer!')
            print('The total amount of attempts will be shown in the end. Have fun!')
            print('--------------------------------------------------------------------------------')
        elif user == '3': #Start game
            os.system('cls')
            print('--------------------------------------------------------------------------------') 
            print('It is advisable to read the rules and gameplay before starting.')
            print('--------------------------------------------------------------------------------')
            confirm = input('Are you sure to continue?:(Y/N)')
            if confirm.upper() == 'Y': #Confirmation to start game
                os.system('cls')
                break
            else:
                os.system('cls')
                print('--------------------------------------------------------------------------------')
        elif user == '4': #Quits game 
            q, correct_order, cont = True, 4, 'N'
            break
        elif user == 'DEBUG': #User can enter a secret passcode for debugging purposes
            os.system('cls')
            hidden = True
            print('--------------------------------------------------------------------------------')
            print('Debug mode activated!')
            print('--------------------------------------------------------------------------------')
        else: #Incorrect input
            os.system('cls')
            print('--------------------------------------------------------------------------------')
            print('Incorrect input! Try again.')
            print('--------------------------------------------------------------------------------')

    for x in range(4): #Randomization of code
        y = random.randint(0,5)
        Ans.append(Selection[y])

    attempt = 0
    while correct_order != 4: #Guessing starts, breaks out of while loop only if all four inputs are correct in order
        b, c = False, False
        print('--------------------------------------------------------------------------------')
        print('                            Selections: [red, pink, blue, orange, yellow, green]')
        print('Guess #'+str(attempt + 1)+':')
        print("\nYou can enter 'q', 'n' or 'm' at any time to either quit the game, generate a\nnew code or go back to main menu.\n")

        if hidden == True: #Shows answer when debugging
            print('*Answer is',Ans)
        print('--------------------------------------------------------------------------------')

        for i in range(4): #User guessing loop
            User.append(input(f'Enter the {Order[i]} color:'))
            if 'q' in User or 'Q' in User: #Check if user wants other options first
                os.system('cls')
                q,cont,b = True,'N',True
                break
            elif 'n' in User or 'N' in User:
                Ans = []
                for x in range(4):
                    y = random.randint(0,5)
                    Ans.append(Selection[y])
                os.system('cls')
                print('--------------------------------------------------------------------------------')
                print('New code generated!')
                attempt,c,User = 0,True,[]
                break
            elif 'm' in User or 'M' in User:
                os.system('cls')
                q,hidden,Ans,attempt,b,User = True,False,[],0,True,[]
                break
                
        if b == True: #Redirect to wanted option if any
            break
        elif c == True:
            continue

        User_checklist = input_validate(User) #Validation starts

        if User_checklist == [True,True,True,True]: #Proceeds to checking only if all answers are validated
            correct_order,wrong_order = check_ans(User,Ans)
            print('\n[Correct color(s) in the correct place = '+str(correct_order)+']')
            print('[Correct color(s) but in the wrong place = '+str(wrong_order)+']\n')
            User, q = [], False
            attempt += 1
        else: #Prints out error inputs if any then back to guessing loop
            for x in range(4):
                if User_checklist[x] == False:
                    Error.append(User[x])

            print('\n',Error,'is not part of the list! Try again.')
            User, Error = [], [] #Resets error list and user list for next guess

    if q != True: #Congratulate when code is found
        print('--------------------------------------------------------------------------------')
        print('Congratulations! The code is indeed '+str(Ans)+'.\nYou took',attempt,'attempts in total!')
        if attempt == 1: #Easter egg 1
            print('[Creator]:"Oh wow... you actually guessed it in one attempt."')
            print('[Creator]:"I did not even bother about the grammatical error..."')
            print('[Creator]:"You beat me! Anyways..."')
        print('--------------------------------------------------------------------------------')
        cont = input('Do you want to play again?(Y/N):')
        os.system('cls')
        correct_order, Ans, hidden = 0, [], False #Initialize values if user wants to continue

os.system('cls') #End of the program if user doesn't continue
print('--------------------------------------------------------------------------------')
if User != []:
    print(f'Too bad, the answer was {Ans}.\nBetter luck next time!')
print('End of the game. Thank you for playing!')
if attempt == 0: #Easter egg 2
    print('[Creator]:"You did not even try... :("')
print('--------------------------------------------------------------------------------')
end = input('Enter any key to continue...')
