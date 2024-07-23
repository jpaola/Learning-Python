"""
Using the Caesar Cipher technique decipher the following message:

'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx
jxu iqcu evviuj!'

The Caesar Cipher works by shifting letters by a certain offset. For example, a message "hello" using an offset of 3
would encode a message by shifting each letter 3 places to the left with respect to the alphabet. So "h" becomes "e",
"e" becomes "b", "l" becomes "i", and "o" becomes "l". Then I have my encoded message, "ebiil"!

Now I can send you my message and the offset, and you can decode it by shifting each letter 3 places to the right. The
best thing is that Julius Caesar himself used this cipher, that's why it's called the Caesar Cipher!

Our message above will require an offset of 10 to decode it.
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

translated_message = ""

for character in message:
    if character in alphabet:
        character_index = alphabet.find(character)
        translated_message += alphabet[(character_index + 10) % 26]
    else:
        translated_message += character
print(translated_message)

"""

Decoded message: 
hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me 
a message back with the same offset!

"""

"""
Now let's have fun and send back an encoded message, but this time using an offset of 8 and use any character casing.
"""

alphabet_all_case = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
my_message_back = "Hi there! I received your message and using the Caesar Cipher is fun! Let's have game night!"

translated_message = ""

for character in my_message_back:
    if character in alphabet_all_case:
        character_index = alphabet_all_case.find(character)
        translated_message += alphabet_all_case[(character_index - 8) % 52]
    else:
        translated_message += character
print(translated_message)

"""
Encrypted message: 
za lZWjW! A jWUWanWV qgmj eWkkSYW SfV mkafY lZW uSWkSj uahZWj ak Xmf! DWl'k ZSnW YSeW faYZl!
"""

"""
Next, make functions for decoding and encoding. Here is another message, this time with two 
encoded messages.

The first one is coded just like before with an offset of ten, and it contains a hint for decoding the second message!

First message:

    jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.
    
Second message:

    bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!

"""


def caesar_decode(offset, encrypted_message):
    decoded_message = ""

    for char in encrypted_message:
        if char in alphabet:
            char_index = alphabet.find(char)
            decoded_message += alphabet[(char_index + offset) % 26]
        else:
            decoded_message += char
    return decoded_message


first_message = caesar_decode(10, "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.")
print(first_message)  # Response is "the offset for the second message is fourteen."

second_message = caesar_decode(14, "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!")
print(second_message)  # Response is "performing multiple caesar ciphers to code your messages is even more secure!"


def caesar_encode(offset, encrypted_message):
    encoded_message = ""

    for char in encrypted_message:
        if char in alphabet:
            char_index = alphabet.find(char)
            encoded_message += alphabet[(char_index - offset) % 26]
        else:
            encoded_message += char
    return encoded_message


"""
Next we have a message but we do not know the offset value. Let's brute force a few checks and see if we can break 
through.

Message :  'vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px 
ptgm mh dxxi hnk fxlltzxl ltyx.'

"""

count = 10

while count > 0:
    hidden_message = caesar_decode(count, "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh "
                                          "kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.")
    print(hidden_message + " offset: {}".format(count))
    count -= 1

"""
Output:

frpsxwhuv kdyh uhqghuhg doo ri wkhvh rog flskhuv revrohwh. zh'oo kdyh wr uhdoob vwhs xs rxu jdph li zh zdqw wr nhhs rxu phvvdjhv vdih. offset: 10
eqorwvgtu jcxg tgpfgtgf cnn qh vjgug qnf ekrjgtu qduqngvg. yg'nn jcxg vq tgcnna uvgr wr qwt icog kh yg ycpv vq mggr qwt oguucigu uchg. offset: 9
dpnqvufst ibwf sfoefsfe bmm pg uiftf pme djqifst pctpmfuf. xf'mm ibwf up sfbmmz tufq vq pvs hbnf jg xf xbou up lffq pvs nfttbhft tbgf. offset: 8
computers have rendered all of these old ciphers obsolete. we'll have to really step up our game if we want to keep our messages safe. offset: 7
bnlotsdqr gzud qdmcdqdc zkk ne sgdrd nkc bhogdqr narnkdsd. vd'kk gzud sn qdzkkx rsdo to ntq fzld he vd vzms sn jddo ntq ldrrzfdr rzed. offset: 6
amknsrcpq fytc pclbcpcb yjj md rfcqc mjb agnfcpq mzqmjcrc. uc'jj fytc rm pcyjjw qrcn sn msp eykc gd uc uylr rm iccn msp kcqqyecq qydc. offset: 5
zljmrqbop exsb obkaboba xii lc qebpb lia zfmebop lyplibqb. tb'ii exsb ql obxiiv pqbm rm lro dxjb fc tb txkq ql hbbm lro jbppxdbp pxcb. offset: 4
ykilqpano dwra najzanaz whh kb pdaoa khz yeldano kxokhapa. sa'hh dwra pk nawhhu opal ql kqn cwia eb sa swjp pk gaal kqn iaoowcao owba. offset: 3
xjhkpozmn cvqz mziyzmzy vgg ja ocznz jgy xdkczmn jwnjgzoz. rz'gg cvqz oj mzvggt nozk pk jpm bvhz da rz rvio oj fzzk jpm hznnvbzn nvaz. offset: 2
wigjonylm bupy lyhxylyx uff iz nbymy ifx wcjbylm ivmifyny. qy'ff bupy ni lyuffs mnyj oj iol augy cz qy quhn ni eyyj iol gymmuaym muzy. offset: 1

Our message is hidden using the offset of 7.
"""