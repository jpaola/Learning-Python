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

A function consists of many parts, so let’s first get familiar with its core - a function definition.

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
Like a list comprehension, a dictionary comprehension is a Pythonic way to create a dictionary. They can be used to filter and manipulate data in tons of useful ways. The syntax is as follows:

```commandline
new_dict = { expression for key, value in old_dict.items() if condition }
```

The `if` condition at the end is optional, but is a great tool for filtering data. For example, given a dictionary with a person’s name and age, make a new dictionary that only contains people with an age under 25:

```commandline
person_age = { "Mark": 55, "Shiela": 28, "Bryce": 24, "Jim": 41, "Eric": 33, "Ally": 23 }
person_age_filtered = { name: age for name, age in person_age.items() if age < 25 }
```

The expression is `name: age`, as that’s how the new dictionary will be formatted. Then, the typical for loop iteration, `for name, age in person_age.items()`. Lastly, the if condition filters out the results.

The expression can also perform operations on the data being extracted. For example, to create a dictionary with key value pairs of a number and its square given a list of numbers:

```commandline
nums_list = [ 1, 2, 3, 4, 5 ]
nums_squared = { num: num**2 for num in nums_list }
```

`nums_squared` will produce a result of: `{ 1: 1, 2: 4, 3: 9, 4: 16, 5: 25 }`

### Replacing an Entry in an Existing Dictionary
If a key needs to be updated in an existing dictionary, it uses the same syntax for adding an entry into a dictionary (`dictionary[new_key] = new_value)`, but instead, the new_key argument is replaced with an already existing key in the desired dictionary `(dictionary[existing_key] = new_value)`.

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
Sometimes we want to get a key and remove it from the dictionary. Imagine we were running a raffle, and we have this dictionary mapping ticket numbers to prizes:

```commandline
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
```

When we get a ticket number, we want to return the prize and also remove that pair from the dictionary, since the prize has been given away. We can use `.pop()` to do this. Just like with `.get()`, we can provide a default value to return if the key does not exist in the dictionary:

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
Sometimes we want to operate on all of the keys in a dictionary. For example, if we have a dictionary of students in a math class and their grades:

```commandline
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
```

We want to get a roster of the students in the class, without including their grades. We can do this with the built-in `list()` function:

```commandline
print(list(test_scores))
# Prints ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]
```

Dictionaries also have a `.keys()` method that returns a `dict_keys` object. A `dict_keys` object is a view object, which provides a look at the current state of the dictionary, without the user being able to modify anything. The `dict_keys` object returned by `.keys()` is a set of the keys in the dictionary. You cannot add or remove elements from a `dict_keys` object, but it can be used in the place of a list for iteration:

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
Dictionaries have a `.values()` method that returns a `dict_values` object (just like a `dict_keys` object but for values!) with all the values in the dictionary. It can be used in the place of a list for iteration:

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
You can get both the keys and the values with the `.items()` method. Like `.keys()` and `.values()`, it returns a `dict_list` object. Each element of the `dict_list` returned by `.items()` is a tuple consisting of:

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
