user_input = input("Please enter a string: ")
uppercase_count = 0
lowercase_count = 0
number_count = 0
other_count = 0
for char in user_input:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        number_count += 1
    else:
        other_count += 1
print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)
print("Numbers:", number_count)
print("Other characters:", other_count)
