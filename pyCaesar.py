#!/usr/bin/env python

## pyCaesar v0.1
## Copyright (c) 2019 Patrick McDowell
## This code is licensed under the MIT license.

## ToDo: graceful interupt handler
##       import/export text from/to external file

lowerCase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperCase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def processCipher(action, text, rot):
    cipherText = ''

    # if we are decrypting the message, rotate backwards
    if (action == 'D' or action =='d'):
        rot *= -1

    # iterate through each letter in text, assess its numeric alphabetical postion, 
    # calculate its new position, then build a string with the new values
    for letter in text:
        if letter in lowerCase:
            pos = lowerCase.index(letter)
            newPos = rotate(pos, rot)
            cipherText += lowerCase[newPos]

        elif letter in upperCase:
            pos = upperCase.index(letter)
            newPos = rotate(pos, rot)
            cipherText += upperCase[newPos]
        
        else:
            cipherText += letter

    return cipherText

def rotate(num, rot):
    rotatedNum = num + rot

    # if the rotated number exceeds the number of letters in the alphabet, rotate back to the beginning
    if rotatedNum >= 26:
        rotatedNum -= 26
    return rotatedNum

def main():
    print """
                ____                           
  _ __  _   _ / ___|__ _  ___  ___  __ _ _ __ 
 | '_ \| | | | |   / _` |/ _ \/ __|/ _` | '__|
 | |_) | |_| | |__| (_| |  __/\__ \ (_| | |   
 | .__/ \__, |\____\__,_|\___||___/\__,_|_|   
 |_|    |___/                                                                 
    """

    print "\npyCaesar is a python script that will apply a Caesar cipher of a specified rotation to a block of text. It is capable of encrypting or decrypting, and can use positive or negative rotations.\n"
    
    # make sure we get a valid action
    while True:
        action = raw_input("Encrypt or decrypt (E/D)? ")
        if (action == 'e' or action == 'E' or action == 'd' or action == 'D'):
            break
        else:
            print "Type 'E' to encrypt or 'D' to decrypt."
    
    # make sure we get valid text
    while True:
        try:
            text = raw_input("Enter message: ")
        except:
            print "Could not parse message, please check formatting and try again."
            continue
        if text == '':
            print "No input detected, please try again."
        else:
            break

    # make sure we get a valid rotation
    while True:
        rot = int(raw_input("Enter rotation: "))
        if (rot > -26 and rot < 26):
            break
        else:
            print "Please enter a valid rotation between -25 and 25."
            continue

    cipherText = processCipher(action, text, rot)

    if (action  == 'E' or action == 'e'):
        print "\n-------------------\n" + "| Encrypted text: |\n" + "-------------------\n" + cipherText + "\n"
    else:
        print "\n-------------------\n" + "| Decrypted text: |\n" + "-------------------\n" + cipherText + "\n"

if __name__ == '__main__':
    main()