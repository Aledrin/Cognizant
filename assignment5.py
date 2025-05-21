#Task 1
def welcome(name):
    print(f"Hello, {name}! Welcome ")

def add(n1, n2):
    return n1 + n2

user = input("Please, enter your name: ")
n1 = int(input("Give me a number: "))
n2 = int(input("Give me other number: "))


welcome(user)
result = add(n1, n2)
print(f"The sum of {n1} and {n2} is {result}.")

#Task 2
def describe(mypet,animal="dog"):
    print(f"\nI have a {animal}.")
    print(f"My {animal}'s name is {mypet.title()}.")
def main():
    mypet = input("Enter your pet's name: ")
    animal = input("Enter the type of animal (press Enter to default to 'dog'): ")

    if animal.strip() == "":
        describe(mypet)
    else:
        describe(mypet, animal)
main()

#Task 3
def sandwich(*ingredients):
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
def main2():
    print("Enter your sandwich ingredients one at a time.")
    print("Type 'done' when you're finished.\n")
    
    ingredients = []
    while True:
        ingredient = input("Add ingredient: ")
        if ingredient.lower() == "done":
            break
        elif ingredient.strip() != "":
            ingredients.append(ingredient)
    
    sandwich(*ingredients)
main2()

#Task 4
def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main3():
    print("Calculate factorial and Fibonacci separately.\n")
    
   
    try:
        num_fact = int(input("Enter a non-negative integer for factorial: "))
        if num_fact < 0:
            print("Please enter a non-negative number for factorial.")
            return
    except ValueError:
        print("That is not a valid number for factorial.")
        return
    try:
        num_fib = int(input("Enter a non-negative integer for Fibonacci: "))
        if num_fib < 0:
            print("Please enter a non-negative number for Fibonacci.")
            return
    except ValueError:
        print("That is not a valid number for Fibonacci.")
        return

    fact_result = factorial(num_fact)
    fib_result = fibonacci(num_fib)


    print(f"\nThe factorial of {num_fact} is {fact_result}, and the {num_fib}th Fibonacci number is {fib_result}.")


main3()
