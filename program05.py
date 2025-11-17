import random

num = random.randint(1, 100)
chance = 7

print("🎉 Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 100.")
print("You have 7 chances. Good luck!\n")

while chance > 0:
    print(f"Chances left: {chance}")
    user_input = int(input("Enter your guess: "))

    # Validate input
    if user_input < 1 or user_input > 100:
        print("⚠️ Please enter a number between 1 and 100.\n")
        continue  # Do NOT reduce chances

    chance -= 1  # Reduce chance only for valid inputs

    if user_input == num:
        print(f"\n🎉 Correct! The number was {num}.")
        print(f"🏆 You won in {7 - chance} attempts!")
        break

    elif user_input > num:
        print("📉 Wrong guess! Try a lower number.\n")

    elif user_input < num:
        print("📈 Wrong guess! Try a higher number.\n")

if chance == 0:
    print("\n❌ You lose!")
    print(f"The correct number was: {num}")
