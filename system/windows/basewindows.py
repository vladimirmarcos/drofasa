import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import sqlite3

from system.conexion.basedatos import searchalldata,convertintdata,datavaluescombo,dataexist,convertdataint,savedata


class BaseForm:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.create_widgets()
    
    def create_widgets(self):
        self.framebase=ttk.Frame(master=self.parent_frame)
        self.framebase.grid(row=0,column=0)
        self.createbuttonwidget()
        self.createdsearchwidget()
        self.createtreeviewframe()
        self.searchdata()
        self.treeviewdata()
        self.entsearch.focus()

    def createbuttonwidget(self):
        """funtion to create button
        """        
        self.buttonframe=ttk.Labelframe(master=self.framebase,width=100)  
        self.buttonframe.grid(row=1,column=0,sticky=NSEW) 

        self.buttoncreate = ttk.Button(self.buttonframe, text="Crear", 
                                             command=self.createdata,
                                             width=20,bootstyle=SUCCESS)
        self.buttoncreate.grid(row=0, column=0,padx=10, pady=10)

        self.buttonmodifity = ttk.Button(self.buttonframe, text="Modificar", 
                                             command=self.modifidata,
                                             width=20,bootstyle=WARNING)
        self.buttonmodifity.grid(row=0, column=1,padx=10, pady=10)

        self.buttondelete = ttk.Button(self.buttonframe, text="Eliminar", 
                                             command=self.deletedata,
                                             width=20,bootstyle=DANGER)
        self.buttondelete.grid(row=0, column=2,padx=10, pady=10)
    
    def createdsearchwidget(self):
        """ funtion to create search frame
        """        
        self.searchframe=ttk.Labelframe(master=self.framebase,width=20)  
        self.searchframe.grid(row=0,column=0,sticky=NSEW) 
        searchlabel=ttk.Label(master=self.searchframe,text="Busqueda por ")
        searchlabel.grid(row=0,column=0,padx=10,pady=10)

        self.valuessearch=[""]
        self.searchoption= ttk.Combobox(
        self.searchframe,
        state="readonly",
        values=self.valuessearch,width=20
         )
        self.searchoption.set(self.valuessearch[0])
        self.searchoption.grid(row=0,column=1, pady=5,sticky="w")

        self.entsearch=ttk.Entry(master=self.searchframe,width=100)
        self.entsearch.grid(row=0,column=2,padx=10,pady=10,sticky=NSEW)

    def createtreeviewframe(self):
        """Funtion to create treeview with scrollbars"""

        self.treeviewframe = ttk.Labelframe(master=self.framebase)
        self.treeviewframe.grid(row=2, column=0, sticky=NSEW)

        self.treviewlist = ttk.Treeview(
            master=self.treeviewframe,
            height=30,
            columns=self.headinglist,
            show='headings'
        )

        self.yscroll = ttk.Scrollbar(self.treeviewframe, orient='vertical', command=self.treviewlist.yview,bootstyle=SUCCESS)
        self.treviewlist.configure(yscrollcommand=self.yscroll.set)

        self.xscroll = ttk.Scrollbar(self.treeviewframe, orient='horizontal', command=self.treviewlist.xview,bootstyle=SUCCESS)
        self.treviewlist.configure(xscrollcommand=self.xscroll.set)
        
        self.treviewlist.grid(row=0, column=0, sticky=NSEW)
        self.yscroll.grid(row=0, column=1, sticky=NS)
        self.xscroll.grid(row=1, column=0, sticky=EW)

        self.treeviewframe.grid_rowconfigure(0, weight=1)
        self.treeviewframe.grid_columnconfigure(0, weight=1)

        for i, j in zip(self.headinglist, self.headingtext):
            self.treviewlist.heading(i, text=j, anchor=W)

        for i, j in zip(self.headinglist, self.widthdate):
            self.treviewlist.column(i, width=j, stretch=False)

        # Aumentar el tamaño de la fuente para aumentar el alto de las filas
        self.treviewlist.tag_configure('row', font=('Helvetica', 8))

        
        self.treviewlist.bind("<Button-3>", self.copy_to_clipboard)
        
    def copy_to_clipboard(self, event):
        """Copy de data selection

        Args:
            event (_type_): _description_
        """        
        
        item_id = self.treviewlist.identify_row(event.y)
        column = self.treviewlist.identify_column(event.x)
        if item_id and column:
            col_index = int(column.replace("#", "")) - 1
            row_values = self.treviewlist.item(item_id, 'values')
            if row_values:
                value_to_copy = row_values[col_index]
                self.treeviewframe.clipboard_clear()  
                self.treeviewframe.clipboard_append(value_to_copy)  
                  
    def cleartreview(self,triview):
        """Clear trieview

        Args:
            triview (Triewiv): Some triewiv
        """              
        data=triview.get_children()
        for element in data:
            triview.delete(element)

    def writtetreview(self,triewiew,data):
        """_summary_

        Args:
            triewiew (_type_): _description_
            data (_type_): _description_
        """        
        for element in data:
            triewiew.insert('', 'end', values=element)      

    def searchdata(self):
        tupleauxiliar=searchalldata(self.table)
        self.data=[list(tupla) for tupla in tupleauxiliar]
        

    def treeviewdata(self):
        pass  

    def createdata(self):
        pass

    def modifidata(self):
        self.currentvalueselection=self.treviewlist.focus()
        self.currentvalue=self.treviewlist.item(self.currentvalueselection,'values')
        if self.currentvalue!="":
            self.showdatamodifi()
        else:
            messagebox.showerror("Error","No se selecciono ningún dato")
    
    def showdatamodifi(self):
        pass

    def deletedata(self):
        pass

    def convertintegretdata(self,table,campo,data):
        """_summary_

        Args:
            table (_type_): _description_
            campo (_type_): _description_
            data (_type_): _description_

        Returns:
            _type_: _description_
        """        
        newdata=convertintdata(table,campo,data)[0]
        return newdata
    
    def selectdatacombo(self,table):
        """_summary_

        Args:
            table (_type_): _description_

        Returns:
            _type_: _description_
        """        
        tupleauxiliar=datavaluescombo(table)
        values=[tupla[0] for tupla in tupleauxiliar]
        values.insert(0,"")
        return values

    def savenewdata(self,frame,table,exist,message,data):
        """_summary_

        Args:
            frame (_type_): _description_
            table (_type_): _description_
            exist (_type_): _description_
            message (_type_): _description_
        """           
        
        if not (dataexist(table,exist.get(),"nombre")):
                 savedata(message,data)
                 messagebox.showinfo("",f"El dato {exist.get()} fue agregado exitosamente a la base de datos")
                 self.canceldata(frame)
        else:
                messagebox.showerror("Error",f"El dato {exist.get()} ya existe en la base de datos")

    def verifnewdata(self):
        pass

    def canceldata(self,frame):
        self.clearframe(frame)
        self.create_widgets()

    def clearframe(self,frame):
        frame.destroy()

    def writteentry(self,listentry,valueentry,flag):
        """_summary_

        Args:
            listentry (_type_): _description_
            valueentry (_type_): _description_
            flag (_type_): _description_
        """              
        for i,j in zip(listentry,valueentry):
            i.delete(0, ttk.END)  
            i.insert(0, j)  
        if flag==0:
            for i in listentry:
                i.config(state=NORMAL)
            return
        elif flag==1:
            for i in listentry:
                i.config(state=READONLY)
            return
        else:
            for i in listentry:
                i.config(state=DISABLED)
            return

    def savemodifidata(self,message,data,frame):
        """_summary_

        Args:
            message (_type_): _description_
            data (_type_): _description_
        """        
        try:
            savedata(message,data)
            messagebox.showinfo("Cambio","¡Se actualizo el dato en la base de datos.!")
            self.canceldata(frame)
        except sqlite3.OperationalError:
            messagebox.showerror("Error","La base de datos esta ocupada. Espere un momento")
    
    def convertdatatointeger(self,table,campo,data):
        """_summary_

        Args:
            table (_type_): _description_
            campo (_type_): _description_
            data (_type_): _description_

        Returns:
            _type_: _description_
        """        
        newdata=convertdataint(table,campo,data)[0]
        return newdata