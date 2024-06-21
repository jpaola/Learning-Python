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

#### Range

The `range()` function returns a sequence of numbers, starting from `0` by default, and increments by `1` (by default), and stops before a specified number.

Syntax:
```
range(start, stop, step)
```

- `start`	- Optional. An integer number specifying at which position to start. Default is `0`
- `stop`	- Required. An integer number specifying at which position to stop (`not included`).
- `step`	- Optional. An integer number specifying the incrementation. Default is `1`


```
x = range(2, 14, 4)
print(list(x))
# Output: [2, 6, 10]
```

#### Slicing Lists I
In Python, often we want to extract only a portion of a list. Dividing a list in such a manner is referred to as slicing.

Lets assume we have a list of letters:

```
letters = ["a", "b", "c", "d", "e", "f", "g"]
```

Suppose we want to select from "b" through "f".

We can do this using the following syntax: `letters[start:end]`, where:

start is the index of the first element that we want to include in our selection. In this case, we want to start at "b", which has index 1.
end is the index of one more than the last index that we want to include. The last element we want is "f", which has index 5, so end needs to be 6.

```
sliced_list = letters[1:6]
print(sliced_list)
```

Would output:

```
["b", "c", "d", "e", "f"]
```


#### Slicing Lists II

Slicing syntax in Python is very flexible.

Take the list fruits as our example:

```
fruits = ["apple", "cherry", "pineapple", "orange", "mango"]
```

If we want to select the first `n` elements of a list, we could use the following code:

```
fruits[:n]
```

For our `fruits` list, suppose we wanted to slice the first three elements.

The following code would start slicing from index `0` and up to index `3`. Note that the fruit at index `3` (`orange`) is not included in the results.

```
print(fruits[:3])
```

Would output:

```
['apple', 'cherry', 'pineapple']
```
We can do something similar when we want to slice the `last n elements` in a list:

```
fruits[-n:]
```

For our `fruits` list, suppose we wanted to slice the last two elements.

This code slices from the element at index `-2` up through the last index.

```
print(fruits[-2:])
```

Would output:

```
['orange', 'mango']
```

Negative indices can also accomplish taking `all but n last elements` of a list.

```
fruits[:-n]
```

For our fruits example, suppose we wanted to slice all but the last element from the list.

This example starts counting from the `0` index up to the element at index `-1`.

```
print(fruits[:-1])
```

Would output:

```
['apple', 'cherry', 'pineapple', 'orange']
```


#### Sorting I
Often, we will want to sort a list in either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order.

The `.sort()` method sorts a list in alphabetical order.

```
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
names.sort()
print(names)
# Output : ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
```

`.sort()` also provides us the option to go in reverse. Instead of sorting in ascending order, we can do so in descending order.

```
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
names.sort(reverse=True)
print(names)
# Output: ['Xander', 'Willow', 'Giles', 'Buffy', 'Angel']

```

#### Sorting II
A second way of sorting a list in Python is to use the built-in function `sorted()`.

The `sorted()` function is different from the `.sort()` method in two ways:

It comes before a list, instead of after as all built-in functions do.
It generates a new list rather than modifying the one that already exists.

Using `.sort()`:
```
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
sorted_names = sorted(names)
print(sorted_names)
# Output: ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
```

Using `sorted()`:

```
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
sorted_names = sorted(names)
print(names)
# Output: ["Xander", "Buffy", "Angel", "Willow", "Giles"]
```

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