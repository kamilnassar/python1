print("Starting calculator...")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

def start():
    if operation == "+":
        result = add(one, three)
    elif operation == "-":
        result = subtract(one, three)
    elif operation == "/":
        result = divide(one, three)
    elif operation == "*":
        result = multiply(one, three)
    print(one, operation, three, "=", result)

def secondNum():
    global three
    print("Enter the second number in your calculation:")
    three = int(input())
    print("Calculator starting...")
    start()

def checkBeforeStart():
    if operation in ("1", "2", "3", "4"):
        secondNum()
    else:
        print("Something went wrong in your input.")
        print("Please wait...")
        print("Starting over...")
        firstNum()
    
def cal():
    global operation
    print("First number is successfully added, now please choose your calculation:")
    print("1 ===> +")
    print("2 ===> -")
    print("3 ===> /")
    print("4 ===> *")
    operation = input()
    checkBeforeStart()

def firstNum():
    global one
    print("Enter the first number in your calculation:")
    one = int(input())
    cal()

firstNum()
