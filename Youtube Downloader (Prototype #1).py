import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pytube import YouTube

# Fungsi untuk memperbarui opsi resolusi setelah URL dimasukkan
def update_resolutions():
    url = url_entry.get()  # Mendapatkan URL dari input pengguna
    try:
        yt = YouTube(url)
        resolutions = [stream.resolution for stream in yt.streams.filter(progressive=True)]
        resolution_menu['values'] = list(set(resolutions))  # Mengisi opsi resolusi
        if resolutions:
            resolution_menu.current(0)  # Set default ke resolusi pertama
        messagebox.showinfo("Sukses", "Resolusi berhasil dimuat.")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal mendapatkan resolusi: {str(e)}")

# Fungsi untuk mendownload video
def download_video():
    url = url_entry.get()  # Mendapatkan URL dari input pengguna
    folder = folder_entry.get() or "C:/Youtube Download"  # Mendapatkan folder, default ke "C:/Youtube Download"
    resolution = resolution_menu.get()  # Mendapatkan resolusi yang dipilih

    # Jika folder default tidak ada, buat folder
    if not os.path.exists(folder):
        os.makedirs(folder)

    try:
        yt = YouTube(url)
        stream = yt.streams.filter(res=resolution, progressive=True).first()  # Filter berdasarkan resolusi
        stream.download(folder)  # Mendownload ke folder yang ditentukan
        messagebox.showinfo("Sukses", f"Video berhasil diunduh di: {folder}")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal mengunduh video: {str(e)}")

# Fungsi untuk memilih folder tujuan
def select_folder():
    folder = filedialog.askdirectory()  # Dialog untuk memilih folder
    if folder:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder)

# Membuat window utama
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("400x350")

# Label dan entry untuk URL video YouTube
url_label = tk.Label(root, text="Link YouTube:")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Label dan entry untuk folder tujuan
folder_label = tk.Label(root, text="Folder tujuan:")
folder_label.pack(pady=10)
folder_entry = tk.Entry(root, width=50)
folder_entry.pack()

# Tombol untuk memilih folder tujuan
select_folder_btn = tk.Button(root, text="Pilih Folder", command=select_folder)
select_folder_btn.pack(pady=5)

# Menambahkan jarak
spacer = tk.Label(root, text="", font=("Helvetica", 8, "italic"), fg="#A9A9A9")  # Spacer untuk memberi jarak
spacer.pack(pady=0)  # Memberi jarak vertikal tambahan

# Label dan dropdown menu untuk memilih resolusi
resolution_label = tk.Label(root, text="Pilih Resolusi:")
resolution_label.pack(pady=5)
resolution_menu = ttk.Combobox(root, state="readonly", width=30)
resolution_menu.pack()

# Tombol untuk memuat resolusi
load_resolutions_btn = tk.Button(root, text="Muat Resolusi", command=update_resolutions)
load_resolutions_btn.pack(pady=5)

# Menambahkan jarak
spacer = tk.Label(root, text="")

# Menambahkan jarak
spacer = tk.Label(root, text="Made by: Mycticount Xeta Ahlovely", font=("Helvetica", 8, "italic"), fg="#A9A9A9")  # Spacer untuk memberi jarak
spacer.pack(pady=1)  # Memberi jarak vertikal tambahan

# Tombol untuk mendownload video
download_btn = tk.Button(root, text="Download Video", command=download_video)
download_btn.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()
