import sys
import random
words=False 
guess_limit=2
guess_count=0
out_of_guesses=False
number = random.randint(1,10)
print("Try to guess the number between 1 to 10 in 3 guesess")

guess1 = int(input('Enter your first guess-->'))
if guess1 == number :
    guess_count+=1
    print("You guessed it on the first try! You must be genius!")
    sys.exit()
elif guess1>number:
    print("Your guess is too high!")
elif guess1<number:
    print("Your guess is too low!")
else:
    out_of_guesses=True

if out_of_guesses:
    print("Out of guesses,YOU LOSE!")


print("You have 2 guessts left")
guess2 =int(input("Enter your second guess-->"))
if guess2 == number:
    print("You guest it in the second try! Great job!")
    sys.exit()
elif guess2 > number:
    print("Your guess is too high!")
elif guess2<number:
    print("Your guess is too low!")
else:
    out_of_guesses=True

if out_of_guesses:
    print("Out of guesses,YOU LOSE!")


print("You have 1 guess left")
guess3 =int(input("Enter your third guess-->"))
if guess2 == number:
    print("You guessed it! Nice!")
    sys.exit()
elif guess3 > number:
    print("Your guess is too high!")
elif guess3<number:
    print("Your guess is too low!")
else:
    out_of_guesses=True


print("Out of guesses,YOU LOSE!")
    
print("Your secter number was " , number)