# ui/splash_screen.py

import tkinter as tk

class SplashScreen(tk.Toplevel):
    def __init__(self, master, on_close):
        super().__init__(master)
        self.on_close = on_close

        self.configure(bg="#fdfdfd")
        self.geometry("400x250")
        self.overrideredirect(True)

        self.center_window()

        title = tk.Label(self, text="NutriTrack", font=("Helvetica", 24, "bold"), bg="#fdfdfd", fg="#c90000")
        title.pack(expand=True, pady=(40, 10))

        subtitle = tk.Label(self, text="Monitoring Gizi Harian Anda", font=("Helvetica", 12), bg="#fdfdfd")
        subtitle.pack()

        self.after(2000, self.close)

    def close(self):
        self.on_close()
        self.destroy()

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"+{x}+{y}")
