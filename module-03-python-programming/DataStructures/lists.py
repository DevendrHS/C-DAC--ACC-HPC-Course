# List --store multiple values in a single variable
# Lists are mutable data types in Python.  

data = [10, 20, 30,"python", 40,True,3.14, 50]
print(data)

data[0] = 100  # Modifying the first element of the list
print(data)

data.append("Devendra")  # Adding an element to the end of the list
print(data)

data.insert(2, "Java")  # Adding an element at a specific index
print(data)

data.remove(30)  # Removing an element from the list
print(data)

data.pop(0)  # Removing the last element from the list
print(data)



