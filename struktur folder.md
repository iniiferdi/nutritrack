nutritrack/
├── main.py                     # Entry point aplikasi
├── data/
│   └── food_data.json          # Data makanan dan nilai gizi
├── ui/
│   ├── splash_screen.py        # Tampilan splash screen awal
│   ├── main_window.py          # Window utama setelah splash
│   ├── food_input_form.py      # Form input makanan harian
│   ├── daily_summary_view.py   # Ringkasan konsumsi harian
│   └── weekly_summary_view.py  # Rekap dan grafik mingguan
├── core/
│   ├── food_database.py        # Fungsi akses data makanan (HashMap)
│   ├── nutrition_logic.py      # Perhitungan total gizi & evaluasi
│   └── stack_logger.py         # Stack untuk pencatatan makanan & undo
├── assets/
│   └── logo.png                # Logo/splash/icon aset
├── README.md                   # Penjelasan singkat proyek
└── requirements.txt            # (opsional) daftar dependensi
