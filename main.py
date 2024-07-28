from tkinter import *
import random

colors = ["blue", "purple", "red", "green", "orange", "grey"]

def choose_color():
    global chosen_color
    chosen_color = random.choice(colors)
    print(f"Color to guess: {chosen_color}")

def check_color(selected_color):
    if selected_color == chosen_color:
        result_label.config(text="You Won!", fg="green")
    else:
        result_label.config(text="Wrong! Try Again.", fg="red")

root = Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Guess the Color")
root.config(bg="skyblue")

heading = Label(root, text="Guess The Color!", bg="skyblue", font="Roboto 15")
heading.place(x=230, y=20)

result_label = Label(root, text="", bg="skyblue", font="Roboto 12")
result_label.place(x=230, y=70)

button_properties = {
    "blue": {"bg": "blue", "fg": "white", "x": 50, "y": 150},
    "purple": {"bg": "purple", "fg": "white", "x": 250, "y": 150},
    "red": {"bg": "red", "fg": "white", "x": 450, "y": 150},
    "green": {"bg": "green", "fg": "white", "x": 50, "y": 250},
    "orange": {"bg": "orange", "fg": "white", "x": 250, "y": 250},
    "grey": {"bg": "grey", "fg": "white", "x": 450, "y": 250}
}

for color_name, props in button_properties.items():
    Button(
        root,
        text=color_name.capitalize(),
        bg=props["bg"],
        fg=props["fg"],
        width=8,
        height=2,
        font="Roboto 12",
        command=lambda color=color_name: check_color(color)
    ).place(x=props["x"], y=props["y"])

choose_color()

root.mainloop()
