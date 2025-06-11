import tkinter as tk
from ui.food_input_form import FoodInputForm
from ui.daily_summary_view import DailySummaryView
from ui.weekly_summary_view import WeeklySummaryView
from ui.components.sidebar import Sidebar

class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#EBECE6")
        self.master = master

        self.setup_ui()

    def setup_ui(self):
        self.sidebar = Sidebar(self, self.show_input, self.show_daily, self.show_weekly)

        self.container = tk.Frame(self, bg="#EBECE6")
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

