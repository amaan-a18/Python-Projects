import tkinter as tk
from time import strftime
from datetime import datetime

is_24hr = True
current_color = "#00ffff"

themes = {
    "Cyan": "#00ffff",
    "Lime": "#39ff14",
    "Red": "#ff0055",
    "Purple": "#bf00ff",
    "Yellow": "#ffff00"
}

root = tk.Tk()
root.title("Digital Clock")
root.geometry("600x300")
root.configure(bg="#0f0f0f")


clock_label = tk.Label(root, font=("Orbitron", 50), bg="#0f0f0f", fg=current_color)
clock_label.pack(pady=20)

date_label = tk.Label(root, font=("Orbitron", 20), bg="#0f0f0f", fg=current_color)
date_label.pack()

def update_time():
    now = datetime.now()
    time_format = "%H:%M:%S" if is_24hr else "%I:%M:%S %p"
    time_str = now.strftime(time_format)
    date_str = now.strftime("%A, %d %B %Y")
    clock_label.config(text=time_str)
    date_label.config(text=date_str)
    root.after(1000, update_time)

def toggle_format():
    global is_24hr
    is_24hr = not is_24hr

def change_color(color):
    global current_color
    current_color = color
    clock_label.config(fg=current_color)
    date_label.config(fg=current_color)

button_frame = tk.Frame(root, bg="#0f0f0f")
button_frame.pack(pady=10)

for theme_name, color in themes.items():
    btn = tk.Button(button_frame, text=theme_name, command=lambda c=color: change_color(c),
                    bg="#1a1a1a", fg=color, font=("Arial", 10), width=8)
    btn.pack(side="left", padx=5)


toggle_btn = tk.Button(root, text="Toggle 12/24 Hr", command=toggle_format,
                       bg="#1a1a1a", fg="#ffffff", font=("Arial", 10))
toggle_btn.pack(pady=10)


update_time()
root.mainloop()
