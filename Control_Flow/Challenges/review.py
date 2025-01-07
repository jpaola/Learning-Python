"""
1) Count Letters

For the first code challenge, we are going to count the number of unique letters in a string. This means that when we
are looking at the word, any new letters should be counted and any duplicates should not be counted. There are a few
ways to solve this, but we can use the provided alphabet string to ensure that duplicates are not counted. Here is
what we need to do:

Define the function to accept one parameter — the word whose letters we are counting
Create a counter to keep track of unique letters
Loop through every letter in our alphabet string. If the current letter was found in our word, increase our count
Return the count after looping through all letters.
"""

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def unique_english_letters(word):
    unique = 0
    for letter in letters:
        if letter in word:
            unique += 1
    return unique


print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4


"""
2) Count X

Next, we are going to try something a bit different. This time we are going to count the number of occurrences of a 
certain letter within a string. Our function will accept a parameter for a string and another for the character which 
we are going to count. For example, providing the word "mississippi" and the character 's' would result in an answer 
of 4. These are the steps we need to take:

Define the function to accept two parameters. word for the input string and x for the single character
Create a counter to keep track of the occurrences
Loop through every letter in the string. If the current letter is equal to the input letter, increase our counter
Return the counter after looping through the entire string.
"""


def count_char_x(word, x):
    occurrences = 0
    for letter in word:
        if letter == x:
            occurrences += 1
    return occurrences


print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1


"""
3) Count Multi X

Now let’s change our function to compare against an entire string instead of a single character. This function should 
accept a string and a substring to compare against. The number of occurrences of the second parameter within the 
first parameter string are returned. What this means is that we are checking the number of occurrences of the shorter 
string (second parameter) within the longer string (first parameter). One way to accomplish this is using the split 
function. Here is how to do that:

Define the function to accept two parameters. word for the input string and x for the second string we are searching for
Split the string into substrings based on the second input parameter
Count the number of instances the substring appeared in the first input string based on the split string
Return the result
"""


def count_multi_char_x(word, x):
    splits = word.split(x)
    return len(splits) - 1


print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1


"""
4) Substring Between

Here is a challenging problem. We need a function that is able to extract a portion of a string between two 
characters. The function will take three parameters where the first parameter is the string we are going to extract 
the substring from, the second input is the starting character of our substring and the third character is the ending 
character of our substring. Here are the steps we can use:

Define the function to accept three parameters, one string and two characters find the starting index of our 
substring using the second input parameter find the ending index of our substring using the third input parameter If 
neither of the indices are -1, return the portion of the first input parameter string between the starting and ending 
indices (not including the starting and ending index) If either of the indices are -1, that means the start or end of 
the substring didn’t exist in our string. Return the original string in this case.
"""


def substring_between_letters(word, start, end):
    start_ind = word.find(start)
    end_ind = word.find(end)
    if start_ind > -1 and end_ind > -1:
        return word[start_ind + 1:end_ind]
    return word


print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"


"""
5) X Length

Let’s use the split method in a different way. We need a new function that is able to accept two inputs: one for a 
sentence and another for a number. The function returns True if every single word in the sentence has a length 
greater than or equal to the number provided. These are the steps:

Define the function to accept two parameters, one string, and one number
Split up the sentence into an array of words
Loop through the words. If the length of any of the words is less than the provided number return False
If we made it through the loop without returning False then return True
"""


def x_length_words(sentence, x):
    words = sentence.split(" ")
    for word in words:
        if len(word) < x:
            return False
    return True


print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True


"""
6) Check Name

You are creating an app that allows users to interact and share their coding project ideas online. The first step is 
to provide your name in the application and a greeting for other people to see which contains your name. Let’s create 
a function that is able to check if a user’s name is located within their greeting. We need a function that accepts 
two parameters, a string for our sentence and a string for a name. The function should return True if the name exists 
within the string (ignoring any differences in capitalization). Here is what we need to do:

Define the function to accept two parameters, one string for the sentence and one string for the name
Convert all of the strings to the same case so we don’t have to worry about differences in capitalization
Check if the name is within the sentence. If so, then return True. Otherwise, return False
"""


def check_for_name(sentence, name):
    return name.lower() in sentence.lower()


