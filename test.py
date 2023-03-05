import string
import random

def caesar(plaintext):
    plaintext = plaintext[::-1]
    p1 = plaintext[:len(plaintext)//2]
    p2 = plaintext[len(plaintext)//2:]
    return ''.join(random.choices(string.ascii_letters, k=5)) + plaintext + ''.join(random.choices(string.ascii_letters, k=5))

x = caesar('10 Days of Venus and Jupiter')
print(x.replace(' ', '%20'))
