import random
import hangman_stages
import words_file

# Difficulty levels
difficulty_levels = {
    "Easy": 10,
    "Medium": 6,
    "Hard": 4
}

# Choose difficulty level
print("Select Difficulty Level:")
for i, level in enumerate(difficulty_levels.keys(), 1):
    print(f"{i}. {level}")

while True:
    try:
        difficulty_choice = int(input("Choose a difficulty (1-3): ")) - 1
        if difficulty_choice < 0 or difficulty_choice >= len(difficulty_levels):
            raise ValueError
        difficulty = list(difficulty_levels.keys())[difficulty_choice]
        lives = difficulty_levels[difficulty]
        break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")

# Word selection and initialization
chosen_word = random.choice(words_file.word_list)
print(chosen_word)  # For testing purposes, remove this in production
display = ["_" for _ in chosen_word]
used_hints = False  # To track if a hint has been used
game_over = False

print(f"Difficulty Level: {difficulty} | Lives: {lives}")
print(display)

# Game loop
while not game_over:
    guessed_letter = input("Guess a letter or type 'hint' for a hint: ").lower()

    if guessed_letter == "hint":
        if not used_hints:
            hint_letter = next((letter for letter in chosen_word if letter not in display), None)
            if hint_letter:
                print(f"Hint: The word contains the letter '{hint_letter}'")
                used_hints = True  # Limit to one hint per game
            else:
                print("No hints available.")
        else:
            print("You have already used your hint.")
        continue

    # Check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter

    print(display)

    if guessed_letter not in chosen_word:
        lives -= 1
        print(f"Wrong guess. You lost a life. Lives remaining: {lives}")
        if lives == 0:
            game_over = True
            print("You lose!! The word was:", chosen_word)

    if "_" not in display:
        game_over = True
        print("You Win!!")

    print(hangman_stages.stages[lives])
