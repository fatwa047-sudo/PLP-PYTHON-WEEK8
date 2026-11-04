# toolkit.py - My Python Toolkit
import random

tasks = []  # shared list, so tasks stay saved while the program runs

# Tool 1: To-do list. Lets you add, view and remove tasks (a list that changes).
def todo_list():
    while True:
        print(f"\nTo-do list ({len(tasks)} tasks)")
        action = input("a) add  v) view  r) remove  b) back: ").lower()
        if action == "a":
            task = input("New task: ")
            tasks.append(task)
            print(f"Added '{task}'!")
        elif action == "v":
            if len(tasks) == 0:
                print("No tasks yet.")
            else:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
        elif action == "r":
            num = input("Task number to remove: ")
            if num.isdigit() and 1 <= int(num) <= len(tasks):
                removed = tasks.pop(int(num) - 1)
                print(f"Removed '{removed}'.")
            else:
                print("That task number doesn't exist.")
        elif action == "b":
            break
        else:
            print("Please choose a, v, r or b.")

# Tool 2: Guessing game. Loops until you find the secret number (1-10).
def guessing_game():
    secret = random.randint(1, 10)
    attempts = 0
    print("I'm thinking of a number between 1 and 10.")
    while True:
        guess = input("Your guess: ")
        if not guess.isdigit():
            print("Please type a whole number.")
            continue
        guess = int(guess)
        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} tries.")
            break

# Tool 3: Grade checker. Uses conditionals to turn a score into a grade.
def grade_checker():
    score = input("Enter your score (0-100): ")
    if not score.isdigit() or int(score) > 100:
        print("Please enter a number from 0 to 100.")
    else:
        score = int(score)
        if score >= 80:
            grade = "A"
        elif score >= 70:
            grade = "B"
        elif score >= 60:
            grade = "C"
        else:
            grade = "D"
        print(f"With {score}, your grade is {grade}.")

# Main menu loop: runs until the user chooses Quit
print("Welcome to My Python Toolkit!")
while True:
    print("\n=== My Toolkit ===")
    print("1. To-do list")
    print("2. Guessing game")
    print("3. Grade checker")
    print("4. Quit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        todo_list()
    elif choice == "2":
        guessing_game()
    elif choice == "3":
        grade_checker()
    elif choice == "4":
        print("Goodbye! Thanks for using the toolkit.")
        break
    else:
        print("Oops! That's not on the menu. Please pick 1, 2, 3 or 4.")
        
