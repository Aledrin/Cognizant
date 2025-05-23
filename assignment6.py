#Task 1
print("===Task 1===")
try:
     n = int(input("Please, enter a number: "))
     print(100 / n)
except ValueError:
    print("Invalid input! That's not a valid number!")
except ZeroDivisionError:
    print("Oops! You can't divide by zero!")

#Task 2
print("===Task 2===")
# 1. IndexError: Happens when you try to access a list index that doesn't exist
try:
    sample_list = [1, 2, 3]
    print(sample_list[5])  # This index is out of range (only 0 to 2 are valid)
except IndexError:
    print("IndexError occurred! List index out of range.")

# 2. KeyError: Happens when you try to access a key in a dictionary that doesn't exist
try:
    sample_dict = {'name': 'Alex', 'age': 24}
    print(sample_dict['birthday'])  # 'birthday' key is not in the dictionary
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

# 3. TypeError: Happens when you try to perform an invalid operation between different types
try:
    number = 34
    text = "apples"
    result = number + text  # You cannot add an int and a string
except TypeError:
    print("TypeError occurred! Unsupported operand types.")

#Task 3
print("===Task 3===")
try:
    
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))

    # Attempt division
    result = n1 / n2

except ZeroDivisionError:
    # Handles division by zero
    print("Error: Cannot divide by zero.")

except ValueError:
    # Handles invalid numeric input
    print("Error: Please enter valid numbers.")

else:
    # Executes only if no exception occurs
    print(f"The result is {result}.")

finally:
    # Always executes
    print("This block always executes.")