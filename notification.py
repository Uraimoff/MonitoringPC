from pushbullet import Pushbullet
import requests
import time
from datetime import datetime
import os
import random
import tkinter as tk
from tkinter import messagebox
from config import API_KEY


pb = Pushbullet(API_KEY)

# Array of keyword-passcode pairs
keyword_passcode_list = [
    {"keyword": "lemon", "passcode": "melon"},
    {"keyword": "apple", "passcode": "banana"},
    {"keyword": "orange", "passcode": "grape"},
]

# Select a random item from the list
selected_item = random.choice(keyword_passcode_list)

# Function to create the "Success" folder if the passcode is correct and unlock the screen
def check_passcode():
    entered_passcode = passcode_entry.get()
    if entered_passcode == selected_item["passcode"]:
        # Unlock the screen by destroying the window
        root.destroy()
    else:
        messagebox.showerror("Error", "Incorrect passcode. Please try again.")
        passcode_entry.delete(0, tk.END)  # Clear the passcode entry field

# Function to restrict closing the window using the close (X) button
def on_exit_attempt():
    messagebox.showwarning("Restricted", "You cannot close this window without entering the correct passcode.")

# Function to check if the PC is online
def is_online():
    try:
        # Try to access Google to check internet connection
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Check every 10 seconds if the PC is online
while True:
    if is_online():
        # Get the current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Send a notification to your phone
        pb.push_note("PC Status", f"Your PC WIN-SADIKOFF is online! at {current_time}")
        # Exit loop after sending notification
        break
    time.sleep(10)
    
    # Create the main Tkinter window
root = tk.Tk()
root.title("Custom Lock Screen")

# Set the window to fullscreen and remove the title bar
root.attributes("-fullscreen", True)
root.overrideredirect(True)

# Set transparency for the entire window to simulate glassmorphism effect
root.attributes("-alpha", 0.9)

# Override the close button behavior
root.protocol("WM_DELETE_WINDOW", on_exit_attempt)

# Configure the main background to a dark color
root.configure(bg="black")

# Center Frame for glassmorphism effect
center_frame = tk.Frame(root, bg='#ffffff', width=400, height=250)
center_frame.place(relx=0.5, rely=0.5, anchor="center")

# Label for Keyword
keyword_label = tk.Label(center_frame, text=f"Keyword: {selected_item['keyword']}", font=("Arial", 16), fg="black", bg='#ffffff')
keyword_label.pack(pady=10)

# Passcode Entry
passcode_entry = tk.Entry(center_frame, show="*", font=("Arial", 14), justify='center')
passcode_entry.pack(pady=10)

# Submit Button
submit_button = tk.Button(center_frame, text="Submit", command=check_passcode, font=("Arial", 14), fg="white", bg="#333", bd=0)
submit_button.pack(pady=10)

# Centering the frame contents and setting padding
center_frame.pack_propagate(False)
center_frame.configure(bg='#ffffff', borderwidth=0, relief="solid")

# Styling the Entry and Button
passcode_entry.config(bg='#ffffff', borderwidth=2, relief="solid")
submit_button.config(width=15, height=1, borderwidth=0, relief="solid", cursor="hand2")

# Run the Tkinter event loop
root.mainloop()
