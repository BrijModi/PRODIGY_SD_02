# Importing important libraries
import tkinter as tk
from tkinter import messagebox
import random

# Creating a variable to count attempt and game starts with 1st attempt 
Attempt = 1

# Font used
FONT = ("Courier", 13, "normal")

# Generating a random number between 1 and 200
Random_Number = int(random.randint(1,200))

# Game Working
def Guess_Number():
    global Attempt
    User_Guess = int(E1.get())

    if User_Guess == Random_Number:
        messagebox.showinfo("Game", f"You Win! \nYou took {Attempt} attempts to win.")

    elif User_Guess > Random_Number:
        Attempt += 1
        messagebox.showinfo("Oops", "Too High.")

    elif User_Guess < Random_Number:
        Attempt += 1
        messagebox.showinfo("Oops", "Too Low.")

    else:
        messagebox.showinfo("Error", "Enter a valid number.")

# Window
root = tk.Tk()
root.geometry('400x200')
root.resizable(False, False)
root.title('Number Guessing Game')

# Label
L1 = tk.Label(root, text='Guess the Number :\n(1 - 200)', font=FONT)
L1.place(x=30, y=50)

# Entry Box
E1 = tk.Entry(root)
E1.place(x=230, y=53)

# Button
B1 = tk.Button(root, text='Guess', font=FONT, command=Guess_Number)
B1.place(x=175, y=140)

# Run
root.mainloop()
