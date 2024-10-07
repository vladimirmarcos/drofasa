import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

from system.windows.basewindows import BaseForm

class ConceptoCompraForm(BaseForm):
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.headinglist=("id","nombre","iva","siap") 
        self.widthdate=(80,300,200,600)
        self.headingtext=("Id","Nombre","I.V.A.","Clasificación S.I.A.P.")
        self.table="conceptocompra"
        self.create_widgets()
        

    def treeviewdata(self):
        for i in self.data:
            i[2]=self.convertintegretdata("iva", "nombre", i[2])
            i[3]=self.convertintegretdata("siap","nombre",i[3])
        self.writtetreview(self.treviewlist,self.data)
    
    def createdata(self):
        self.framebase.destroy()
        self.newframebase=ttk.LabelFrame(master=self.parent_frame)
        self.newframebase.grid(row=0,column=0)

        namelabel=ttk.Label(master=self.newframebase,text="Nombre: ")
        namelabel.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)

        self.entname=ttk.Entry(master=self.newframebase,width=50)
        self.entname.grid(row=0,column=1,padx=10,pady=10,sticky=NSEW)


        namelabel=ttk.Label(master=self.newframebase,text="I.V.A.: ")
        namelabel.grid(row=1,column=0,padx=10,pady=10,sticky=NSEW)

        self.entname=ttk.Entry(master=self.newframebase,width=50)
        self.entname.grid(row=1,column=1,padx=10,pady=10,sticky=NSEW)


        namelabel=ttk.Label(master=self.newframebase,text="Clasificación S.I.A.P. : ")
        namelabel.grid(row=2,column=0,padx=10,pady=10,sticky=NSEW)

        self.entname=ttk.Entry(master=self.newframebase,width=50)
        self.entname.grid(row=2,column=1,padx=10,pady=10,sticky=NSEW)
            