# author - Aaditya Sinha
# date - 01 July 2023

# string

a = "This is a string"
print(a)

# len() - returns length

b = len(a)
print("String length is ",b)

# upper() - returns to upper case

c = a.upper()
print(c)

# lower() - returns to lower case

d = a.lower()
print(d)

# capitalize() 

e = a.capitalize()
print(e)

# strip() - removes leading and trailing white space

f = "     hello     "
print(f)
g = f.strip()
print(g)

# string indexing 

h = "Hello World"
print(h[0])     # returns 'H'
print(h[-1])    # returns 'd'

# string slicing

print(h[0:5])   # returns 'Hello' 
print(h[-5:])   # returns 'World'
print(h[3:8],'\n')   # returns 'lo Wo'

# concatenation

i = "app"
j = "le"
print(i+j)  

# formatting

name = "Bob"
age = 30
message = "My name is {} and I am {} years old.".format(name, age)
print(message) 

# replace 

k = name.replace("Bob","Aadi")
print(k)

print(h.find("d"))