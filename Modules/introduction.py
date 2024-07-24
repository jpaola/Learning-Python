import random
from datetime import datetime
from matplotlib import pyplot as plt
from decimal import Decimal
from library import always_three

current_time = datetime.now()
print(current_time)  # Will output your current time in the following format: 2024-07-24 18:04:55.228019

#################

random_list = [random.randint(1, 100) for number in range(101)]
randomer_number = random.choice(random_list)
print(randomer_number)  # Output will be a random number ranging from 1 to 100

#################

numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)
# Output will be a list of 12 random numbers ranging from 0 to 1000
# Ex. [24, 0, 475, 25, 518, 870, 109, 672, 76, 665, 281, 769]
# and a line graph with these values as plots
print(numbers_b)

plt.plot(numbers_a, numbers_b)
plt.show()

#################

two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)  # Output: 0.89

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)  # Output: 0.3445

#################


# calling functions from our own modules/file
print(always_three())   # Output: 3
