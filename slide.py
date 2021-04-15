from tkinter import *

root = Tk()

pw = PanedWindow()
pw.pack(fill="both", expand=True)

f1 = Frame(width=200, height=200, background="bisque")
f2 = Frame(width=200, height=200, background="pink")

pw.add(f1)
pw.add(f2)

# adding some widgets to the left...
text = Text(f1, height=20, width=20, wrap="none")
#ysb = Scrollbar(f1, orient="vertical", command=text.yview)
#xsb = Scrollbar(f1, orient="horizontal", command=text.xview)
#text.configure(yscrollcommand=ysb.set, xscrollcommand=xsb.set)

f1.grid_rowconfigure(0, weight=1)
f1.grid_columnconfigure(0, weight=1)

#xsb.grid(row=1, column=0, sticky="ew")
#ysb.grid(row=0, column=1, sticky="ns")
text.grid(row=0, column=0, sticky="nsew")

# and to the right...
#b1 = Button(f2, text="Click me!")
#s1 = Scale(f2, from_=1, to=20, orient="horizontal")

#b1.pack(side="top", fill="x")
#s1.pack(side="top", fill="x")

root.mainloop()
