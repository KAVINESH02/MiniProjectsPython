import random 

user_wins = 0
bot_wins = 0


options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type your choice [Rock / Paper / Scissors / q to Quit] : ").lower()
    if user_input == "q":
        print("Game quited")
        break
    if user_input not in options:
        print("Type a valid option: ")
        continue
    
    rand_num = random.randint(0,2)
    bot_input = options[rand_num]
    
    print("Computer picked "+bot_input+ ".")
    
    if user_input == bot_input:
        print("Its a draw ")
        user_wins = user_wins
        bot_wins = bot_wins
        
        
    elif user_input == "rock" and bot_input =="scissors":
        print("You won!!")
        user_wins +=1
                
    elif user_input == "paper" and bot_input == "rock":
        print("You won!!")
        user_wins +=1
        
        
    elif user_input == "scissors" and bot_input == "paper":
        print("You won!!")
        user_wins +=1

            
    else:
        print("You lost :(")
        bot_wins +=1
         
    
print("You won" , user_wins , " times !!!")
print("Computer won " , bot_wins , "times !!")
print("GoodBye!!!!")
    