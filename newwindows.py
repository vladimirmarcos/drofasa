import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import webbrowser

class Program:
    def __init__(self,root):
        
        self.root = root
        self.frame = None
        
        # Etiquetas principales
        self.label_contabilidad = ttk.Label(master=self.root, text="concepto de compra", bootstyle="primary")
        self.label_contabilidad.grid(row=0,column=1)
        self.label_contabilidad.bind("<Button-1>", self.show_labels_1)  # Detecta clic

        self.label_2 = ttk.Label(master=self.root, text="Etiqueta 2", bootstyle="success")
        self.label_2.grid(row=0,column=3)
        self.label_2.bind("<Button-1>", self.show_labels_2)

    def show_labels_1(self, event):
        """Muestra una lista de etiquetas cuando se hace clic en 'Etiqueta 1'."""
        webbrowser.open("http://127.0.0.1:5000/conceptodecompra")

    def show_labels_2(self, event):
        """Muestra una lista de etiquetas cuando se hace clic en 'Etiqueta 2'."""
        label_c = ttk.Label(master=self.root, text="Sub-etiqueta 2A", bootstyle="warning")
        #label_c.pack(pady=5)
        #label_c.bind("<Button-1>", lambda e: self.on_click("Sub-etiqueta 2A"))
        
        label_d = ttk.Label(master=self.root, text="Sub-etiqueta 2B", bootstyle="warning")
        #label_d.pack(pady=5)
        #label_d.bind("<Button-1>", lambda e: self.on_click("Sub-etiqueta 2B"))

    def on_click(self, label_name):
        """Acción al hacer clic en una sub-etiqueta."""
        messagebox.showinfo("Información", f"Hiciste clic en {label_name}")

