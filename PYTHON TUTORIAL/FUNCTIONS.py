#FUNCTIONS
def printSuccess():
    print("Task was successful")
    print("Moving to the next")
    print("Send me the next task")
    print("Hello, This is Phace!")

""""" Function name should be descriptive
Doc string 
#
"""""
def printSuccess2():
    """""This funciton does nothing except printing a message.
    That the Message is hello
    """""
    print("Hello")

help(printSuccess2)

#FUNCTION (INPUT ARGUMENTS)
"""""
The function prints the message supplied by the user
or prints that msg is not in the form of string
"""""
def printMessage(msg):
    if isinstance(msg,str):
        print(msg)
    else:
        print("your input argument is not a string")
        print("Here is the type of what you have supplied",type(msg))

printMessage(1902.1)

def after(msg1,msg2):

    if msg1>msg2:
        print("Msg1 is greater than Msg2:", msg1)
    elif msg2>msg1:
        print("Msg2 is greater than Msg1:", msg2)
    else:
        print("They are the same")

after(1,3)

#FUNCTIONS(ORDER OF INPUT ARGUMENTS)
def f(c2,c1,c3):
    print(c1,c2,c3)

f(2,4,6)
f(c1="A",c2="B",c3="C")

# Function(variables inside)
def add(x,y):
    c=x+y
    return c# you can call a variable inside a function for it to be accessed

# Function(variables inside)
def myadd(x,y):
    c=x+y
    return c
     # you can call a variable inside a function for it to be accessed
d= myadd(3,2)
print(d)
print(type(d))

#FUNTIONS( variable number of input arguments)
def sum(*args):
    s=0
    for i in range(len(args)):
        s+=args[i]
    return s

sum(2,4,5)
print(sum(2,4,5,8,9,0,11,23,4))

def printallvals(**r):
    for x in r:
        print("Variable name is:", x,"ANd value is,:",r[x])

printallvals(a=3,b="B",c="CCC",e=182.9,d=True)
    return x

def f(**u):
    for p in u:
        print(p, u[p])

print(f(c1="a",c2="b",c3="d"))

#DEFAULT VALUES
def f(sum=0):
    print(sum)

#DEFAULT VALUES
def gg(s=4):
    print(s)

print(gg())
print(gg(56))

L=[1,2,3]
L2=L
L2[0]=9
print(L)

def ff(L=[1,2,3,4,5]):
    for i in L:
        print(i)
ff()
ff(L2)

#MODULE