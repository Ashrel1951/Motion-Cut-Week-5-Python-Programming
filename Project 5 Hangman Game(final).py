import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# displays the categories
categories = {
    "Animals": ["elephant", "giraffe", "dolphin", "kangaroo", "penguin","lion","tiger","insects","bears"],
    "Fruits": ["apple", "banana", "cherry", "mango", "grape","cucumber","orange","melon","kiwi","blueberry"],
    "Countries": ["brazil", "canada", "japan", "germany", "india","united states","denmark","oman","zimbabwe"],
}

# let's the user select the difficulty level
difficulty_levels = {
    "Easy": 10,
    "Medium": 7,
    "Hard": 5,
}

# displays the diffrent stages of Hangman.
def display_hangman(tries):
    stages = [
        """
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
    ]
    return stages[tries]

def get_word(category):
    return random.choice(categories[category])

def hangman():
    clear_screen()
    print("Welcome to Hangman!\n")

    # choose category
    print("Categories:")
    for i, category in enumerate(categories.keys(), 1):
        print(f"{i}. {category}")
    
    while True:
        try:
            category_choice = int(input("Choose a category (1-3): ")) - 1
            if category_choice < 0 or category_choice >= len(categories):
                raise ValueError("Invalid choice.")
            category = list(categories.keys())[category_choice]
            break
        except ValueError:
            print("Invalid input. Please select a valid category number.")

    # choose difficulty level
    print("\nDifficulty Levels:")
    for i, level in enumerate(difficulty_levels.keys(), 1):
        print(f"{i}. {level}")
    
    while True:
        try:
            difficulty_choice = int(input("Choose a difficulty level (1-3): ")) - 1
            if difficulty_choice < 0 or difficulty_choice >= len(difficulty_levels):
                raise ValueError("Invalid choice.")
            difficulty = list(difficulty_levels.keys())[difficulty_choice]
            break
        except ValueError:
            print("Invalid input. Please select a valid difficulty level number.")

    max_tries = difficulty_levels[difficulty]
    word = get_word(category)
    guessed_word = ["_" for _ in word]
    guessed_letters = []
    tries = max_tries

    while tries > 0 and "_" in guessed_word:
        clear_screen()
        print(display_hangman(max_tries - tries))
        print(f"Category: {category} | Difficulty: {difficulty}")
        print(f"Word: {' '.join(guessed_word)}")
        print(f"Guessed Letters: {', '.join(guessed_letters)}")
        print(f"Tries Left: {tries}")

        if input("Do you want a hint? (yes/no): ").lower() == "yes":
            hint = next((c for c in word if c not in guessed_word), None)
            if hint:
                print(f"Hint: The word contains the letter '{hint}'")
            else:
                print("No more hints available.")

        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            tries -= 1

    clear_screen()
    if "_" not in guessed_word:
        print("Congratulations! You guessed the word:", word)
    else:
        print(display_hangman(max_tries - tries))
        print("Game Over. The word was:", word)

if __name__ == "__main__":
    hangman()
