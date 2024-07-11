"""
Create a function called username_generator take two inputs, first_name and last_name and returns a user_name. The username should be a slice of the first three letters of their first name and the first four letters of their last name. If their first name is less than three letters or their last name is less than four letters it should use their entire names.

For example, if the employee’s name is Abe Simpson the function should generate the username AbeSimp.
"""


def username_generator(first_name, last_name):
    if len(first_name) < 3:
        if len(last_name) < 3:
            user_name = first_name + last_name
        else:
            user_name = first_name + last_name[:4]
    elif len(last_name) < 3:
        user_name = first_name[:3] + last_name
    else:
        user_name = first_name[:3] + last_name[:4]
    return user_name


"""
Now for the temporary password, they want the function to take the input user name and shift all of the letters by one 
to the right, so the last letter of the username ends up as the first letter and so forth. For example, if the username 
is AbeSimp, then the temporary password generated should be pAbeSim.

Start by defining a function called password_generator that takes one parameter user_name and defines an empty string 
named password within the function body.
"""


def password_generator1(user_name):
    password = user_name[-1] + user_name[0:-2]
    return password


"""
Inside password_generator, create a for loop that iterates through the indices of user_name by going from 
0 to len(user_name).

The loop should create the password by shifting all the letters of user_name one to the right. To do so, add the letter 
at the previous index of user_name to password with each pass of the loop.

After the for loop but still within the definition of password_generator, return the password.
"""


def password_generator2(user_name):
    password = ""
    for index in range(0, len(user_name)):
        password += user_name[index - 1]
    return password
