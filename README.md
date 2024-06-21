# Introduction

A compilation of small projects/scripts following my journey with learning concepts of the Python programming language.

## Details
Each sub-folder holds a `README.md` file with details for that project/script, packages necessary and execution details.

## Notes
### Common Errors
In Python, there are many different ways of classifying errors, but here are some common ones:

1. SyntaxError: Error caused by not following the proper structure (syntax) of the language.
2. NameError: Errors reported when the interpreter detects a variable that is unknown.
3. TypeError: Errors thrown when an operation is applied to an object of an inappropriate type.

### Variables and naming convention

A variable can have a short name (like x and y) or a more descriptive name (age, grade, grocery_list).

Rules for Python variables:

- A variable name must start with a letter or the underscore character. It cannot start with a number.
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _).
- Variable names are case-sensitive (num, Num, and NUM are three different variables).


### Lists
A list in Python is a sequence data type used for storing a comma-separated collection of objects in a single variable. Lists are always ordered and can contain different types of objects (strings, integers, booleans, etc.). Since they are mutable data types, lists are a good choice for dynamic data (that may be added or removed over time).

Lists can either be defined with square brackets ([]) or with the built-in list() constructor method. In any case, the values initially passed to the new list must be comma-separated.

```
# With square brackets
list_a = []

# With built-in function
list_b = list()
```

The following example showcases how lists can hold items of the same type or a mix of different types:


```
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_2 = ["one", 2, "3"]
```

Methods:

- `.count()` - A list method to count the number of occurrences of an element in a list.
- `.insert()` - A list method to insert an element into a specific index of a list.
- `.pop()` - A list method to remove an element from a specific index or from the end of a list.
- `range()` - A built-in Python function to create a sequence of integers.
- `len()` -  A built-in Python function to get the length of a list.
- `.sort()` /  `sorted()` - A method and built-in function to sort a list.
- `.append()` - A list method to insert an element at the end of the list.
- `.remove()` - A list method to remove the first instance of a specified element.

### Data Types

Python is a strongly typed language, in the sense that at runtime it prevents typing errors and it engages in little implicit type conversion or casting, i.e. converting one type to another without a specific call to a conversion function.

Python includes the following categories of built-in data types:

- String type: `str`
- Boolean type: `bool`
- Binary types: `bytes`, `bytearray`, `memoryview`
- Number types: `int`, `float`, `complex`
- Sequence Types: `list`, `range`, `tuple`
- Set types: `set`, `frozenset`
- Dictionary type: `dict`

`type()` - The type() function can be used to retrieve the data type of an object:

```
message = "Hello, world!"

print(type(message))
# Output: <class 'str'>

```

`isinstance()` - The isinstance() function can be used to test if an object is an instance of a specified type. This will print a boolean value for each function call, indicating if the object is an instance of the given type:

```
word = "purple"
languages = ("Python", "JavaScript", "Go")

print(isinstance(word, str)) # Output: True
print(isinstance(languages, list)) # Output: False
print(isinstance(languages, tuple)) # Output: True

```