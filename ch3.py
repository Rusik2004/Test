def num_divide3(num):
    count = 0
    for i in range(1, num + 1):
        if i % 3 == 0:
            count += 1
    return count
while True:
    user_input = input("Enter a positive integer or 'done' to quit: ")
    if user_input.lower() == 'done':
        print("bye !!!")
        break
    try:
        num = int(user_input)
        if num <= 0:
            print("Please enter a positive integer.")
        else:
            result = num_divide3(num)
            print(f"The number of numbers divisible by 3 from 1 to {num} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a positive integer or 'done' to quit.")