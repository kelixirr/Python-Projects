import sys 
import os
import random
from collections import defaultdict, Counter

# a function to load the file 
def load_file(infile):
    
    """Read and return text file as a string of lowercase"""

    with open(infile, encoding='utf-8', errors='ignore') as f:
        loaded_string = f.read().lower()
    return loaded_string

# a function to convert string into dict
def make_dict(text, shift):
    
    """ Return dictionary of characters and shifted indexes"""

    char_dict = defaultdict(list)
    
    for index, char in enumerate(text):
        char_dict[char].append(index+shift)

    return char_dict


# Encrypting the message
def encrypt(message, char_dict):
    
    """Return list of indexes represting characters in a message"""

    encrypted = []

    for char in message.lower():
        if len(char_dict[char]) > 1:
            index = random.choice(char_dict[char])
        # random choice fails if there is only one choice    
        elif len(char_dict[char]) == 1:
            index = char_dict[char][0]
        elif len(char_dict[char]) == 0:
            print("\nCharacter {} not in dictionary".format(char))
            continue 
        encrypted.append(index)
    return encrypted

# Decrypting the message
def decrypt(message, text, shift):
    """Decrypt ciphertext list and return plaintext string"""

    plaintext = ''
    indexes = [s.replace(',','').replace('[', '').replace(']','') for s in message.split()]

    for i in indexes:
        plaintext += text[int(i) - shift]
    return plaintext

# checking for failure or duplicate keys to prevent encryption from compromise

def check_for_fail(ciphertext):
    """ Return True if ciphertext contains any duplicate keys."""

    check = [k for k, v, in Counter(ciphertext).items() if v > 1]

    if len(check) > 0:
        return True 

# creating the main function for users experience

def main():
    
    # enter the message 
    message = input("Enter plaintext or ciphertext: ")

    # asking for encryption or decryption
    process = input("Enter 'encrypt' or 'decrypt': ")
    
    while process not in ('encrypt', 'decrypt'):
        process = input("Invalid value.Enter digit from 1 to 366")

    # creating a shift value: 
    shift = int(input("Shift value(1-366) = "))

    while not 1<= shift <=366:
        shift = int(input("Invalid value.Enter digit from 1 to 366: "))

    # accepting file and validating it   
    infile = input("Enter filename with extension")

    if not os.path.exists(infile):
        print("File {} not found. Terminating.".format(infile), file=sys.stderr)
        sys.eixt(1)

    # storing the file and creating dict
    text = load_file(infile)
    char_dict =  make_dict(text, shift)

    # conditions for encryption

    if process == 'encrypt':
        ciphertext = encrypt(message, char_dict)

        if check_for_fail(ciphertext):
            print("\nProblem finding unique keys.", file=sys.stderr)
            sys.exit()
        
        # to help you guide you what to put in message print the contents of character dictionary

        print("\nCharacter and number occurrences in char_dict:\n")

        print("{: >10}{: >10}{: >10}".format('Character', 'Unicode', 'Count'))

        for key in sorted(char_dict.keys()):
            print('{:>10}{:>10}{:>10}'.fomat(repr(key)[1:-1], str(ord(key)), len(char_dict[key])))

        print("\nNumber of distint characters: {}".format(len(char_dict)))
        print("Total number of characters:{:,}\n".format(len(text)))

        print("encrypted ciphertext = \n{}\n".format(ciphertext))
        print("decrypted plaintext = ")

        for i in ciphertext: 
            print(text[i - shift], end='', flush=True)

    # condition for decryption
    elif process == 'decrypt':
        plaintext = decrypt(message, text, shift)
        print("\Nndecrypted plaintext = \n{}".format(plaintext))
            
        



