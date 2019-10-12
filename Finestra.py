from tkinter import *
from tkinter import ttk
Finestra = Tk()
Finestra.resizable(True, True)

#La sezione Menu Frame 
menubar = Menu(Finestra); filemenu = Menu(menubar, tearoff=0)
frame = ttk.Frame(Finestra)
frameinalto = ttk.Frame(Finestra)
frameLato = ttk.Frame(Finestra)

#Le Entry per la griglia
entry0 = ttk.Entry(frameinalto)
entry1 = ttk.Entry(frameinalto)

#La sezione per le scrolbar
xscrollbar = ttk.Scrollbar(frame, orient=HORIZONTAL);
yscrollbar = ttk.Scrollbar(frame, orient=VERTICAL)

#la sezione per il Canvas
canvas = Canvas(frame, width=600, height=600,bg='white',xscrollcommand=xscrollbar.set,yscrollcommand=yscrollbar.set)
canvas.grid()

#sezione sprite mappe
image = "sprite.png"
listaquadrati = []

#Le Funzioni per gli oggetti
def chiudi_finestra():
    Finestra.destroy()

def cancella_disegno():
    canvas.delete("all")

def ins_image(event):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    sprite = PhotoImage(file=image)
    global id
    id = canvas.create_image(x,y,image=sprite)
    listaquadrati.append(sprite)

def remove(event):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    for z in listaquadrati:
        canvas.delete(id)
    listaquadrati.remove(z)

def get_ottieni_griglia():
    Riga = int(entry0.get())
    Colonna = int(entry1.get())
    canvas.delete("all")
    for y in range(Riga):
        for x in range(Colonna):
            x0 = y * 50
            y0 = x * 50
            questo = canvas.create_rectangle(x0+100, y0+50, x0+50, y0+100)
            print(questo)
    
    canvas.bind('<Button-1>', ins_image)
    canvas.bind('<Button-3>', remove)
    
    xscrollbar.grid(row=1, column=0, sticky="ew")
    yscrollbar.grid(row=0, column=1, sticky="ns")

    xscrollbar.config(command=canvas.xview)
    yscrollbar.config(command=canvas.yview)

    canvas.config( scrollregion=( 0, 0, 100+(Riga * 50), (Colonna * 50)+100 ))

#Widget per il Frame in Alto e i suoi grid() deo bottoni

Disegna = ttk.Button(frameinalto, text="Carica", command=get_ottieni_griglia).grid(row=0,column=3)
CancDisegno = ttk.Button(frameinalto, text="Cancella", command=cancella_disegno).grid(row=0,column=4)

Label(frameinalto, text="Insert Righe / Colonne:").grid(row=0)
entry0.grid(row=0,column=1)
entry1.grid(row=0,column=2)

#Menu dell Applicazione
menubar.add_cascade(label="File", menu=filemenu) 
filemenu.add_command(label="Salva",)
filemenu.add_separator()
filemenu.add_command(label="Esci",command=chiudi_finestra)

#I Grid() per la sezione Canvas

frameinalto.grid(row=0,column=1,sticky="w")
frame.grid(row=1,column=1)

#I widget per la sezione frame Lato in costruzione
button0 = ttk.Button(frame, text="Bottone Uno",
                     command=get_ottieni_griglia).grid( row=0, column=4, rowspan=2, padx=10, pady=10, sticky="n")

#L'avvio dei vari widget dopo il widget canvas in ordine di paternita e avvio
frameLato.grid(row=0, column=0)

#Eventi del sistema TK()
Finestra.config(menu=menubar)
Finestra.mainloop()