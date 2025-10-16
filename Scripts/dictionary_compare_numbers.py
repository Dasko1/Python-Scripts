# Enter numbers and compare them or add them.

numbers = {"a": "",
           "b": ""}

for i in range(1):
    first_num = 	input("Enter first number: ")
    second_num = 	input("Enter second number: ")
    
    numbers["a"] = first_num
    numbers["b"] = second_num
    
    sum = int(first_num) + int(second_num)
    
    if numbers["a"] > numbers["b"]:
        print(numbers["a"]  + " is bigger than " + numbers["b"] + "!")
    else:
        print(numbers["b"]  + " is bigger than " + numbers["a"] + "!")
    
print("\nThe first value is: ",numbers["a"])
print("The sum of the entered values is: ",sum)