
# Table of Contents

 * [Introduction](#introduction)
    * [Details](#details)
 * [Notes](#notes)
    * [Common Errors](#common-errors)
    * [Variables](#variables-and-naming-convention)
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

## Introduction

A compilation of small projects/scripts following my journey with learning concepts of the Python programming language.

### Details
Each sub-folder holds a `README.md` file with details for that project/script, packages necessary and execution details.

## Notes
### Common Errors
In Python, there are many different ways of classifying errors, but here are some common ones:

1. SyntaxError: Error caused by not following the proper structure (syntax) of the language.
2. NameError: Errors reported when the interpreter detects a variable that is unknown.
3. TypeError: Errors thrown when an operation is applied to an object of an inappropriate type.

### Variables and naming convention
A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character _.

The equal sign `=` is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed.

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

### Tuples
Tuple is one of the built-in data types in Python. A Python tuple is a sequence of comma separated items, enclosed in parentheses (). The items in a Python tuple need not be of same data type. Like `Lists` a tuple is an ordered collection of items. Each item in the tuple has a unique position index, starting from 0.

To access values in tuple, use the square brackets for slicing along with the index or indices to obtain value available at that index.

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
Removing individual tuple elements is not possible. There is, of course, nothing wrong with putting together another tuple with the undesired elements discarded.

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

#### Combining Lists
In Python, we have an assortment of built-in functions that allow us to build our programs faster and cleaner. One of those functions is `zip()`.

The `zip()` function allows us to quickly combine associated data-sets without needing to rely on multi-dimensional lists.

```
names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]
```

If we wanted to create a nested list that paired each name with a height, we could use the built-in function `zip()`.

The `zip()` function takes two (or more) lists as inputs and returns an object that contains a list of pairs. Each pair contains one element from each of the inputs. This is how we would do it for our `names` and `heights` lists:

```
names_and_heights = zip(names, heights)
```

If we were to then examine this new variable names_and_heights, we would find it looks a bit strange:

```
print(names_and_heights)
# Output: <zip object at 0x7f1631e86b48>
```

This zip object contains the location of this variable in our computer’s memory. To properly print the list we must use the built-in function `list()`:

```
converted_list = list(names_and_heights)
print(converted_list)

# Output : [('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 64)]
```

Notice two things:

1. Our data set has been converted from a zip memory object to an actual list (denoted by `[ ]`)
2. Our inner lists don’t use square brackets `[ ]` around the values. This is because they have been converted into `tuples` (an immutable type of list).


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

### Loops
A loop is a control structure that can execute a statement or group of statements repeatedly. Python has three types of loops: while loops, for loops, and nested loops.


#### While Loops

A while loop will repeatedly execute a code block as long as a condition evaluates to `True`.

The condition of a while loop is always checked first before the block of code runs. If the condition is not met initially, then the code block will never run.

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

#### For Loops
A for loop can be used to iterate over and perform an action one time for each element in a list.

Proper for loop syntax assigns a temporary value, the current item of the list, to a variable on each successive iteration:

```
for <temporary variable> in <collection>:
  <action>
```

1. A `for` keyword indicates the start of a `for` loop.
2. A `<temporary variable>` that is used to represent the value of the element in the collection the loop is currently on.
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

##### For Loops with Range
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

##### List Comprehension
Python list comprehensions provide a concise way for creating lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses: `[EXPRESSION for ITEM in LIST <if CONDITIONAL>]`.

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

#### Nested Loops

Loops can be nested inside other loops. Nested loops can be used to access items of lists which are inside other lists. The item selected from the outer loop can be used as the list for the inner loop to iterate over.

```
groups = [["Jobs", "Gates"], ["Newton", "Euclid"], ["Einstein", "Feynman"]]

# This outer loop will iterate over each list in the groups list
for group in groups:
  # This inner loop will go through each name in each list
  for name in group:
    print(name)

```

#### Break Keyword
In a loop, the break keyword escapes the loop, regardless of the iteration number. Once break executes, the program will continue to execute after the loop.

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

#### Continue Keyword
The continue keyword is used inside a loop to skip the remaining code inside the loop code block and begin the next loop iteration.

```
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

# Print only positive numbers:
for i in big_number_list:
  if i < 0:
    continue
  print(i)
```

### Functions
A function consists of many parts, so let’s first get familiar with its core - a function definition. 

**Note:** Function names in Python are written in snake_case.

```
def function_name():
  # functions tasks go here
```

There are some key components we want to note here:

The def keyword indicates the beginning of a function (also known as a function header). The function header is followed by a name in snake_case format that describes the task the function performs. It’s best practice to give your functions a descriptive yet concise name.
Following the function name is a pair of parenthesis ( ) that can hold input values known as parameters (more on parameters later in the lesson!). In this example function, we have no parameters.

A colon : to mark the end of the function header.
Lastly, we have one or more valid python statements that make up the function body (where we have our python comment).

Notice we’ve indented our` # function tasks go here` comment. Like loops and conditionals, code inside a function must be indented to show that they are part of the function.

```
def trip_welcome():
  print("Welcome to Tripcademy!") 
  print("Let's get you to your destination.")
```

**Note**: Pasting this code into the editor and clicking Run will result in an empty output terminal. The `print()` statements within the function will not execute since our function hasn’t been used.

`SyntaxError: unexpected EOF while parsing.` will occur when we don’t populate a function with any statements. EOF stands for “End of File” — Python is telling you that it was expecting some code in the body of the function, but it hit the end of the file first.

The process of executing the code inside the body of a function is known as calling it (This is also known as “executing a function”). To call a function in Python, type out its name followed by parentheses `( )`.

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

#### Types of Arguments

In Python, there are 3 different types of arguments we can give a function.

1. **Positional arguments**: arguments that can be called by their position in the function definition.
2. **Keyword arguments**: arguments that can be called by their name.
3. **Default arguments**: arguments that are given default values.

Positional Arguments depend on their positions in the function call. Let’s look at a function called `calculate_taxi_price()` that allows our users to see how much a taxi would cost to their destination 🚕.

```
def calculate_taxi_price(miles_to_travel, rate, discount):
  print(miles_to_travel * rate - discount )
```

In this function, `miles_to_travel` is *positioned* as the first parameter, rate is positioned as the second parameter, and discount is the third. When we call our function, the position of the arguments will be mapped to the positions defined in the function declaration.

```
# 100 is miles_to_travel
# 10 is rate
# 5 is discount
calculate_taxi_price(100, 10, 5)
```

Alternatively, we can use *Keyword Arguments* where we explicitly refer to what each argument is assigned to in the function call. Notice in the code example below that the arguments do not follow the same order as defined in the function declaration.

```
calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)
```

Lastly, sometimes we want to give our function parameters default values. We can provide a default value to a parameter by using the assignment operator (=). This will happen in the function declaration rather than the function call.

Here is an example where the discount argument in our `calculate_taxi_price` function will always have a default value of 10:

```
def calculate_taxi_price(miles_to_travel, rate, discount = 10):
  print(miles_to_travel * rate - discount )
```

When using a default argument, we can either choose to call the function without providing a value for a discount (and thus our function will use the default value assigned) or overwrite the default argument by providing our own:

```
# Using the default value of 10 for discount.
calculate_taxi_price(10, 0.5)

# Overwriting the default value of 10 with 20
calculate_taxi_price(10, 0.5, 20)
```

#### Built-in Functions

[Built-in functions](https://docs.python.org/3/library/functions.html) are functions that come built into Python ready for us to use. Some examples of built-in functions are `print()`, `len()` and `str()`.

```
destination_name = "Bogota, Colombia"

# Built-in function: len()
length_of_destination = len(destination_name)

# Built-in function: print()
print(length_of_destination)

# Output: 16 (including spaces)
```

There are even more obscure built-in functions like `help()` where Python will print documentation for us and provide some details:

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

#### Scope
`Scope` refers to the areas where variables are visible and accessible. Variables that can be accessed anywhere in a Python program are in the global scope. Conversely, variables that are defined within the body of structures like classes and methods exist only in the local scope.

1. *Local Scope* - Suppose a variable is initialized within a function. This variable can only be used within that function and not from outside the function.

```
def my_function():
 x = 200
 print(x)

my_function()
```

2. *Global Scope* - A variable initialized in the main body is defined as a global variable and can be used anywhere in the code, including nested blocks, loops, etc. This is because these variables exist in the global scope of the code.

```
x = 200

def fun():
  print(x)

fun()

print(x)
```

3. *Nested Functions and Local Scope* - In the example below, a variable `x` is defined within the local scope of the `outer_function()` function, followed by a defined `inner_function()` function. Since `inner_function()` exists within the local scope of `outer_function()`, `x` can be accessed and printed within `inner_function()`:

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

#### Return Values

The `return` keyword is used to return a value from a Python function. The value returned from a function can be assigned to a variable which can then be used in the program.

In the example below, the `check_leap_year()` function returns a string that indicates if the passed parameter is a leap year or not.

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

Sometimes we may want to **return more than one value** from a function. We can return several values by separating them with a comma. Take a look at this example of a function that allows users in our travel application to check the upcoming week’s weather (starting on Monday):

```
weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']

def threeday_weather_report(weather):
  first_day = " Tomorrow the weather will be " + weather[0]
  second_day = " The following day it will be " + weather[1]
  third_day = " Two days from now it will be " + weather[2]
  return first_day, second_day, third_day
```

This function takes in a set of data in the form of a list for the upcoming week’s weather. We can get our returned function values by assigning them to variables when we call the function:

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