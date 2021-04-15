import tkinter as tk

# --- functions ---

def on_click():
    global current_image_number
    current_image_number += 1
    if current_image_number == len(images):
        current_image_number = 0
    canvas.itemconfig(image_id, image=images[current_image_number])

# --- main ---

root = tk.Tk()

# canvas for image
canvas = tk.Canvas(root, width=60, height=60)
canvas.pack()

# button to change image
button = tk.Button(root, text="Change", command=on_click)
button.pack()

# images
images = [
    tk.PhotoImage(file="image_0.png"),
    tk.PhotoImage(file="image_0.png"),
    tk.PhotoImage(file="image_1.png"),
]
current_image_number = 0

# set first image on canvas
image_id = canvas.create_image(0, 0, anchor='nw', image=images[current_image_number])

root.mainloop()
