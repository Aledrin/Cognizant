import logging

# Set up logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError as e:
            print("Invalid input! Please enter a valid number.")
            logging.error(f"ValueError occurred: {e}")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("Oops! Division by zero is not allowed.")
        logging.error(f"ZeroDivisionError occurred: {e}")
        return None

def display_menu():
    print("\nWelcome to Calculator!")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("> ")

        if choice == '5':
            print("Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            try:
                if choice == '1':
                    result = add(num1, num2)
                    print(f"Result: {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"Result: {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"Result: {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    if result is not None:
                        print(f"Result: {result}")
            except Exception as e:
                print("An unexpected error occurred.")
                logging.error(f"Unexpected error: {e}")
            finally:
                print("Operation completed.\n")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
