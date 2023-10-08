while True:
    user_input = input("Please enter a string (or 'done' to exit): ")
    
    if user_input == 'done':
        print("Bye!")
        break
    special_chars = [',', '.', ':', '!', '?']
    cleaned_input = ''.join(char for char in user_input if char not in special_chars)
 
    cleaned_input = cleaned_input.upper()
    
    print(cleaned_input)

