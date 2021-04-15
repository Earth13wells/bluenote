from tkinterhtml import HtmlFrame

import tkinter as tk

root = tk.Tk()

frame = HtmlFrame(root, horizontal_scrollbar="auto")
 
frame.set_content("<html></html>")
root.mainloop()
