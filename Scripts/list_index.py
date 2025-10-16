import random

fruit_getter = random.randint(0, 4)

fruits = ["apples", "bananas", "cherries", "dates"]

fruit_position = (fruits.index("bananas"))
print(fruit_position)

fruit_in_position = fruits[fruit_getter]
print(fruit_in_position)

print("\nThe fruit in list position " + str(fruit_getter) + " is: " + str(fruits[fruit_getter]))