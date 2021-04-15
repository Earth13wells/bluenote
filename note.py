from tkinter import *
from tkinter import ttk as ttk
#from tkinter import ttk
import PIL
from PIL import Image, ImageDraw

root = Tk()
root.title("DiverseSimplePython")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)


tabControl.add(tab1, text ='tab1')
tabControl.add(tab2, text ='tab2')
tabControl.add(tab3, text ='tab3')
tabControl.add(tab4, text ='tab4')
tabControl.add(tab5, text ='tab5')

tabControl.pack(expand = 1, fill ="both")

#Art
def save():
    global image_number
    filename = f'image_{image_number}.png'   # image_number increments by 1 at every save
    image1.save(filename)
    image_number += 1


def activate_paint(e):
    global lastx, lasty
    cv.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y


def paint(e):
    global lastx, lasty
    x, y = e.x, e.y
    if x > (lastx - 50) and x < (lastx + 50):
        if y > (lasty - 50) and y < (lasty + 50):
            cv.create_line((lastx, lasty, x, y), width=1)
    #  --- PIL
            draw.line((lastx, lasty, x, y), fill='black', width=1)
    lastx, lasty = x, y
lastx, lasty = None, None
image_number = 0

cv = Canvas(root, width=640, height=480, bg='white')

image1 = PIL.Image.new('RGB', (640, 480), 'white')
draw = ImageDraw.Draw(image1)

cv.bind('<1>', activate_paint)
cv.pack(expand=YES, fill=BOTH)

btn_save = Button(text="save", command=save)
btn_save.pack()




# Tab1

# scrollbar = Scrollbar(tab1)
# scrollbar.grid(column=2, row=1, sticky="nsew")
#
# text = Text(tab1, height=5, width=50, yscrollcommand=scrollbar.set)
# text.grid(column=1, row=1)
#
# scrollbar.config(command=text.yview)
#
# ttk.Label(tab1, text = "Notes").grid(column = 1, row = 0, padx = 30, pady = 0)
#
root.mainloop()
