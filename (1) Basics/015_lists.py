# author - Aaditya Sinha
# date - 09 July 2023

# lists

list1 = [1,2,3,4,5]
print(list1)
print("\n")

# accessing elements

a = list1[0]    # gives 1
b = list1[2]    # gives 3
c = list1[-1]   # gives 5
print(a)
print(b)
print(c)
print("\n")

# modifying list elements

list1[0] = 10
list1[1] = 100
print(list1,"\n")

# len() - returns length

print(len(list1),"\n")  

# append() - adds an element to the end

list1.append(70)
print(list1,"\n")

# inseert(pos , value) - adds an element at the index

list1.insert(6,80)
print(list1,"\n")

# remove() - removes the first occurrence of a specified value from a list.

list1.remove(80)
print(list1,"\n")

# pop() - removes and returns the element at a specific index in a list.

a = list1.pop(1)
print(a)       # returns 100
print(list1,"\n")

# sort() - sorts the elements of a list in ascending order.

list1.sort()
print(list1,"\n")

# reverse() - reverses the order of the elements in a list.

list1.reverse()
print(list1,"\n")

# slicing

list2 = list1[1:4]
print(list2,"\n")

list3 = list1[-4:-1]
print(list3,"\n")

