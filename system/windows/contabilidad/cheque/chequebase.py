import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

from system.windows.basewindows import BaseForm

class ChequeraBaseForm(BaseForm):
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.headinglist=("id","nombre","li","ls","va") 
        self.widthdate=(80,300,200,350,200,200)
        self.headingtext=("Id","Banco","Limite Inferior.","Limite Superior","Proximo Valor valido")
        self.table="chequeracomun"
        self.create_widgets()
        
    def treeviewdata(self):
        self.writtetreview(self.treviewlist,self.data)
    
    def createdata(self):
        self.framebase.destroy()
        
        self.newframebase=ttk.LabelFrame(master=self.parent_frame)
        self.newframebase.grid(row=0,column=0)

        bancolabel=ttk.Label(master=self.newframebase,text="Banco: ")
        bancolabel.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)

        self.entbanco=ttk.Entry(master=self.newframebase,width=50)
        self.entbanco.grid(row=0,column=1,padx=10,pady=10,sticky=NSEW)
        self.entbanco.focus()

        label=ttk.Label(master=self.newframebase,text="Limite inferior: ")
        label.grid(row=1,column=0,padx=10,pady=10,sticky=NSEW)
        

        self.entiva=ttk.Combobox(master=self.newframebase,values=self.ivavalue,width=50,state=READONLY)
        self.entiva.grid(row=1,column=1,padx=10,pady=10,sticky=NSEW)
        self.entiva.set(self.ivavalue[0])


        siaplabel=ttk.Label(master=self.newframebase,text="Limite superior : ")
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
        self.entcc.set(self.ccvalue[0])


        ctlabel=ttk.Label(master=self.newframebase,text="Cuentas Tesoreria : ")
        ctlabel.grid(row=4,column=0,padx=10,pady=10,sticky=NSEW)

        self.ctvalue=self.selectdatacombo("cuentastesoreria")
        self.entct=ttk.Combobox(master=self.newframebase,width=50,values=self.ccvalue,state=READONLY)
        self.entct.grid(row=4,column=1,padx=10,pady=10,sticky=NSEW)
        self.entct.set(self.ctvalue[0])

        buttoncancel = ttk.Button(self.newframebase, text="Cancelar", 
                                             command= lambda: self.canceldata(self.newframebase),
                                             width=20,bootstyle=DANGER)
        buttoncancel.grid(row=5, column=0,padx=10, pady=10)

        buttoncreate = ttk.Button(self.newframebase, text="Crear", 
                                             command= self.verifnewdata,
                                             width=20,bootstyle=SUCCESS)
        buttoncreate.grid(row=5, column=1,padx=10, pady=10)

    def verifnewdata(self):
         if (self.entname.get()=="" or self.entiva.get()=="" or self.entsiap.get()=="" or self.entcc.get()=="" or self.entct.get()==""):
            messagebox.showerror("Error","Los campos de Nombre, SIAP, IVA, Cuenta contables o Cuentas de tesorería no pueden estar vacíos")
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
   
    def showdatamodifi(self):
        self.clearframe(self.framebase)

        self.newframebase=ttk.LabelFrame(master=self.parent_frame)
        self.newframebase.grid(row=0,column=0)

        namelabel=ttk.Label(master=self.newframebase,text="Nombre: ")
        namelabel.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)

        self.entname=ttk.Entry(master=self.newframebase,width=50)
        self.entname.grid(row=0,column=1,padx=10,pady=10,sticky=NSEW)
        self.writteentry([self.entname],[self.currentvalue[1]],1)


        ivalabel=ttk.Label(master=self.newframebase,text="I.V.A.: ")
        ivalabel.grid(row=1,column=0,padx=10,pady=10,sticky=NSEW)
        self.ivavalue=self.selectdatacombo("iva")

        self.entiva=ttk.Combobox(master=self.newframebase,values=self.ivavalue,width=50,state=READONLY)
        self.entiva.grid(row=1,column=1,padx=10,pady=10,sticky=NSEW)
        
        valueiva=self.convertdatatointeger("iva","nombre",self.currentvalue[2])
        self.entiva.set(self.convertintegretdata("iva","nombre",valueiva))


        siaplabel=ttk.Label(master=self.newframebase,text="Clasificación S.I.A.P. : ")
        siaplabel.grid(row=2,column=0,padx=10,pady=10,sticky=NSEW)

        self.siapvalue=self.selectdatacombo("siap")
        self.entsiap=ttk.Combobox(master=self.newframebase,width=50,values=self.siapvalue,state=READONLY)
        self.entsiap.grid(row=2,column=1,padx=10,pady=10,sticky=NSEW)
        valuesiap=self.convertdatatointeger("siap","nombre",self.currentvalue[3])
        self.entsiap.set(self.convertintegretdata("siap","nombre",valuesiap))

        cclabel=ttk.Label(master=self.newframebase,text="Cuentas contable : ")
        cclabel.grid(row=3,column=0,padx=10,pady=10,sticky=NSEW)

        self.ccvalue=self.selectdatacombo("cuentacontable")
        self.entcc=ttk.Combobox(master=self.newframebase,width=50,values=self.ccvalue,state=READONLY)
        self.entcc.grid(row=3,column=1,padx=10,pady=10,sticky=NSEW)
        valuescc=self.convertdatatointeger("cuentacontable","nombre",self.currentvalue[4])
        self.entcc.set(self.convertintegretdata("cuentacontable","nombre",valuescc))

        ctlabel=ttk.Label(master=self.newframebase,text="Cuentas tesoreria : ")
        ctlabel.grid(row=4,column=0,padx=10,pady=10,sticky=NSEW)

        self.ctvalue=self.selectdatacombo("cuentastesoreria")
        self.entct=ttk.Combobox(master=self.newframebase,width=50,values=self.ctvalue,state=READONLY)
        self.entct.grid(row=4,column=1,padx=10,pady=10,sticky=NSEW)
        valuesct=self.convertdatatointeger("cuentastesoreria","nombre",self.currentvalue[5])
        self.entct.set(self.convertintegretdata("cuentastesoreria","nombre",valuesct))

        buttoncancel = ttk.Button(self.newframebase, text="Cancelar", 
                                             command= lambda: self.canceldata(self.newframebase),
                                             width=20,bootstyle=DANGER)
        buttoncancel.grid(row=5, column=0,padx=10, pady=10)

        buttoncreate = ttk.Button(self.newframebase, text="Modificar", 
                                             command= self.verifdatamodif,
                                             width=20,bootstyle=SUCCESS)
        buttoncreate.grid(row=5, column=1,padx=10, pady=10)

    def verifdatamodif(self):  
        if self.entiva.get()=="" or self.entsiap.get()=="" or self.entcc.get()=="" or self.entct.get()=="":
            messagebox.showerror("Error","Alguno de los campos quedo vacío")
        else:
            savedata=(self.convertdatatointeger("iva","nombre",self.entiva.get()),
                      self.convertdatatointeger("siap","nombre",self.entsiap.get()),
                      self.convertdatatointeger("cuentacontable","nombre",self.entcc.get()),
                      self.convertdatatointeger("cuentastesoreria","nombre",self.entct.get()),
                      self.currentvalue[0])
            message=f"UPDATE conceptocompra SET (ivaid,siapid,ccid,ctid)=(?,?,?,?) WHERE id= ?"
            self.savemodifidata(message,savedata,self.newframebase)

