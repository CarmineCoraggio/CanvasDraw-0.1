import tkinter as tk
from PIL import Image, ImageTk

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=500, height=500)
        self.canvas.grid()
        
        self.rows = 6
        self.columns = 6
        
        self.tiles = {}
        self.sprite = tk.PhotoImage(file="Sprite.png")
        self.lista = []
        
        
        self.canvas.bind("<Configure>", self.schacchiera)
        
 

    def schacchiera(self, event):
        self.canvas.delete("rect")
        for column in range(self.columns):
            for row in range(self.rows):
                x1 = column * 50 + 50
                y1 = row * 50 + 50
                x2 = x1 + 50
                y2 = y1 + 50
                
                tile = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", tags="rect")
                self.tiles[row, column] = tile
                self.overlapp = self.canvas.find_overlapping(x1, y1, x2, y2)
                
                self.canvas.tag_bind(tile, "<1>", lambda event, row=row, column=column: self.clicked(row, column))
                

    def clicked(self, row, column):
        tile = self.tiles[row, column]
        tile_color = self.canvas.itemcget(tile, "fill")
        
        
        new_color = "white"
        if tile_color == "white":
            new_color = "green"

        else:
            new_color = "white"
        
        
        self.canvas.itemconfigure(tile, fill=new_color)
        



class Sprite():
    def __init__(self, objcanvas, sprite):
        self.objcanvas = objcanvas
        self.x = 100
        self.y = 100
        self.sprite = sprite
        self.objcanvas.create_image(self.x, self.y, image=self.sprite)
        
        

if __name__ == "__main__":
    app = App()
    app.mainloop()