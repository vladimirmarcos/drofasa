import ttkbootstrap as ttk
from ttkbootstrap.constants import *


from system.windows.contabilidad.conceptocompra import ConceptoCompraForm

class AdminMenu:
    def __init__(self, root):
        self.root = root
        #self.login_screen = login_screen
        self.frame = None
        self.create_menu()
        self.show_main_menu()

    def create_menu(self):
        self.menu_bar = ttk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.contabilidad_menu = ttk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Contabilidad", menu=self.contabilidad_menu)
        self.contabilidad_menu.add_command(label="Conceptos de compras", command=self.cuentacontabilidad)
        #self.user_menu.add_command(label="Modificar/Eliminar Usuario", command=self.show_modify_user_form)
        #self.user_menu.add_separator()
        #self.user_menu.add_command(label="Cerrar Sesión", command=self.logout)

        self.drugs_menu = ttk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Drogas", menu=self.drugs_menu)
        self.drugs_menu.add_command(label="Agregar Droga", command="self.show_add_drugs_form")
        self.drugs_menu.add_command(label="Ver Drogas", command="self.show_view_drugs_form")

    def show_main_menu(self):
        self.clear_frame()
        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(pady=100)

        self.label = ttk.Label(self.frame, text="Admin Menu", font=("Helvetica", 24))
        self.label.pack(pady=20)
        
    def clear_frame(self):
        if self.frame:
            self.frame.destroy()
        self.frame = ttk.Frame(self.root)
        self.frame.pack()
    
    def cuentacontabilidad(self):
        self.clear_frame()
        ConceptoCompraForm(self.frame)