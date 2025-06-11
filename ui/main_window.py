# ui/main_window.py

import tkinter as tk
from ui.food_input_form import FoodInputForm
from ui.daily_summary_view import DailySummaryView
from ui.weekly_summary_view import WeeklySummaryView

class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#fdfdfd")
        self.master = master

        self.setup_ui()

    def setup_ui(self):
        sidebar = tk.Frame(self, bg="#c90000", width=200)
        sidebar.pack(side="left", fill="y")

        tk.Label(sidebar, text="NutriTrack", font=("Helvetica", 16, "bold"), bg="#c90000", fg="white").pack(pady=20)

        btn_input = tk.Button(sidebar, text="Input Makanan", command=self.show_input, bg="white")
        btn_input.pack(fill="x", padx=10, pady=5)

        btn_daily = tk.Button(sidebar, text="Ringkasan Hari Ini", command=self.show_daily, bg="white")
        btn_daily.pack(fill="x", padx=10, pady=5)

        btn_weekly = tk.Button(sidebar, text="Ringkasan Mingguan", command=self.show_weekly, bg="white")
        btn_weekly.pack(fill="x", padx=10, pady=5)

        # Kontainer Utama
        self.container = tk.Frame(self, bg="#fdfdfd")
        self.container.pack(side="right", fill="both", expand=True)

        self.active_frame = None
        self.show_input()

    def switch_frame(self, new_frame_class):
        if self.active_frame:
            self.active_frame.destroy()
        self.active_frame = new_frame_class(self.container)
        self.active_frame.pack(fill="both", expand=True)

    def show_input(self):
        self.switch_frame(FoodInputForm)

    def show_daily(self):
        self.switch_frame(DailySummaryView)

    def show_weekly(self):
        self.switch_frame(WeeklySummaryView)
