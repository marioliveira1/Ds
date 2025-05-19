from tkinter import *


class App:
    def __init__(self, root):
        self.frame1 = Frame(root)
        self.frame1.pack()
        Label(self,framel,text="Conversão de Centimetro para Polegada",
        font=("Verdana", "14", "bold"), height=3).pack()

      
        
    Label(self,framel,text="Centimetro(s):").pack(side=LEFT)
    self.centimetro=Entry(self.framel)
    self.centimetro.focus_force()
    self.centimetro.pack(side=LEFT)
    Button(self,frame1,text="Converter",command=self.converter)


    Label(self.frame1,text="Polegada(s):").pack(side=LEFT)