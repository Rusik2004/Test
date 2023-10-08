user_input = input("Enter a string: ")
print("Input string =", user_input)

index = len(user_input) - 1

while index >= 0:
    print(user_input[index])
    index -= 1