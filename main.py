import tkinter as tk
from ui.main_window import MainWindow

def run_app():
    root = tk.Tk()
    root.withdraw()

    root.title("NutriTrack - Monitoring Gizi")
    root.geometry("900x600")
    root.configure(bg="#EBECE6")
    root.state('zoomed')

    root.deiconify()
    app = MainWindow(root)
    app.pack(fill="both", expand=True)    

    root.mainloop()

if __name__ == "__main__":
    run_app()
