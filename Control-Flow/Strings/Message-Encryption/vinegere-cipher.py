"""
Vigenère Cipher, invented by an Italian cryptologist named Giovan Battista Bellaso in the 16th
century, but named after another cryptologist from the 16th century, Blaise de Vigenère.

The Vigenère Cipher is a poly alphabetic substitution cipher, as opposed to the Caesar Cipher which was a
mono alphabetic substitution cipher. What this means is that opposed to having a single shift applied to every
letter, the Vigenère Cipher has a different shift for each letter. The value of the shift for each letter
is determined by a given keyword.

Consider the message:

    barry is the spy

If we want to code this message, first we choose a keyword. For this example, we'll use the keyword

    dog

Now we repeat the keyword over and over to generate a keyword phrase that is the same length as the message we want
to code. So if we want to code the message "barry is the spy" our keyword phrase is "dogdo gd ogd ogd". Now we are
ready to start coding our message. We shift each letter of our message by the place value of the corresponding letter
in the keyword phrase, assuming that "a" has a place value of 0, "b" has a place value of 1, and so forth.

              message:    b  a  r  r  y    i  s    t  h  e    s  p  y

       keyword phrase:    d  o  g  d  o    g  d    o  g  d    o  g  d

resulting place value:    24 12 11 14 10   2  15   5  1  1    4  9  21

So we shift "b", which has an index of 1, by the index of "d", which is 3. This gives us a place value of 24,
which is "y". Remember to loop back around when we reach either end of the alphabet! Then continue the trend: we
shift "a" by the place value of "o", 14, and get "m", we shift "r" by the place value of "g", 15, and get "l",
shift the next "r" by 4 places and get "o", and so forth. Once we complete all the shifts, we end up with our coded
message:

    ymlok cp fbb ejv

As you can imagine, this is a lot harder to crack without knowing the keyword! So now comes the hard part. I'll give
you a message and the keyword, and you'll see if you can figure out how to crack it! Ready? Okay here's my message:

    txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!

and the keyword to decode my message is

    friends

Like the Ceasar Cipher, you'll only want to shift characters that are in the alphabet. Your keyword phrase should
ignore any
spaces and punctuation in the original message. For example, given the message

ciphers are awesome!

and the keyword

cat

the keyword phrase would be:

catcatc atc atcatca

and the encoded string would be:

aiwfeyq ayc adcsvke!

Each letter in the alphabet has a specified index as follows.

a   |b  |c  |d  |e  |f  |g  |h  |i  |j  |k  |l  |m  |n  |o  |p  |q  |r  |s  |t  |u  |v  |w  |x  |y  |z  |
0   |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |11 |12 |13 |14 |15 |16 |17 |18 |19 |20 |21 |22 |23 |24 |25 |

If we have a keyword: 'banana' and a message 'h lbvr pdaaugs' the cipher would look as follows.

    h   l   b   v   r   p   d   a   a   u   g   s
    7   11  1   21  17  15  3   0   0   20  6   18
    b   a   n   a   n   a   b   a   n   a   n   a
    1   0   13  0   13  0   1   0   13  0   13  0
+__________________________________________________
    8   11  14  21  4   15  4   0   13  20  19  18

Therefore, the encrypted message would look like:
    i   l   o   v   e   p   e   a   n   u   t   s

"""

alphabet = "abcdefghijklmnopqrstuvwxyz"


def vigenere_cipher_decoder(keyword, encrypted_message):
    decoded_message = ""
    keyword_phrase = ""
    keyword_index = 0

    # map the keyword to the encrypted message, for example, in this case: 'b anan abanana' for 'h lbvr pdaaugs'
    for character in encrypted_message:
        if keyword_index >= len(keyword):
            keyword_index = 0
        if character in alphabet:
            keyword_phrase += keyword[keyword_index]
            keyword_index += 1
        else:
            keyword_phrase += character

    #  at this point keyword_phrase = 'b anan abanana'

    for index in range(len(encrypted_message)):
        #  if the character is in the alphabet
        if encrypted_message[index] in alphabet:
            # store the index of the character into old_character_index
            #     h   l   b   v   r   p   d   a   a   u   g   s
            #     7   11  1   21  17  15  3   0   0   20  6   18
            old_character_index = alphabet.find(encrypted_message[index])

            # additionally, find and get the keyword_phrase character index and assign it to the offset_index
            #     b   a   n   a   n   a   b   a   n   a   n   a
            #     1   0   13  0   13  0   1   0   13  0   13  0
            offset_index = alphabet.find(keyword_phrase[index])

            # now, let us get the new_character using this offset and concatenate with the decoded_message
            # +__________________________________________________
            #     8   11  14  21  4   15  4   0   13  20  19  18
            #     i   l   o   v   e   p   e   a   n   u   t   s

            new_character = alphabet[(old_character_index + offset_index) % 26]
            decoded_message += new_character
        else:
            # if the character is not a part of or within the alphabet, concatenate to the decoded message as is
            decoded_message += encrypted_message[index]

    return decoded_message


vigenere_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
vigenere_keyword = "friends"
decode_message = vigenere_cipher_decoder(vigenere_keyword, vigenere_message)
print("decode_message: {}".format(
    decode_message))  # Expected output: 'you were able to decode this? nice work! you are becoming quite the expert
# at crytography!'

"""

Finally, let's write a function that can encode a message using a given keyword and write out a message to send to a 
friend.

"""


def vigenere_cipher_encoder(keyword, message):
    encoded_message = ""
    keyword_phrase = ""
    keyword_index = 0

    # map the keyword to the encrypted message, for example, in this case: 'b anan abanana' for 'i love peanuts'
    for character in message:
        if keyword_index >= len(keyword):
            keyword_index = 0
        if character in alphabet:
            keyword_phrase += keyword[keyword_index]
            keyword_index += 1
        else:
            keyword_phrase += character

    #  at this point keyword_phrase = 'b anan abanana'

    for index in range(len(message)):
        #  if the character is in the alphabet
        if message[index] in alphabet:
            # store the index of the character into old_character_index
            #     i   l   o   v   e   p   e   a   n   u   t   s
            #     8   11  14  21` 4   15  4   0   13  20  19  18
            old_character_index = alphabet.find(message[index])

            # additionally, find and get the keyword_phrase character index and assign it to the offset_index
            #     b   a   n   a   n   a   b   a   n   a   n   a
            #     1   0   13  0   13  0   1   0   13  0   13  0
            offset_index = alphabet.find(keyword_phrase[index])

            # now, let us get the new_character using this offset and concatenate with the encoded_message
            # -__________________________________________________
            #      7  11  1   21  17  15  3   0   0   20  6   18
            #      h  l   b   v   r   p   d   a   a   u   g   s

            new_character = alphabet[(old_character_index - offset_index) % 26]
            encoded_message += new_character
        else:
            # if the character is not a part of or within the alphabet, concatenate to the encoded_message as is
            encoded_message += message[index]

    return encoded_message


encode_message = vigenere_cipher_encoder("banana", "i love peanuts")
print("encode_message: {}".format(encode_message))  # Expected output: 'h lbvr pdaaugs`

# Let's test that the same encrypted message gets masked correctly
print("decoded banana message: {}".format(vigenere_cipher_decoder("banana", "h lbvr pdaaugs")))
