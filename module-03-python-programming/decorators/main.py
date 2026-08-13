#A decorator is a function that takes another function as input and returns a modified/enhanced function.

# A decorator adds behavior to an existing function without changing the original function's source code.


def hello():
    print("Hello")

x = hello

x()

# function as an argument to another function

def hello():
    print("Hello")

def execute(func):
    func()

execute(hello)

# function returning another function

def outer():
    
    def inner():
        print("Hello")

    return inner

x = outer()

x()