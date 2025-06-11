import tkinter as tk

class Sidebar(tk.Frame):
    def __init__(self, master, on_input, on_daily, on_weekly):
        super().__init__(master, bg="#F9FAF4", width=260)
        self.pack(side="left", fill="y")
        self.pack_propagate(False)
        
        border_right = tk.Frame(master, bg="#E1E2DC", width=1)  # warna border dan lebar
        border_right.pack(side="left", fill="y")

        # Logo dan Judul
        tk.Label(self, text="NutriTrack", font=("Roboto", 16, "bold"),
                 bg="#F9FAF4", fg="#151513").pack(pady=(0, 28))

        # Tombol Tambah
        add_btn = tk.Button(self, text="Add new food", bg="#CDEB65", fg="#000",
                            font=("Roboto", 10, "bold"), bd=0, relief="flat",
                            activebackground="#CDEB65", padx=10, pady=6)
        add_btn.pack(fill="x", padx=24, pady=(0, 20))

        # Menu Navigasi
        self.create_nav_button("Input Makanan", on_input)
        self.create_nav_button("Ringkasan Hari Ini", on_daily)
        self.create_nav_button("Ringkasan Mingguan", on_weekly)

    def create_nav_button(self, text, command):
        btn = tk.Button(self, text=text, anchor="w", command=command, bg="#F9FAF4",
                        fg="#151513", font=("Roboto", 10),
                        relief="flat", bd=0, highlightthickness=0,
                        activebackground="#EFEFEA", padx=20, pady=8)
        btn.pack(fill="x", padx=12, pady=2)
