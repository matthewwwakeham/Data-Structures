# Tuples
my_tuple = (1, 2, 3)

print (my_tuple[0]) # Prints index 0. Output = 1.

print (my_tuple[1]) # Prints index 1. Output = 2.

print (my_tuple[2]) # Prints index 2. Output = 3.


# Multiple Values and Unpacking
my_tuple = 1, 2 ,3

x, y, z = my_tuple

# Immutable
# my_tuple[0] = 10 # Raises an exception.

# Length
print("Length:", len(my_tuple)) # How long is it?
print(my_tuple.count(2)) # How many of x is in the tuple?