def quiz():
    # Define the characters and corresponding answers
    characters = {
        "Strawberry Shortcake": 0,
        "Blueberry Muffin": 0,
        "Orange Blossom": 0,
        "Lemon Meringue": 0,
        "Raspberry Torte": 0,
        "Plum Pudding": 0,
        "Cherry Jam": 0
    }

    # Define the questions and the corresponding answer choices
    questions = [
        {
            "question": "What's your favorite color?",
            "choices": {
                "a": "Pink",
                "b": "Blue",
                "c": "Orange",
                "d": "Lemon",
                "e": "Red",
                "f": "Purple",
                "g": "Indigo"
            }
        },
        {
            "question": "Which season do you prefer?",
            "choices": {
                "a": "Summer!",
                "b": "I love the beach, so Summer!",
                "c": "The season of flowers, Spring!",
                "d": "As long as the sun is shining!",
                "e": "Winter, I love the snow",
                "f": "The fall, I love the colors",
                "g": "Right between summer and fall"
            }
        },
        {
            "question": "What is your favorite day of the week?",
            "choices": {
                "a": "Fridayyyy, it is the happiest day of the week",
                "b": "Wednesday? I love the middle of the week",
                "c": "Saturday! I love to sleep in",
                "d": "Monday for sure, I love to start fresh",
                "e": "Thursday, it's almost the weekend",
                "f": "Sunday, it's so nice to be able to relax",
                "g": "Friday. Staying up all night is the best"
            }
        },
        {
            "question": "What is your favorite day of the week?",
            "choices": {
                "a": "Fridayyyy, it is the happiest day of the week",
                "b": "Wednesday? I love the middle of the week",
                "c": "Saturday! I love to sleep in",
                "d": "Monday for sure, I love to start fresh",
                "e": "Thursday, it's almost the weekend",
                "f": "Sunday, it's so nice to be able to relax",
                "g": "Friday. Staying up all night is the best"
            }
        },
        {
            "question": "What is your favorite food?",
            "choices": {
                "a": "Candy? Cake? Anything sweet!",
                "b": "Mmm burgers",
                "c": "Fruit is always a safe choice",
                "d": "I love a good salad",
                "e": "Pizza is the best!",
                "f": "Sour candy is the best!!",
                "g": "Sushi! Sushi! Sushi!"
            }
        },
        # Add more questions as needed
    ]

    # Ask each question
    for q in questions:
        print(q["question"])
        for key, value in q["choices"].items():
            print(f"{key}: {value}")

        answer = input("Enter the letter corresponding to your choice: ").lower()

        # Increment the corresponding character count
        if answer in q["choices"]:
            character = q["choices"].items()
            print(character)
            print(f"You chose: {character}")
            characters[character] += 1
        else:
            print("Invalid choice, please try again.")
            continue

    # Determine the character with the highest count
    result_character = max(characters, key=characters.get)

    # Output the result
    print(f"\nBased on your answers, you are most like: {result_character}!")


# Run the quiz
quiz()
