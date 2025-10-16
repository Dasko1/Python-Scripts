import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

string1 = ""
num_letters = 1
for char in range(0, num_letters):
    string1 = random.choice(letters)
print(string1)


# To increase number of letters printed, enter desired number of letters in l.5 & change l.7 to "+=".