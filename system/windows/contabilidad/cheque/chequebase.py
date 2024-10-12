import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

from system.windows.basewindows import BaseForm
from system.conexion.basedatos import query,savedata

class ChequeraBaseForm(BaseForm):
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.headinglist=("id","nombre","li","ls","va") 
        self.widthdate=(80,300,200,350,200)
        self.headingtext=("Id","Banco","Limite Inferior.","Limite Superior","Proximo Valor valido")
        self.table="chequeracomun"
        self.tableauxiliar="chequescomunes"
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
        

        self.entlm=ttk.Entry(master=self.newframebase,width=50)
        self.entlm.grid(row=1,column=1,padx=10,pady=10,sticky=NSEW)


        lslabel=ttk.Label(master=self.newframebase,text="Limite superior : ")
        lslabel.grid(row=2,column=0,padx=10,pady=10,sticky=NSEW)

        self.entls=ttk.Entry(master=self.newframebase,width=50)
        self.entls.grid(row=2,column=1,padx=10,pady=10,sticky=NSEW)

       

        buttoncancel = ttk.Button(self.newframebase, text="Cancelar", 
                                             command= lambda: self.canceldata(self.newframebase),
                                             width=20,bootstyle=DANGER)
        buttoncancel.grid(row=3, column=0,padx=10, pady=10)

        buttoncreate = ttk.Button(self.newframebase, text="Crear", 
                                             command= self.verifnewdata,
                                             width=20,bootstyle=SUCCESS)
        buttoncreate.grid(row=3, column=1,padx=10, pady=10)

    def verifnewdata(self):
         if (self.entbanco.get()=="" or self.entlm.get()=="" or self.entls.get()==""):
            messagebox.showerror("Error","Los campos de Banco, Límite Superior o Ingerior no pueden estar vacíos")
         else:
            if not (self.verifnumer(self.entlm,0)):
                 messagebox.showerror("Error", "el límite inferior no es un valor valido como entero =/")
            elif not (self.verifnumer(self.entls,0)):
                 messagebox.showerror("Error", "el límite superior no es un valor valido como entero =/")
            elif self.veriflimit(self.entlm.get())==1:
                 messagebox.showerror("Error", "el límite inferior ya existe en otra chequera, verifique el dato")
            elif self.veriflimit(self.entls.get())==1:
                 messagebox.showerror("Error", "el límite superior ya existe en otra chequera, verifique el dato")
            else:
                 data=(self.entbanco.get(),
                       self.entlm.get(),
                       self.entls.get(),
                       self.entlm.get(),
                       1)
                 message=message=f'''INSERT INTO chequeracomun (nombre,li,ls,va,estado) VALUES (?, ?,?,?,?)'''
                 savedata(message,data)
                 messagebox.showinfo("",f"El cheque fue agregado exitosamente a la base de datos")
                 self.canceldata(self.newframebase)
                 
    def veriflimit(self,value):
        message=f"""SELECT 
                            CASE 
                            WHEN EXISTS (
            SELECT 1
            FROM {self.table}
            WHERE li <= {value} AND ls >= {value}
        ) 
        THEN 1 
        ELSE 0 
    END AS resultado;"""
        return query(message,0)

    def showdatamodifi(self):
        """_summary_
        """        
        self.clearframe(self.framebase)

        self.newframebase=ttk.LabelFrame(master=self.parent_frame,width=600)
        self.newframebase.grid(row=0,column=2,sticky=NSEW)

        banknamelabel=ttk.Label(master=self.newframebase,text="Nombre Banco: ")
        banknamelabel.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)

        self.entnamebank=ttk.Entry(master=self.newframebase,width=50)
        self.entnamebank.grid(row=0,column=1,padx=10,pady=10,sticky=NSEW)
        self.writteentry([self.entnamebank],[self.currentvalue[1]],1)

        chequeraidlabel=ttk.Label(master=self.newframebase,text="ID Chequera: ")
        chequeraidlabel.grid(row=1,column=0,padx=10,pady=10,sticky=NSEW)

        self.chequeraid=ttk.Entry(master=self.newframebase,width=50)
        self.chequeraid.grid(row=1,column=1,padx=10,pady=10,sticky=NSEW)
        self.writteentry([self.chequeraid],[self.currentvalue[0]],1)
        
        message=f"SELECT * FROM {self.tableauxiliar} WHERE estado=1"
        query(message,1)
        
        self.createtreechequeras()
        self.cleartreview(self.treviewcheque )
        self.writteches(query(message,1),self.treviewcheque)
        

        buttoncancel = ttk.Button(self.newframebase, text="Cancelar", 
                                             command= lambda: self.canceldata(self.newframebase),
                                             width=20,bootstyle=DANGER)
        buttoncancel.grid(row=5, column=0,padx=10, pady=10)

        buttoncreate = ttk.Button(self.newframebase, text="Dar de Baja", 
                                             command= self.verifdatamodif,
                                             width=20,bootstyle=WARNING)
        buttoncreate.grid(row=5, column=1,padx=10, pady=10)

    def verifdatamodif(self): 
        self.currentchequeselection=self.treviewcheque.focus()
        self.currentvaluecheque=self.treviewcheque.item(self.currentchequeselection,'values') 
        if self.currentvaluecheque!="":
            ask=messagebox.askquestion("Consulta","Esta seguro de dar de baja el cheque del cliente tanto ")
            self.clearframe(self.treeviewframe )
            self.canceldata(self.newframebase)
        else:
            messagebox.showerror("Error","No se selecciono ningún cheque de la chequera")
        """ 
        if self.entiva.get()=="" or self.entsiap.get()=="" or self.entcc.get()=="" or self.entct.get()=="":
            messagebox.showerror("Error","Alguno de los campos quedo vacío")
        else:
            savedata=(self.convertdatatointeger("iva","nombre",self.entiva.get()),
                      self.convertdatatointeger("siap","nombre",self.entsiap.get()),
                      self.convertdatatointeger("cuentacontable","nombre",self.entcc.get()),
                      self.convertdatatointeger("cuentastesoreria","nombre",self.entct.get()),
                      self.currentvalue[0])
            message=f"UPDATE conceptocompra SET (ivaid,siapid,ccid,ctid)=(?,?,?,?) WHERE id= ?"
            self.savemodifidata(message,savedata,self.newframebase)"""

    def writteches(self,data,triewiew):
        for element in data:
            triewiew.insert('', 'end', values=[element[0],element[1],element[3]])
         
    def createtreechequeras(self):
        """Funtion to create treeview with scrollbars"""

        self.treeviewframe = ttk.Labelframe(master=self.parent_frame)
        self.treeviewframe.grid(row=1, column=2, sticky=NSEW)

        self.treviewcheque = ttk.Treeview(
            master=self.treeviewframe,
            height=30,
            columns=["id","numero","monto"],
            show='headings'
        )

        self.yscroll = ttk.Scrollbar(self.treeviewframe, orient='vertical', command=self.treviewlist.yview,bootstyle=SUCCESS)
        self.treviewcheque.configure(yscrollcommand=self.yscroll.set)

        self.xscroll = ttk.Scrollbar(self.treeviewframe, orient='horizontal', command=self.treviewlist.xview,bootstyle=SUCCESS)
        self.treviewcheque.configure(xscrollcommand=self.xscroll.set)
        
        self.treviewcheque.grid(row=0, column=0, sticky=NSEW)
        self.yscroll.grid(row=0, column=1, sticky=NS)
        self.xscroll.grid(row=1, column=0, sticky=EW)

        self.treeviewframe.grid_rowconfigure(0, weight=1)
        self.treeviewframe.grid_columnconfigure(0, weight=1)

        for i, j in zip(["id","numero","monto"], ["I.D.","Número","Monto"]):
            self.treviewcheque.heading(i, text=j, anchor=W)

        for i, j in zip(["id","numero","monto"], [50,200,300]):
            self.treviewcheque.column(i, width=j, stretch=False)

        self.treviewcheque.tag_configure('row', font=('Helvetica', 8))

    def createbuttonwidget(self):
        super().createbuttonwidget()
        self.buttonmodifity.config(text="Dar de baja cheque")