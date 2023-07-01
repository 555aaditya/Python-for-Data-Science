# author - Aaditya Sinha
# date - 01 July 2023

# try - except block

try:
    a = int(input("Enter a Number : "))
    b = int(input("Enter a Number : "))

    div1 = a/b
    print("quotient is : ",div1)

except ZeroDivisionError:
    print("Denominator can not be 0")


