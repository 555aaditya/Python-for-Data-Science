# author - Aaditya Sinha
# date - 30 June 2023

x = 30  # Global Scope

def a_function(a,b):
    y = a+b  # Local Scope
    return y

# Outputting
print(a_function(4,6))
print(x)