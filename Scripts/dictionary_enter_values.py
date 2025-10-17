# This creates a dictionary where the User enters names & favorite programming languages.
# See ll.31-46 for how it works!! 

# Create an empty dictionary to store the user data
user_profiles = {}

# Set a flag to control the while loop
polling_active = True

# Start the loop
while polling_active:
    # Prompt the user for the name and favorite language
    name = input("\nWhat is your name? ")
    language = input("What is your favorite programming language? ")

    # Add the user's input to the dictionary
    user_profiles[name] = language

    # Ask the user if they want to enter another profile
    repeat = input("Would you like to add another user? (yes/no) ")
    if repeat.lower() == 'no':
        # If the user enters 'no', change the flag to exit the loop
        polling_active = False

# Print the results of the poll
print("\n--- User Profiles ---")
for name, language in user_profiles.items():
    print(f"{name}'s favorite language is {language}.")
    

# How the code works

# Initialize an empty dictionary: user_profiles = {} creates an empty dictionary that will
# be populated during the loop.
# 
# Use a flag: A variable named polling_active is set to True. This flag keeps the while loop
# running as long as it remains True.
# 
# Get user input: Inside the loop, the input() function prompts the user to enter a key (name)
# and a value (language).
# Add to the dictionary: The line user_profiles[name] = language adds a new key-value pair
# to the dictionary. If the key already exists, its value is updated.
# Control the loop: The program asks the user if they want to continue. If the user enters
# "no," the polling_active flag is set to False, and the loop terminates.
# Print the final dictionary: After the loop ends, a for loop iterates through the dictionary's
# items to print each stored profile. 
