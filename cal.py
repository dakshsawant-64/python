def operation():
    noone = input("> Enter first number: ")
    if noone == 'quit':
        print("Exiting the calculator. Goodbye!")
        return False
    notow = input("> Enter second number: ")
    if notow == 'quit':
        print("Exiting the calculator. Goodbye!")
        return False
    symbol = input("> Enter operation (+, -, *, /): ")
    if symbol == 'quit':
        print("Exiting the calculator. Goodbye!")
        return False

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
        return True
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
        return True


def f():
    while True:
        quitornot = input("> Do you want to quit? (yes/no/stopask): ").strip().lower()
        if quitornot == 'yes':
            print("Exiting the calculator. Goodbye!")
            break
        elif quitornot == "stopask":
            print("You can start entering numbers and operations.")
            while True:
                if not operation():
                    break
        else:
            if not operation():
                break


if __name__ == "__main__":
    f()