print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False


"""
7) Every Other Letter

For this next challenge, we are going to create a function that extracts every other letter from a string and returns 
the resulting string. There are a few different ways you can solve this problem. Here are the steps needed for one of 
the ways:

Define the function to accept one parameter for the string
Create a new empty string to hold every other letter from the input string
Loop through the input string while incrementing by two every time
Inside the loop, append the character at the current location to the new string we initialized earlier
Return the new string
"""


def every_other_letter(word):
    every_other = ""
    for index in range(0, len(word), 2):
        every_other += word[index]
    return every_other


print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print


"""
8) Reverse

This one is similar to the last challenge. Instead of selecting every other letter, we want to reverse the entire 
string. This can be performed in a similar manner, but we will need to modify the range we are using. Here is what we 
need to do:

Define the function to accept one parameter for the string
Create a new empty string to hold the reversed string
Loop through the input string by starting at the end, and working towards the beginning
Inside the loop, append the character at the current location to the new string we initialized earlier
Return the result
"""


def reverse_string(word):
    reverse = ""
    for index in range(len(word) - 1, -1, -1):
        reverse += word[index]
    return reverse


print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print


"""
9) Make Spoonerism

A Spoonerism is an error in speech when the first syllables of two words are switched. For example, a Spoonerism is 
made when someone says “Belly Jeans” instead of “Jelly Beans”. We are going to make a function that is similar, 
but instead of using the first syllable, we are going to switch the first character of two words. Here is what we 
need to do:

Define the function to accept two parameters for our two words
Get the first character of the first word and the first character of the second word
Get the remaining characters of the first word and the remaining characters of the second word.
Append the first character of the second word to the remaining character of the first word
Append a space character
Append the first character of the first word to the remaining characters of the second word.
Return the result
"""


def make_spoonerism(word1, word2):
    return word2[0] + word1[1:] + " " + word1[0] + word2[1:]


print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a


"""
10) Add Exclamation

Let’s say we are writing a program that displays a large message on a blimp and we need to fill in any missing space 
if a short phrase is provided. Our function will accept a string and if the size is less than 20, it will fill in the 
remaining space with exclamation marks until the size reaches 20. If the provided string already has a length greater 
than 20, then we will simply return the original string. Here are the steps:

Define the function to accept one parameter for our string
Loop while the length of our input string is less than 20
Inside the loop, append an exclamation mark
Once done, return the result
"""


def add_exclamation(word):
    while len(word) < 20:
        word += "!"
    return word


print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn


"""
11) Sum Values

For the first code challenge, we are going to look at only the values in a dictionary. This function should sum up 
all of the values from the key-value pairs in the dictionary. Here are the steps we need:

Define the function to accept one parameter for our dictionary
Create a variable to keep track of our sum
Loop through every value in the dictionary
Inside the loop, add each value to the sum
Return the sum
"""


def sum_values(my_dictionary):
    total = 0
    for value in my_dictionary.values():
        total += value
    return total


print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))
# should print 10
print(sum_values({10: 1, 100: 2, 1000: 3}))
# should print 6


"""
12) Even Keys

Next, we are going to do something similar, but we are going to use the keys in order to retrieve the values. 
Additionally, we are going to only look at every even key within the dictionary. Here are the steps:

Define the function to accept one parameter for our dictionary
Create a variable to keep track of our sum
Loop through every key in the dictionary
Inside the loop, if the key is even, add the value from the even key
After the loop, return the sum
"""


def sum_even_keys(my_dictionary):
    total = 0
    for key in my_dictionary.keys():
        if key % 2 == 0:
            total += my_dictionary[key]
    return total


print(sum_even_keys({1: 5, 2: 2, 3: 3}))
# should print 2
print(sum_even_keys({10: 1, 100: 2, 1000: 3}))
# should print 6


"""
13) Add Ten

Let’s loop through the keys again, but this time let’s modify the values within the dictionary. Our function should 
add 10 to every value in the dictionary and return the modified dictionary. Here is what we need to do:

Define the function to accept one parameter for our dictionary
Loop through every key in the dictionary
Retrieve the value using the key and add 10 to it. Make sure to re-save the new value to the original key.
After the loop, return the modified dictionary
"""


