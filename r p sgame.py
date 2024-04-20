import tkinter as tk
import random

def get_user_choice():
    user_choice = user_input.get().lower()
    user_input.delete(0, tk.END)
    if user_choice not in ['rock', 'paper', 'scissors']:
        label_result.config(text="Invalid choice. Please choose rock, paper, or scissors.")
    else:
        play(user_choice)

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    label_result.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    update_score(result)

def update_score(result):
    global user_score, computer_score
    if 'win' in result:
        user_score += 1
    elif 'lose' in result:
        computer_score += 1
    label_score.config(text=f"Your score: {user_score}\nComputer's score: {computer_score}")

# Create main window
window = tk.Tk()
window.title("Rock Paper Scissors")

# Create user input field
user_input = tk.Entry(window, width=20)
user_input.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

# Create buttons
button_submit = tk.Button(window, text="Submit", width=10, command=get_user_choice)
button_submit.grid(row=0, column=2, padx=5, pady=10)
button_quit = tk.Button(window, text="Quit", width=10, command=window.quit)
button_quit.grid(row=0, column=3, padx=5, pady=10)

# Create result label
label_result = tk.Label(window, text="", font=("Helvetica", 12))
label_result.grid(row=1, column=0, columnspan=4)

# Create score label
user_score = 0
computer_score = 0
label_score = tk.Label(window, text=f"Your score: {user_score}\nComputer's score: {computer_score}", font=("Helvetica", 12))
label_score.grid(row=2, column=0, columnspan=4)

window.mainloop()
