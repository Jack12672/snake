from tkinter import * 

SPEED=10
CASE=20

class Grid():
    def __init__(self,dimension:tuple [int,int]):
        self.grid=[]
        self.dimension=dimension 
        temp=[]
        for x in range (dimension[0]):
            for y in range (dimension[1]):
                temp.append(0)
            self.grid.append(temp)
            temp=[]  

class Can(Canvas):
    def __init__(self,canvas,dimension):
        self.dimension=dimension
        super().__init__(canvas,bg="white",width=dimension[0]*CASE,height=dimension[1]*CASE)
        self.grid=Grid(dimension)


    def draw_grid(self):      
        color='blue'
        w=self.dimension[0]*CASE
        h=self.dimension[1]*CASE
        for x in range (0,w+1,CASE):
            self.create_line(x,0,x,h,width = 1, fill=color)
        for y in range (0,h+1,CASE):
            self.create_line(0,y,w,y,width = 1, fill=color)
        self.pack()



class Window_0(Frame):
    def __init__(self,dimension): 
        Frame.__init__(self)
        self.w=Can(self.master,dimension)
        w=dimension[0]*CASE
        h=dimension[1]*CASE
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        posx=int((screen_width-w)/2)
        posy=int((screen_height-h)/2)
        self.master.title('Snake IA 2025')
        self.master.geometry('%dx%d+%d+%d' % (w,h,posx,posy))
        self.master.bind("<Button-1>",lambda event: self.mousedown_left(event))
        self.master.bind("<Button-2>",lambda event: self.mousedown_scroll_wheel(event))
        self.master.bind("<Button-3>",lambda event: self.mousedown_right(event))
        self.master.bind("<B1-Motion>",lambda event: self.move_mouse(event))
        # child=Windows(bg='green',width=300,height=300 )
        self.w.draw_grid()

    def move_mouse (self,event):
        if self.button_left_press:
            x, y = int(event.x/CASE), int(event.y/CASE)
            if self.w.can.grid[x][y].obj==0:
                x1=x*CASE+CASE
                y1=y*CASE+CASE

    
    def mousedown_left(self, event):
        pass

    def mouseup_left(self, event):
        pass
        
    def mousedown_scroll_wheel(self, event):
        pass

    def mousedown_right(self, event):
        pass

    def start(self):
        pass
    def start(self):
        self.w.update_grid()
        self.w.after(SPEED,self.start)


class Windows(Toplevel):
    def __init__(self, **Arguments):
        Toplevel.__init__(self, **Arguments)
        self.title('child')
        self.geometry('+%d+%d' %(1200,50))
        self.bind("<Button-1>",lambda event: self.mousedown(event))
        self.bind("<Button-3>",lambda event: self.mousedown_right(event))

    def mousedown(self, event):
        x, y = event.x, event.y 
    
    def mousedown_right(self, event):
        x, y = event.x, event.y 


if __name__=="__main__":
    t=Window_0((30,30))
    t.mainloop()