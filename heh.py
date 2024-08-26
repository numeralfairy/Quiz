def quiz():
    # List of characters in order
    characters_list = [
        "Strawberry Shortcake",
        "Blueberry Muffin",
        "Orange Blossom",
        "Lemon Meringue",
        "Raspberry Torte",
        "Plum Pudding",
        "Cherry Jam"
    ]

    # Initialize a dictionary to keep track of the counts for each character
    characters = {character: 0 for character in characters_list}

    # Define the questions
    questions = [
        "What's your favorite color?",
        "Which season do you prefer?",
        "What is your favorite day of the week?",
        "What is your favorite food?"
    ]

    # Define the answer choices for each question
    answer_choices = [
        ["Pink", "Blue", "Orange", "Yellow", "Red", "Purple", "Indigo"],
        ["Summer", "Spring", "Fall", "Winter", "Sunny days", "Snowy days", "Rainy days"],
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        ["Cake", "Fruit", "Salad", "Pizza", "Burgers", "Sushi", "Candy"]
    ]

    # Ask each question
    for i in range(len(questions)):
        print(questions[i])
        for j, choice in enumerate(answer_choices[i]):
            print(f"{chr(97 + j)}: {choice}")

        answer = input("Enter the letter corresponding to your choice: ").lower()

        # Convert the answer to the corresponding index
        answer_index = ord(answer) - 97  # 'a' is 97 in ASCII, so 'a' corresponds to index 0, 'b' to 1, etc.

        # Increment the corresponding character count if the input is valid
        if 0 <= answer_index < len(characters_list):
            selected_character = characters_list[answer_index]
            characters[selected_character] += 1
        else:
            print("Invalid choice, please try again.")
            continue

    # Determine the character with the highest count
    result_character = max(characters, key=characters.get)

    # Output the result
    print(f"\nBased on your answers, you are most like: {result_character}!")

# Run the quiz
quiz()

