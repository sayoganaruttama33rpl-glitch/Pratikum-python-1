# 1. Variabel dan Tipe Data
angka = 10                # int
harga = 15000.5           # float
nama = "Python"           # str
barang = ["beras", "minyak", "telur"]  # list

print("Tipe data masing-masing variabel:")
print(type(angka))
print(type(harga))
print(type(nama))
print(type(barang))

print("\n----------------------------")

# 2. List dan Manipulasi
belanja = ["beras", "minyak", "telur"]

# Menambahkan item ke list
belanja.append("gula")
belanja.append("kopi")

print("Daftar belanja:")
for item in belanja:
    print("-", item)

print("\n----------------------------")

# 3. Dictionary
harga_belanja = {
    "beras": 12000,
    "minyak": 17000,
    "telur": 24000,
    "gula": 15000,
    "kopi": 20000
}

# Hitung total harga belanja
total = sum(harga_belanja.values())

print("Harga belanjaan:")
for item, harga in harga_belanja.items():
    print(f"{item}: Rp{harga:,}")

print(f"Total belanja: Rp{total:,}")

print("\n----------------------------")

# 4. Fungsi
def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

# Contoh pemanggilan fungsi
p, l = 10, 5
luas, keliling = hitung_persegi_panjang(p, l)
print(f"Luas persegi panjang ({p}x{l}) = {luas}")
print(f"Keliling persegi panjang = {keliling}")

print("\n----------------------------")

# 5. Percabangan
usia = int(input("Masukkan usia Anda: "))

if 0 <= usia <= 13:
    kategori = "Anak"
elif 14 <= usia <= 24:
    kategori = "Remaja"
elif 25 <= usia <= 49:
    kategori = "Dewasa"
else:
    kategori = "Lansia"

print(f"Anda termasuk kategori: {kategori}")