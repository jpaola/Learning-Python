sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print(sensors)
# Output: {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}


oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone",
                 "Animated Feature": "Zootopia"}
oscar_winners.update({"Supporting Actress": "Viola Davis"})
oscar_winners["Best Picture"] = "Moonlight"

print(oscar_winners)
# Output: {'Best Picture': 'Moonlight', 'Best Actor': 'Casey Affleck', 'Best Actress': 'Emma Stone',
# 'Animated Feature': 'Zootopia', 'Supporting Actress': 'Viola Davis'}


"""

You have two lists, representing some drinks sold at a coffee shop and the milligrams of caffeine in each. First, 
create a variable called 'zipped_drinks' that is an iterator of pairs between the 'drinks' list and the 'caffeine' list.

Create a dictionary called drinks_to_caffeine by using a dict comprehension that goes through the zipped_drinks 
iterator and turns each tuple pair into a key:value item."""

drinks = {"espresso", "chai", "decaf", "drip"}
caffeine = {64, 40, 0, 120}

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key: value for key, value in zipped_drinks}
print(drinks_to_caffeine)

# Output: {'espresso': 64, 'chai': 0, 'decaf': 40, 'drip': 120}


"""

We are building a music streaming service. We have provided two lists, representing songs in a user’s library and the 
amount of times each song has been played.

Using a dict comprehension, create a dictionary called plays that goes through zip(songs, playcounts) and creates a 
song:playcount pair for each song in songs and each playcount in playcounts.

After printing plays, add a new entry to it. The entry should be for the song "Purple Haze" and the playcount is 1.

This user has caught Aretha Franklin fever and listened to “Respect” 5 more times. Update the value for "Respect" to 
be 94 in the plays dictionary.

Create a dictionary called library that has two key: value pairs:

    - key "The Best Songs" with a value of plays, the dictionary you created
    - key "Sunday Feelings" with a value of an empty dictionary
"""

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key: value for key, value in zip(songs, playcounts)}
print(plays)

# Output: {'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 44, "What's Going On": 21, 'Respect': 89,
# 'Good Vibrations': 5}

plays.update({"Purple Haze": 1})
plays["Respect"] = 94
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)
# Output: {'The Best Songs': {'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 44, "What's Going On": 21,
# 'Respect': 94, 'Good Vibrations': 5, 'Purple Haze': 1}, 'Sunday Feelings': {}}


"""

Once you have a dictionary, you can access the values in it by providing the key.

"""

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"],
                   "earth": ["Taurus", "Virgo", "Capricorn"], "air": ["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])
# OR print(zodiac_elements.get("earth"))
# Output: ['Taurus', 'Virgo', 'Capricorn']

print(zodiac_elements["fire"])
# OR print(zodiac_elements.get("fire"))
# Output: ['Aries', 'Leo', 'Sagittarius']


"""

You are designing the video game Big Rock Adventure. We have provided a dictionary of items that are in the 
player’s inventory which add points to their health meter. In one line, add the corresponding value of the key 
"stamina grains" to the health_points variable and remove the item "stamina grains" from the dictionary. If the key 
does not exist, add 0 to health_points.

In one line, add the value of "power stew" to health_points and remove the item from the dictionary. If the key does 
not exist, add 0 to health_points.

In one line, add the value of "mystic bread" to health_points and remove the item from the dictionary. If the key 
does not exist, add 0 to health_points.

Print available_items and health_points.

"""

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25,
                   "stamina grains": 15, "power stew": 30}

health_points = 20
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items, "\n", health_points)
# Output: {'health potion': 10, 'cake of the cure': 5, 'green elixir': 20, 'strength sandwich': 25}
#  65

#########################

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931,
            "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18,
                 "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
# Output: dict_keys(['teraCoder', 'pythonGuy', 'samTheJavaMaam', 'lyleLoop', 'keysmithKeith'])
print(lessons)
# Output: dict_keys(['functions', 'syntax', 'control flow', 'loops', 'lists', 'classes', 'dictionaries'])

#########################

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18,
                 "dictionaries": 18}

total_exercises = 0

for value in list(num_exercises.values()):
    total_exercises += value

print(total_exercises)
# Output: 115


#########################

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37,
                           "Aerospace Engineer": 9}

for occupation, percent in pct_women_in_occupation.items():
    print("Women make up {} percent of {}".format(percent, occupation))

"""
Output:
Women make up 28 percent of CEO
Women make up 9 percent of Engineering Manager
Women make up 58 percent of Pharmacist
Women make up 40 percent of Physician
Women make up 37 percent of Lawyer
Women make up 9 percent of Aerospace Engineer
"""

#########################

tarot = {1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor", 5: "The Hierophant",
         6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice",
         12: "The Hanged Man", 13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star",
         18: "The Moon", 19: "The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}

spread = {"past": tarot.pop(13), "present": tarot.pop(22), "future": tarot.pop(10)}

for key, value in spread.items():
    print("Your {} is the {} card.".format(key, value))

# Output:
# Your past is the Death card.
# Your present is the The Fool card.
# Your future is the Wheel of Fortune card.


#########################

oscars = {"Best Picture": "Moonlight", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone",
          "Animated Feature": "Zootopia"}

for element in oscars:
    print(element)

# Output:
# Best Picture
# Best Actor
# Best Actress
# Animated Feature
