import string

# ----- Some Hints -----
# This will give you a string with all the lowercase letters in the alphabet
alphabet = string.ascii_lowercase
print(f"{alphabet = }")

# You can look up the index of a letter in the alphabet like this:
index = alphabet.index("n")
print(f"position of 'n' in the alphabet: {index}")

# The computer already thinks of all the characters it can print out as numbers.
# If you want to, you can look up what number a character corresponds to in
# "ASCII" encoding:
ascii_number = ord("n")
print(f"ascii number representation of 'n': {ascii_number}")

ascii_letter = chr(4)
print(f"ascii letter at position #4: {ascii_letter}")

# ----- Your Algorithm -----

# Your task is to encrypt this secret message into ciphertext
plaintext = "nein"

# Initialize your ciphertext an empty string
ciphertext = ""
for character in plaintext:
    if character in "aejou":
        encrypted_character = "n"
    else:
        encrypted_character = character
    ciphertext += encrypted_character

print(f"{ciphertext = }")