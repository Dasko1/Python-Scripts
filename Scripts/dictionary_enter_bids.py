# This creates a dictionary where the User enters names & bids.  Various ways to print results.

# Create an empty dictionary to store the user data
user_bids = {}

# Set a flag to control the while loop
polling_active = True

# Start the loop
while polling_active:
    # Prompt the user for the name and favorite bid
    name = input("\nWhat is your name? ")
    bid = input("What is your bid? ")
    bid_int = int(bid)

    # Add the user's input to the dictionary
    user_bids[name] = bid_int

    # Ask the user if they want to enter another profile
    repeat = input("Would you like to add another user? (yes/no) ")
    if repeat.lower() == 'no':
        # If the user enters 'no', change the flag to exit the loop
        polling_active = False

# Print the results of the poll
print(f"\nThe dictionary is: {user_bids}" )
winning_bid = max(user_bids.values())
print(f"Highest: {winning_bid}")

# Get the highest bidder!
winning_bidder = max(user_bids, key=user_bids.get)


print("\n--- User Profiles ---")
for name, bid in user_bids.items():
    print(f"{name}'s bid is {bid}.")  

print(f"\nThe winner is: {winning_bidder} with {winning_bid}")
