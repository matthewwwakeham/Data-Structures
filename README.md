# Data-Structures
Data Structures in Python. I explore lists, tuples, dictionaries, sets, arrays, stacks, queues, trees and graphs.

## What is a List?
A list is a data structure in Python that holds an ordered collection of items. Items can be of any data type (integer, float, string, etc.). Lists are also mutable which means they can be modified after creation.

### How to Create a List
Lists can be created by enclosing items in square brackets '[ ]'.  
For example: **my_list = [1, 2, 3, 4, 5]**.

### How to Access Elements in a List
Elements in a list can be accessed via index. Indexing starts from 0 and elements can be accessed individually or in slices.  
The starting index is not included in the output.

**Code**  
```
my_list = [1, 2, 3, 4, 5]
print(my_list[0])
print(my_list[2:4])
```
**Output**  
```
Output: 1
Output: [3, 4]
```

### Various Operations
You can add an item to the end of a list with append:  

**Code**  
```
my_list.apped(6)
```

**Output**   
```
my_list = [1, 2, 3, 4, 5, 6]
```

You can insert a new item at a specific position in a list:  

**Code**  
```
my_list.insert(2, 'new_item')
```
**Output**  
```
my_list = [1, 2, new_item, 3, 4, 5, 6]
```

You can also remove an item from a list:  

**Code**  
```
del my_list[3]
```
**Output**  
```
my_list = [1, 2, new_item, 4, 5, 6]
```

You can even extract a portion of a list by slicing:  

**Code**  
```
sliced_list = my_list[1:4]
```
**Output**  
```
Output: [2, new_item, 4]
```

### Iteration
By using loops you can iterate over elements in a list.  

**Code**  
```
for item in my_list:
  print(item)
```  
**Output**  
```
All items in the list are printed: [1, 2, new_item, 4, 5, 6]
```

### List Comprehensions
List comprehensions are a concise way to create lists.   

**Code**  
```
squares = [x**2 for x in range(10)]
```
**Output**  
```
Output: squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Nested Lists
A list can contain other lists of elements.  

**Code**  
```
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### List Operations
Lists support some opperations like concatenation (+), repetition (*), membership (in) and length (len()).

**Code**  
```
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
```
**Output**  
```
Output: concatenated_list = [1, 2, 3, 4, 5 6]
```

### List Mutability
Lists are mutable which means their elements can be changed without generating a new list.

## Tuples
