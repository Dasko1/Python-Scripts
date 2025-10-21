def format_name(f_name, l_name):
    first = f_name.title()
    last = l_name.title()
    return f"\nThe full name is: {first} {last}"

print(format_name(input("Enter first name: "), input("Enter last name: ")))