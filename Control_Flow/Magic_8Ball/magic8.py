# Magic 8-Ball 🎱
# Paola jiron
import random

'''
All possible answers in order:

1. Yes - definitely!
2. It is decidedly so
3. Without a doubt
4. Reply hazy, try again
5. Ask again later
6. Better not tell you now
7. My sources say no
8. Outlook not so good
9. Very doubtful
10. I hate to be the bearer of bad news
11. Absolutely!
12. Things are quite unclear
13. Ask a different question
14. Not to be mean but, try asking something realistic
15. Hmmm... do you really want to know?
16. No...
'''

name = input("Enter your name: ")
question = input("Ask me something: ")
answer = ""
random_number = random.randint(1,16)


if question == "":
    print("Did you want to ask me something?")
else:
    if random_number == 1:
        answer = "Yes - definitely!"
    elif random_number == 2:
        answer = "It is decidedly so"
    elif random_number == 3:
        answer = "Without a doubt"
    elif random_number == 4:
        answer = "Reply hazy, try again"
    elif random_number == 5:
        answer = "Ask again later"
    elif random_number == 6:
        answer = "Better not tell you now"
    elif random_number == 7:
        answer = "My sources say no"
    elif random_number == 8:
        answer = "Outlook not so good"
    elif random_number == 9:
        answer = "Very doubtful"
    elif random_number == 10:
        answer = "I hate to be the bearer of bad news"
    elif random_number == 11:
        answer = "Absolutely!"
    elif random_number == 12:
        answer = "Things are quite unclear"
    elif random_number == 13:
        answer = "Ask a different question"
    elif random_number == 14:
        answer = "Not to be mean but, try asking something realistic"
    elif random_number == 15:
        answer = "Hmmm... do you really want to know?"
    elif random_number == 16:
        answer = "No..."
    else:
        answer = "Error"
    
    if name == "":
        print("Question: " + question)
    else:
        print(name + " asks: " + question)
    print("Magic 🎱 8-Ball's answer: " + answer)