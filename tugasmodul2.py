print("Daftar paket makanan")
print("1. Ayam - Rp20.000")
print("2. Sapi - Rp35.000")
print("3. Cumi-cumi - Rp45.000")
pilihan_paket = int(input("Paket nomor berapa yang akan dipesan (1/2/3)?"))
if pilihan_paket == 1 :
    nama_paket = "Ayam"
    harga_paket = 20000
elif pilihan_paket == 2 :
    nama_paket = "Sapi"
    harga_paket = 35000
elif pilihan_paket == 3 :
    nama_paket = "Cumi-cumi"
    harga_paket = 45000
else :
    print("Pilihan paket makanan tidak valid")
jarak = float(input("Berapa jarak rumah ke restoran? "))
if jarak<1 :
    ongkir = 0
elif 1<=jarak<=3 :
    ongkir = 7000
else :
    ongkir = 15000
biaya_total = harga_paket+ongkir
print(f"Pilihan paket makanan yang dipesan adalah {nama_paket}")
print(f"Harga paket makanan yang dipesan adalah {harga_paket}")
print(f"Ongkir yang perlu dibayar adalah {ongkir}")
print(f"Biaya total yang perlu dibayar adalah Rp{biaya_total}")