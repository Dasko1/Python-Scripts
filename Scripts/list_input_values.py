# This creates a list in which you can enter values until you enter '$'.

# Enter when you want to stop putting values into the list
endChar = 'no'

# Clearing user input variable
list1 = ''

# Start with an empty list!
chars = []

# This is how you enter a list of values!
print("Enter your values, enter 'no' to finish.") # User prompt
while list1 != endChar: # Continue until 'no' is entered
    list1 = input("Value: ") # Get value
    chars.append(list1) # Add element to list

# Print out the list without the final 'no'!
del chars[-1]
print(chars)