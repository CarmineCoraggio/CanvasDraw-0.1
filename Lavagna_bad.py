from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class App_Manager(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.my_canvas = MyObjCanvas(self)
        
        
        self.my_canvas.canvas.grid()
        self.grid()


class MyObjCanvas():
    def __init__(self, objframe):
        
        self.canvas = Canvas(objframe,  width=400, height=400)
        self.sprite = PhotoImage(file="Sprite.png")
        self.drawgrid = DrawGrid(self.canvas, 6, 6)
        self.drawgrid.draw_grid()
        
        self.canvas.bind("<Button-1>", self.insert_sprite)
        
    def insert_sprite(self, event):
        self.x = self.canvas.canvasx(event.x)
        self.y = self.canvas.canvasy(event.y)
        
        self.quadrato = self.drawgrid.clickQuadrato(self.x, self.y)
        self.img = Insert_Sprite(self.canvas, self.quadrato.x, self.quadrato.y, self.sprite)
        ###self.img.draw()
        print(self.quadrato.x,self.quadrato.y ,self.quadrato.lato)
        
          
        
class DrawGrid():
    def __init__(self, objcanvas, righe , colonne):
        self.obj_canvas = objcanvas
        self.righe = righe
        self.colonne = colonne
        self.griglia = []
        
    
    def draw_grid(self):
        for y in range(self.colonne):
            for x in range(self.righe):
                
                self.x = (y * 50) + 50
                self.y = (x * 50) + 50
                
                self.drawrect = DrawRect(self.obj_canvas, self.x, self.y, 50)
                self.griglia.append(self.drawrect)
    
                
                
    def clickQuadrato(self, clickX, clickY):

        quadrato = None
        for x in self.griglia:
            if (x.contiene(clickX, clickY) == True):
                quadrato = x
                              
        return quadrato

    



class DrawRect():
    def __init__(self, objcanvas, x, y, lato):
        self.objcanvas = objcanvas
        self.x = x
        self.y = y
        self.lato = lato
        self.id_ = self.objcanvas.create_rectangle(self.x, self.y, self.x + self.lato, self.y + self.lato)
        self.selected = None
        
    def contiene(self, puntoX, puntoY):
        dentro = False
        if self.x < puntoX < (self.x + self.lato):
            if self.y < puntoY < (self.y + self.lato):
                dentro = True
        return dentro
       

class Insert_Sprite():
    def __init__(self, objcanvas, x, y, sprite):
        self.objcanvas = objcanvas
        self.x = x
        self.y = y
        self.sprite = sprite
        self.objcanvas.create_image(self.x, self.y, image=self.sprite, anchor=NW)
 

    def contiene(self, puntoX, puntoY):
        dentro = False
        if self.x < puntoX < (self.x + self.sprite.width()):
            if self.y < puntoY < (self.y + self.sprite.height()):
                dentro = True
        return dentro

    ###def draw(self):
    ###    self.objcanvas.create_image(self.x, self.y, image=self.sprite, anchor=NW)

  

if __name__ == "__main__":

    root = Tk()
    app_1 = App_Manager(root)
    app_1.master.wm_title("Lavagna")
    app_1.mainloop()