# python use pass by reference objects model

#when u pasa value to a function ,python passes the reference of the  object,
# not the actual object or copy of it

# but it depend what type of dara type of parameter you accepting,
#if it is mutable then same address  will be there 


# 1. python variable are name

x=10 # beginner might be imagine that x is a box which contains 10,
#but it is not true, x is a name which is pointing to the object 10 in memory


print(id(x))


#Python objects have:

#a type
#a value
#an identity

# pass a variable to a function

def change(x):
    x = 100

a = 10
change(a)

print(a)

# case 3 list----

def change(numbers):
    numbers[0] = 100

a = [10, 20, 30]

change(a)

print(a)

# scientific distinction

x =10 # rebinding
# make the name x point to a new object 10 in memory

# mutation--
nun = [10, 20, 30] # make the name nun point to a new object 10 in memory
nun[0]=100
