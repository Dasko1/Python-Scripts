fruits = ["Apple", "Pear", "Orange"]
shift_amount = 1


shift1 = fruits.index('Apple')
print("The position of the selected fruit is: " + str(shift1))
print("The fruit in position " + str(shift1) + " is: " + fruits[shift1])

print("\nNow move one over!")

new_pos1 = shift1 + shift_amount

print("The new position of the selected fruit is: " + str(new_pos1))
print("The fruit in position " + str(new_pos1) + " is: " + fruits[new_pos1])
