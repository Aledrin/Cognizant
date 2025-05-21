import turtle

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

def draw_tree(branch_length, t):

    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_tree(branch_length - 15, t)
        t.left(40)
        draw_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

def get_positive_integer(prompt):
    
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    while True:
        print("\n==== Recursive Functions Menu ====")
        print(" 1. Calculate factorial")
        print(" 2. Calculate Fibonacci number")
        print(" 3. Draw fractal tree")
        print(" 4. Exit")

        choice = input("Please select an option (1-4): ")

        if choice == "1":
            n = get_positive_integer("Enter a number to calculate its factorial: ")
            result = factorial(n)
            print(f"The factorial of {n} is {result}.")

        elif choice == "2":
            n = get_positive_integer("Enter the position of the Fibonacci number: ")
            result = fibonacci(n)
            print(f"The {n}th Fibonacci number is {result}.")

        elif choice == "3":
            print("Preparing to draw fractal tree...")
            screen = turtle.Screen()
            screen.title("Recursive Fractal Tree")
            t = turtle.Turtle()
            t.speed(0)
            t.left(90)  
            t.up()
            t.backward(100)
            t.down()
            t.color("green")
            draw_tree(100, t)
            print("Drawing complete. Close the window to continue.")
            screen.mainloop() 

        elif choice == "4":
            print("Thank you for using the program! Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
