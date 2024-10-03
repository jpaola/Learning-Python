can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
    if hasattr(element, "count"):
        print(str(type(element)) + " has the count attribute!")
    else:
        print(str(type(element)) + " does not have the count attribute :(")

'''
Output:
<class 'dict'> does not have the count attribute :(
<class 'str'> has the count attribute!
<class 'int'> does not have the count attribute :(
<class 'list'> has the count attribute!

This is because dictionaries and integers both do not have a .count attribute, while strings and lists do. In this 
exercise, we have iterated through can_we_count_it and used hasattr() to determine which elements have a .count 
attribute.
'''