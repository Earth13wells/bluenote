import tkinter

def get_text():
    content = body.get(1.0, "end-1c")
    entry_content.set(content)

master = tkinter.Tk()

body = tkinter.Text(master)
body.pack()

entry_content = tkinter.StringVar()
entry = tkinter.Entry(master, textvariable=entry_content)
entry.pack()

button = tkinter.Button(master, text="Get tkinter.Text content", command=get_text)
button.pack()

master.mainloop()
