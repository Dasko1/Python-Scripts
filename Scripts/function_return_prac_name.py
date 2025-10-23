def format_name(f_name, l_name):
    first = f_name.title()
    last = l_name.title()
    return f"\nThe full name is: {first} {last}"

print(format_name(input("Enter first name: "), input("Enter last name: ")))


"""The flow first goes to l.1 of the function format_name; the flow then goes to the function
call at l.6, where the arguments get inputted. The flow then goes to l.1, where the arguments
input in l.6 are put into the parameters of the function. The flow then goes to ll.2-3 for the
logic, and the output key word, return, outputs everything done by the function format_name!
"""