# This program is dont have any reasoning state, it executes what we have hardcoded.
def calculator(a, b, operation):

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":
        if b == 0:
            return "Error: cannot divide by zero"

        return a / b

    else:
        return "Error: unknown operation"