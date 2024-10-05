import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from system.menu.menuadmin import AdminMenu


def main():
    
    root = ttk.Window(themename="darkly")
    root.state('zoomed')  
    app = AdminMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()