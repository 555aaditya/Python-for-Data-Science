# author - Aaditya Sinha
# date - 09 July 2023

# Tuples

tuple1 = (1, 2, 3, 4, 5)

# accessing elements

print(tuple1[0])   # returns 1
print(tuple1[2])   # returns 3
print(tuple1[-1],"\n")  # returns 5

# len()

print(len(tuple1),"\n")  # returns 5

# immutable nature

new_tuple = tuple1 + (4, 5)     # Concatenation
sliced_tuple = tuple1[1:3]      # Slicing

print(new_tuple)
print(sliced_tuple,"\n")

# max()

print(max(tuple1),"\n")

# min()

print(min(tuple1),"\n")

# sum()

print(sum(tuple1),"\n")

