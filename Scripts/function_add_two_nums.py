# Using a function with return to enter two numbers!  Remember the x & 7 of l.3 are the
# parameters and the inputs from l.9 are the arguments!

def add_two_nums(x, y):
    sum = int(x) + int(y)
    return f"Sum: {sum}"


print(add_two_nums(input("Enter first number: "), input("Enter second number: ")))