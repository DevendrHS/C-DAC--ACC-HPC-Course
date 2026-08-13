def add(x,y):
    # function is a block of code which is executed when it is called
    # python use def keyword to define a function

    return x+y

result = add(10,20)
print(result)



# calculation


def calculation(x,y):
    add = x+y
    sub = x-y
    mul = x*y
    div = x/y
    return add,sub,mul,div
var1,var2,var3,var4 = calculation(10,20)
print(var1) 
print(var2)
print(var3)
print(var4)

# greeting function

def greet():
    print("Hello, welcome to the world of Python programming!")
greet()