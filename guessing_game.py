import random

b= random.randint(5,26)
found = 0

while found == 0:
    guess = int(input(" Guess my number"))
    if guess > b:
        print(" You guessed too high")

    if guess< b:
        print(" you guessed too low")

    if  guess == b:
        found = 1
        
print("you found the number, Hurray")

