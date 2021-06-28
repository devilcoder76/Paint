from tkinter import *

window=Tk()
def text():
    if i:
        inp=i.get()
        print(inp)

canvas=Canvas(window,bg="white",cursor="")

i=Entry(window,width=10)
button=Button(window,text="set",command=text)
i.grid(row=0,column=0)
button.grid(row=0,column=12)
canvas.grid(row=0,column=0,sticky="nsew")
window.mainloop()

self.inputbox=Entry(self.MainWindow,width=5)
self.inputbutton=Button(self.MainWindow,text="Set width",command=self.change_width)
self.inputbox.grid(row=270,column=20)
self.inputbutton.grid(row=270,column=27)
        