import random
number_to_guess = random.randint(1, 100)

n= int(input("Give me a number: "))
print("Your number is",n)
at=0
while n != number_to_guess:
    
    if n > number_to_guess:
        print("Too high! Try again.")
    if n < number_to_guess:
        print("Too low! Try again.")
    at+=1
    print ("Your attempts are:",at)
    if at==10:
        print ("Game over!")
        break
    
    n = int(input("Guess the number: "))

    
if n==number_to_guess:
    print("Congratulations! You guessed it!")
else:
    print("Better luck next time!")