def add_ten(my_dictionary):
    for key in my_dictionary.keys():
        my_dictionary[key] += 10
    return my_dictionary


print(add_ten({1: 5, 2: 2, 3: 3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10: 1, 100: 2, 1000: 3}))
# should print {10:11, 100:12, 1000:13}


"""
14) Values That Are Keys

We are making a program that will create a family tree. Using a dictionary, we want to return a list of all the 
children who are also parents of other children. Using dictionaries we can consider those people to be values which 
are also keys in our dictionary of family data. Here is what we need to do:

Define the function to accept one parameter for our dictionary
Create an empty list to hold the values we find
Loop through every value in the dictionary
Inside the loop, test if the current value is a key in the dictionary. If it is then append it to the list of values we found
After the loop, return the list of values which are also keys
"""


def values_that_are_keys(my_dictionary):
    value_keys = []
    for value in my_dictionary.values():
        if value in my_dictionary:
            value_keys.append(value)
    return value_keys


print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
# should print [1, 4]
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))
# should print ["a"]


"""
15) Largest Value

For the last challenge, we are going to create a function that is able to find the maximum value in the dictionary 
and return the associated key. This is a twist on the max algorithm since it is using a dictionary rather than a 
list. These are the steps:

Define the function to accept one parameter for our dictionary Initialize the starting key to a very low number 
Initialize the starting value to a very low number Iterate through the dictionary’s key/value pairs. Inside the loop, 
if the current value is larger than the current largest value, replace the largest key and largest value with the 
current ones you are looking at Once you are done iterating through all key/value pairs, return the key which has the 
largest value
"""


def max_key(my_dictionary):
    largest_key = float("-inf")
    largest_value = float("-inf")
    for key, value in my_dictionary.items():
        if value > largest_value:
            largest_value = value
            largest_key = key
    return largest_key


print(max_key({1: 100, 2: 1, 3: 4, 4: 10}))
# should print 1
print(max_key({"a": 100, "b": 10, "c": 1000}))
# should print "c"


"""
16) Word Length Dict

Let’s start by writing a function that creates a new dictionary based on a list of strings. The keys of our 
dictionary will be every string in our list of strings, while the values will be the length of each of the words in 
the string list. Here are the steps:

Define the function to accept one parameter for our list of strings
Create a new empty dictionary
Loop through every string in the list of strings
Inside the loop, add the string as a key and the length of the string as the value to the dictionary
After the loop, return the new dictionary
"""


def word_length_dictionary(words):
    word_lengths = {}
    for word in words:
        word_lengths[word] = len(word)
    return word_lengths


print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}


"""
17) Frequency Count

This next function is similar, but instead of counting the length of each string in the list of strings, we will be 
counting the frequency of each string. This function will also accept a list of strings as input and return a new 
dictionary. Here is what we need to do:

Define the function to accept one parameter for our list of strings Create a new empty dictionary Loop through every 
string in the list of strings Inside the loop, if the string is NOT already in our dictionary, store the string as a 
key with a value of 0 in our dictionary. Otherwise, if the string is already in our dictionary, increment the value 
by 1. After the loop, return the new dictionary
"""


def frequency_dictionary(words):
    freqs = {}
    for word in words:
        if word not in freqs:
            freqs[word] = 0
        freqs[word] += 1
    return freqs


print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0, 0, 0, 0, 0]))
# should print {0:5}


"""
18) Unique Values

Now let’s try reading a dictionary as input and finding how many values are unique. The function should return a 
number which is the count of all values from the dictionary without including duplicates. These are the steps:

Define the function to accept one parameter for our dictionary
Create a new empty list
Loop through every value in our dictionary
Inside the loop, if the value is not already in our list, append the value to our list
After the loop, return the length of our list
"""


def unique_values(my_dictionary):
    seen_values = []
    for value in my_dictionary.values():
        if value not in seen_values:
            seen_values.append(value)
    return len(seen_values)


print(unique_values({0: 3, 1: 1, 4: 1, 5: 3}))
# should print 2
print(unique_values({0: 3, 1: 3, 4: 3, 5: 3}))
# should print 1


