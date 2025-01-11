def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "devide":
        if num2 == 0:
            print("A number is not divisible by zero!")
        else:
            return num1 / num2
    else:
        print("Not allowed operation!")

