from tkinter import *

class window:
    def __init__(self):
        
        #Setting x and y variables for mouse position
        self.x,self.y,self.rid,self.lid,self.oid=0,0,None,None,None
        #Setting count 
        self.extra=0
        self.width=5
        #setting mainwindow
        
        self.color="black"
        self.MainWindow=Tk()
        self.MainWindow.title("Css Designer")
        self.MainWindow.state("zoomed")
        self.MainWindow.rowconfigure(0,weight=1)
        self.MainWindow.columnconfigure(0,weight=1)
        
        #Setting canvas to draw on
        self.inputbox=Entry(self.MainWindow,width=5)
        self.inputbutton=Button(self.MainWindow,text="Set width",command=self.change_width)
        
        self.Canvas=Canvas(self.MainWindow,bg="#FFFFFF")
        self.Canvas.grid(row=0,column=0,sticky='nsew',)
        self.inputbox.grid(row=0,column=20)
        self.inputbutton.grid(row=0,column=27)
        id=self.Canvas.create_rectangle(20,50,45,70,fill="black")
        self.Canvas.tag_bind(id,'<Button-1>',lambda x:self.change_color("black"))
        id=self.Canvas.create_rectangle(50,50,75,70,fill="orange")
        self.Canvas.tag_bind(id,'<Button-1>',lambda x:self.change_color("orange"))
        id=self.Canvas.create_rectangle(80,50,105,70,fill="green")
        self.Canvas.tag_bind(id,'<Button-1>',lambda x:self.change_color("green"))
        id=self.Canvas.create_rectangle(110,50,135,70,fill="blue")
        self.Canvas.tag_bind(id,'<Button-1>',lambda x:self.change_color("blue"))
        id=self.Canvas.create_rectangle(140,50,165,70,fill="red")
        self.Canvas.tag_bind(id,'<Button-1>',lambda x:self.change_color("red"))
        id=self.Canvas.create_rectangle(20,80,60,120,fill="")
        self.Canvas.tag_bind(id,'<Button-1>',self.rect_bind)
        id=self.Canvas.create_line(20,170,80,170)
        self.Canvas.tag_bind(id,'<Button-1>',self.freeline_bind)
        id=self.Canvas.create_line(20,190,80,190)
        self.Canvas.tag_bind(id,'<Button-1>',self.line_bind)
        id=self.Canvas.create_oval(20,210,80,240)
        self.Canvas.tag_bind(id,"<Button-1>",self.oval_bind)
        id=self.Canvas.create_rectangle(20,240,40,260)
        self.Canvas.tag_bind(id,"<Button-1>",self.eraser_bind)
        self.Canvas.bind("<Button-1>",self.put_mouse)
        print("Window start:")
        
        #setting window loop
        self.MainWindow.mainloop()
    
    def pointer(self,shape):
        self.MainWindow.config(cursor=shape)
        
    def rect_bind(self,event):#key binding to rectangle
        print("Rectange bind:")
        self.pointer("arrow")
        self.Canvas.bind("<B1-Motion>",self.drawrectangle)
    
    def freeline_bind(self,event):#key binding to free line
        self.pointer("arrow")    
        print("freeLine bind:")
        self.Canvas.bind("<B1-Motion>",self.drawfreeline)
    
    def oval_bind(self,event):
        self.pointer("arrow")
        print("Oval Bind:")
        self.Canvas.bind("<B1-Motion>",self.drawoval)
        
    def line_bind(self,event):
        print("Line bind:")
        self.Canvas.bind("<B1-Motion>",self.drawline)
    
    def eraser_bind(self,event):
        print("Eraser bind:")
        self.pointer("circle")
        self.Canvas.bind("<B1-Motion>",self.eraser)
        
    def change_color(self,color):#to set the color of the current pointer
        print("Color changed:")
        self.color=color
    def change_width(self):
        width=int(self.inputbox.get())
        if (width>0):
            self.width=width
        
    def put_mouse(self,event):#to set values of x and y to current x and y
            print("Clicked")
            self.x,self.y,self.rid,self.lid,self.oid=event.x,event.y,None,None,None
    def eraser(self,event):
        self.Canvas.create_line(self.x,self.y,event.x,event.y,fill="#FFFFFF",width=self.width)
        self.x,self.y=event.x,event.y
    
    def drawfreeline(self,event):
        self.Canvas.create_line(self.x,self.y,event.x,event.y,fill=self.color,width=self.width)
        self.x,self.y=event.x,event.y
    
    def drawline(self,event):
        try:
            self.Canvas.delete(self.lid)
        except Exception:
            return
        finally: 
            self.lid=self.Canvas.create_line(self.x,self.y,event.x,event.y,fill=self.color,width=self.width)
    
    def drawoval(self,event):
        try:
            self.Canvas.delete(self.oid)
        except Exception:
            return
        finally:
            self.oid=self.Canvas.create_oval(self.x,self.y,event.x,event.y,outline=self.color,width=self.width)

    def drawrectangle(self,event):
        print("Move")
        try:
            self.Canvas.delete(self.rid)
        except Exception:
            print("Omago")
            return
        finally:
            print(self.color)
            self.rid=self.Canvas.create_rectangle(self.x,self.y,event.x,event.y,outline=self.color,width=self.width)
        
                     
app=window()     
