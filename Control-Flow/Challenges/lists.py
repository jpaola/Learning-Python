"""
Append Size

Create a function called append_size that has one parameter named my_list.
The function should append the size of my_list (inclusive) to the end of my_list.
The function should then return this new list.

For example, if my_list was [23, 42, 108], the function should return [23, 42, 108, 3]
because the size of my_list was originally 3.
"""


def append_size(my_list):
    my_list.append(len(my_list))
    return my_list


print(append_size([23, 42, 108]))
# Should print [23, 42, 108, 3]

"""
Append Sum

Write a function named append_sum that has one parameter — a list named named my_list.
The function should add the last two elements of my_list together and append the result to my_list. 
It should do this process three times and then return my_list.

For example, if my_list started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].
"""


def append_sum(my_list):
    my_list.append(my_list[-1] + my_list[-2])
    my_list.append(my_list[-1] + my_list[-2])
    my_list.append(my_list[-1] + my_list[-2])
    return my_list


print(append_sum([1, 1, 2]))
# Should print [1, 1, 2, 3, 5, 8]

"""
Larger List

Write a function named larger_list that has two parameters named my_list1 and my_list2.
The function should return the last element of the list that contains more elements. 
If both lists are the same size, then return the last element of my_list1.
"""


def larger_list(my_list1, my_list2):
    if len(my_list1) >= len(my_list2):
        return my_list1[-1]
    else:
        return my_list2[-1]


print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
# Should print 5

"""
More Than N

Create a function named more_than_n that has three parameters named my_list, item, and n.
The function should return True if item appears in the list more than n times. 
The function should return False otherwise.
"""


def more_than_n(my_list, item, n):
    if my_list.count(item) > n:
        return True
    else:
        return False


print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
# Should print True


"""
Combine Sort

Write a function named combine_sort that has two parameters named my_list1 and my_list2.
The function should combine these two lists into one new list and sort the result. Return the new sorted list.
#"""


def combine_sort(my_list1, my_list2):
    unsorted = my_list1 + my_list2
    sorted_list = sorted(unsorted)
    return sorted_list


# or return sorted(my_list1 + my_list2) but the previous is more legible

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
# Should print [-10, 2, 2, 4, 5, 5, 10, 10]

"""
Every Three Sums

Create a function called every_three_nums that has one parameter named start.
The function should return a list of every third number between start and 100 (inclusive). 
For example, every_three_nums(91) should return the list [91, 94, 97, 100]. 
If start is greater than 100, the function should return an empty list.
"""


def every_three_nums(start):
    return list(range(start, 101, 3))


print(every_three_nums(91))
# Should print [91, 94, 97, 100]

"""
Remove Middle

Create a function named remove_middle which has three parameters named my_list, start, and end.
The function should return a list where all elements in my_list with an index between start and end (inclusive) have 
been removed. For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 
have been removed: remove_middle([4, 8 , 15, 16, 23, 42], 1, 3)

To make this problem easier, we can use slicing. For example, if we wanted all elements up to a certain index we can
use my_list[:index] and to get all elements after a certain index we can use my_list[index+1:].
"""


def remove_middle(my_list, start, end):
    return my_list[:start] + my_list[end + 1:]


print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
# Should print [4, 23, 42]

"""
More Frequent Item

Create a function named more_frequent_item that has three parameters named my_list, item1, and item2.
Return either item1 or item2 depending on which item appears more often in my_list.
If the two items appear the same number of times, return item1. Remember that we can easily count the number of 
occurrences of an item in our list using my_list.count(item1).
"""


def more_frequent_item(my_list, item1, item2):
    item1_occurrence = my_list.count(item1)
    item2_occurrence = my_list.count(item2)

    if item1_occurrence > item2_occurrence:
        return item1
    elif item2_occurrence > item1_occurrence:
        return item2
    else:
        return item1


# alternatively...
# def more_frequent_item(my_list, item1, item2):
#   if my_list.count(item1) >= my_list.count(item2):
#     return item1
#   else:
#     return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
# Should print 3

"""
Double Index

Create a function named double_index that has two parameters: a list named my_list and a single number named index.
The function should return a new list where all elements are the same as in my_list except for the element at index. 
The element at index should be double the value of the element at index of the original my_list.
If index is not a valid index, the function should return the original list.
For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:

double_index([1, 2, 3, 4], 2)

After writing your function, un-comment the call to the function that we’ve provided for you to test your results.
We can use slicing to get the values up to an index my_list[0:index] and from an index to the end my_list[index+1:]. 
Also, to append to the end of a list we can use the append() function.
"""


def double_index(my_list, index):
    # Checks to see if index is too big
    if index >= len(my_list):
        return my_list
    else:
        # Gets the original list up to index
        my_new_list = my_list[0:index]
    # Adds double the value at index to the new list
    my_new_list.append(my_list[index] * 2)
    #  Adds the rest of the original list
    my_new_list = my_new_list + my_list[index + 1:]
    return my_new_list


print(double_index([3, 8, -10, 12], 2))
# Should print [3, 8, -20, 12]

