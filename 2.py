def calculator():
    print("Welcome to the simple calculator!")
    
    while True:
        try:
            # Get the first number from the user
            num1 = float(input("Please enter the first number: "))
        
            # Get the second number from the user
            num2 = float(input("Please enter the second number: "))
        
            # Display operation choices
            print("Please choose an operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
        
            # Get the operation choice from the user
            operation = input("Enter the number corresponding to the operation: ")
        
            # Perform the calculation based on the user's choice
            if operation == '1' or operation == '+':
                result = num1 + num2
                print(f"The result of {num1} + {num2} is: {result}")
            elif operation == '2' or operation == '-':
                result = num1 - num2
                print(f"The result of {num1} - {num2} is: {result}")
            elif operation == '3' or operation == '*':
                result = num1 * num2
                print(f"The result of {num1} * {num2} is: {result}")
            elif operation == '4' or operation == '/':
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result of {num1} / {num2} is: {result}")
                else:
                    print("Error: Division by zero is not allowed.")
            else:
                print("Invalid operation choice. Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")

        # Ask the user if they want to perform another calculation
        cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

# Run the calculator
calculator()


