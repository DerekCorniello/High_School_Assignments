import random
number = random.randint(1,26)
print "You have 10 guesses..."

for i in range(1,11):

    guess = input("Guess a number between 1 and 25. ")

    if number == guess:
        print "Congratulations! You picked the right number!"
        break
    
    elif number > guess:
        print "Guess higher!"

    elif number < guess:
        print "Guess lower!"

    print "You have " + str(10 - i) + " guesses left. "
    print "\n"
    
print "Game Over! The correct number was " + str(number)