"""
Middle Item

Create a function called middle_element that has one parameter named my_list. If there are an odd number of elements 
in my_list, the function should return the middle element. If there are an even number of elements, the function should 
return the average of the middle two elements.
"""


def middle_element(my_list):
    if len(my_list) % 2 == 0:
        sum = my_list[int(len(my_list) / 2)] + my_list[int(len(my_list) / 2) - 1]
        return sum / 2
    else:
        return my_list[int(len(my_list) / 2)]


print(middle_element([5, 2, -10, -4, 4, 5]))
# Should print -7.0

"""
Divisible by 10

Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.
Return the count of how many numbers in the list are divisible by 10.
"""


def divisible_by_ten(nums):
    count = 0
    for num in nums:
        if num % 10 == 0:
            count += 1
    return count


print(divisible_by_ten([20, 25, 30, 35, 40]))
# Should print 3

"""
Greetings

Create a function named add_greetings() which takes a list of strings named names as a parameter.

In the function, create an empty list that will contain each greeting. Add the string 'Hello, ' in front of each name 
in names and append the greeting to the list. Return the new list containing the greetings.
"""


def add_greetings(names):
    greetings = []

    for name in names:
        greetings.append("Hello, " + str(name))
    return greetings


print(add_greetings(["Owen", "Max", "Sophie"]))
# Should print ['Hello, Owen', 'Hello, Max', 'Hello, Sophie']


"""
Delete Starting EVEN Numbers

Write a function called delete_starting_evens() that has a parameter named my_list.

The function should remove elements from the front of my_list until the front of the list is not even. The function 
should then return my_list.

For example if my_list started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(my_list) should return [11, 12, 15].

Make sure your function works even if every element in the list is even!

Use a while loop to check two things. First, check if the list has at least one element, using len(my_list). 
Second, check to see if the first element is odd using mod (%). If both of those are True, slice off the first 
element of the list using my_list = my_list[1:].
"""


def delete_starting_evens(my_list):
    while len(my_list) > 0 and my_list[0] % 2 == 0:
        my_list = my_list[1:]
    return my_list


print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
# Should print [11, 12, 15] and []


"""
ODD Indices

Create a function named odd_indices() that has one parameter named my_list.
The function should create a new empty list and add every element from my_list that has an odd index. 
The function should then return this new list. For example, odd_indices([4, 3, 7, 10, 11, -2]) 
should return the list [3, 10, -2].
"""


def odd_indices(my_list):
    odd_index_list = []
    for index in range(1, len(my_list), 2):
        odd_index_list.append(my_list[index])
    return odd_index_list


print(odd_indices([4, 3, 7, 10, 11, -2]))
# Should print [3, 10, -2]

"""
Exponents

Create a function named exponents() that takes two lists as parameters named bases and powers. 
Return a new list containing every number in bases raised to every number in powers.

For example, consider the following code.

exponents([2, 3, 4], [1, 2, 3])

the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first add two to the first. Then two to the second. 
Then two to the third, and so on.

Use nested for loops. The outer for loop should loop through all of the bases and the inner for loop should loop 
through all of the powers. Remember a ** b is a to the power of b
"""


def exponents(bases, powers):
    results = []
    for base in bases:
        for power in powers:
            results.append(base ** power)
    return results


print(exponents([2, 3, 4], [1, 2, 3]))
# Should print [2, 4, 8, 3, 9, 27, 4, 16, 64]

"""
Larger Sum

Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.
The function should return the list whose elements sum to the greater number. If the sum of the elements of each list 
are equal, return lst1. 

Create variables named sum1 and sum2 and set them to be 0. Loop through each list separately 
and add to the appropriate variable. After looping through each list, compare the two sums in an if statement and return 
the correct list.
"""


def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0

    for value in lst1:
        sum1 += value

    for value in lst2:
        sum2 += value

    if sum1 >= sum2:
        return lst1
    else:
        return lst2


print(larger_sum([1, 9, 5], [2, 3, 7]))
# Should print [1, 9, 5]

"""
Over 9000

Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.
The function should sum the elements of the list until the sum is greater than 9000. When this happens, 
the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should 
return total sum of all the elements. If the list is empty, the function should return 0.

For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

Create a variable named sum that begins at 0. Loop through all of the elements of lst and use a break when the sum is 
greater than 9000. Return sum after the loop.
"""


def over_nine_thousand(lst):
    sum = 0
    for number in lst:
        if sum > 9000:
            break
        sum += number
    return sum


print(over_nine_thousand([8000, 900, 120, 5000]))
# Should print 9020

"""
Max Num

Create a function named max_num() that takes a list of numbers named nums as a parameter.
The function should return the largest number in nums without resorting to sorting the list.

Create a variable called maximum to track the max number, and have it start as the first element in the list. 
Loop through all of the numbers in the list, and if a number is ever greater than the current max number, 
the max number should be re-set to that number.
"""


def max_num(nums):
    maximum = nums[0]
    for num in nums:
        if num > maximum:
            maximum = num
    return maximum


print(max_num([50, -10, 0, 75, 20]))
# Should print 75


