import string
import random

def caesar(plaintext, shift):
    # output = ""
    # for ch in plaintext:
    #     if ch == " ":
    #         output += ch
    #     else:
    #         output += chr(ord(ch) + shift)
    # return output
    plaintext = plaintext[::-1]
    p1 = plaintext[:len(plaintext)//2]
    p2 = plaintext[len(plaintext)//2:]
    return ''.join(random.choices(string.ascii_letters, k=5)) + plaintext + ''.join(random.choices(string.ascii_letters, k=5))

print(caesar('10 Days of Venus and Jupiter', -10))