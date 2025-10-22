# ======================================
# 📘 Belajar Python Dasar + Tipe Data
# ======================================
# 🔹 Peraturan Umum Python:
# 1. Baris dieksekusi dari atas ke bawah.
# 2. Indentasi (spasi di awal baris) wajib untuk blok kode (biasanya 4 spasi).
# 3. Huruf besar & kecil dianggap berbeda (case-sensitive).
# 4. Komentar dimulai dengan tanda (#).
# 5. Variabel dibuat langsung tanpa deklarasi tipe (dinamis).
# 6. Gunakan tanda kutip (' atau ") untuk teks (string).
# 7. Gunakan titik dua (:) setelah if, for, while, def, class, dll.
# 8. Simpan file Python dengan ekstensi .py
# 9. Hindari nama variabel yang sama dengan kata kunci Python (seperti if, for, class).

# ======================================
# 🔹 Peraturan Tipe Data Python:
# 1. Python mengenali tipe data secara otomatis (dynamic typing).
# 2. Gunakan fungsi type() untuk melihat tipe datanya.
# 3. Konversi tipe bisa dilakukan dengan int(), float(), str(), bool(), list(), dsb.
# 4. Nilai kosong ditulis dengan None (bukan null).
# 5. List, Tuple, Set, dan Dictionary punya aturan sendiri.
# 6. Semua tipe data adalah objek di Python.

# ======================================
# 🔹 Contoh Tipe Data Dasar
# ======================================

# String (teks)
nama = "Zaqi"
print("Nama:", nama, "| Tipe:", type(nama))  # Output: <class 'str'>

# Integer (bilangan bulat)
umur = 17
print("Umur:", umur, "| Tipe:", type(umur))  # Output: <class 'int'>

# Float (bilangan desimal)
tinggi = 1.75
print("Tinggi:", tinggi, "| Tipe:", type(tinggi))  # Output: <class 'float'>

# Boolean (True/False)
pelajar = True
print("Pelajar:", pelajar, "| Tipe:", type(pelajar))  # Output: <class 'bool'>

# None (kosong / tidak bernilai)
nilai = None
print("Nilai:", nilai, "| Tipe:", type(nilai))  # Output: <class 'NoneType'>

# ======================================
# 🔹 Tipe Data Koleksi
# ======================================

# List → bisa diubah (mutable), urutannya terjaga
buah = ["apel", "mangga", "pisang"]
print("List:", buah, "| Tipe:", type(buah))
buah.append("jeruk")  # menambah elemen baru
print("Setelah ditambah:", buah)

# Tuple → tidak bisa diubah (immutable)
warna = ("merah", "hijau", "biru")
print("Tuple:", warna, "| Tipe:", type(warna))

# Set → tidak berurutan, tidak ada duplikat
angka = {1, 2, 3, 3, 2}
print("Set:", angka, "| Tipe:", type(angka))

# Dictionary → pasangan key : value
data = {"nama": "Zaqi", "umur": 17, "kota": "Jakarta"}
print("Dictionary:", data, "| Tipe:", type(data))
print("Akses nama:", data["nama"])

# ======================================
# 🔹 Konversi Tipe Data
# ======================================
x = 5
y = float(x)  # ubah int ke float
z = str(x)    # ubah int ke string
print("x:", x, "| y:", y, "| z:", z)
print("Tipe y:", type(y), "| Tipe z:", type(z))

# ======================================
# 🔹 Ringkasan Singkat
# ======================================
# str   → teks
# int   → bilangan bulat
# float → bilangan desimal
# bool  → logika True/False
# list  → kumpulan data bisa diubah
# tuple → kumpulan data tidak bisa diubah
# set   → kumpulan data unik
# dict  → data pasangan key:value
# None  → tidak ada nilai

# ======================================
# 📘 Akhir Program
# ======================================
print("\nSelesai! Kamu sudah belajar tipe data dasar di Python 😊")
