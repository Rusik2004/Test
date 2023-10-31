numbers = []
while True:
    user_input = input("Please enter an integer (type 'done' to exit): ")
    if user_input == 'done':
        break
    try:
        number = int(user_input)
        numbers.append(number)
        average = sum(numbers) / len(numbers)
        print(f"{numbers} , average = {average:.2f}")
    except ValueError:
        print("Invalid input. Please enter an integer or 'done' to exit.")
print("---------- Bye !! --------------")