"""
19) Count First Letter

This function accepts a dictionary where the keys are last names and the values are lists of first names of people 
who have that last name. We need to calculate the number of people who have the same first letter in their last name. 
Here are the steps we need:

Define the function to accept one parameter for our dictionary Create a new empty dictionary called letters Loop 
through every key in our names dictionary Inside the loop, get the first letter of the last name we are looking at. 
If the first letter is not in our letter dictionary, add it as a key and set the value to the number of people that 
have that last name. Otherwise, if the first letter is already in our letter dictionary, increment the value stored 
with that key by the number of people that have that last name After the loop, return the letters dictionary
"""


def count_first_letter(names):
    letters = {}
    for key in names:
        first_letter = key[0]
        if first_letter not in letters:
            letters[first_letter] = 0
        letters[first_letter] += len(names[key])
    return letters


print(
    count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(
    count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}


"""
20) Setting Up ur Robot

Let’s begin by creating the class for our robot. We will begin by setting up the instance variables to keep track of 
important data related to the robot. Here are the steps we need to do:

Create a new class called DriveBot
Set up a basic constructor (no parameters needed)
Initialize three instance variables within our constructor which all default to 0: motor_speed, direction, and sensor_range
"""


class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0


robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

"""
21) Adding Robot Logic

Now we want to add some logic to our robot. It would be very useful to be able to control our robot, so we are going 
to create a control_bot method which changes the speed and direction. We are also going to create a method called 
adjust_sensor. This method is used to change the range of our robot’s sensors which are used to detect obstacles. 
Here are the steps:

Define a function within the DriveBot class which accepts two additional parameters: one for a new speed and one for 
a new direction Replace the instance variables for speed and direction with the input parameters Define another 
function called adjust_sensor which accepts one additional parameter Replace the instance variable sensor_range with 
the input parameter
"""


class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range


robot_1 = DriveBot()
robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

"""
22) Enhanced Constructor

It can be tedious manually setting the values for each instance variable after we have created an object from the 
DriveBot class. We can enhance our constructor to automatically assign the values we provide to the instance 
variables. Instead of taking zero parameters, we are going to make the constructor take three parameters. Here is 
what we need to do:

Modify the constructor to take three parameters (in addition to self): one for motor_speed, one for direction, 
and one for sensor_range For the first parameter, make the default value 0 For the second parameter, make the default 
value 180 For the third parameter, make the default value 10 Within the constructor, replace the instance variables 
with the variables from the input parameters
"""


class DriveBot:
    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range


robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot()
robot_2.motor_speed = 35
robot_2.direction = 75
robot_2.sensor_range = 25

print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)

"""
23) Controlling Them All

We want to add a new feature that allows the user to control multiple robots at once. The robots should be able to 
all have the same latitude and longitude GPS destination coordinates as well as a setting for disabling them all 
called all_disabled. We can accomplish this using class variables. Here is how we can do it:

Create a new class variable within the DriveBot class called all_disabled and set it equal to False Create a new 
class variable within the DriveBot class called latitude and set it equal to -999999 Create a new class variable 
within the DriveBot class called longitude and set it equal to -999999 Outside of the class, test the class variables 
by setting the longitude of all robots to 50.0, the latitude to -50.0 and all_disabled to True
"""


class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999

    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range


robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

# Change the latitude, longitude, and all_disabled values for all three robots using only three lines of code!

DriveBot.longitude = 50.0
DriveBot.latitude = -50.0
DriveBot.all_disabled = True

print(robot_1.latitude)
print(robot_2.longitude)
print(robot_3.all_disabled)

"""
24) Identifying Robots

In order to keep track of the robots we are creating, we want to be able to assign an ID value to each robot when it 
is created. If we create five robots in a row, we want the IDs of each robot to be 1, 2, 3, 4, and 5 respectively. 
This can be accomplished by using a class variable counter which increments and is assigned to an instance variable 
for the ID whenever the constructor is called. Here are the steps:

Create a new class variable in the DriveBot class called robot_count
In the constructor, increment the robot_count by 1
After incrementing the value, assign the value of robot_count to a new instance variable called id.
"""


class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range


robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

print(robot_1.id)
print(robot_2.id)
print(robot_3.id)
