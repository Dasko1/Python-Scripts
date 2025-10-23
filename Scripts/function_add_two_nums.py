# Using a function with return to enter two numbers!

def add_two_nums(x, y):
    sum = int(x) + int(y)
    return f"Sum: {sum}"


print(add_two_nums(input("Enter first number: "), input("Enter second number: ")))