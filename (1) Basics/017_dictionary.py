# author - Aaditya Sinha
# date - 09 July 2023

# Dictionary

dict1 = {"a": 10, "b": 20, "c": 30}
print(dict1,"\n")

# Accessing

print(dict1["b"],"\n")     # gives 20

# modifying values

dict1["a"] = 100
print(dict1,"\n")

# len()

print(len(dict1),"\n")

# adding values

dict1["d"] = 40
print(dict1,"\n")

# pop

a = dict1.pop("d")
print(a)
print(dict1,"\n")

# iterating

for key, value in dict1.items():
    print(key, value)
