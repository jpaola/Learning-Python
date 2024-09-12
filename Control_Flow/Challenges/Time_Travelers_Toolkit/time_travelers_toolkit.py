"""
In this project, you’ll create a Python script to simulate the experience of time travel using various Python
modules. You’ll start by building a custom module, then work with dates and times, perform precise calculations,
implement random selection features, and finally, generate a personalized time travel message.
"""
import random
import custom_module
import datetime as dt
from decimal import Decimal

todays_date = dt.datetime.now()
base_cost = Decimal('1000.00')
time_travel_cost = abs(base_cost - Decimal('100.00'))
final_cost = f"{time_travel_cost: .2f}"
random_year = random.randint(1800, 2025)
destination = random.choice(
    ["France", "Egypt", "China", "North America", "Africa", "Russia", "Japan", "Central America", "Korea",
     "South America", "Australia"])

print(custom_module.generate_time_travel_message(year=random_year, destination=destination, cost=final_cost))
