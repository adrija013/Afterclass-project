import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    result = ""

    if user_choice == computer_choice:
        result = f"Tie! Both chose {user_choice}"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = f"You win! {user_choice} beats {computer_choice}"
    else:
        result = f"You lose! {computer_choice} beats {user_choice}"

    result_label.config(text=result)

def play_game():
    for btn in buttons: 
        btn.config(command=lambda choice=btn.cget("text"): determine_winner(choice))

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
instruction_label.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

buttons = []
choices = ["Rock", "Paper", "Scissors"]
for choice in choices:
    btn = tk.Button(root, text=choice, width=15, height=2)
    btn.pack(pady=5)
    buttons.append(btn)

play_game()


root.mainloop()