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
    sortedList = sorted(unsorted)
    return sortedList


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
    item1_occurence = my_list.count(item1)
    item2_occurence = my_list.count(item2)

    if (item1_occurence > item2_occurence):
        return item1
    elif (item2_occurence > item1_occurence):
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
    while (len(my_list) > 0 and my_list[0] % 2 == 0):
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
        if (sum > 9000):
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
        if (num > maximum):
            maximum = num
    return maximum


print(max_num([50, -10, 0, 75, 20]))
# Should print 75
