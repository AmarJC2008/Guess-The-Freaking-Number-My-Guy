import random 

print("Number Guessing Game")

number = random.randint(1,9)

chances = 0

print("Guess a Number (Between 1 and 9):")

while chances < 5:
    
    guess = int(input("Enter Your Guess:-"))
    
    if guess == number:
        
        print("Congratulations You Are Legally Smart and Dumb at the same time!!!!!")
        break
    elif guess < number:
        print("Your guess was too low: You should probably guess a number higher than", guess)
        
    else:
        print("Your guess was on drugs so you might wanna confiscate them so he lowers down to", guess)
        
        chances += 1
        
        
        if not chances < 5:
            print("YOU LOSE SO START DOING YOUR HOMEWORK INSTEAD OF PLAYING GAMES!!! The number is", number)