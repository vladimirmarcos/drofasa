import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

from system.windows.basewindows import BaseForm

class ConceptoCompraForm(BaseForm):
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.headinglist=("id","nombre","iva","siap","cc") 
        self.widthdate=(80,300,200,600,600)
        self.headingtext=("Id","Nombre","I.V.A.","Clasificación S.I.A.P.","Cuentas contables")
        self.table="conceptocompra"
        self.create_widgets()
        

    def treeviewdata(self):
        for i in self.data:
            i[2]=self.convertintegretdata("iva", "nombre", i[2])
            i[3]=self.convertintegretdata("siap","nombre",i[3])
            i[4]=self.convertintegretdata("cuentacontable","nombre",i[4])
        self.writtetreview(self.treviewlist,self.data)
    
    def createdata(self):
        self.framebase.destroy()
        
        self.newframebase=ttk.LabelFrame(master=self.parent_frame)
        self.newframebase.grid(row=0,column=0)

        namelabel=ttk.Label(master=self.newframebase,text="Nombre: ")
        namelabel.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)

        self.entname=ttk.Entry(master=self.newframebase,width=50)
        self.entname.grid(row=0,column=1,padx=10,pady=10,sticky=NSEW)


        ivalabel=ttk.Label(master=self.newframebase,text="I.V.A.: ")
        ivalabel.grid(row=1,column=0,padx=10,pady=10,sticky=NSEW)
        self.ivavalue=self.selectdatacombo("iva")

        self.entiva=ttk.Combobox(master=self.newframebase,values=self.ivavalue,width=50,state=READONLY)
        self.entiva.grid(row=1,column=1,padx=10,pady=10,sticky=NSEW)
        self.entiva.set(self.ivavalue[0])


        siaplabel=ttk.Label(master=self.newframebase,text="Clasificación S.I.A.P. : ")
        siaplabel.grid(row=2,column=0,padx=10,pady=10,sticky=NSEW)

        self.siapvalue=self.selectdatacombo("siap")
        self.entsiap=ttk.Combobox(master=self.newframebase,width=50,values=self.siapvalue,state=READONLY)
        self.entsiap.grid(row=2,column=1,padx=10,pady=10,sticky=NSEW)
        self.entsiap.set(self.siapvalue[0])

        cclabel=ttk.Label(master=self.newframebase,text="Cuentas contable : ")
        cclabel.grid(row=3,column=0,padx=10,pady=10,sticky=NSEW)

        self.ccvalue=self.selectdatacombo("cuentacontable")
        self.entcc=ttk.Combobox(master=self.newframebase,width=50,values=self.ccvalue,state=READONLY)
        self.entcc.grid(row=3,column=1,padx=10,pady=10,sticky=NSEW)
        self.entcc.set(self.siapvalue[0])

        buttoncancel = ttk.Button(self.newframebase, text="Cancelar", 
                                             command= lambda: self.canceldata(self.newframebase),
                                             width=20,bootstyle=DANGER)
        buttoncancel.grid(row=4, column=0,padx=10, pady=10)

        buttoncreate = ttk.Button(self.newframebase, text="Crear", 
                                             command= self.verifnewdata,
                                             width=20,bootstyle=SUCCESS)
        buttoncreate.grid(row=4, column=1,padx=10, pady=10)

    def verifnewdata(self):
         if (self.entname.get()=="" or self.entiva.get()=="" or self.entsiap.get()=="" or self.entcc.get()==""):
            messagebox.showerror("Error","Los campos de Nombre, SIAP, IVA o Cuenta contables no pueden estar vacíos")
         else:
            data=(self.entname.get(),
            self.convertdatatointeger("iva","nombre",self.entiva.get()),
            self.convertdatatointeger("siap","nombre",self.entsiap.get()),
            self.convertdatatointeger("cuentacontable","nombre",self.entcc.get()))
            message=f'''INSERT INTO conceptocompra (nombre,ivaid,siapid,ccid) VALUES (?, ?,?,?)'''
            self.savenewdata(self.newframebase,
                             "conceptocompra",
                             self.entname
                             ,message,data)
   