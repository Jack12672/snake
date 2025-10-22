from tkinter import * 
import random
import time

SPEED=100
CASE=20

class Snake():
    def __init__(self,dimension):
        self.isalive=True
        self.dx=0
        self.dy=1
        self.position=[]
        self.length=3
        self.fruit=(0,0)
        x1=int(dimension[0]/2)
        y1=int(dimension[1]/2)
        x1=1
        y1=1
        self.head=((x1,y1))
        self.position.append(self.head)
        y1+=1
        self.position.append((x1,y1))
        x1-=1
        self.position.append((x1,y1))


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
        self.obj=[]
        self.fruit=0
        self.grid=Grid(dimension)
        self.snake=Snake(dimension)
        super().__init__(canvas,bg="white",width=dimension[0]*CASE,height=dimension[1]*CASE)

    def draw_grid(self):      
        color='blue'
        w=self.dimension[0]*CASE
        h=self.dimension[1]*CASE
        for x in range (0,w+1,CASE):
            self.create_line(x,0,x,h,width = 1, fill=color)
        for y in range (0,h+1,CASE):
            self.create_line(0,y,w,y,width = 1, fill=color)
        self.pack()

    def draw_snake(self):
        for i in range (self.snake.length):
            x,y=self.snake.position[i][0],self.snake.position[i][1]
            x0,y0=x*CASE,y*CASE
            x1,y1=x0+CASE,y0+CASE
            self.obj.append(self.create_oval(x0,y0,x1,y1,width = 1, fill="green"))
            self.grid.grid[x][y]=1
        self.pack()

    def draw_fruit(self):
        
        maxx,maxy=self.dimension
        isvalid=True
        x,y=0,0     
        while isvalid:
            seed = time.time() / 3600
            random.seed(seed)
            x=random.randrange(maxx)
            seed = time.time() / 3600 
            random.seed(seed)
            y=random.randrange(maxy)
            if self.grid.grid[x][y]==0 : isvalid=False

        self.snake.fruit=(x,y)
        x0,y0=x*CASE,y*CASE
        x1,y1=x0+CASE,y0+CASE
        self.fruit=self.create_oval(x0,y0,x1,y1,width = 1, fill="red")


    def update (self):
        l=self.snake.length
        for i in range (self.snake.length-2,-1,-1):
            x,y=self.snake.position[i][0],self.snake.position[i][1]
            x1,y1=self.snake.position[i+1][0],self.snake.position[i+1][1]
            self.snake.position[i+1]=(x,y)
            self.move(self.obj[i+1],(x-x1)*CASE,(y-y1)*CASE)

        x,y=self.snake.position[0][0]+self.snake.dx,self.snake.position[0][1]+self.snake.dy
        self.snake.head=(x,y)
        if self.check_obstacle() == False:   
            self.snake.position[0]=(x,y)
            self.grid.grid[x][y]=1
            self.move(self.obj[0],self.snake.dx*CASE,self.snake.dy*CASE)

        if self.check_fruit():
            x,y=self.snake.position[l-1][0],self.snake.position[l-1][1]
            self.snake.position.append((x,y))
            self.obj.append(self.create_oval(x*CASE,y*CASE,x*CASE+CASE,y*CASE+CASE,width = 1, fill="green"))
            self.snake.length+=1
            self.delete(self.fruit)
            self.draw_fruit()
        else: 
            x,y=self.snake.position[l-1][0],self.snake.position[l-1][1]
            self.grid.grid[x][y]=0           
        self.pack()
        

    def check_obstacle (self):
        x,y = self.snake.head
        res=False
        if x<0 or x>self.grid.dimension[0]-1 : 
            self.snake.isalive=False
            res=True
        if y<0 or y>self.grid.dimension[1]-1: 
            self.snake.isalive=False
            res=True
        if self.grid.grid[x][y]!=0:
            res=True
            self.snake.isalive=False
        return res


    def check_fruit(self):
        x,y = self.snake.head
        xf,yf = self.snake.fruit
        if (x==xf and y==yf): return True
        else: return False





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
        self.master.bind("<KeyPress-Left>",lambda event: self.left(event))
        self.master.bind("<KeyPress-Right>",lambda event: self.right(event))
        self.master.bind("<KeyPress-Up>",lambda event: self.up(event))
        self.master.bind("<KeyPress-Down>",lambda event: self.down(event))

        self.master.bind("<Button-1>",lambda event: self.mousedown_left(event))
        self.master.bind("<Button-2>",lambda event: self.mousedown_scroll_wheel(event))
        self.master.bind("<Button-3>",lambda event: self.mousedown_right(event))
        self.master.bind("<B1-Motion>",lambda event: self.move_mouse(event))
        # child=Windows(bg='green',width=300,height=300 )
        self.w.draw_grid()
        self.w.draw_snake()
        self.w.draw_fruit()

    def left (self,event):
        self.w.snake.dx=-1
        self.w.snake.dy=0

    def right (self,event):
        self.w.snake.dx=1
        self.w.snake.dy=0
        
    def up (self,event):
        self.w.snake.dy=-1
        self.w.snake.dx=0
        
    def down (self,event):
        self.w.snake.dy=1
        self.w.snake.dx=0

    def move_mouse (self,event):
        pass
    
    def mousedown_left(self, event):
        self.w.snake.isalive=True
        self.start()

    def mouseup_left(self, event):
        pass
        
    def mousedown_scroll_wheel(self, event):
        self.w.snake.isalive=False
        for y in range (30):
            l="|"
            for x in range (30):
                if self.w.grid.grid[x][y]==1 : l+="O" 
                else: l+=" "
            l+="|"
            print (l)
        print('_______________________________')


    def mousedown_right(self, event):
        self.w.update()

    def start(self):
        pass

    def start(self):
        if self.w.snake.isalive:
            self.w.update()
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