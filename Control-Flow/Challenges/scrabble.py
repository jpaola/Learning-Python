"""

Create a dictionary called player_to_words that maps players to a list of the words they have played. This table
represents the data to transcribe into your dictionary:


player1	    wordNerd	   Lexi Con	    Prof Reader
BLUE	    EARTH	       ERASER	    ZAP
TENNIS	    EYES	       BELLY	    COMA
EXIT	    MACHINE	       HUSKY	    PERIOD

Create an empty dictionary called player_to_points.

Iterate through the items in player_to_words. Call each player and each list of words.

Within your loop, create a variable called player_points and set it to 0.

Within the loop, create another loop that goes through each word in words and adds the value of score_word() with
word as an input.

After the inner loop ends, set the current player value to be a key of player_to_points, with a value of player_points.

player_to_points should now contain the mapping of players to how many points they’ve scored. Print this out to see
the current standings for this game!

If you’ve calculated correctly, wordNerd should be winning by 1 point.

"""

#  NOTE: I could have called the built-in function to either set upper or lower, but I wanted to prevent calling
#  that function for every word or letter in the list. In a larger application, it's good to know which approach is
#  best suited. Here, I chose to keep a list of all cases for every letter in the alphabet. I am certain there are
#  better approaches.
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 1, 3, 3, 2, 1, 4, 2, 4, 1, 8,
          5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {key: value for key, value in zip(letters, points)}

letters_to_points[" "] = 0

player_to_words = {"player 1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": [
    "ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}


# letters_to_points should look like this: {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
# 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 4, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4,
# 'x': 8, 'y': 4, 'z': 10, 'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5,
# 'L': 1, 'M': 3, 'N': 4, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4,
# 'Z': 10, ' ': 0}

# A function that computes the score per word played
def score_word(word):
    point_total = 0

    for letter in word:
        point_total += letters_to_points.get(letter, 0)
    return point_total


# A function that would take in a player and a word, and add that word to the list of words they’ve played
def play_word(player, word):
    if player in player_to_words:
        player_to_words[player].append(word)
    else:
        player_to_words[player] = [word]


# A function that you can call any time a word is played
def update_point_totals():
    player_to_points = {}
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points
    return player_to_points


print(update_point_totals())
# Output: {'player 1': 29, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31}

play_word("foo", "bar")
print(player_to_words)
# Output: {'player 1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER',
# 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD'], 'foo': ['bar']}

print(update_point_totals())
#  Output: {'player 1': 29, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31, 'foo': 5}

brownie_points = score_word("BROWNIE")
print(brownie_points)
# Output: 15
