#Create bricks
#Create moving platform and ball
#Make ball bounce off of other surfaces
#Make bricks disappear when hit
#Make a continuous score display
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=600,height=600, background='white')
player = drawpad.create_rectangle(260,590,340,595, fill = "blue")
ball = drawpad.create_oval(293,576,307,590, fill = "white")
brick1 = drawpad.create_rectangle(30,20,80,50, fill='green')
brick2 = drawpad.create_rectangle(30,100,80,130, fill='green')
brick3 = drawpad.create_rectangle(30,180,80,210, fill='green')
brick4 = drawpad.create_rectangle(100,20,150,50, fill='green')
brick5 = drawpad.create_rectangle(100,100,150,130, fill='green')
brick6 = drawpad.create_rectangle(100,180,150,210, fill='green')
brick7 = drawpad.create_rectangle(170,20,220,50, fill='green')
brick8 = drawpad.create_rectangle(170,100,220,130, fill='green')
brick9 = drawpad.create_rectangle(170,180,220,210, fill='green')
brick10= drawpad.create_rectangle(240,20,290,50, fill='green')
brick11= drawpad.create_rectangle(240,100,290,130, fill='green')
brick12= drawpad.create_rectangle(240,180,290,210, fill='green')
brick13= drawpad.create_rectangle(310,20,360,50, fill='green')
brick14= drawpad.create_rectangle(310,100,360,130, fill='green')
brick15= drawpad.create_rectangle(310,180,360,210, fill='green')
brick16= drawpad.create_rectangle(380,20,430,50, fill='green')
brick17= drawpad.create_rectangle(380,100,430,130, fill='green')
brick18= drawpad.create_rectangle(380,180,430,210, fill='green')
brick19= drawpad.create_rectangle(450,20,500,50, fill='green')
brick20= drawpad.create_rectangle(450,100,500,130, fill='green')
brick21= drawpad.create_rectangle(450,180,500,210, fill='green')
brick22= drawpad.create_rectangle(520,20,570,50, fill='green')
brick23= drawpad.create_rectangle(520,100,570,130, fill='green')
brick24= drawpad.create_rectangle(520,180,570,210, fill='green')
brickA1 = drawpad.create_rectangle(60,60,110,90, fill='cyan')
brickA2 = drawpad.create_rectangle(60,140,110,170, fill='cyan')
brickA3 = drawpad.create_rectangle(130,60,180,90, fill='cyan')
brickA4 = drawpad.create_rectangle(130,140,180,170, fill='cyan')
brickA5 = drawpad.create_rectangle(200,60,250,90, fill='cyan')
brickA6 = drawpad.create_rectangle(200,140,250,170, fill='cyan')
brickA7 = drawpad.create_rectangle(270,60,320,90, fill='cyan')
brickA8 = drawpad.create_rectangle(270,140,320,170, fill='cyan')
brickA9 = drawpad.create_rectangle(340,60,390,90, fill='cyan')
brickA10= drawpad.create_rectangle(340,140,390,170, fill='cyan')
brickA11= drawpad.create_rectangle(410,60,460,90, fill='cyan')
brickA12= drawpad.create_rectangle(410,140,460,170, fill='cyan')
brickA13= drawpad.create_rectangle(480,60,530,90, fill='cyan')
brickA14= drawpad.create_rectangle(480,140,530,170, fill='cyan')

class myApp(object):
    def __init__(self, parent):
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        # Score
        self.prompt = "Score:"
        
        self.label1 = Label(root, text=self.prompt, width=len(self.prompt), bg='green')
        self.label1.pack()

        self.score = 0
        
        self.rocketsTxt = Label(root, text=str(self.score), width=len(str(self.score)), bg='green')
        self.rocketsTxt.pack()

        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
        
    def animate(self):
        global drawpad
        
    def key(self,event):
        global drawpad

            
app = myApp(root)
root.mainloop()