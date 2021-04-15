from tkinter import *
from tkinter import messagebox as mbox
from tkinter import filedialog
import markdown
from tkinterhtml import HtmlFrame
import PIL
from PIL import Image, ImageDraw, ImageTk
#
#Functions
#
def get_text(a): # get text from amrkdown, and convert to html, and set html content
    content = text_f1.get(1.0, "end-1c")
    entry_content.set(markdown.markdown(content))
    content = markdown.markdown(content)
    #print(f'<html><body style=\"background-color:grey;\">{content}</html>')
    f3.set_content(f"<html><body style=\"background-color:grey;\">{content}</html>")
#
def save(): #Save Image as filename
    global filename
    if filename_entered.get() != "":
        filename = filename_entered.get()
    image1.save(filename)
#
def save_file(): #Save Image as filename
    global mdfile
    if mdfile_entered.get() != "":
        mdfile = mdfile_entered.get()
    content = text_f1.get(1.0, "end-1c")
    try:
        with open(mdfile,'r+') as myfile:
            myfile.seek(0)
            myfile.write(content)
            myfile.truncate()
    except FileNotFoundError:
        with open(mdfile, 'w') as f:
            f.write(content)
#
def save_html():
    global mdfile
    if mdfile_entered.get() != "":
        mdfile = f"{mdfile_entered.get()}.html"
    content = text_f1.get(1.0, "end-1c")
    #entry_content.set(markdown.markdown(content ) )
    content = markdown.markdown(content )
    try:
        with open(mdfile,'r+') as myfile:
            myfile.seek(0)
            myfile.write(f'<html><body style=\"background-color:grey;\">{content}</html>')
            myfile.truncate()
    except FileNotFoundError:
        with open(mdfile, 'w') as f:
            f.write(f'<html><body style=\"background-color:grey;\">{content}</html>')
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
#
def browseImages(): #Open file browser, so user can chose image file
    global filename
    filename = filedialog.askopenfilename(
        initialdir = "~/bluenote",
        title = "Select a File",
        filetypes = (("imageFiles", f"*.png*"),
                    ("allFiles", "*.*"))
        )
    global im
    im = PhotoImage(file = f"{filename}")
    f2.itemconfig(image_id, image=im)
    filename_entered.set(filename)
#
def browseFiles(): #Open file browser, so user can chose md file
    global mdfile
    mdfile = filedialog.askopenfilename(
        initialdir = "~/bluenote",
        title = "Select a File",
        filetypes = (("markDownFiles", f"*.md*"),
                    ("allFiles", "*.*"))
        )
    text_f1.delete("1.0","end")
    with open(mdfile) as f: s = f.read()
    text_f1.insert(END, s)
    mdfile_entered.set(mdfile)
#
def cancelFiles():
    global mdfile
    text_f1.delete("1.0","end")
    with open(mdfile) as f: s = f.read()
    text_f1.insert(END, s)
#
def insert():
    #text_f1.insert(INSERT, f'\n![{filename}]({filename} \"{filename}\")\n')
    #<img src="myImage.png">
    text_f1.insert(INSERT, f'\n#{filename}\n<img src="{filename}">\n')

#
# THIS WORKS HERE, NO TOUCHY
#
root = Tk() #all

try:
    im = PhotoImage(file = f"image_0.png")
except:
    im = PIL.Image.new('RGB', (500, 480),'grey')
    im.save("image_0.png")
    im = PhotoImage(file = "image_0.png")
filename = "image_0.png"
#
mdfile = ""
#
#Making layout
#
pw1 = PanedWindow(width=1000, height=1000)
pw1.pack(fill="both", expand=True)
#
#add Markdown Frame to PanedWindow 1
#
f1 = Canvas(pw1, width=500, height=500) # Make frame for MD
text_f1 = Text(f1, height=50, width=50, wrap="none", background="grey")
text_f1.pack(expand=True, fill="both")
pw1.add(f1)
#
#Second paned window to hold html and images
#
pw2 = PanedWindow(pw1, orient=VERTICAL, height=500)
pw1.add(pw2)
#
#Add image editor to PanedWindow 2
#
f2 = Canvas(pw2, width=100, height=500, background="light grey") # make canvas for drawing
f2.pack(side='top', expand='yes')
image_id = f2.create_image( 0, 0, image = im, anchor = "nw")
pw2.add(f2)
#
#add html window to PanedWindow 2
#
f3 = HtmlFrame(root, horizontal_scrollbar="auto", height=100, width=100)
#f3.pack(side='top', fill='x', expand='no')
pw2.add(f3)
#
#Setup
#
lastx, lasty = None, None
try:
    image1 = PIL.Image.open("image_0.png")
except:
    image1 = PIL.Image.new('RGB', (500, 480), 'grey')
global draw
draw = ImageDraw.Draw(image1)
#
#f1.grid_rowconfigure(0, weight=1)
#f1.grid_columnconfigure(0, weight=1)
f3.grid_rowconfigure(0, weight=1)
f3.grid_columnconfigure(0, weight=1)
#
#Buttons and text boxes
#
frame_f1 = Frame(f1)
frame_f1.pack()
#
btn_file = Button(f1, text="browseFiles", command=browseFiles)
btn_file.pack(side="left")
#
btn_cancel_file = Button(f1, text="cancel", command=cancelFiles)
btn_cancel_file.pack(side="left")
#
btn_save_file = Button(f1, text="save", command=save_file)
btn_save_file.pack(side="left")
#
btn_save_html = Button(f1, text="saveHTML", command=save_html)
btn_save_html.pack(side="right")
#
mdfile_entered = StringVar()
mdfile_entered.set(mdfile)
md_filename = Entry(frame_f1, width = 45, textvariable = mdfile_entered)
md_filename.pack(side="bottom")
#
frame_f2 = Frame(f2)
frame_f2.pack()
#
btn_insert = Button(frame_f2, text="insert", command=insert)
btn_insert.pack(side="left")
#
btn_save_img = Button(frame_f2, text="save", command=save)
btn_save_img.pack(side="left")
#
btn_img = Button(frame_f2, text="browseFiles", command=browseImages)
btn_img.pack(side="left")
f2.bind('<B1-Motion>', activate_paint)
#
filename_entered = StringVar()
filename_entered.set(filename)
txt_filename = Entry(frame_f2, width = 45, textvariable = filename_entered)
txt_filename.pack(side="left")
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
