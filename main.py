import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from system.menu.menuadmin import AdminMenu


def main():
    
    root = ttk.Window(themename="darkly")
    root.state('zoomed')  
    root.grid_columnconfigure(0, weight=1)  
    root.grid_rowconfigure(0,weight=1)
    AdminMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()