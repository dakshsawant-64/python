e = 1
while True:
    quitornot = input("> Do you want to quit? (yes/no/stopask): ").strip().lower()
    if quitornot == 'yes':
        print("Exiting the calculator. Goodbye!")
        break
    elif quitornot == "stopask":
        while True:
                noone = input("> Enter first number: ")
                if noone == 'quit':
                    print("Exiting the calculator. Goodbye!")
                    break
                notow = input("> Enter second number: ")
                if notow == 'quit':
                    print("Exiting the calculator. Goodbye!")
                    break
                symbol = input("> Enter operation (+, -, *, /): ")
                if symbol == 'quit':
                    print("Exiting the calculator. Goodbye!")
                    break
                if notow == 'quit':
                    print("Exiting the calculator. Goodbye!")
                    break
                try:
                    num1 = int(noone)
                    num2 = int(notow)
                    if symbol == '+':
                        print(f"Result: {num1 + num2}")
                    elif symbol == '-':
                        print(f"Result: {num1 - num2}")
                    elif symbol == '*':
                        print(f"Result: {num1 * num2}")
                    elif symbol == '/':
                        if num2 != 0:
                            print(f"Result: {num1 / num2}")
                        else:
                            print("Error: Cannot divide by zero.")
                    else:
                        print("Error: Invalid operation. Please use +, -, *, or /.")
                except ValueError:
                    print("Error: Invalid input. Please enter valid numbers.")
    noone = input("> Enter first number: ")
    notow = input("> Enter second number: ")
    symbol = input("> Enter operation (+, -, *, /): ")
    try:
        num1 = int(noone)
        num2 = int(notow)
        if symbol == '+':
            print(f"Result: {num1 + num2}")
        elif symbol == '-':
            print(f"Result: {num1 - num2}")
        elif symbol == '*':
            print(f"Result: {num1 * num2}")
        elif symbol == '/':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Cannot divide by zero.")
        else:
            print("Error: Invalid operation. Please use +, -, *, or /.")
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
