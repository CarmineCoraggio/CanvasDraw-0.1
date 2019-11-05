import tkinter as tk
from PIL import Image, ImageTk

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.sprite = tk.PhotoImage(file="Sprite.png")
        self.xscrollbar = tk.Scrollbar(self, orient='horizontal')
        self.yscrollbar = tk.Scrollbar(self, orient='vertical')
        self.canvas = tk.Canvas(self, width=850, height=600, xscrollcommand=self.xscrollbar.set, yscrollcommand=self.yscrollbar.set)
        
        self.rows = 20
        self.columns = 20
        self.griglia()
        
        ###Mouse Event
        self.canvas.bind("<B1-Motion>", self.click)
        self.canvas.bind("<B3-Motion>", self.click_delete)

        ###show object tkinter
        self.canvas.grid()

        self.xscrollbar.config(command=self.canvas.xview)
        self.yscrollbar.config(command=self.canvas.yview)
        self.xscrollbar.grid(row=1, column=0, sticky="we")
        self.yscrollbar.grid(row=0, column=1, sticky="nsew")
      
        
    def griglia(self):
        offsetscroll = 100
        for column in range(self.columns):
            for row in range(self.rows):
                x1 = column * 50 + 50
                y1 = row * 50 + 50
                x2 = x1 + 50
                y2 = y1 + 50
                self.rectid = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", tags="rect")
                self.canvas.config(scrollregion=(0, 0, x1+offsetscroll, y1+offsetscroll))
                
        
    def click(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        
        self.overlap = self.canvas.find_overlapping(x, y, x, y)
        
        
        grid_tipe = self.canvas.type(self.overlap)
        if grid_tipe == "rectangle":
            
            self.x = self.canvas.coords(self.overlap)[0]
            self.y = self.canvas.coords(self.overlap)[1]
            
            self.idimg = self.canvas.create_image(self.x, self.y, image=self.sprite, anchor="nw", tags="img")
            
            
        """   
        for x in self.overlap:
            imgtipe = self.canvas.type(x)
            if imgtipe == "image":
                print(x)
                self.canvas.delete(x)
        """
            
         
    def click_delete(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.overlap = self.canvas.find_overlapping(x, y, x, y)
        
        
        for x in self.overlap:
            
            imgtipe = self.canvas.type(x)
            if imgtipe == "image":
                
                self.canvas.delete(x)
                
            if imgtipe == "rectangle":
                print(imgtipe)
                ###self.x = self.canvas.coords(self.overlap)[0]
                ###self.y = self.canvas.coords(self.overlap)[1]
                ###self.rectid2 = self.canvas.create_rectangle(self.x, self.y, self.x+50, self.y+50, fill="green", tags="rect")
                



if __name__ == "__main__":
    app = App()
    app.mainloop()

