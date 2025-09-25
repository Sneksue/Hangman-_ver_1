import random
from hangman_assist import word_list, stages
chosen_word = random.choice(word_list)
chance = 6
guessed_letter = []

print(chosen_word)

while chance > 0:
    placeholder = ""
    for letter in chosen_word:
        if letter in guessed_letter:
            placeholder += letter
        else:
            placeholder += "_"

    print(stages[chance])
    print(placeholder)
    print(f"\n{guessed_letter}")
    print(f"You have {chance} left.")

    guess = str(input("Please enter a letter:\n")).lower()
    guessed_letter.append(guess)

    display = ""

    for letter in chosen_word:
        if letter in guessed_letter:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        chance -= 1
        print("Please try again:\n")

    if "_" not in display:
        print("\nYou win!")
        break

    if chance == 0:
        print(stages[0])
        print("\nYou Lose!")
        print(f"The word is {chosen_word}")
        break
    