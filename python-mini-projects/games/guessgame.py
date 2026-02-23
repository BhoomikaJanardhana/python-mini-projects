import random

best_score = None

while True:
    number = random.randint(1, 100)
    attempts = 7
    used = 0

    print("\nGuess the number (1-100)")

    while attempts > 0:
        guess = int(input("Enter guess: "))
        used += 1
        attempts -= 1

        if guess == number:
            print("Correct! You used", used, "attempts")
            if best_score is None or used < best_score:
                best_score = used
            break

        elif guess > number:
            print("Too High!")

        else:
            print("Too Low!")

        print("Attempts left:", attempts)

        if abs(guess - number) <= 5:
            print("Hint: Very Close!")

    else:
        print("You lost! Number was:", number)

    print("Best score:", best_score)

    again = input("Play again? (yes/no): ")
    if again.lower() != "yes":
        break