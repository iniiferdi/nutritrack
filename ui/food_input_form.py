import tkinter as tk
from tkinter import ttk, messagebox

class FoodHashMap:
    def __init__(self):
        self.food_data = {
            "Nasi Putih": {"kalori": 130, "protein": 2.4, "lemak": 0.2, "karbohidrat": 28},
            "Ayam Goreng": {"kalori": 250, "protein": 20, "lemak": 15, "karbohidrat": 0},
            "Sayur Bayam": {"kalori": 40, "protein": 3, "lemak": 0.5, "karbohidrat": 5}
        }

    def get_food_list(self):
        return list(self.food_data.keys())

    def get_nutrition(self, food_name):
        return self.food_data.get(food_name, None)

class FoodInputForm(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#F9FAF4")
        self.food_map = FoodHashMap()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Input Makanan yang Dikonsumsi", font=("Helvetica", 16, "bold"), bg="#fdfdfd").pack(pady=10)

        self.selected_food = tk.StringVar()
        food_options = self.food_map.get_food_list()
        self.food_dropdown = ttk.Combobox(self, textvariable=self.selected_food, values=food_options, state="readonly", width=30)
        self.food_dropdown.pack(pady=5)

        tk.Label(self, text="Jumlah (gram/ml):", bg="#fdfdfd").pack()
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(pady=5)

        submit_btn = tk.Button(self, text="Tambahkan", command=self.submit_food, bg="#c90000", fg="white")
        submit_btn.pack(pady=10)

    def submit_food(self):
        food = self.selected_food.get()
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Masukkan jumlah dalam angka.")
            return

        if food:
            nutrition = self.food_map.get_nutrition(food)
            if nutrition:
                print(f"Makanan: {food}, Jumlah: {amount}, Gizi/100g: {nutrition}")
                messagebox.showinfo("Berhasil", f"{food} telah ditambahkan.")
                self.amount_entry.delete(0, 'end')
        else:
            messagebox.showwarning("Peringatan", "Silakan pilih makanan.")
