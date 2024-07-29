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
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)

# Output: {'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 44, "What's Going On": 21, 'Respect': 89, 'Good Vibrations': 5}

plays.update({"Purple Haze": 1})
plays["Respect"] = 94
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)
# Output: {'The Best Songs': {'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 44, "What's Going On": 21, 'Respect': 94, 'Good Vibrations': 5, 'Purple Haze': 1}, 'Sunday Feelings': {}}