"""
Same Values

Write a function named same_values() that takes two lists of numbers of equal size as parameters.
The function should return a list of the indices where the values were equal in lst1 and lst2.

For example, the following code should return [0, 2, 3]

same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])

Loop through all of the indices of each list using for index in range(len(lst1)) and compare lst1[index] to lst2[index]. 
Append index to a new list if those two items are equal.
"""


def same_values(lst1, lst2):
    result = []

    for index in range(len(lst1)):
        if lst1[index] == lst2[index]:
            result.append(index)

    return result


print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
#  Should print [0, 2, 3]


"""
Reversed List

Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.
The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.

For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

Let's say the lists are of size 5. You want to compare lst1[0] with lst2[4], lst1[1] with lst2[3] and so on.
Loop through the numbers created by range(len(lst1)) using a variable named index

Compare lst1[index] to lst2[len(lst2) - 1 - index]. If those two items are not equal, return False. If you loop through 
the entire list and you never return False, that means that every item was equal, and you should return True.
"""


def reversed_list(lst1, lst2):
    for index in range(len(lst1)):
        if lst1[index] != lst2[len(lst2) - 1 - index]:
            return False
    return True


print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
#  Should print True then False


"""
Tenth Power

Write a function named tenth_power() that has one parameter named num. The function should return num raised to 
the 10th power.
"""


def tenth_power(num):
    return num ** 10


print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024


"""
Write a function named square_root() that has one parameter named num. 
Use exponents (**) to return the square root of num.

Remember to use def when defining the function. To take the square root of a value, you can use the power operator **. 
The square root of a number is the same as taking the ½ power of the number. For example, the square root of 6 would 
look like: 6 ** 0.5.
"""


def square_root(num):
    return num ** 0.5


print(square_root(16))
# should print 4
print(square_root(100))
# should print 10


"""
Win Percentage

Create a function called win_percentage() that takes two parameters named wins and losses.
This function should return out the total percentage of games won by a team based on these two numbers.

In order to calculate the ratio of wins out of total games we can use wins / (wins + losses) where wins + losses is 
equal to the total number of games. To convert that value to a percentage, multiply it by 100.
"""


def win_percentage(wins, losses):
    total_games = wins + losses
    ratio_won = wins / total_games
    return ratio_won * 100


print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100


"""
Average

Write a function named average() that has two parameters named num1 and num2. The function should return the average 
of these two numbers.

To calculate the average of two numbers we add the first and second number, then divide the result by 2: 
(first + second) / 2
"""


def average(num1, num2):
    return (num1 + num2) / 2


print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0


"""
Remainder

Write a function named remainder() that has two parameters named num1 and num2.
The function should return the remainder of twice num1 divided by half of num2.

In order to calculate the remainder of two numbers, we can use the modulus operator %. For example, the remainder of 5 
divided by 2 is equal to 1 and we can get this result using 5 % 2.
"""


def remainder(num1, num2):
    return (2 * num1) % (num2 / 2)


print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0


"""
First Three Multiples

Write a function named first_three_multiples() that has one parameter named num.
This function should print the first three multiples of num. Then, it should return the third multiple.

For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21.

For this function, we need to print() out the results of each multiplication * then return a single value. For example, 
printing the result of 3 times 5 would look like print(3 * 5) and returning it would look like return 3 * 5.
"""


def first_three_multiples(num):
    print(num)
    print(2 * num)
    print(3 * num)
    return 3 * num


first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0


"""
Tip

Create a function called tip() that has two parameters named total and percentage.
This function should return the amount you should tip given a total and the percentage you want to tip.

Calculating the tip value will look something like this: (total * percentage) / 100
"""


def tip(total, percentage):
    return (total * percentage) / 100


print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0


"""
Bond, James Bond

Write a function named introduction() that has two parameters named first_name and last_name.
The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name.

In order to concatenate strings in python, we can use the + operator. For example, if we wanted to create the string 
'Hello, how are you?' from multiple strings, we could do: 'Hello' + ', ' + 'how are you?'
"""


def introduction(first_name, last_name):
    return last_name + ", " + first_name + " " + last_name


print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou


"""
Dog Years

Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. Write a function named 
dog_years() that has two parameters named name and age.

The function should compute the age in dog years and return the following string:

"{name}, you are {age} years old in dog years"

Test this function with your name and your age!

Since the age in dog years age * 7 is a number, we need to convert it to a string when concatenating using str(). 
For example: 'The age is: '+ str(age * 7).
"""


def dog_years(name, age):
    age_to_dog_years = age * 7
    return name + ", you are " + str(age_to_dog_years) + " years old in dog years"


print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"


"""
All Operations


Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d. The function should print 3 lines and return 1 value.

- First, print the sum of a and b.
- Second, print c minus d.
- Third, print the first number printed, multiplied by the second number printed.
- Finally, return the third number printed modulo a.

To make this problem easier, you can store the result of each mathematical operation into a variable and use them as the 
results in step 4. For example: first_result = a + b. Also, remember that you can take the modulo of a number with %.
"""


def lots_of_math(a, b, c, d):
    first = a + b
    second = c - d
    third = first * second
    fourth = third % a
    print(first)
    print(second)
    print(third)
    return fourth


print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
