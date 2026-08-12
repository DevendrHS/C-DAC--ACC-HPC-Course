# string is a sequence of characters. 
# It is an immutable data type in Python. 
# Strings can be created by enclosing characters in single quotes, double quotes, or triple quotes.

name = "Devendra"
print(name)

print(name[0])  # Accessing the first character of the string
print(name[1])  # Accessing the second character of the string
print(name[2])  # Accessing the third character of the string


print(name[-1])  # Accessing the last character of the string   

print(name[0:4])  # Accessing a substring from index 0 to 3

print(name[1:4])  # Accessing a substring from index 1 to 

print(name[::1])  # Accessing every first character of the string

print(name[::-2])  # Reversing the string

text = "Hello, World!"
print(text)  # Printing the entire string
print (text[7])
print (text.upper())  # Converting the string to uppercase
print (text.lower())  # Converting the string to lowercase
print (text.capitalize())  # Converting the first character to uppercase
print (text.title())  # Converting the first character of each word to uppercase
print (text.removeprefix("Hello, "))  # Removing the prefix "Hello, " from the string
print (text.removesuffix("!"))  # Removing the suffix "!" from the string       
print (text.replace("Wor", "Python"))  # Replacing "World" with "Python" in the string



print (len(text))  # Getting the length of the string   
