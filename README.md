# Index

* [Introduction](#introduction)
* [Common Errors](#common-errors)
* [Variables](#variables-and-naming-convention)
* [Control Flow](#control-flow)
    * [`elif` Statement](#elif-statement)
    * [`or` Operator](#or-operator)
    * [Equal Operator `==`](#equal-operator)
    * [Not Equals Operator `!=`](#not-equals-operator)
    * [Comparison Operators](#comparison-operators)
    * [`if` Statement](#if-statement)
    * [`else` Statement](#else-statement)
    * [`and` Statement](#and-statement)
    * [Boolean Values](#boolean-values)
    * [`not` Operator](#not-operator)
* [Lists](#lists)
    * [Range](#range)
    * [Slicing Lists I](#slicing-lists-i)
    * [Slicing Lists II](#slicing-lists-ii)
    * [Sorting I](#sorting-i)
    * [Sorting II](#sorting-ii)
* [Tuples](#tuples)
    * [Combining Lists](#combining-lists)
* [Data Types](#data-types)
* [Loops](#Loops)
    * [While Loops](#while-loops)
    * [For Loops](#for-loops)
        * [For Loops with Range](#for-loops-with-range)
        * [List Comprehension](#list-comprehension)
    * [Nested Loops](#nested-loops)
    * [Break Keyword](#break-keyword)
    * [Continue Keyword](#continue-keyword)
* [Functions](#functions)
    * [Types of Arguments](#types-of-arguments)
    * [Built-in Functions](#built-in-functions)
    * [Scope](#scope)
    * [Return Values](#return-values)
    * [Lambda Functions](#lambda-functions)
      * [Syntax of Lambda Functions](#syntax-of-lambda-functions)
      * [Using Lambda Functions](#using-lambda-functions)
      * [Advantages and Limitations](#advantages-and-limitations)
      * [Lambda Best Practices](#lambda-best-practices)
    * [Map Functions](#map-functions)
    * [How `map()` Works](#how-map-works)
    * [Using `map()` with Built-in Functions](#using-map-with-built-in-functions)
    * [Using `map()` with Lambda Functions](#using-map-with-lambda-functions)
    * [Multiple Iterables with `map()`](#multiple-iterables-with-map)
    * [Advantages of Using `map()`](#advantages-of-using-map)
    * [When to Use `map()`](#when-to-use-map)
    * [Alternatives to `map()`](#alternatives-to-map)
    * ['map()` Best Practices](#map-best-practices)
* [Strings](#strings)
    * [Accessing the Characters of a String](#accessing-the-characters-of-a-string)
    * [Iterate String](#iterate-string)
    * [The `in` Syntax](#the-in-syntax)
    * [String Concatenation](#string-concatenation)
    * [Immutable String](#immutable-strings)
    * [IndexError](#indexerror)
    * [Multi-Line Strings](#multi-line-strings)
    * [Escape Characters](#escape-characters)
    * [Modifying Strings](#modifying-strings)
    * [Formatting Strings](#formatting-strings)
    * [Built-in String Methods](#built-in-string-methods)
        * [Splitting Strings](#splitting-strings)
        * [Joining Strings](#joining-strings)
        * [Stripping Strings](#stripping-strings)
        * [Replacing Strings](#replacing-strings)
        * [Finding Strings](#finding-strings)
        * [Formatting Strings Using `.format()](#formatting-strings-using-format)
    * [Substrings](#substrings)
        * [Retrieving Single Characters](#retrieving-single-characters)
        * [Negative Start Index](#negative-start-index)
        * [End Index](#end-index)
        * [Negative Step Value](#negative-step-value)
        * [Keyword `in`](#keyword-in)
        * [`.find()` Method](#find-method)
* [Modules](#modules)
    * [Date and Time in Python](#date-and-time-in-python)
    * [Aliasing with ‘as’ keyword](#aliasing-with-as-keyword)
    * [Import Python Modules](#import-python-modules)
    * [random.randint() and random.choice()](#randomrandint-and-randomchoice)
    * [Module importing](#module-importing)
    * [Standard Modules](#standard-modules)
    * [Third-Party Modules](#third-party-modules)
* [Introduction to Dictionaries in Python](#introduction-to-dictionaries-in-python)
    * [Creating a Dictionary](#creating-a-dictionary)
    * [Accessing a Dictionary](#accessing-a-dictionary)
    * [Iterating Through a Dictionary](#iterating-through-a-dictionary)
    * [Adding an Entry](#adding-an-entry)
    * [Creating a Dictionary using Dictionary Comprehension](#creating-a-dictionary-using-dictionary-comprehension)
    * [Replacing an Entry in an Existing Dictionary](#replacing-an-entry-in-an-existing-dictionary)
    * [Built-in Dictionary Methods](#built-in-dictionary-methods)
        * [Safely Get a Key](#safely-get-a-key)
        * [Delete a Key](#delete-a-key)
        * [Get All Keys](#get-all-keys)
        * [Get All Values](#get-all-values)
        * [Get All Items](#get-all-items)
* [Files](#files)
  * [File Handling](#file-handling)
  * [Files and Command Line](#files-and-command-line)
  * [About __main__](#about-__main__)
  * [File Methods](#file-methods)
    * [Iterating Through Lines](#iterating-through-lines)
    * [Reading a Line](#reading-a-line)
    * [Writing a File](#writing-a-file)
    * [Appending to a File](#appending-to-a-file)
    * [The "with" Keyword](#the-with-keyword)
  * [CSV Files](#csv-files)
    * [Reading CSV Files](#reading-csv-files)
    * [Reading Different Types of CSV Files](#reading-different-types-of-csv-files)
    * [Writing a CSV File](#writing-a-csv-file)
  * [JSON Files](#json-files)
    * [Reading JSON Files](#reading-json-files)
    * [Writing a JSON File](#writing-a-json-file)
* [Classes](#classes)
  * [Instantiate Python Class](#instantiate-python-class)
  * [Python Class Variables](#python-class-variables)
  * [`class` methods](#class-methods)
  * [Dunder Methods](#dunder-methods)
    * [`__init__` method](#__init__-method)
    * [`__repr__` method](#__repr__-method)
  * [`__main__` in Python](#__main__-in-python)
  * [`type()` function](#type-function)
  * [`dir()` function](#dir-function)

## Introduction

A compilation of small projects/scripts following my journey with learning concepts of the Python programming language.

## Common Errors

In Python, there are many different ways of classifying errors, but here are some common ones:

1. SyntaxError: Error caused by not following the proper structure (syntax) of the language.
    * A `SyntaxError` is reported by the Python interpreter when some portion of the code is incorrect. This can include
      misspelled keywords, missing or too many brackets or parentheses, incorrect operators, missing or too many
      quotation marks, or other conditions.

        ```
        age = 7 + 5 = 4

        File "<stdin>", line 1
        SyntaxError: can't assign to operator
        ```

2. NameError: Errors reported when the interpreter detects a variable that is unknown.
3. TypeError: Errors thrown when an operation is applied to an object of an inappropriate type.

## Variables and naming convention

A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a
list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore
character _.

The equal sign `=` is used to assign a value to a variable. After the initial assignment is made, the value of a
variable can be updated to new values as needed.

A variable can have a short name (like x and y) or a more descriptive name (age, grade, grocery_list).

Rules for Python variables:

- A variable name must start with a letter or the underscore character. It cannot start with a number.
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _).
- Variable names are case-sensitive (num, Num, and NUM are three different variables).

## Control Flow

### `elif` Statement

The Python `elif` statement allows for continued checks to be performed after an initial `if` statement. An `elif`
statement differs from the `else` statement because another expression is provided to be checked, just as with the
initial `if` statement.

If the expression is `True`, the indented code following the `elif` is executed. If the expression evaluates to `False`,
the code can continue to an optional `else` statement. Multiple `elif` statements can be used following an initial `if`
to perform a series of checks. Once an `elif` expression evaluates to `True`, no further `elif` statements are executed.

```
# elif Statement

pet_type = "fish"

if pet_type == "dog":
  print("You have a dog.")
elif pet_type == "cat":
  print("You have a cat.")
elif pet_type == "fish":
  # this is performed
  print("You have a fish")
else:
  print("Not sure!")
```

### `or` Operator

The Python `or` operator combines two Boolean expressions and evaluates to `True` if at least one of the expressions
returns `True`. Otherwise, if both expressions are `False`, then the entire expression evaluates to `False`.

```
True or True      # Evaluates to True
True or False     # Evaluates to True
False or False    # Evaluates to False
1 < 2 or 3 < 1    # Evaluates to True
3 < 1 or 1 > 6    # Evaluates to False
1 == 1 or 1 < 2   # Evaluates to True
```

### Equal Operator `==`

The equal operator, `==`, is used to compare two values, variables or expressions to determine if they are the same.

If the values being compared are the same, the operator returns `True`, otherwise it returns `False`.

The operator takes the data type into account when making the comparison, so a string value of `"2"` is not considered
the same as a numeric value of `2`.

```
# Equal operator

if 'Yes' == 'Yes':
  # evaluates to True
  print('They are equal')

if (2 > 1) == (5 < 10):
  # evaluates to True
  print('Both expressions give the same result')

c = '2'
d = 2

if c == d:
  print('They are equal')
else:
  print('They are not equal')
```

### Not Equals Operator `!=`

The Python not equals operator, `!=`, is used to compare two values, variables or expressions to determine if they are
NOT the same. If they are NOT the same, the operator returns `True`. If they are the same, then it returns `False`.

The operator takes the data type into account when making the comparison so a value of `10` would NOT be equal to the
string value `"10"` and the operator would return `True`. If expressions are used, then they are evaluated to a value
of `True` or `False` before the comparison is made by the operator.

```
# Not Equals Operator

if "Yes" != "No":
  # evaluates to True
  print("They are NOT equal")

val1 = 10
val2 = 20

if val1 != val2:
  print("They are NOT equal")

if (10 > 1) != (10 > 1000):
  # True != False
  print("They are NOT equal")
```

### Comparison Operators

In Python, *relational operators* compare two values or expressions. The most common ones are:

* `<` less than
* `>` greater than
* `<=` less than or equal to
* `>=` greater than or equal too

If the relation is sound, then the entire expression will evaluate to `True`. If not, the expression evaluates
to `False`.

```
a = 2
b = 3
a < b  # evaluates to True
a > b  # evaluates to False
a >= b # evaluates to False
a <= b # evaluates to True
a <= a # evaluates to True
```

### `if` Statement

The Python `if` statement is used to determine the execution of code based on the evaluation of a Boolean expression.

* If the `if` statement expression evaluates to `True`, then the indented code following the statement is executed.
* If the expression evaluates to `False` then the indented code following the `if` statement is skipped and the program
  executes the next line of code which is indented at the same level as the `if` statement.

```
# if Statement

test_value = 100

if test_value > 1:
  # Expression evaluates to True
  print("This code is executed!")

if test_value > 1000:
  # Expression evaluates to False
  print("This code is NOT executed!")

print("Program continues at this point.")
```

### `else` Statement

The Python `else` statement provides alternate code to execute if the expression in an `if` statement evaluates
to `False`.

The indented code for the `if` statement is executed if the expression evaluates to `True`. The indented code
immediately following the `else` is executed only if the expression evaluates to `False`. To mark the end of the `else`
block, the code must be unindented to the same level as the starting `if` line.

```
# else Statement

test_value = 50

if test_value < 1:
  print("Value is < 1")
else:
  print("Value is >= 1")

test_string = "VALID"

if test_string == "NOT_VALID":
  print("String equals NOT_VALID")
else:
  print("String equals something else!")
```

### `and` Statement

The Python `and` operator performs a Boolean comparison between two Boolean values, variables, or expressions. If both
sides of the operator evaluate to `True` then the `and` operator returns `True`. If either side (or both sides)
evaluates to `False`, then the `and` operator returns `False`. A non-Boolean value (or variable that stores a value)
will always evaluate to `True` when used with the `and` operator.

```
True and True     # Evaluates to True
True and False    # Evaluates to False
False and False   # Evaluates to False
1 == 1 and 1 < 2  # Evaluates to True
1 < 2 and 3 < 1   # Evaluates to False
"Yes" and 100     # Evaluates to True
```

### Boolean Values

Booleans are a data type in Python, much like integers, floats, and strings. However, booleans only have two values:

* `True`
* `False`

Specifically, these two values are of the bool type. Since booleans are a data type, creating a variable that holds a
boolean value is the same as with other data types.

```
is_true = True
is_false = False

print(type(is_true)) 
# will output: <class 'bool'>
```

### `not` Operator

The Python Boolean `not` operator is used in a Boolean expression in order to evaluate the expression to its inverse
value. If the original expression was `True`, including the `not` operator would make the expression `False`, and vice
versa.

```
not True     # Evaluates to False
not False    # Evaluates to True
1 > 2        # Evaluates to False
not 1 > 2    # Evaluates to True
1 == 1       # Evaluates to True
not 1 == 1   # Evaluates to False
```

## Lists

A list in Python is a sequence data type used for storing a comma-separated collection of objects in a single variable.
Lists are always ordered and can contain different types of objects (strings, integers, booleans, etc.). Since they are
mutable data types, lists are a good choice for dynamic data (that may be added or removed over time).

Lists can either be defined with square brackets ([]) or with the built-in list() constructor method. In any case, the
values initially passed to the new list must be comma-separated.

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
- `len()` - A built-in Python function to get the length of a list.
- `.sort()` /  `sorted()` - A method and built-in function to sort a list.
- `.append()` - A list method to insert an element at the end of the list.
- `.remove()` - A list method to remove the first instance of a specified element.

### Range

The `range()` function returns a sequence of numbers, starting from `0` by default, and increments by `1` (by default),
and stops before a specified number.

Syntax:

```
range(start, stop, step)
```

- `start`    - Optional. An integer number specifying at which position to start. Default is `0`
- `stop`    - Required. An integer number specifying at which position to stop (`not included`).
- `step`    - Optional. An integer number specifying the incrementation. Default is `1`

```
x = range(2, 14, 4)
print(list(x))
# Output: [2, 6, 10]
```

### Slicing Lists I

In Python, often we want to extract only a portion of a list. Dividing a list in such a manner is referred to as
slicing.

Lets assume we have a list of letters:

```
letters = ["a", "b", "c", "d", "e", "f", "g"]
```

Suppose we want to select from "b" through "f".

We can do this using the following syntax: `letters[start:end]`, where:

start is the index of the first element that we want to include in our selection. In this case, we want to start at "b",
which has index 1.
end is the index of one more than the last index that we want to include. The last element we want is "f", which has
index 5, so end needs to be 6.

```
sliced_list = letters[1:6]
print(sliced_list)
```

Would output:

```
["b", "c", "d", "e", "f"]
```

### Slicing Lists II

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

The following code would start slicing from index `0` and up to index `3`. Note that the fruit at index `3` (`orange`)
is not included in the results.

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

### Sorting I

Often, we will want to sort a list in either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order.

The `.sort()` method sorts a list in alphabetical order.

```
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
names.sort()
print(names)
# Output : ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
```

`.sort()` also provides us the option to go in reverse. Instead of sorting in ascending order, we can do so in
descending order.

```
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
names.sort(reverse=True)
print(names)
# Output: ['Xander', 'Willow', 'Giles', 'Buffy', 'Angel']

```

### Sorting II

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

## Tuples

Tuple is one of the built-in data types in Python. A Python tuple is a sequence of comma separated items, enclosed in
parentheses (). The items in a Python tuple need not be of same data type. Like `Lists` a tuple is an ordered collection
of items. Each item in the tuple has a unique position index, starting from 0.

To access values in tuple, use the square brackets for slicing along with the index or indices to obtain value available
at that index.

```
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print ("tup1[0]: ", tup1[0]);
print ("tup2[1:5]: ", tup2[1:5]);
# Output: 
# tup1[0]:  physics 
# tup2[1:5]:  [2, 3, 4, 5]
```

** `Tuples are immutable` which means you cannot update or change the values of tuple elements.

```
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print (tup3);

# Output: (12, 34.56, 'abc', 'xyz')
```

Removing individual tuple elements is not possible. There is, of course, nothing wrong with putting together another
tuple with the undesired elements discarded.

To explicitly remove an entire tuple, just use the `del` statement.

```
tup = ('physics', 'chemistry', 1997, 2000);
print (tup);
del tup;
print ("After deleting tup : ");
print (tup);

# Output:
# ('physics', 'chemistry', 1997, 2000)
# After deleting tup :
# Traceback (most recent call last):
#    File "test.py", line 9, in <module>
#       print (tup);
# NameError: name 'tup' is not defined
```

Note an exception raised, this is because after `del tup` tuple does not exist any more

### Combining Lists

In Python, we have an assortment of built-in functions that allow us to build our programs faster and cleaner. One of
those functions is `zip()`.

The `zip()` function allows us to quickly combine associated data-sets without needing to rely on multi-dimensional
lists.

```
names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]
```

If we wanted to create a nested list that paired each name with a height, we could use the built-in function `zip()`.

The `zip()` function takes two (or more) lists as inputs and returns an object that contains a list of pairs. Each pair
contains one element from each of the inputs. This is how we would do it for our `names` and `heights` lists:

```
names_and_heights = zip(names, heights)
```

If we were to then examine this new variable names_and_heights, we would find it looks a bit strange:

```
print(names_and_heights)
# Output: <zip object at 0x7f1631e86b48>
```

This zip object contains the location of this variable in our computer’s memory. To properly print the list we must use
the built-in function `list()`:

```
converted_list = list(names_and_heights)
print(converted_list)

# Output : [('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 64)]
```

Notice two things:

1. Our data set has been converted from a zip memory object to an actual list (denoted by `[ ]`)
2. Our inner lists don’t use square brackets `[ ]` around the values. This is because they have been converted
   into `tuples` (an immutable type of list).

## Data Types

Python is a strongly typed language, in the sense that at runtime it prevents typing errors and it engages in little
implicit type conversion or casting, i.e. converting one type to another without a specific call to a conversion
function.

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

`isinstance()` - The isinstance() function can be used to test if an object is an instance of a specified type. This
will print a boolean value for each function call, indicating if the object is an instance of the given type:

```
word = "purple"
languages = ("Python", "JavaScript", "Go")

print(isinstance(word, str)) # Output: True
print(isinstance(languages, list)) # Output: False
print(isinstance(languages, tuple)) # Output: True

```

## Loops

A loop is a control structure that can execute a statement or group of statements repeatedly. Python has three types of
loops: while loops, for loops, and nested loops.

### While Loops

A while loop will repeatedly execute a code block as long as a condition evaluates to `True`.

The condition of a while loop is always checked first before the block of code runs. If the condition is not met
initially, then the code block will never run.

```
while condition:
  # Code inside
```

This loop will only run 1 time:

```
hungry = True

while hungry:
  print("Time to eat!")
  hungry = False
```

### For Loops

A for loop can be used to iterate over and perform an action one time for each element in a list.

Proper for loop syntax assigns a temporary value, the current item of the list, to a variable on each successive
iteration:

```
for <temporary variable> in <collection>:
  <action>
```

1. A `for` keyword indicates the start of a `for` loop.
2. A `<temporary variable>` that is used to represent the value of the element in the collection the loop is currently
   on.
3. An `in` keyword separates the temporary variable from the collection used for iteration.
4. A `<collection>` to loop over. In our examples, we will be using a list.
5. An `<action>` to do anything on each iteration of the loop.

Example:

```
board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

for game in board_games:
    print(game)

Output:
Settlers of Catan
Carcassone
Power Grid
Agricola
Scrabble

```

### For Loops with Range

In Python, a for loop can be used to perform an action a specific number of times in a row.

The `range()` function can be used to create a list that can be used to specify the number of iterations in a for loop.

```
# Print the numbers 0, 1, 2:
for i in range(3):
  print(i)

# Print "WARNING" 3 times:
for i in range(3):
  print("WARNING")
```

### List Comprehension

Python list comprehensions provide a concise way for creating lists. It consists of brackets containing an expression
followed by a for clause, then zero or more for or if clauses: `[EXPRESSION for ITEM in LIST <if CONDITIONAL>]`.

The expressions can be anything - any kind of object can go into a list.

A list comprehension always returns a list.

Example 1:

```
# List comprehension for the squares of all even numbers between 0 and 9
result = [x**2 for x in range(10) if x % 2 == 0]

print(result)
# [0, 4, 16, 36, 64]
```

Example 2:

```
# subtract/add/multiply/etc for each value in the list and assign to new list
prices = [30, 25, 40, 20, 20, 35, 50, 35]
new_prices = [price - 5 for price in prices]
print(new_prices)

# Output: [25, 20, 35, 15, 15, 30, 45, 30]
```

### Nested Loops

Loops can be nested inside other loops. Nested loops can be used to access items of lists which are inside other lists.
The item selected from the outer loop can be used as the list for the inner loop to iterate over.

```
groups = [["Jobs", "Gates"], ["Newton", "Euclid"], ["Einstein", "Feynman"]]

# This outer loop will iterate over each list in the groups list
for group in groups:
  # This inner loop will go through each name in each list
  for name in group:
    print(name)

```

### Break Keyword

In a loop, the break keyword escapes the loop, regardless of the iteration number. Once break executes, the program will
continue to execute after the loop.

```
numbers = [0, 254, 2, -1, 3]

for num in numbers:
  if (num < 0):
    print("Negative number detected!")
    break
  print(num)
```

In this example, the output would be:

```
0
254
2
Negative number detected!
```

### Continue Keyword

The continue keyword is used inside a loop to skip the remaining code inside the loop code block and begin the next loop
iteration.

```
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

# Print only positive numbers:
for i in big_number_list:
  if i < 0:
    continue
  print(i)
```

## Functions

A function consists of many parts, so let’s first get familiar with its core, a function definition.

**Note:** Function names in Python are written in snake_case.

```
def function_name():
  # functions tasks go here
```

There are some key components we want to note here:

The def keyword indicates the beginning of a function (also known as a function header). The function header is followed
by a name in snake_case format that describes the task the function performs. It’s best practice to give your functions
a descriptive yet concise name.
Following the function name is a pair of parenthesis ( ) that can hold input values known as parameters (more on
parameters later in the lesson!). In this example function, we have no parameters.

A colon : to mark the end of the function header.
Lastly, we have one or more valid python statements that make up the function body (where we have our python comment).

Notice we’ve indented our` # function tasks go here` comment. Like loops and conditionals, code inside a function must
be indented to show that they are part of the function.

```
def trip_welcome():
  print("Welcome to Tripcademy!") 
  print("Let's get you to your destination.")
```

**Note**: Pasting this code into the editor and clicking Run will result in an empty output terminal. The `print()`
statements within the function will not execute since our function hasn’t been used.

`SyntaxError: unexpected EOF while parsing.` will occur when we don’t populate a function with any statements. EOF
stands for “End of File” — Python is telling you that it was expecting some code in the body of the function, but it hit
the end of the file first.

The process of executing the code inside the body of a function is known as calling it (This is also known as “executing
a function”). To call a function in Python, type out its name followed by parentheses `( )`.

```
def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station.")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")

directions_to_timesSq()

# Output:
#   Walk 4 mins to 34th St Herald Square train station.
#   Take the Northbound N, Q, R, or W train 1 stop.
#   Get off the Times Square 42nd Street stop.
```

### Types of Arguments

In Python, there are 3 different types of arguments we can give a function.

1. **Positional arguments**: arguments that can be called by their position in the function definition.
2. **Keyword arguments**: arguments that can be called by their name.
3. **Default arguments**: arguments that are given default values.

Positional Arguments depend on their positions in the function call. Let’s look at a function
called `calculate_taxi_price()` that allows our users to see how much a taxi would cost to their destination 🚕.

```
def calculate_taxi_price(miles_to_travel, rate, discount):
  print(miles_to_travel * rate - discount )
```

In this function, `miles_to_travel` is *positioned* as the first parameter, rate is positioned as the second parameter,
and discount is the third. When we call our function, the position of the arguments will be mapped to the positions
defined in the function declaration.

```
# 100 is miles_to_travel
# 10 is rate
# 5 is discount
calculate_taxi_price(100, 10, 5)
```

Alternatively, we can use *Keyword Arguments* where we explicitly refer to what each argument is assigned to in the
function call. Notice in the code example below that the arguments do not follow the same order as defined in the
function declaration.

```
calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)
```

Lastly, sometimes we want to give our function parameters default values. We can provide a default value to a parameter
by using the assignment operator (=). This will happen in the function declaration rather than the function call.

Here is an example where the discount argument in our `calculate_taxi_price` function will always have a default value
of 10:

```
def calculate_taxi_price(miles_to_travel, rate, discount = 10):
  print(miles_to_travel * rate - discount )
```

When using a default argument, we can either choose to call the function without providing a value for a discount (and
thus our function will use the default value assigned) or overwrite the default argument by providing our own:

```
# Using the default value of 10 for discount.
calculate_taxi_price(10, 0.5)

# Overwriting the default value of 10 with 20
calculate_taxi_price(10, 0.5, 20)
```

### Built-in Functions

[Built-in functions](https://docs.python.org/3/library/functions.html) are functions that come built into Python ready
for us to use. Some examples of built-in functions are `print()`, `len()` and `str()`.

```
destination_name = "Bogota, Colombia"

# Built-in function: len()
length_of_destination = len(destination_name)

# Built-in function: print()
print(length_of_destination)

# Output: 16 (including spaces)
```

There are even more obscure built-in functions like `help()` where Python will print documentation for us and provide
some details:

```
help("string")
```

Would output (this is the shortened version, to view the full output try this on your IDE):

```
Help on module string:

NAME
    string - A collection of string constants.

MODULE REFERENCE
    https://docs.python.org/3.6/library/string
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.
```

### Scope

`Scope` refers to the areas where variables are visible and accessible. Variables that can be accessed anywhere in a
Python program are in the global scope. Conversely, variables that are defined within the body of structures like
classes and methods exist only in the local scope.

1. *Local Scope* - Suppose a variable is initialized within a function. This variable can only be used within that
   function and not from outside the function.

```
def my_function():
 x = 200
 print(x)

my_function()
```

2. *Global Scope* - A variable initialized in the main body is defined as a global variable and can be used anywhere in
   the code, including nested blocks, loops, etc. This is because these variables exist in the global scope of the code.

```
x = 200

def fun():
  print(x)

fun()

print(x)
```

3. *Nested Functions and Local Scope* - In the example below, a variable `x` is defined within the local scope of
   the `outer_function()` function, followed by a defined `inner_function()` function. Since `inner_function()` exists
   within the local scope of `outer_function()`, `x` can be accessed and printed within `inner_function()`:

```
def outer_function():
  x = 200
  # Initialized in outer function

  def inner_function():
    print(x)
  inner_function()

outer_function()
# Output: 200
```

### Return Values

The `return` keyword is used to return a value from a Python function. The value returned from a function can be
assigned to a variable which can then be used in the program.

In the example below, the `check_leap_year()` function returns a string that indicates if the passed parameter is a leap
year or not.

```
def check_leap_year(year):
  if year % 4 == 0:
    return str(year) + " is a leap year."
  else:
    return str(year) + " is not a leap year."

year_to_check = 2018

returned_value = check_leap_year(year_to_check)

print(returned_value)

# Output: 2018 is not a leap year.
```

Sometimes we may want to **return more than one value** from a function. We can return several values by separating them
with a comma. Take a look at this example of a function that allows users in our travel application to check the
upcoming week’s weather (starting on Monday):

```
weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']

def threeday_weather_report(weather):
  first_day = " Tomorrow the weather will be " + weather[0]
  second_day = " The following day it will be " + weather[1]
  third_day = " Two days from now it will be " + weather[2]
  return first_day, second_day, third_day
```

This function takes in a set of data in the form of a list for the upcoming week’s weather. We can get our returned
function values by assigning them to variables when we call the function:

```
monday, tuesday, wednesday = threeday_weather_report(weather_data)

print(monday)
print(tuesday)
print(wednesday)
```

This will print:

```
Tomorrow the weather will be Sunny
The following day it will be Sunny
Two days from now it will be Cloudy
```

### Lambda Functions
Lambda functions, also known as anonymous functions, are small, inline functions that can have any number of arguments but only one expression. They are defined using the `lambda` keyword and are typically used for short, simple operations.

Unlike regular functions defined with `def`, lambda functions don’t have a name and are usually used in situations where you need a simple function for a short period of time.

Let’s compare a regular function with a lambda function:
```commandline
# Regular function 

def square(x): 

    return x ** 2 

  

# Lambda function 

square_lambda = lambda x: x ** 2 
```

Both functions square the input, but the lambda function is more concise.

#### Syntax of Lambda Functions
The basic syntax of a lambda function is:

```
lambda [arguments]: [expression] 
```
Here are a couple of simple examples:

```
# Lambda function to add two numbers 

add = lambda a, b: a + b 

print(add(3, 5))  # Output: 8 

  

# Lambda function to print a name 

greeting = lambda name: f"Hello, {name}!" 

print(greeting("Alice"))  # Output: Hello, Alice! 
```

#### Using Lambda Functions
Lambda functions are most commonly used as arguments to higher-order functions such as `map()`, `filter()`, and `sorted()`. Higher-order functions are functions that can accept other functions, such as lambda functions, as arguments. Let’s look at some examples:

- *Using Lambda with map()* - The `map()` function applies the given lambda function to each item in a list:
```commandline
numbers = [1, 2, 3, 4, 5] 

squared = list(map(lambda x: x ** 2, numbers)) 

print(squared)  # Output: [1, 4, 9, 16, 25] 
```
In this example, the lambda function `lambda x: x ** 2` squares each number in the `numbers` list. The `map()` function applies this lambda to each element, resulting in a new list where every number is squared.

- *Using Lambda with filter()* - The `filter()` function creates a new list of elements for which the given lambda 
function returns True:
```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) 

print(even_numbers)  # Output: [2, 4, 6, 8, 10] 

```
Here, the lambda function `lambda x: x % 2 == 0` checks if a number is even. The `filter()` function uses this lambda to keep only the even numbers from the original list, creating a new list containing only even numbers.

- *Using Lambda wih sorted()* - The `sorted()` function can use a lambda function as a key for custom sorting:

```
students = [('Alice', 'A', 15), ('Bob', 'B', 12), ('Charlie', 'A', 20)] 

sorted_students = sorted(students, key=lambda x: x[2]) 

print(sorted_students) 

# Output: [('Bob', 'B', 12), ('Alice', 'A', 15), ('Charlie', 'A', 20)] 
```
In this case, the lambda function `lambda x: x[2]` is used as the key for sorting. It tells the `sorted()` function to use the third element (index 2) of each tuple for comparison. As a result, the list of students is sorted based on their age (the third element in each tuple).

#### Advantages and Limitations
Lambda functions offer several advantages:

- They are concise and can make code more readable for simple operations.
- They’re convenient for small, throwaway functions, especially as arguments to higher-order functions.

However, they also have limitations:

- They can only contain expressions, not statements.
- They are limited to a single expression, which can make complex operations difficult.
- They can be harder to debug due to their anonymous nature.

#### Lambda Best Practices
Use lambda functions when:

- You need a simple function for a short period.
- You’re passing a simple function as an argument to higher-order functions.

Avoid lambda functions when:

- The operation is complex or requires multiple expressions.
- You need to reuse the function multiple times (define a regular function instead).

When lambda functions become too complex, it’s often better to use a regular function defined with `def`. This improves readability and makes your code easier to maintain.

Lambda functions are a powerful feature in Python that allow you to write more concise and functional code. They’re particularly useful for simple operations and as arguments to higher-order functions. However, it’s important to use them judiciously and switch to regular functions when the logic becomes more complex.

### Map Functions
The `map()` function is a built-in function in Python that applies a given function to each item in an iterable (like a list, tuple, or string) and returns a new iterable as a result.

The basic syntax of `map()` is:

```
map(function, iterable, [iterable2, iterable3, ...]) 
```
- `function` -  is the function to apply to each item in the iterable(s)
- `iterable` - is the iterable (or optionally multiple iterables) to process

#### How `map()` Works
Let’s break down how `map()` works with a simple example:

```
def double(x): 
    return x * 2 
 
numbers = [1, 2, 3, 4, 5] 
doubled_numbers = map(double, numbers) 

print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10] 
```
In this example, `map()` applies the `double` function to each number in the `numbers` list, creating a new iterator with the results.

#### Using `map()` with Built-in Functions
We can use `map()` with Python’s built-in functions. For example, we can quickly convert a list of strings to integers:
```
# Converting strings to integers 
str_nums = ['1', '2', '3', '4', '5'] 
int_nums = list(map(int, str_nums)) 

print(int_nums)  # Output: [1, 2, 3, 4, 5] 
```
Or find the length of another list of strings:

```
# Finding the length of strings 
words = ['apple', 'banana', 'cherry'] 
word_lengths = list(map(len, words)) 

print(word_lengths)  # Output: [5, 6, 6] 
```

#### Using `map()` with Lambda Functions
But `map()` is most often used in conjunction with lambda functions for quick, one-off operations. For example, here we easily double each number in a list:

```
numbers = [1, 2, 3, 4, 5] 
doubled = list(map(lambda x: x * 2, numbers)) 

print(doubled)  # Output: [2, 4, 6, 8, 10] 
```

#### Multiple Iterables with `map()`
`map()` can also work with multiple iterables, assuming the function can take multiple inputs:

```
list1 = [1, 2, 3] 
list2 = [10, 20, 30] 
result = list(map(lambda x, y: x + y, list1, list2)) 

print(result)  # Output: [11, 22, 33] 
```

#### Advantages of Using `map()`
1. `Readability`: `map()` can make our code more concise and easier to read, especially for simple operations on iterables.
2. `Memory Efficiency`: `map()` returns an iterator, which means it doesn’t create the entire result list in memory at 
   once. This can be beneficial when working with large datasets.
3. `Functional Programming`: `map()` encourages a functional programming style, which can lead to more maintainable and 
   testable code.

#### When to Use `map()`
Use `map()` when:

- We need to apply a function to every item in an iterable.
- We want to transform data without explicitly writing a for loop.
- We are working with large datasets and want to avoid creating intermediate lists.

#### Alternatives to `map()`
While `map()` is powerful, there also are alternatives:

1. `List Comprehensions`: Often more readable for simple operations.

```
doubled = [x * 2 for x in numbers] 
```

2. `Generator Expressions`: Similar to list comprehensions but return an iterator.

```
doubled = (x * 2 for x in numbers) 
```

3. `For Loops`: More verbose but sometimes clearer for complex operations.

```
doubled = [] 
for x in numbers: 
   doubled.append(x * 2) 
```

#### `map()` Best Practices
- Use `map()` when it makes your code more readable and concise.
- For complex operations, consider using a regular function instead of a lambda.
- Remember that `map()` returns an iterator. If you need a list, wrap it with `list()`.
- When working with multiple iterables, ensure they have the same length to avoid unexpected results.

The `map()` function is a powerful tool in Python for applying a function to every item in an iterable. It’s particularly useful for data transformation tasks and can lead to more concise and functional code. However, like any tool, it’s important to use it judiciously. Sometimes a list comprehension or a simple for loop might be more appropriate.

## Strings

A string is a sequence of characters contained within a pair of single quotes `(')` or double quotes `(")`. Strings can
store
words, sentences, or whole paragraphs. They can be any length and can contain letters, numbers, symbols, and spaces.

```commandline
message1 = "I am a string"
message2 = 'I am also a string'
```

### Accessing the Characters of a String

Python strings can be indexed using the same notation as lists, since strings are lists of characters.
A single character can be accessed with bracket notation ([index]), or a substring can be accessed using slicing
([start:end]). Indexing with negative numbers counts from the end of the string.

```commandline
myString = "Hello, World!"

var_1 = myString[0]
var_2 = myString[7:]
var_3 = myString[1:4]

print("var_1: " + var_1) # Output: var_1: H
print("var_2: " + var_2) # Output: var_2: World!
print("var_3: " + var_3) # Output: var_3: ell

str = 'yellow'
str[1]     # => 'e'
str[-1]    # => 'w'
str[4:6]   # => 'ow'
str[:4]    # => 'yell'
str[-3:]   # => 'low'
```

### Iterate String

To iterate through a string in Python, `“for…in”` notation is used.

```commandline
str = "hello"
for c in str:
  print(c)
  
# h
# e
# l
# l
# o
```

### The `in` Syntax

The `in` syntax is used to determine if a letter or a substring exists in a string. It returns `True` if a match is
found,
otherwise `False` is returned.

```commandline
game = "Popular Nintendo Game: Mario Kart"

print("l" in game) # Prints: True
print("x" in game) # Prints: False
```

### String Concatenation

To combine the content of two strings into a single string, Python provides the `+` operator. This process of joining
strings is called concatenation.

```commandline
x = 'One fish, '
y = 'two fish.'

z = x + y

print(z)
# Output: One fish, two fish.
```

### Immutable Strings

Strings are immutable in Python. This means that once a string has been defined, it can’t be changed. There are no
mutating methods for strings. This is unlike data types like lists, which can be modified once they are created.

### IndexError

When indexing into a string in Python, if you try to access an index that does not exist, an `IndexError` is generated.
For example, the following code would create an `IndexError`:

```commandline
fruit = "Berry"
indx = fruit[6] # Throws an IndexError
```

### Multi-Line Strings

Strings can be long or short. For longer text, a multi-line string can be used. Multi-line strings begin and end with
three single or double quotes:

```commandline
my_string = """1 In the beginning God created the heavens and the earth. 2 Now the earth was formless and empty, 
darkness was over the surface of the deep, and the Spirit of God was hovering over the waters. 3 And God said, 
“Let there be light,” and there was light. 4 God saw that the light was good, and he separated the light from the 
darkness. 5 God called the light “day,” and the darkness he called “night.” And there was evening, and there was 
morning—the first day.
"""
```

### Escape Characters

Sometimes a string may have a character that Python tries to interpret, such as '. This will raise an error, because
the interpreter thinks the second ' marks the end of the string.

```commandline
my_string = 'It's a lovely day!'

print(my_string)

# Output
  File "main.py", line 1
    my_string = 'It's a lovely day!'
                    ^
SyntaxError: invalid syntax
```

These characters can be “escaped” by adding a backslash beforehand. The \ is called an escape character.
The backslash will not be visible if the string is printed.
This problem can be avoided by wrapping strings containing `'` characters in double quotes.

```commandline
my_string = 'It\'s a lovely day!'

print(my_string)
# Output: It's a lovely day!

#####

my_string = "It's a lovely day!"

print(my_string)
# Output: It's a lovely day!
```

Python also has a series of non-printing characters that can modify strings. For example, `\n` adds a new line and `\t`
adds a tab:

```commandline
note = "I am on top!\nI am on bottom. \n\tI am indented!"

print(note)
```

This will output:

```commandline
I am on top!
I am on bottom.
        I am indented!
```

### Modifying Strings

Python has special operators to modify strings. For example, `+` can be used to concatenate strings, and `*` can be used
to multiply a string. The keyword in can be used to see if a given character or substring exists in a string.

```commandline
string_one = "Hello, "
string_two = "World! "
combo = string_one + string_two

print(combo)
# Output: Hello, World!

new_combo = combo * 2

print(new_combo)
# Output: Hello, World! Hello, World!

if "World" in new_combo:
  print("It's here!")
  # Output: It's here!
```

Strings can also be formatted with either of the following:

* The `f/F` flag (placed before the opening quotation mark).
* The `.format()` method (requires manually adding placeholders).

### Formatting Strings

Python can use comparison operators to compare the contents of two strings. The operators behave as they do with
numeric arguments:

| Operator	 |          Term	           |                                                                             Description |
|-----------|:------------------------:|----------------------------------------------------------------------------------------:|
| `==`	     |          Equal           |                                                 	Returns True if two strings are equal. | 
| `!=`	     |        Not equal         |                                             	Returns True if two strings are not equal. |
| `<`	      |        Less than         |                   	Returns True if the left string is lexically prior the right string. | 
| `>`	      |       Greater than       |                	Returns True is the left string comes lexically after the right string. |
| `<=`	     |  Less than or equal to   |    	Returns True if the left string is equal to or lexically prior to the right string. |
| `>=`	     | Greater than or equal to | 	Returns True if the left string is equal to or comes lexically after the right string. |

### Built-in String Methods

Python has a number of built-in string methods that manipulate strings. However, when these methods are called, the
original string will not be changed, so any modifications will need to be saved to a new variable. A few useful built-in
string methods are listed below.

- `capitalize()` - Takes in a string, and returns a copy of the string in capital case.
- `casefold()` - Returns a copy of the string with all characters in lowercase.
- `center()` - Returns a new string with the specified padding.
- `count()` - Finds the number of times the specified substring occurs within a given string.
- `encode()` - Encodes a given string.
- `endswith()` - Checks whether a string ends with a given value.
- `find()` - Takes in a substring (and optionally start/end index), return the index number of the first occurrence of
  the substring inside a string.
- `format()` - Returns a string with values inserted via placeholders.
- `format_map()` - Returns the values from a given dictionary.
- `index()` - Searches through a string variable for the occurrence of a pattern or a substring.
- `isalnum()` - Returns True if all the characters in a given string are alphanumeric.
- `isalpha()` - Returns True if all characters in a string are letters of the alphabet, otherwise it returns False.
- `isascii()` - Returns True if all characters in a string are ASCII characters; otherwise, it returns False.
- `isdecimal()` - Checks whether a string consists of only decimal characters.
- `isdigit()` - Checks if all the elements in the string are digits and returns a boolean flag.
- `isidentifier()` - Takes in a string and returns True if the string is a valid Python identifier, else returns False.
- `islower()` - Takes in a string and returns True if all the letters in the string are in lowercase, else returns
  False. Ignores spaces, newlines, numeric and special characters in the string.
- `isnumeric()` - Verifies that all the characters within the string variable are numeric.
- `isprintable()` - Returns True if all characters in the string are printable or the string is empty, otherwise False
  if any character in the string is non-printable.
- `isspace()` - Checks if all the characters in a string are whitespace characters.
- `istitle()` - Checks if a given string is in title case.
- `isupper()` - Takes in a string and returns True if all the letters in the string are in uppercase, else returns
  False. Ignores spaces, newlines, numeric and special characters in the string.
- `join()` - Concatenates all items from an iterable into a single string.
- `ljust()` - Left-aligns a string with a specified fill character.
- `lower()` - Takes a string, and returns a copy of that string in which all letters are lowercase. Numbers and symbols
  are not changed.
- `lstrip()` - Removes leading characters from a string.
- `partition()` - Searches a string for a given keyword and splits that string into a three part tuple.
- `replace()` - Replace a specific substring with another substring.
- `rfind()` - Finds the last occurrence of a specified substring and returns the starting index.
- `rindex()` - Locates the highest index of the substring within a string variable.
- `rjust()` - Adds padding to the left of the given string.
- `rpartition()` - Used to split a string into three parts based on a specified separator.
- `rsplit()` - Splits a string into a list of substrings from the right end of the string based on a specified
  delimiter.
- `rstrip()` - Removes trailing characters from a string.
- `split()` - Converts a string to a list. It takes a specified delimiter and a maximum number of items to split as
  optional parameters.
- `splitlines()` - Used to split a multi-line string into a list of lines.
- `startswith()` - Checks whether or not a string starts with a given value.
- `strip()` - Eliminates any trailing spaces at the beginning and end of a string. Specific characters can be passed in
  as an argument to be removed instead.
- `swapcase()` - Takes a string and returns a copy of that string in which all lowercase letters are uppercase, and all
  uppercase letters are lowercase. Numbers and symbols are not changed.
- `title()` - Takes in a string and returns a copy of the string formatted in the title case: each word in the string is
  capitalized.
- `translate()` - Replaces characters in a string based on a mapping table.
- `upper()` - Takes a string, and returns a copy of that string in which all letters are uppercase. Numbers and symbols
  are not changed.
- `zfill()` - Returns a string with zeros padding the left side based on the integer given.
- `maketrans()` - Returns a transition table based on the given strings.

### Splitting Strings

The string method `.split()` splits a string into a list of items:

- If no argument is passed, the default behavior is to split on whitespace.
- If an argument is passed to the method, that value is used as the delimiter on which to split the string.

Example 1:
General use of the `.split()` method on a string.

```commandline
text = "Silicon Valley"

print(text.split())     
# Prints: ['Silicon', 'Valley']

print(text.split('i'))  
# Prints: ['S', 'l', 'con Valley']
```

Example 2:
Here we are looking to grab the list of author last names within a string containing author names.

```commandline
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,
Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")

print(author_names)

# Output: ['Audre Lorde', 'Gabriela Mistral', 'Jean Toomer', 'An Qi', 'Walt Whitman', 'Shel Silverstein', 
'Carmen Boullosa', 'Kamala Suraiyya', 'Langston Hughes', 'Adrienne Rich', 'Nikki Giovanni']

####

author_last_names = []

for name in author_names:
  author_last_names.append(name.split()[-1])

print(author_last_names)

# Output: ['Lorde', 'Mistral', 'Toomer', 'Qi', 'Whitman', 'Silverstein', 'Boullosa', 'Suraiyya', 'Hughes', 'Rich', 
'Giovanni']
```

Note here that when using `name.split()` the behavior is to split on whitespace so the return value will be a lists of
each author's surnames. When
specifying `[-1]` we are specifying that we only want the last element on the list. In this case the last name of each
author.

Here's what the `name.split()` within the previous code looks like:

```commandline
['Audre', 'Lorde']
['Gabriela', 'Mistral']
['Jean', 'Toomer']
['An', 'Qi']
['Walt', 'Whitman']
['Shel', 'Silverstein']
['Carmen', 'Boullosa']
['Kamala', 'Suraiyya']
['Langston', 'Hughes']
['Adrienne', 'Rich']
['Nikki', 'Giovanni']
```

### Joining Strings

The string method `.join()` concatenates a list of strings together to create a new string joined with the desired
delimiter. The `.join()` method is run on the delimiter and the array of strings to be concatenated together is passed
in as an
argument.

```commandline
my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
print(' '.join(my_munequita))
# => 'My Spanish Harlem Mona Lisa'

print(''.join(my_munequita))
# => 'MySpanishHarlemMonaLisa'
```

### Stripping Strings

The string method `.strip()` can be used to remove characters from the beginning and end of a string.

A string argument can be passed to the method, specifying the set of characters to be stripped. With no arguments to the
method, whitespace is removed.

```
text1 = '   apples and oranges   '
text1.strip()       # => 'apples and oranges'

text2 = '...+...lemons and limes...-...'

# Here we strip just the "." characters
text2.strip('.')    # => '+...lemons and limes...-'

# Here we strip both "." and "+" characters
text2.strip('.+')   # => 'lemons and limes...-'

# Here we strip ".", "+", and "-" characters
text2.strip('.+-')  # => 'lemons and limes'
```

### Replacing Strings

Replace a specific substring with another substring.

```commandline
string.replace(old, new, count)
```

The `.replace()` string method takes in three parameters:

- `old`: The substring to search for. (Required)
- `new`: The substring to replace. (Required)
- `count`: A number specifying how many occurrences of the old value to replace. Default is all occurrences.

```commandline
var = "I like cats and cats like me"
var = var.replace("like", "LOVE")
print(var)
# Output: "I LOVE cats and cats LOVE me"

var = "I like cats and cats like me"
var = var.replace("like", "LOVE", 1)
print(var)
# Output "I LOVE cats and cats like me"
```

### Finding Strings

The Python string method `.find()` returns the index of the first occurrence of the string passed as the argument. It
returns `-1` if no occurrence is found.

```commandline
mountain_name = "Mount Kilimanjaro"
print(mountain_name.find("o")) # Prints 1 in the console.
```

### Formatting Strings using `.format()`

The Python string method `.format()` replaces empty brace (`{}`) placeholders in the string with its arguments.

If keywords are specified within the placeholders, they are replaced with the corresponding named arguments to the
method.

Example 1:
General usage of `.format()`

```commandline
msg1 = 'Fred scored {} out of {} points.'
msg1.format(3, 10)
# => 'Fred scored 3 out of 10 points.'

msg2 = 'Fred {verb} a {adjective} {noun}.'
msg2.format(adjective='fluffy', verb='tickled', noun='hamster')
# => 'Fred tickled a fluffy hamster.'
```

Example 2:
Using built-in String methods along with `.format()`:

```commandline
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(",")

highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip(" "))

highlighted_poems_details = []
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))

titles = []
poets = []
dates = []

for detail in highlighted_poems_details:
  titles.append(detail[0])
  poets.append(detail[1])
  dates.append(detail[-1])

for i in range(0,len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))
```

This will output the following:

```The poem Afterimages was published by Audre Lorde in 1997
The poem The Shadow was published by William Carlos Williams in 1915
The poem Ecstasy was published by Gabriela Mistral in 1925
The poem Georgia Dusk was published by Jean Toomer in 1923
The poem Parting Before Daybreak was published by An Qi in 2014
The poem The Untold Want was published by Walt Whitman in 1871
The poem Mr. Grumpledump's Song was published by Shel Silverstein in 2004
The poem Angel Sound Mexico City was published by Carmen Boullosa in 2013
The poem In Love was published by Kamala Suraiyya in 1965
The poem Dream Variations was published by Langston Hughes in 1994
The poem Dreamwood was published by Adrienne Rich in 1987
```

### Substrings

A substring is a sequence of characters that are part of an original `string`. In Python, substrings can be obtained by
using the slicing feature on a string variable. A slice can be made in a specific position within the string or it can
be made at the default index.

A slice is made by using the open `[` and closed `]` square brackets next to a string variable. Inside the brackets, the
position can be given:

`string[start:end:step]`

- `start` defaults to 0 and gives the initial position the slice will start from.
- `end` defaults to -1 and is the position where the slicing will end.
- `step` defaults to 1 and indicates the number of steps to take in between indexes.

### Retrieving Single Characters

The following examples show different ways of obtaining substrings from an original string `name`. When only one index
is specified, a single character is returned. An index of `0` retrieves the first character of the string. Negative
numbers work on the string backwards. For example, index `-1` retrieves the last character of the string.

```commandline
name = "Code Ninja"
print(name[0])

# Output: C

####

print(name[-1])

# Output: a
```

### Negative Start Index

Using a negative start index `(-n)` with the default end value accesses the last `n` characters of the string. The
following
gives access to the last three characters of the string:

```commandline
print(name[-3:])

# Output: nja
```

### End Index

To specify only an end index, use `[:n]`, where n is the ending position. This will return the first `n` characters.

```
print(name[:4])

# Output: Code
```

### Negative Step Value

Given a negative step value, returns the results backward:

```commandline
reversed = name[::-2]
print(reversed)

# Output: anNeo
```

### Keyword `in`

The `in` keyword can be used to check for a specific substring, like in the example below:

```
print('de' in name)

# Output: True
```

### `.find()` Method

The string method `.find()` can also be used to find a subset. It returns the index of the first occurrence of the
substring. If the substring is not found, it returns `-1`.

```commandline
name = "Code Ninja"
print(name.find('ni'))
```

## Modules

In the world of programming, we care a lot about making code reusable. In most cases, we write code so that it can be
reusable for ourselves. But sometimes we share code that’s helpful across a broad range of situations.

In this lesson, we’ll explore how to use tools other people have built in Python that are not included automatically for
you when you install Python. Python allows us to package code into `files` or `sets` of files called `modules`.

A module is a collection of Python declarations intended broadly to be used as a tool. Modules are also often referred
to as “libraries” or “packages” — a package is really a directory that holds a collection of modules.

Usually, to use a module in a file, the basic syntax you need at the top of that file is:

```commandline
from module_name import object_name
```

Often, a library will include a lot of code that you don’t need that may slow down your program or conflict with
existing code. Because of this, it makes sense to only import what you need.

One common library that comes as part of the Python Standard Library is `datetime`. `datetime` helps you work with dates
and times in Python.

```commandline
from datetime import datetime

current_time = datetime.now()
print(current_time) # Should print your current time for example '2024-07-24 20:57:42.479196'
```

### Date and Time in Python

Python provides a module named datetime to deal with dates and times.

It allows you to set `date`, `time` or both `date` and `time` using the `date()`, `time()` and `datetime()` functions
respectively, after importing the `datetime` module.

```commandline
import datetime
feb_16_2019 = datetime.date(year=2019, month=2, day=16)
feb_16_2019 = datetime.date(2019, 2, 16)
print(feb_16_2019) #2019-02-16

time_13_48min_5sec = datetime.time(hour=13, minute=48, second=5)
time_13_48min_5sec = datetime.time(13, 48, 5)
print(time_13_48min_5sec) #13:48:05

timestamp= datetime.datetime(year=2019, month=2, day=16, hour=13, minute=48, second=5)
timestamp = datetime.datetime(2019, 2, 16, 13, 48, 5)
print (timestamp) #2019-01-02 13:48:05
```

### Aliasing with ‘as’ keyword

Notice that when we want to invoke the `randint()` function we call `random.randint()`. This is the default behavior
where Python offers a namespace for the module. A namespace isolates the `functions`, `classes`, and `variables`
defined in the module from the code in the file doing the importing. Your *local namespace*, meanwhile, is where your
code is run.

Python defaults to naming the namespace after the module being imported, but sometimes this name could be ambiguous or
lengthy. Sometimes, the module’s name could also conflict with an object you have defined within your local namespace.

Fortunately, this name can be altered by *aliasing* using the `as` keyword:

```commandline
import module_name as name_you_pick_for_the_module
```

Here is the `as` keyword in use:

```commandline
# Aliasing matplotlib.pyplot as plt
from matplotlib import pyplot as plt
plt.plot(x, y)

# Aliasing calendar as c
import calendar as c
print(c.month_name[1])
```

### Import Python Modules

The Python **import** statement can be used to import Python modules from other files.

Modules can be imported in three different ways: `import module`, `from module import functions`,
or `from module import *`.

`from module import *` is discouraged, as it can lead to a cluttered local namespace and can make the namespace unclear.

The `*` is known as a `“wildcard”` and matches anything and everything. This syntax is considered dangerous because
it could *pollute* our local namespace. Pollution occurs when the same name could apply to two possible things. For
example, if you happen to have a function `floor()` focused on floor tiles, using `from math import *` would also import
a function `floor()` that rounds down floats.

```commandline
# Three different ways to import modules:
# First way
import module
module.function()

# Second way
from module import function
function()

# Third way
from module import *
function()
```

### random.randint() and random.choice()

In Python, the `random` module offers methods to simulate non-deterministic behavior in selecting a random number from a
range and choosing a random item from a list.

The `randint()` method provides a uniform random selection from a range of integers. The `choice()` method provides a
uniform selection of a random element from a sequence.

```commandline

# Returns a random integer N in a given range, such that start <= N <= end
# random.randint(start, end)
r1 = random.randint(0, 10)  
print(r1) # Random integer where 0 <= r1 <= 10

# Prints a random element from a sequence
seq = ["a", "b", "c", "d", "e"]
r2 = random.choice(seq)
print(r2) # Random element in the sequence
```

### Module importing

In Python, you can import and use the content of another file using `import filename`, if it is in the same folder as
the current file you are writing.

```commandline

# file1 content
# def f1_function():
#	  return "Hello World"

# file2
import file1

# Now we can use f1_function, because we imported file1
f1_function()
```

### Standard Modules
Python comes with several different built-in modules that provide a variety of functions. They include:

* The `collections` module provides additional collection types.
* The `functools` module provides functions supporting a `functional programming` approach.
* The `glob` module allows matching file paths per `Unix` shell rules.
* The `json` module provides functions for dealing with `JSON` objects.
* The `math` module provides useful mathematical functions.
* The `random` module provides functions for dealing with random numbers.
* The `time` module provides various functions for dealing with time.

### Third-Party Modules
Python has a very broad selection of third-party modules that are devoted to particular tasks.

These are third-party Python modules that have topic entries:

* `NumPy`: a popular open-source Python library used for complex mathematical operations and multi-dimensional `arrays`.
* `Pandas`: a popular open-source Python module used for data analysis and manipulation.

Below is a selection of other third-party modules of note:

* `PySpark` - A Python API for Apache Spark, consisting of several modules.
* `Pytorch` - An open-source framework that offers an optimized tensor library for deep learning.
* `tqdm` - A module that allows the generation of progress bars in Python.

## Introduction to Dictionaries in Python

A dictionary is a data set of key-value pairs. It provides a way to map pieces of data to each other and allows for
quick access to values associated with keys.

In Python, dictionaries are dynamic and mutable, which means they can change.

Note: As of Python version 3.7, dictionaries are ordered based on insertion, but this is not the case in previous
versions.

**Syntax**

```commandline
dictionary_name = { key1: value1,  key2: value2,  key3: value3 }
```

Each entry in a dictionary is a key-value pair. Each pair is separated by a comma.

Dictionary keys must be immutable types such as numbers and strings because keys should not change. Keys cannot be lists
because lists are mutable, and it will raise a `TypeError`.

Values can be any type, such as strings, numbers, lists, and even other dictionaries.

### Creating a Dictionary

An empty dictionary is created with curly braces:

```commandline
diner = {}
```

An empty dictionary can also be created using the built-in function, `dict()`, with no arguments:

```commandline
diner = dict()
```

A dictionary with entries:

```commandline
coffee_shop = { "cold brew": 3.50, "latte": 4.25, "cappuccino": 3.99 }
```

The three key-value pairs in the `coffee_shop` dictionary:

```commandline
"cold brew": 3.50
"latte": 4.25
"cappuccino": 3.99
```

### Accessing a Dictionary

The values in a dictionary can be accessed by passing the associated key name in a `dictionary[key]` syntax:

```commandline
coffee_shop = { "cold brew": 3.50, "latte": 4.25, "cappuccino": 3.99 }

print(coffee_shop["cold brew"])
# Output: 3.5
```

When a value is retrieved from a key that does not exist, `KeyError` is raised. If a value is assigned to a key that
does not exist, the new key-value pair will be added. If a value is assigned to an existing dictionary key, it replaces
the existing value.

### Iterating Through a Dictionary

There are several ways to iterate through a dictionary depending on which data that is accessed: keys, values, or both.

The following consists of four `for` loops that iterate through the `coffee_shop` dictionary:

```commandline
coffee_shop = { "cold brew": 3.50, "latte": 4.25, "cappucino": 3.99 }

for key in coffee_shop.keys():
    print(key)

for value in coffee_shop.values():
    print(value)

for item in coffee_shop.items():
    print(item)

for key, value in coffee_shop.items():
    print(key, value)
    
 # Output:
    cold brew
    latte
    cappucino
    3.5
    4.25
    3.99
    ('cold brew', 3.5)
    ('latte', 4.25)
    ('cappucino', 3.99)
    cold brew 3.5
    latte 4.25
    cappucino 3.99
```

The for loops access and print each key, value, key-value tuple, and individual key-values in coffee_shop, respectively.

### Adding an Entry

To add an entry, use square brackets to create an index into a `new_key` and assign it a `new_value`:

```commandline
my_dict[new_key] = new_value
```

### Creating a Dictionary using Dictionary Comprehension

Like a list comprehension, a dictionary comprehension is a Pythonic way to create a dictionary. They can be used to
filter and manipulate data in tons of useful ways. The syntax is as follows:

```commandline
new_dict = { expression for key, value in old_dict.items() if condition }
```

The `if` condition at the end is optional, but is a great tool for filtering data. For example, given a dictionary with
a person’s name and age, make a new dictionary that only contains people with an age under 25:

```commandline
person_age = { "Mark": 55, "Shiela": 28, "Bryce": 24, "Jim": 41, "Eric": 33, "Ally": 23 }
person_age_filtered = { name: age for name, age in person_age.items() if age < 25 }
```

The expression is `name: age`, as that’s how the new dictionary will be formatted. Then, the typical for loop
iteration, `for name, age in person_age.items()`. Lastly, the if condition filters out the results.

The expression can also perform operations on the data being extracted. For example, to create a dictionary with key
value pairs of a number and its square given a list of numbers:

```commandline
nums_list = [ 1, 2, 3, 4, 5 ]
nums_squared = { num: num**2 for num in nums_list }
```

`nums_squared` will produce a result of: `{ 1: 1, 2: 4, 3: 9, 4: 16, 5: 25 }`

### Replacing an Entry in an Existing Dictionary

If a key needs to be updated in an existing dictionary, it uses the same syntax for adding an entry into a
dictionary (`dictionary[new_key] = new_value)`, but instead, the new_key argument is replaced with an already existing
key in the desired dictionary `(dictionary[existing_key] = new_value)`.

```commandline
person_age = { "Mark": 55, "Shiela": 28, "Bryce": 24, "Jim": 41, "Eric": 33, "Ally": 23 }

# Looks like it's Mark's Birthday! Let's update our dictionary to reflect his new age:
person_age['Mark'] = 56
```

Now, when the `"Mark"` key is accessed from the `person_age` dictionary, it will produce value 56.

### Built-in Dictionary Methods

- `.clear()` - Removes all entries in a dictionary.
- `.copy()` - Returns a copy of a dictionary.
- `.fromkeys()` - Returns a dictionary with the specified keys.
- `.get()` - Returns the value of a dictionary entry for a specified key, with an optional fallback value.
- `.items()` - Returns a list of tuples for each key-value pair in a dictionary.
- `.keys()` - Returns a list of keys for a dictionary.
- `.pop()` - Returns the value of a specified key, then removes the key-value pair from a dictionary.
- `.popitem()` - Returns the last inserted key-value pair from a dictionary as a tuple, and removes the entry.
- `.setdefault()` - Returns the value of a specified key. If the key does not exist, it is inserted with the specified
  value.
- `.update()` - Adds the entries in a specified dictionary, or iterable of key-value pairs, to a dictionary.
- `.values()` - Returns a view of values for a dictionary.

#### Safely Get a Key

We can’t predict every key a user may call and add all of those placeholder values to our dictionary.

Dictionaries have a `.get()` method to search for a value instead of `the_dict[key]` notation we have been using.
If the key you are trying to `.get()` does not exist, it will return `None` by default:

```commandline
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

# this line will return 632:
building_heights.get("Shanghai Tower")

# this line will return None:
building_heights.get("My House")
```

You can also specify a value to return if the key does not exist.

For example, we might want to return a building height of 0 if our desired building is not in the dictionary:

```commandline
print(building_heights.get('Shanghai Tower', 0)) # Prints 632
print(building_heights.get('Mt Olympus', 0)) # Prints 0
print(building_heights.get('Kilimanjaro', 'No Value')) # Prints 'No Value'
```

#### Delete a Key

Sometimes we want to get a key and remove it from the dictionary. Imagine we were running a raffle, and we have this
dictionary mapping ticket numbers to prizes:

```commandline
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
```

When we get a ticket number, we want to return the prize and also remove that pair from the dictionary, since the prize
has been given away. We can use `.pop()` to do this. Just like with `.get()`, we can provide a default value to return
if the key does not exist in the dictionary:

```commandline
print(raffle.pop(320291, "No Prize"))
# Prints "Gift Basket"
print(raffle)
# Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(100000, "No Prize"))
# Prints "No Prize"
print(raffle)
# Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(872921, "No Prize"))
# Prints "Concert Tickets"
print(raffle)
# Prints {223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}
```

`.pop()` works to delete items from a dictionary, when you know the key value.

#### Get All Keys

Sometimes we want to operate on all of the keys in a dictionary. For example, if we have a dictionary of students in a
math class and their grades:

```commandline
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
```

We want to get a roster of the students in the class, without including their grades. We can do this with the
built-in `list()` function:

```commandline
print(list(test_scores))
# Prints ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]
```

Dictionaries also have a `.keys()` method that returns a `dict_keys` object. A `dict_keys` object is a view object,
which provides a look at the current state of the dictionary, without the user being able to modify anything.
The `dict_keys` object returned by `.keys()` is a set of the keys in the dictionary. You cannot add or remove elements
from a `dict_keys` object, but it can be used in the place of a list for iteration:

```commandline
for student in test_scores.keys():
    print(student)
```

will yield:

```commandline
Grace
Jeffrey
Sylvia
Pedro
Martin
Dina
```

#### Get All Values

Dictionaries have a `.values()` method that returns a `dict_values` object (just like a `dict_keys` object but for
values!) with all the values in the dictionary. It can be used in the place of a list for iteration:

```
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

for score_list in test_scores.values():
 print(score_list)
```

will yield:

```commandline
[80, 72, 90]
[88, 68, 81]
[80, 82, 84]
[98, 96, 95]
[78, 80, 78]
[64, 60, 75]
```

There is no built-in function to get all the values as a list, but if you *really* want to, you can use:

```commandline
list(test_scores.values())
```

However, for most purposes, the dict_values object will act the way you want a list to act.

#### Get All Items

You can get both the keys and the values with the `.items()` method. Like `.keys()` and `.values()`, it returns
a `dict_list` object. Each element of the `dict_list` returned by `.items()` is a tuple consisting of:

```commandline
(key, value)
```

To iterate through, you can use the following syntax:

```commandline
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
 print(company + " has a value of " + str(value) + " billion dollars. ")
```

which will yield the following output:

```commandline
Apple has a value of 184 billion dollars.
Google has a value of 141.7 billion dollars.
Microsoft has a value of 80 billion dollars.
Coca-Cola has a value of 69.7 billion dollars.
Amazon has a value of 64.8 billion dollars.
```

## Files
Computers use file systems to store and retrieve data. Each file is an individual container of related information. If you’ve ever saved a document, downloaded a song, or even sent an email, you’ve created a file on some computer somewhere.

Files are named locations on the computer’s disk that permanently store information for future use of its data. They 
are used to permanently store data in non-volatile memory (e.g., hard disk) as opposed to volatile sources like Random Access Memory `RAM`, which loses its data when the computer is turned off.

### File Handling
Handling files is a common feature that many languages use to work with the computer's file system. In Python, file 
handling is possible and usually takes place in the following order:

1. Open (or create) the file.
2. Perform operations on the file, such as reading or writing to it.
3. Close the file to free up any resources used.

**Example 1**
The small example below demonstrates how one process of file handling could work:

```commandline
# Create, or overwrite, a file and open for writing
file = open("myfile.txt", "w")
file.write("Hello world!")
file.close()

# Open existing file to read and print text content
file = open("myfile.txt", "r")
first_two_bytes = file.read(2)
next_three_bytes = file.read(3)
the_rest = file.read()
print(first_two_bytes, next_three_bytes, the_rest, sep="\n")
file.close()
```

In the first part of the code example, a plain text file named `myfile.txt` was created and opened in the `"w"` 
"write"-mode. Then a piece of text was written to the file and closed afterward.

In the next part, a few calls to the `.read()` method are assigned to some `variables` and then each one is printed 
on a new line:

```commandline
He
llo
 world!
```

**Example 2**
Let’s say we had a file called `real_cool_document.txt` with these contents:

```commandline
Wowsers!
```

We could read that file from another, named `script.py`, as follows:

```commandline
with open('real_cool_document.txt') as cool_doc:
  cool_contents = cool_doc.read()
print(cool_contents)

```

This opens a file object called `cool_doc` and creates a new indented block where you can read the contents of the 
opened file. We then read the contents of the file `cool_doc` using `cool_doc.read()` and save the resulting string 
into the variable `cool_contents`. Then we print `cool_contents`, which outputs the statement `Wowsers!`.

### Files and Command Line
Python files can be run as `command line arguments` using their filename.

```commandline
python example_file.py

# Alternate
python3 example_file.py

```

This executes a file's inner `__main__` environment variable, which then runs the code within. This code may include 
variable declarations, operations, and function calls.

### About __main__
Any time a `.py` file is run and interpreted, certain variables are set up and linked with the file. This includes `__main__` environment variable, which is assigned as the file’s `__name__` variable. All Python programs feature these variables, which can be verified as in the following example:

```commandline
# example.py

import imported_example

if __name__ == '__main__':
  print('Example file: ' + __name__)

print('Imported example file: ' + imported_example.__name__)

```

When `python example.py` is run on the command line, the following will be printed:

```commandline
Example file: __main__
Imported example file: imported_example_file
```

The main fine being run, `example.py`, has its `__name__` set to `__main__` while the `imported_example.py` file's 
`__name__` is literally set to the name of the file.

### File Methods

* `.close()` - Allows the user to close an open file within the IDE.
* `.read()` - Allows the user to read the contents of an open file and return the number of associated bytes.
* `.readline()` - Returns the first line of content from an open file.
* `.remove()` - Allows the user to delete a file if it exists.
* `.rmdir()` - Allows the user to delete a folder if it exists.
* `.seek()` - Allows the user to move the location of the file handle's reference point within an open file from one 
  place to another.
* `.truncate()` - Allows the user to resize the file to a given number of bytes when the file is accessed through the 
append mode.
* `.unlink()` - Allows the user to delete a file path if it exists.
* `.writable()` - Allows the user to check if a file is writable or not. The function will return True if the file is 
writable and accessed in append or write mode, and False if it was accessed in read mode.
* `.write()` - Adds additional text to a file when the file is opened in append mode.
* `Context Managers` - Context managers allow users to perform operations within a certain overarching context.

#### Iterating Through Lines
When we read a file, we might want to grab the whole document in a single string, like `.read()` would return. But what if we wanted to store each line in a variable? We can use the `.readlines()` function to read a text file line by line instead of having the whole thing. Suppose we have a file:

*keats_sonnet.txt*
```commandline
To one who has been long in city pent,
’Tis very sweet to look into the fair
And open face of heaven,—to breathe a prayer
Full in the smile of the blue firmament.
```

*script.py*
```commandline
with open('keats_sonnet.txt') as keats_sonnet:
  for line in keats_sonnet.readlines():
    print(line)
```
The above script creates a temporary file object called `keats_sonnet` that points to the file **keats_sonnet.txt.** 
It then iterates over each line in the document and prints the entire file out.

#### Reading a Line
Sometimes you don’t want to iterate through a whole file. For that, there’s a different file method, `.readline()`, which will only read a single line at a time. If the entire document is read line by line in this way subsequent calls to `.readline()` will not throw an error but will start returning an empty string (`""`). Suppose we had this file:

*millay_sonnet.txt*

```commandline
I shall forget you presently, my dear,
So make the most of this, your little day,
Your little month, your little half a year,
Ere I forget, or die, or move away,
```

*script.py*

```commandline
with open('millay_sonnet.txt') as sonnet_doc:
  first_line = sonnet_doc.readline()
  second_line = sonnet_doc.readline()
  print(second_line)
```
This script also creates a file object called `sonnet_doc` that points to the file **millay_sonnet.txt**. It then 
reads in the first line using `sonnet_doc.readline()` and saves that to the variable `first_line`. It then saves the second line (`So make the most of this, your little day,`) into the variable `second_line` and then prints it out.

#### Writing a File
Reading a file is all well and good, but what if we want to create a file of our own? With Python we can do just that. It turns out that our `open()` function that we’re using to open a file to read needs another argument to open a file to write to.

*script.py*
```commandline
with open('generated_file.txt', 'w') as gen_file:
  gen_file.write("What an incredible file!")
```

Here we pass the argument `'w'` to `open()` in order to indicate to open the file in write-mode. The default argument is `'r'` and passing `'r'` to `open()` opens the file in read-mode as we’ve been doing.

This code creates a new file in the same folder as *script.py* and gives it the text `What an incredible file!`. It’s 
important to note that if there is already a file called `generated_file.txt` it will completely overwrite that file, erasing whatever its contents were before.

#### Appending to a File
There is a way to simply add a line to a file without completely deleting it. Instead of opening the file using the 
argument `'w'` for write-mode, we open it with `'a'` for append-mode. If we generate a file with the following contents:

*generate_file.txt*
```commandline
This is a popular file...
```

Then we can add another line to that file with the following code:

*script.py*
```commandline
with open('generated_file.txt', 'a') as gen_file:
  gen_file.write("\n... and it still is")
```

In the code above we open a file object in the temporary variable `gen_file`. This variable points to the file 
*generated_file.txt* and, since it’s open in append-mode, adds the string `\n... and it still is` to the file. The 
newline character `\n` moves to the next line before adding the rest of the string. If you were to open the file 
after running the script, it would look like this:

*generated_file.txt*
```commandline
This was a popular file...
... and it still is
```

Notice that opening the file in append-mode, with `'a'` as an argument to `open()`, means that using the file 
object’s `.write()` method appends whatever is passed to the end of the file. If we were to run *script.py* again, 
this would be what *generated_file.txt* looks like:

*generated_file.txt*
```commandline
This was a popular file...
... and it still is
... and it still is
```

Notice that we've appended `"n\... and it still is"` to the file a second time! This is because in *script.py* we 
opened *generated_file.txt* in append-mode.

#### The "with" keyword
We’ve been opening these files with this `with` block, but it seems a little weird that we can only use our file 
variable in the indented block.

Why is that?

The `with` keyword invokes something called a context manager for the file that we’re calling `open()` on.
This *context manager* takes care of opening the file when we call `open()` and then closing the file after we leave 
the indented block.

Why is closing the file so complicated? 

Well, most other aspects of our code deal with things that Python itself controls. All the variables you create: *integers*, *lists*, *dictionaries* — these are all Python objects, and Python knows how to clean them up when it’s done with them. Since your files exist outside your Python script, we need to tell Python when we’re done with them so that it can close the connection to that file. Leaving a file connection open unnecessarily can affect performance or impact other programs on your computer that might be trying to access that file.

The `with` syntax replaces older ways to access files where you need to call `.close()` on the file object manually.
We can still open up a file and append to it with the old syntax, as long as we remember to close the file connection afterward.

```commandline
fun_cities_file = open('fun_cities.txt', 'a')

# We can now append a line to "fun_cities".
fun_cities_file.write("Montréal")

# But we need to remember to close the file
fun_cities_file.close()
```

In the above script we added “Montréal” as a new line in our file *fun_cities.txt*. However, since we used the 
older-style syntax, we had to remember to close the file afterward. Since this is necessarily more verbose (requires at least one more line of code) without being any more expressive, using `with` is preferred.

### CSV Files
Text files aren’t the only thing that Python can read, but they’re the only thing that we don’t need any additional 
parsing library to understand. CSV files are an example of a text file that impose a structure to their data. CSV 
stands for *Comma-Separated Values* and CSV files are usually the way that data from spreadsheet software (like 
Microsoft Excel or Google Sheets) is exported into a portable format. A spreadsheet that looks like the following,

| Name	          |      Username	      |                  Email |
|----------------|:-------------------:|-----------------------:|
| Roger Smith    |       rsmith	       |  wigginsryan@funmail.com |
| Michelle Beck  |       mlbeck	       |     hcosta@funmail.com |
| Ashley Barker  |      a_bark_x	      |    a_bark_x@funmail.com |
| Lynn Gonzales  |    goodmanjames	    | lynniegonz@funmail.com |
| Jennifer Chase |       chasej        |     jchase@funmail.com |
| Charles Hoover |       choover       |    choover89@funmail.com |
| Adrian Evans   |       adevans       |    adevans98@funmail.com |
| Susan Walter   |      susan82	       |    swilliams@funmail.com |
| Stephanie King |   stephanieking	    | sking@funmail.com |
| Erika Miller   |     jessica32	      |   ejmiller79@funmail.com |

In a CSV file that same exact data would be rendered like this:

*users.csv*

```commandline
Name,Username,Email
Roger Smith,rsmith,wigginsryan@funmail.com
Michelle Beck,mlbeck,hcosta@funmail.com
Ashley Barker,a_bark_x,a_bark_x@funmail.com
Lynn Gonzales,goodmanjames,lynniegonz@funmail.com
Jennifer Chase,chasej,jchase@funmail.com
Charles Hoover,choover,choover89@funmail.com
Adrian Evans,adevans,adevans98@funmail.com
Susan Walter,susan82,swilliams@funmail.com
Stephanie King,stephanieking,sking@funmail.com
Erika Miller,jessica32,ejmiller79@funmail.com
```

Notice that the first row of the CSV file does not represent any data, just the labels of the data that’s 
present in the rest of the file. The rest of the rows of the file are the same as the rows in the spreadsheet 
software, just instead of being separated into different cells, they are separated by commas.

#### Reading CSV Files
In Python we can convert that data into a dictionary using the `csv` library’s `DictReader` object. Here is how we would 
create a list with the email addresses of all the users in the above table:

```
import csv

list_of_email_addresses = []
with open('users.csv', newline='') as users_csv:
  user_reader = csv.DictReader(users_csv)
  for row in user_reader:
    list_of_email_addresses.append(row['Email'])
```

In the above code, we first import our `csv` library, which gives us the tools to parse our CSV file. We then create 
the empty list `list_of_email_addresses` which we’ll later populate with the email addresses from our CSV. Then we 
open the *users.csv* file with the temporary variable `users_csv`.

We pass the additional keyword argument `newline=''` to the file opening `open()` function so that we don’t 
accidentally mistake a line break in one of our data fields as a new row in our CSV (read more about this on the 
<a href="https://docs.python.org/3/library/csv.html#id3" target="_blank">Python documentation</a>).

After opening our new CSV file we use `csv.DictReader(users_csv)` which converts the lines of our CSV file to Python dictionaries which we can use access methods for. The keys of the dictionary are, by default, the entries in the first line of our CSV file. Since our CSV’s first line calls the third field in our CSV “`Email`“, we can use that as the key in each row of our DictReader.

When we iterate through the rows of our `user_reader` object, we access all the rows in our CSV as dictionaries (except for the first row, which we used to label the keys of our dictionary). By accessing the `'Email'` key of each of these rows we can grab the email address in that row and append it to our `list_of_email_addresses`.

#### Reading Different Types of CSV Files
We have been acting like CSV files are Comma-Separated Values files. It is true that CSV stands for that, but it is 
also true that other ways of separating values are valid CSV **files** these days.

People used to call Tab-Separated Values files TSV files, but as other separators grew in popularity everyone realized that creating a new `.[a-z]sv` file format for every value-separating character used is not sustainable.

So we call all files with a list of different values a CSV file and then use different *delimiters* (like a comma or 
tab) to indicate where the different values start and stop.

Let’s say we had an address book. Since addresses usually use commas in them, we’ll need to use a different delimiter for our information. Since none of our data has semicolons (`;`) in them, we can use those.

*addresses.csv*
```commandline
Name;Address;Telephone
Donna Smith;126 Orr Corner Suite 857\nEast Michael, LA 54411;906-918-6560
Aaron Osborn;6965 Miller Station Suite 485\nNorth Michelle, KS 64364;815.039.3661x42816
Jennifer Barnett;8749 Alicia Vista Apt. 288\nLake Victoriaberg, TN 51094;397-796-4842x451
Joshua Bryan;20116 Stephanie Stravenue\nWhitneytown, IA 87358;(380)074-6173
Andrea Jones;558 Melissa Keys Apt. 588\nNorth Teresahaven, WA 63411;+57(8)7795396386
Victor Williams;725 Gloria Views Suite 628\nEast Scott, IN 38095;768.708.3411x954
```

Notice the `\n` character, this is the escape sequence for a new line. The possibility of a new line escaped by a `\n` character in our data is why we pass the `newline=''` keyword argument to the `open()` function.

Also notice that many of these addresses have commas in them! This is okay, we’ll still be able to read it. If we wanted to, say, print out all the addresses in this CSV file we could do the following:

```commandline
import csv

with open('addresses.csv', newline='') as addresses_csv:
  address_reader = csv.DictReader(addresses_csv, delimiter=';')
  for row in address_reader:
    print(row['Address'])
```

Notice that when we call `csv.DictReader` we pass in the `delimiter` parameter, which is the string that’s used to delineate separate fields in the CSV. We then iterate through the CSV and print out each of the addresses.

#### Writing a CSV File
Naturally, if we can read different CSV files, we might want to be able to programmatically create CSV files that save output and data that someone could load into their spreadsheet software. Let’s say we have a big list of data that we want to save into a CSV file. We could do the following:

```commandline
big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}] 

import csv

with open('output.csv', 'w') as output_csv:
  fields = ['name', 'userid', 'is_admin']
  output_writer = csv.DictWriter(output_csv, fieldnames=fields)

  output_writer.writeheader()
  for item in big_list:
    output_writer.writerow(item)
```

In our code above, we had a set of **dictionaries** with the same keys for each, a prime candidate for a CSV. We import 
the `csv` library, and then open a new CSV file in write-mode by passing the `'w'` argument to the `open()` function.

We then define the fields we’re going to be using into a variable called `fields`. We then instantiate our CSV writer object and pass two arguments. The first is `output_csv`, the file handler object. The second is our list of `fields` which we pass to the keyword parameter `fieldnames`.

Now that we’ve instantiated our CSV file writer, we can start adding lines to the file itself! First, we want the headers, so we call `.writeheader()` on the writer object. This writes all the fields passed to `fieldnames` as the first row in our file. Then we iterate through our `big_list` of data. Each `item` in `big_list` is a dictionary with each field in `fields` as the keys. We call `output_writer.writerow()` with the `item` dictionaries which writes each line to the CSV file.

### JSON Files
CSV isn’t the only file format that Python has a built-in library for. We can also use Python’s file tools to read and write JSON. JSON, an abbreviation of JavaScript Object Notation, is a file format inspired by the programming language JavaScript. The name, like CSV is a bit of a misnomer — some JSON is not valid JavaScript (and plenty of JavaScript is not valid JSON).

#### Reading JSON Files
JSON’s format is endearingly similar to Python dictionary syntax, and so JSON files might be easy to read from a Python developer standpoint. Nonetheless, Python comes with a `json` package that will help us parse JSON files into actual Python dictionaries. Suppose we have a JSON file like the following:

*purchase_14781239.json*
```commandline
{
  'user': 'ellen_greg',
  'action': 'purchase',
  'item_id': '14781239',
}
```

We would be able to read that in as a Python dictionary with the following code:

*json_reader.py*
```commandline
import json

with open('purchase_14781239.json') as purchase_json:
  purchase_data = json.load(purchase_json)

print(purchase_data['user'])
# Prints 'ellen_greg'
```

First we import the `json` package. We opened the file using our trusty `open()` command. Since we’re opening it in 
*read-mode* we just need to pass the file name. We save the file in the temporary variable `purchase_json`.

We continue by parsing `purchase_json` using `json.load()`, creating a Python dictionary out of the file. Saving the results into `purchase_data` means we can interact with it. We print out one of the values of the JSON file by keying into the `purchase_data` object.

#### Writing a JSON File
Naturally we can use the `json` library to translate Python objects to JSON as well. This is especially useful in instances where you’re using a Python library to serve web pages, you would also be able to serve JSON. Let’s say we had a Python dictionary we wanted to save as a JSON file:

```commandline
turn_to_json = {
  'eventId': 674189,
  'dateTime': '2015-02-12T09:23:17.511Z',
  'chocolate': 'Semi-sweet Dark',
  'isTomatoAFruit': True
}
```

We’d be able to create a JSON file with that information by doing the following:

```commandline
import json

with open('output.json', 'w') as json_file:
  json.dump(turn_to_json, json_file)
```

We import the `json` module, open up a write-mode file under the variable `json_file`, and then use the `json.dump()
` method to write to the file. `json.dump()` takes two arguments: first the data object, then the file object you want to save.

## Classes
In Python, a class is a template for a data type. A class can be defined using the `class` keyword.

```commandline
# Defining a class
class Animal:
  def __init__(self, name, number_of_legs):
    self.name = name
    self.number_of_legs = number_of_legs
```

### Instantiate Python Class
In Python, a class needs to be instantiated before use.

As an analogy, a class can be thought of as a blueprint (Car), and an instance is an actual implementation of the blueprint (Ferrari).

```commandline
class Car:
  "This is an empty class"
  pass

# Class Instantiation
ferrari = Car()
```

### Python Class Variables
In Python, class variables are defined outside of all methods and have the same value for every instance of the class.

Class variables are accessed with the `instance.variable` or `class_name.variable` syntaxes.

```commandline
class my_class:
  class_variable = "I am a Class Variable!"
  
x = my_class()
y = my_class()

print(x.class_variable) #I am a Class Variable!
print(y.class_variable) #I am a Class Variable!
```

### `class` methods
In Python, *methods* are functions that are defined as part of a **class**. It is common practice that the first 
argument of any method that is part of a class is the actual object calling the method. This argument is usually called `self`.

```commandline
# Dog class
class Dog:
  # Method of the class
  def bark(self):
    print("Ham-Ham")

# Create a new instance
charlie = Dog()

# Call the method
charlie.bark()
# This will output "Ham-Ham"
```

### Dunder Methods
Dunder Methods, alternatively known as magic methods, use a special syntax to perform class-specific operations in 
Python. Here, “dunder” is the short for “double underscores”. The operations that it performs include the following:

- Performing arithmetic operations on numeric-type attributes.
- Initializing a new class instance and binding any necessary attributes.
- Overloading certain methods to make their behaviors unique to that class.

```
# Syntax
class ClassName:
  __methodname__(self, param1, param2, ... paramN):
    # Method body here
```

The `methodname` is all lowercase even if there is more than one word in the name. The first parameter, `self`, is 
never explicitly passed as an argument because it refers to the class instance the method would be called against. However, any parameters defined afterward (`param1, param2, ... paramN`) must be passed as arguments when the dunder method is called.

1. `__init__()` - Initializes a newly created object and is called each time a new class instance is created.
2. `__new__()` - Creates a new instance of a class.
3. `__repr__()` - Returns the string representation of the class
4. `__str__()` - Returns a reader-friendly string representation of a class object.

#### `__init__` method
The `__init__()` method is used to initialize a newly created object. It is called every time the class is instantiated.

Methods that are used to prepare an object being instantiated are called constructors. The word “constructor” is used to describe similar features in other object-oriented programming languages, but programmers who refer to a constructor in Python are usually talking about the `__init__()` method.

*Example 1.*
```commandline
class Animal:
  def __init__(self, voice):
    self.voice = voice

# When a class instance is created, the instance variable
# 'voice' is created and set to the input value.
cat = Animal('Meow')
print(cat.voice) # Output: Meow

dog = Animal('Woof') 
print(dog.voice) # Output: Woof
```

*Example 2.*
In this example `Shouter()` looks a lot like a function call. If it’s a function, can we pass parameters 
to it?

We absolutely can, and those parameters will be received by the `__init__()` method.

```commandline
class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:

      # then shout it out
      print(phrase.upper())

shout1 = Shouter("shout")
# prints "SHOUT"

shout2 = Shouter("shout")
# prints "SHOUT"

shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"
```

#### `__repr__` method
The Python `__repr__()` method is used to tell Python what the *string representation* of the class should be. It can 
only have one parameter, `self`, and it should return a string.

```commandline
class Employee:
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name

john = Employee('John')
print(john) # John
```

### `__main__` in Python
In Python, `__main__` is an identifier used to reference the current file context. When a module is read from standard input, a script, or from an interactive prompt, its `__name__` is set equal to `__main__`.

Suppose we create an instance of a class called `CoolClass`. Printing the `type()` of the instance will result in:

`<class '__main__.CoolClass'>`
This means that the class `CoolClass` was defined in the current script file.

### `type()` function
The Python `type()` function returns the data type of the argument passed to it.

```commandline
a = 1
print(type(a)) # <class 'int'>

a = 1.1
print(type(a)) # <class 'float'>

a = 'b'
print(type(a)) # <class 'str'>

a = None
print(type(a)) # <class 'NoneType'>
```

### `dir()` function
In Python, the built-in `dir()` function, without any argument, returns a list of all the attributes in the current scope.

With an object as argument, `dir()` tries to return all valid object attributes.

```commandline
class Employee:
  def __init__(self, name):
    self.name = name

  def print_name(self):
    print("Hi, I'm " + self.name)


print(dir())
# ['Employee', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'new_employee']

print(dir(Employee))
# ['__doc__', '__init__', '__module__', 'print_name']
```
