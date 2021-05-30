#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

game_restart = True

while game_restart:
    
    print('''
        )                                                                                            
     ( /(                )            (                                     (                        
     )\())  (     )   ( /(   (  (     )\ )     (    (      (        (  (    )\ )      )    )     (   
    ((_)\  ))\   (    )\()) ))\ )(   (()/(    ))\  ))\(  ( )\  (    )\))(  (()/(   ( /(   (     ))\  
     _((_)/((_)  )\  ((_)\ /((_(()\   /(_))_ /((_)/((_)\ )((_) )\ )((_))\   /(_))_ )(_))  )\  '/((_) 
    | \| (_))( _((_))| |(_(_))  ((_) (_)) __(_))((_))((_((_(_)_(_/( (()(_) (_)) __((_)_ _((_))(_))   
    | .` | || | '  \(| '_ / -_)| '_|   | (_ | || / -_(_-(_-| | ' \)/ _` |    | (_ / _` | '  \(/ -_)  
    |_|\_|\_,_|_|_|_||_.__\___||_|      \___|\_,_\___/__/__|_|_||_|\__, |     \___\__,_|_|_|_|\___|  
                                                                   |___/                             
    ''')
    
    print("Welcome!! You have to pick a no. between 0 and 100")
    diff = input("Enter difficulty hard or easy? h/e: ").lower()
    no_of_guess = 0
    if diff == 'h':
        no_of_guess = 5
    else:
        no_of_guess = 10
        
    num = random.randint(0,100)
    game_win = False
    for i in range(1,no_of_guess+1):
        user_num = int(input("Enter your guess: "))
        if user_num == num:
            print(f"Congratulations!! you guessed correct the num {num}")
            game_win = True
            break
        elif user_num < num:
            print("Too Low,")
            print(f"You have {no_of_guess-i} tries remaining")
        elif user_num > num:
            print("Too High,")
            print(f"You have {no_of_guess-i} tries remaining")
    
    if not game_win:
        print("You lost all your tries.You Lose :(")
    
    choice = input("Want to play again?y/n: ").lower()
    if choice == 'n':
        game_restart =False
        

    
        
        
    
        
