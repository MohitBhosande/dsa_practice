import random 
import string 


chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# ENCRIPT
plain_text =input("enter a message to encript: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"the original message : {plain_text}")
print(f"encripted message: {cipher_text}")

# DENCRIPT
cipher_text =input("enter a message to encript: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
print(f"encripted message: {cipher_text}")
print(f"the original message : {plain_text}")