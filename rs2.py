file_name = "romeo.txt"
word_list = []

try:
    with open(file_name, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                if word not in word_list:
                    word_list.append(word)
    word_list.sort()
    print(word_list)

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
