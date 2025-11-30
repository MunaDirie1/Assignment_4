import gameData

print("Welcome to Word Guess!")
print("Guess the 5-letter word.")
print(f"You have {gameData.max_turns} turns.\n")

while gameData.turn_counter < gameData.max_turns:
    guess = input("Enter your guess: ")

    if len(guess) != 5:
        print("Guess must be 5 letters.\n")
        continue

    if not guess.isalpha():
        print("Guess must only contain letters.\n")
        continue

    if gameData.entries(guess):
        print("\nCongratulations! You guessed the word!")
        print("The word was:", gameData.word)
        break

    gameData.turn_counter += 1

    print("\nIncorrect guess.")
    print("Progress:", gameData.display_progress())
    print("Right letters:", gameData.right_letters)
    print("Wrong position letters:", gameData.wrong_pos)
    print("Wrong letters:", gameData.wrong_letters)
    print(f"Turns remaining: {gameData.max_turns - gameData.turn_counter}\n")

# Game over
if gameData.turn_counter >= gameData.max_turns:
    print("\nGame over! The word was:", gameData.word)
    gameData.turn_counter = 0
