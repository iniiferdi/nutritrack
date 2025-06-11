import tkinter as tk

class DailySummaryView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#fdfdfd")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Ringkasan Gizi Hari Ini", font=("Helvetica", 16, "bold"), bg="#fdfdfd").pack(pady=10)

        summary = tk.Label(self, text="[Data gizi harian akan ditampilkan di sini]", bg="#fdfdfd")
        summary.pack(pady=20)
