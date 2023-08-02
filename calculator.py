print("starting calculator...")

x = 1
one = 0
two = ""
three = 0

def start():
    if two == "1":
        one = add
        add + three
        print(one, "+", three, "=", )
    elif two == "-":
        print(one - three)
    elif two == "/":
        print(one / three)
    elif two == "*":
        print(one * three)

def secondNum():
    global three
    print("enter the second number in your calculation,")
    print("")
    print("then press enter")
    print("=====================================================")
    three = int(input())
    print("calculator starting")
    #print(one, two, three)
    start()

def checkBeforeStart():
    if two in ("1", "2", "3", "4"):
        secondNum()
    else:
        print("something whent wrond in your inputs ")
        print("plz wait...")
        print("starting")
        firstNum()
    
def cal():
    global two
    print("first number is successfully added now please choose your calculation")
    print("now to choose your calculation:-")
    print(" 1 ====> +")
    print(" 2 ====> -")
    print(" 3 ====> /")
    print(" 4 ====> *")
    two = input()
   # print(one, two, "not set")
    checkBeforeStart()

def firstNum():
    global one
    print("enter the first number in your calculation,")
    print("")
    print("then press enter")
    print("=====================================================")
    one = int(input())
    cal()

if x == 1:
    firstNum()
