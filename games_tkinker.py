import tkinter as tk
from tkinter import messagebox
import random

# Main window
root = tk.Tk()
root.title("Kids Game Hub")
root.geometry("400x400")

# ---------------------------- Number Guessing ----------------------------
def play_number_guessing():
    def check_guess():
        try:
            guess = int(entry.get())
            if guess == number:
                messagebox.showinfo("Result", "Correct! 🎉")
            else:
                messagebox.showinfo("Result", f"Wrong! It was {number}")
        except:
            messagebox.showwarning("Invalid", "Please enter a valid number")

    number = random.randint(1, 10)
    window = tk.Toplevel(root)
    window.title("Number Guessing")

    tk.Label(window, text="Guess a number between 1 and 10").pack(pady=10)
    entry = tk.Entry(window)
    entry.pack()
    tk.Button(window, text="Check", command=check_guess).pack(pady=10)

# ---------------------------- Rock Paper Scissors ----------------------------
def play_rps():
    def play(player):
        computer = random.choice(['rock', 'paper', 'scissors'])
        result = f"Computer chose {computer}."

        if player == computer:
            result += " It's a tie!"
        elif (player == 'rock' and computer == 'scissors') or \
             (player == 'scissors' and computer == 'paper') or \
             (player == 'paper' and computer == 'rock'):
            result += " You win!"
        else:
            result += " Computer wins!"

        messagebox.showinfo("Result", result)

    window = tk.Toplevel(root)
    window.title("Rock Paper Scissors")
    window.configure(bg="#dff0f5")

    tk.Label(window, text="Choose Rock, Paper, or Scissors").pack(pady=10)
    tk.Button(window, text="Rock", command=lambda: play('rock')).pack(pady=5)
    tk.Button(window, text="Paper", command=lambda: play('paper')).pack(pady=5)
    tk.Button(window, text="Scissors", command=lambda: play('scissors')).pack(pady=5)

# ---------------------------- Math Quiz ----------------------------
def play_math_quiz():
    def check_answer():
        try:
            ans = int(entry.get())
            if ans == a + b:
                messagebox.showinfo("Correct", "✅ Correct!")
            else:
                messagebox.showinfo("Wrong", f"❌ Wrong! The answer was {a + b}")
        except:
            messagebox.showwarning("Invalid", "Please enter a number")
        window.destroy()

    a = random.randint(1, 10)
    b = random.randint(1, 10)

    window = tk.Toplevel(root)
    window.title("Math Quiz")

    tk.Label(window, text=f"What is {a} + {b}?").pack(pady=10)
    entry = tk.Entry(window)
    entry.pack()
    tk.Button(window, text="Check", command=check_answer).pack(pady=10)

# ---------------------------- Word Scramble ----------------------------
def play_scramble():
    def check_word():
       
        if entry.get().lower() == word:
            messagebox.showinfo("Correct", "🎉 Correct!")
            
        else:
            messagebox.showinfo("Wrong", f"❌ Wrong! It was {word}")
        window.destroy()

    
    word_list = ['apple', 'grape', 'banana', 'chikoo','lichie']
    word = random.choice(word_list)
    scrambled = ''.join(random.sample(word, len(word))) #used to scramble (shuffle) the letters of a word
    '''  ''.join(...) takes the list of characters returned by random.sample() and joins them back into a single string'''
    
    print("randomly chosen word from the list is:", word)
    print("word after scrambling is:",scrambled)
   
    window = tk.Toplevel(root)
    window.title("Word Scramble")
    window.geometry("200x200")

    tk.Label(window, text=f"Unscramble: {scrambled}").pack(pady=10)
    entry = tk.Entry(window)
    entry.pack()
    tk.Button(window, text="Submit", command=check_word).pack(pady=10)
   
# ---------------------------- Buttons ----------------------------
tk.Label(root, text="🎮 Welcome to Kids Game Hub", font=("Arial", 16)).pack(pady=20)
tk.Button(root, text="Number Guessing", width=20, command=play_number_guessing).pack(pady=5)
tk.Button(root, text="Rock Paper Scissors", width=20, command=play_rps).pack(pady=5)
tk.Button(root, text="Math Quiz", width=20, command=play_math_quiz).pack(pady=5)
tk.Button(root, text="Word Scramble", width=20, command=play_scramble).pack(pady=5)
tk.Button(root, text="Exit", width=20, command=root.destroy).pack(pady=20)

# Run the GUI loop
root.mainloop()
