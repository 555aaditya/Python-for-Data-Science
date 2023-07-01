# author - Aaditya Sinha
# date - 01 July 2023


# opening a file

# 'r' read
# 'w' write
# 'a' append

a = open("example.txt","w")    # creates a file
a = open("example.txt","r")       # read the file

# writing to a file

b = open("example.txt","a")
b.write("Hello World\n")
b.write("This is the second line\n")
b.write("This is the third line\n")
b.write("This is the fourth line\n")
b.write("This is the fifth line\n")

b = open("example.txt","r")

# reading a file

# read() - prints entire file
# readline() - prints the next line each time it is called and shifts a line forward
# readlines() - reads all the lines and returns as a list

line1 = b.readline()
line2 = b.readline()
print(line1)
print(line2,"\n")

# printing the rest

rest = b.read()
print(rest)

# closing a file
b.close()