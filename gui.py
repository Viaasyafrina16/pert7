import tkinter as tk  # Mengimpor modul tkinter untuk membuat GUI
from tkinter import messagebox  # Mengimpor messagebox untuk menampilkan pesan kesalahan

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try: 
        # Mengecek setiap nilai input pada list entries
        for entry in entries:
            nilai = int(entry.get())  # Mengonversi input ke integer
            if not (0 <= nilai <= 100):  # Memastikan nilai antara 0 dan 100
                raise ValueError("Nilai harus antara 0 dan 100.")  # Menghasilkan error jika nilai di luar rentang
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")  # Menampilkan hasil prediksi jika input valid
    except ValueError as ve:
        # Menampilkan pesan error jika input tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Membuat jendela utama GUI
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Mengatur judul jendela
root.geometry("500x600")  # Mengatur ukuran jendela
root.configure(bg="#ADD8E6")  # Mengatur warna latar belakang jendela

# Membuat label judul di bagian atas
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#ADD8E6")
judul_label.pack(pady=20)  # Menambahkan jarak vertikal sekitar 20 piksel

# Membuat frame untuk menampung input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#ADD8E6")
frame_input.pack(pady=10)  # Menambahkan jarak vertikal sekitar 10 piksel

# Membuat list kosong untuk menyimpan entry input
entries = []
# Mengisi frame dengan 10 label dan input untuk nilai mata pelajaran
for i in range(10):
    # Label untuk setiap mata pelajaran
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Arial", 12), bg="#ADD8E6")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")  # Mengatur posisi dengan grid dan teks rata kanan
    # Input entry untuk nilai mata pelajaran
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)  # Mengatur posisi entry dengan grid
    entries.append(entry)  # Menyimpan entry ke dalam list entries

# Membuat tombol prediksi yang memanggil fungsi hasil_prediksi saat ditekan
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#4CAF50", fg="black")
prediksi_button.pack(pady=30)  # Menambahkan jarak vertikal sekitar 30 piksel

# Label kosong untuk menampilkan hasil prediksi setelah tombol ditekan
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="blue", bg="#ADD8E6")
hasil_label.pack(pady=20)  # Menambahkan jarak vertikal sekitar 20 piksel

# Menjalankan loop utama aplikasi GUI
root.mainloop()
