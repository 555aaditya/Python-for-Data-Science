"""(1) VARIABLES"""

a = 10
b = "Aaditya"
c= 25.34

print(a)
print(b)
print(c)

"""(2) SCOPE OF VARIABLES"""

#Local Scope

def fun1():
  a=10  # a is a local variable
  print(a)

#Calling Function
fun1()

#calling 'a' outside fun1
print(a)

#Global Scope

a=100

def fun2():
  print(a)

#Calling Function
fun2()

#Calling variable outside fun2
print(a)

a = 100

def fun3():
  global a
  a = 200
  print(a)

fun3()
print(a)

a = 50

def fun4():
  a=100
  print(a)

fun4()
print(a)

"""(3) Tokens"""

# keywords - reserved words
# identifiers - variable names
# literals - data stored in a variable

"""(4) Operators"""

# Arithmetic Operators

a = 10
b = 2

print(f"sum of {a} and {b} is : ",a+b)
print(f"difference of {a} and {b} is : ",a-b)
print(f"product of {a} and {b} is : ",a*b)
print(f"quotient of {a} and {b} is : ",a/b)
print(f"modulus of {a} and {b} is : ",a%b)
print(f"exponent of {a} and {b} is : ",a**b)

# Assignment Operators

a = 10
b=0

print("assigning b the same value as a")
b=a
print("value of b is : ",b)

print("\nincrementing value of a")
a+=1
print(a)

print("\ndecrementing value of a")
a-=1
print(a)

print("\nmultiplying with 2 in the same variable")
a*=2
print(a)

print("\ndividing with 5 in the same variable")
a/=5
print(a)

print("\nmodulus with 3 in the same variable")
a%=3
print(a)

# Logical Operator

x = 10
y = 20

a = (x > 5) and (y > 10)
print(a)

b = (x > 5) and (y > 30)
print(b)

c = (x > 11) and (y > 30)
print(c)

print("\n")

d = (x > 5) or (y > 10)
print(d)

e = (x > 5) or (y > 30)
print(e)

f = (x > 11) or (y > 30)
print(f)

print("\n")

g = not (x>11)
print(g)

h = not (x<11)
print(h)

"""(5) Type Conversion"""

a = 3

print(type(a))

# convert to int
print(int(a))

# convert to float
print(float(a))

# convert to complex
print(complex(a))

# convert to string
print(str(a))

# convert to boolean
print(bool(a))

"""(6) Inputting value from user

"""

a = input("enter your name : ")
print(f"hello {a}")

print("\n")

b = int(input("enter a number : "))
c = int(input("enter another number : "))
print(f"the sum of {b} and {c} is {b+c}")

"""(7) Decision Control"""

# if statement

a = int(input("enter your age : "))

if (a>18):
  print("you can vote")

# if - else statement

a = int(input("enter your age : "))

if (a>18):
  print("you can vote")
else:
  print("you can't vote")

# if - elif - else statement

a = int(input("enter a number - "))

if (a>0):
  print("positive number");
elif (a == 0):
  print("zero");
else:
  print("negative number");

"""(8) Loops"""

# while loop
# returns until a certain condition is true

a = 0

while(a<=5):
  print(a)
  a+=1

# for loop
# runs a finite amount of times

a = 0

for i in range(0,6):
  print(a)
  a+=1
