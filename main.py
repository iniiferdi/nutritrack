import tkinter as tk
from ui.splash_screen import SplashScreen
from ui.main_window import MainWindow

def run_app():
    root = tk.Tk()
    root.withdraw()

    root.title("NutriTrack - Monitoring Gizi")
    root.geometry("900x600")
    root.configure(bg="#fdfdfd")

    def show_main_window():
        root.deiconify()
        app = MainWindow(root)
        app.pack(fill="both", expand=True)

    splash = SplashScreen(root, on_close=show_main_window)

    root.mainloop()

if __name__ == "__main__":
    run_app()
