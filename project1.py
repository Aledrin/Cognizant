#First ask for years of the person
age= int(input("How old are you: "))
#then use conditional statements
if age > 18:

    print("Congratulations! You are eligible to vote. Go make a difference!")

elif age == 18:

    print("You are eligible to vote")
#in the last one for make sure to know the years that the person needs lets make an operation
else:
    years= 18-age
    
    print("Oops! You are not eligible yet. But hey, only",years,"more years to go!")