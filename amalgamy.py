from tkinter import *
from tkinter import messagebox as mbox
from tkinter import filedialog

from markdown2 import Markdown
from tkinterhtml import HtmlFrame
import PIL
from PIL import Image, ImageDraw, ImageTk
#
#Functions
#

def get_text(a):
    content = text_f1.get(1.0, "end-1c")
    entry_content.set(markdowner.convert(content))
    content = markdowner.convert(content)
    print(f'<html><body style=\"background-color:grey;\">{content}</html>')
    f3.set_content(f"<html><body style=\"background-color:grey;\">{content}</html>")

#
def save(): #From sketch.py
    try:
        image1.save(filename)
    except:
        global image_number
        filenames = f'image_{image_number}.png'   # image_number increments by 1 at every save
        image1.save(filenames)
        image_number += 1
#
def activate_paint(e): #From sketch.py
    global lastx, lasty
    f2.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y
#
def paint(e): #From sketch.py
    global lastx, lasty
    x, y = e.x, e.y
    if x > (lastx - 25) and x < (lastx + 25):
        if y > (lasty - 25) and y < (lasty + 25):
            f2.create_line((lastx, lasty, x, y), width=1)
            #  --- PIL
            draw.line((lastx, lasty, x, y), fill='black', width=1)
    lastx, lasty = x, y

def browseFiles():
    global filename
    filename = filedialog.askopenfilename(
        initialdir = "~/bluenote",
        title = "Select a File",
        filetypes = (("imageFiles", "*.png*"),
                    ("allFiles", "*.*"))
        )
    global im
    im = PhotoImage(file = f"{filename}")
    f2.itemconfig(image_id, image=im)

#
#Making layout
#
root = Tk() #all


try:
    bg = im = PhotoImage(file = f"image_0.png")
except:
    bg = im = PIL.Image.new('RGB', (500, 480),'grey')
    im.save("image_0.png")
    bg = im = PhotoImage(file = "image_0.png")

pw1 = PanedWindow(width=880, height=500)
pw1.pack(fill="both", expand=True)
#
f1 = Frame(pw1, width=500, height=500) # Make frame for text
pw1.add(f1)
#
pw2 = PanedWindow(pw1, orient=VERTICAL, height=500)
pw1.add(pw2)
#
f2 = Canvas(pw2, width=100, height=500, background="grey") # make canvas for drawing
f2.pack(side='top', expand='yes')
image_id = f2.create_image( 0, 0, image = im, anchor = "nw")
pw2.add(f2)
#
f3 = HtmlFrame(root, horizontal_scrollbar="auto", height=100, width=100)
#f3.pack(side='top', fill='x', expand='no')
pw2.add(f3)
#
#Making text box on left side panel
#
text_f1 = Text(f1, height=50, width=50, wrap="none", background="grey")
#
#Setup
#
markdowner = Markdown()
lastx, lasty = None, None
image_number = 0
try:
    image1 = PIL.Image.open("image_0.png")
except:
    image1 = PIL.Image.new('RGB', (500, 480), 'grey')

draw = ImageDraw.Draw(image1)
#
f1.grid_rowconfigure(0, weight=1)
f1.grid_columnconfigure(0, weight=1)
f3.grid_rowconfigure(0, weight=1)
f3.grid_columnconfigure(0, weight=1)
text_f1.grid(row=0, column=0, sticky="nsew")
#
#Image bindings/Save button
#
btn_save = Button(f2, text="save", command=save)
btn_save.pack(side="top")
btn_file = Button(f2, text="browseFiles", command=browseFiles)
btn_file.pack(side="top")
f2.bind('<1>', activate_paint)
#
#Bind click of markdown to html converter
#
entry_content = StringVar()
text_f1.bind('<1>', get_text)
get_text(1)
#
#Start
#
root.mainloop() # All
