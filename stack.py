from tkinter import *

pw = PanedWindow()
pw.pack(fill=BOTH, expand=1)

left = Label(pw, text="left pane", background="grey")
pw.add(left)

m2 = PanedWindow(pw, orient=VERTICAL)
pw.add(m2)

top = Label(m2, text="top pane", background="green")
m2.add(top)

bottom = Label(m2, text="bottom pane", background="blue")
m2.add(bottom)

mainloop()
