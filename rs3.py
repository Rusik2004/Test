sender_list = []
file_name = "mbox.txt"
line_count = 0
try:
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("From "):
                words = line.split()
                if len(words) > 1:
                    sender = words[1]
                    sender_list.append(sender)
    for sender in sender_list:
        print(sender)
    line_count = len(sender_list)
    print(f"Total {line_count} lines were printed")
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

