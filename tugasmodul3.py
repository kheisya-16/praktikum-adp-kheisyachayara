operasi = True
while operasi :
    print("Operasi yang tersedia : ")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")
    pilihan_operasi = int(input("Operasi nomor berapa yang ingin digunakan (1/2/3/4/5)? "))
    if pilihan_operasi :
        angka_pertama = int(input("Masukkan nilai angka pertama : "))
        angka_kedua = int(input("Masukkan nilai angka kedua : "))
    
        if pilihan_operasi == 1 :
            nama_operasi = "Penjumlahan"
            hasil = angka_pertama+angka_kedua
            print(f"Hasilnya adalah {hasil}")
        elif pilihan_operasi == 2 :
            nama_operasi = "Pengurangan"
            hasil = angka_pertama-angka_kedua
            print(f"Hasilnya adalah {hasil}")
        elif pilihan_operasi == 3 :
            nama_operasi = "Perkalian"
            hasil = angka_pertama*angka_kedua
            print(f"Hasilnya adalah {hasil}")
        elif pilihan_operasi == 4 :
            if angka_kedua == 0 :
                print("Tidak terdefinisi")
            else :
                hasil = angka_pertama/angka_kedua
                print(f"Hasilnya adalah {hasil}")
        else :
            print("Keluar")
            break
        lanjut_hitung = str(input("Apakah ingin diulang (yes/no)? "))   
        if lanjut_hitung == "no" :
            break
    else :
        print("selesai")    
    

