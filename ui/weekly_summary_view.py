import tkinter as tk

class WeeklySummaryView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#fdfdfd")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Ringkasan Gizi Mingguan", font=("Helvetica", 16, "bold"), bg="#fdfdfd").pack(pady=10)

        summary = tk.Label(self, text="[Grafik atau tabel mingguan akan muncul di sini]", bg="#fdfdfd")
        summary.pack(pady=20)
