import random
import string

# Generate a random string of 999 characters using letters, digits, and punctuation
characters = string.ascii_letters + string.digits + string.punctuation
random_string = ''.join(random.choices(characters, k=999))

# Save the string to a text file
with open("random_string_999.txt", "w", encoding="utf-8") as file:
    file.write(random_string)

print("The random string has been saved to 'random_string_999.txt'.")