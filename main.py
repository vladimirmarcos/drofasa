import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import threading


from newwindows import Program
from server.flaskapp import run_flask


def main():
    root = ttk.Window(themename="darkly")
    root.state('zoomed')  
    Program(root)
    root.mainloop()

if __name__ == "__main__": 
    # Hilo para Flask
    flask_thread = threading.Thread(target=run_flask,daemon=True)

# Iniciar el hilo del servidor Flask
    flask_thread.start()
    main()


