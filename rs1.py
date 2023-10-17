while True:
    user_input = input("Please enter two words (or 'done' to exit): ").strip().lower()
    if user_input == 'done' or not user_input:
        print("-- bye !!")
        break
    words = user_input.split()
    if len(words) == 1:
        word1 = word2 = words[0]
    elif len(words) == 2:
        word1, word2 = words[0], words[1]
    else:
        print("Invalid input. Please enter one or two words.")
        continue
    
    if word1 < word2:
        print(f"{word1} comes first")
    elif word2 < word1:
        print(f"{word2} comes first")
    else:
        print("The words are the same.")
