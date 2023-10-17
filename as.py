try:
    file_name = input("Enter a file name: ")
    
    with open(file_name, 'r') as file:
        for line in file:
            print(line.upper(), end='')

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
