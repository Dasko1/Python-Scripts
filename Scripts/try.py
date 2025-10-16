alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
shift_amount = 1
# shift1 = int(input("Places to shift1: "))
# shift1 = alphabet.index('c')
# print(shift1)
# print(alphabet[shift1])
# print(alphabet[0])

# print('_________________________________________________\n')
plain_text = input("Enter plain text: ")			# plain_text ="hello"

x = [plain_text]
y = list(''.join(x))

element_count = len(y)
i = 0
z = 0

while i < element_count:

    shift = alphabet.index(y[z])
    new_pos = shift + shift_amount
    
    for letter in y:
        # print(y[z], end='')					# This is correct! Just advance alphabet 1 to right!
        z += 1
        i += 1
        # new_pos += 1
        print(alphabet[new_pos], end='')
        
print("\n" + alphabet[new_pos])
    
print("")


shift = alphabet.index(y[0])

# What position is 'h' in the list 'alphabet'?
# print("The position of " + y[0] + " in the alphabet list is: " + str(shift))

# print("\nNow move a letter over!")

new_pos = shift + shift_amount

# print("The new position of " + y[1] + " in the alphabet list is: " + alphabet[new_pos])

# print("___________________________________________________\n")

# Success for ll.10-22: You find 1 element in list, then shift1 over by 1 & print that new element!
# fruits = ["Apple", "Pear", "Orange"]
# shift1 = fruits.index('Pear')
# print("The position of the selected fruit is: " + str(shift1))
# print("The fruit in position " + str(shift1) + " is: " + fruits[shift1])
# 
# print("\nNow move one over!")
# 
# new_pos1 = shift1 + shift_amount
# 
# print("The new position of the selected fruit is: " + str(new_pos1))
# print("The fruit in position " + str(new_pos1) + " is: " + fruits[new_pos1])
# 
# print("_______________________________________________\n")
    
# plain_text ="hello"
# x = [plain_text]
# y = list(''.join(x))
# print(y)
# print(y[0])
# 
# shift1_amount = 1
# 

# for letter in plain_text:
#     pos_of_letter1 = y[0]
#     letterNum1 = plain_text.index(pos_of_letter1)
#     # new_pos = int(pos_of_letter1) + shift1_amount
# print(pos_of_letter1)
# print(letterNum1)
# print(new_pos)
    
# for letter in alphabet:
#     # shift1_amount = alphabet.index("c")
#     shift1_amount = 2
# # print(shift1_amount)
# print(alphabet[shift1_amount])