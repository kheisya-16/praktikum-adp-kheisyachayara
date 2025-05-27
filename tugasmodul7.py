def menu():
    print("Menu: ")
    print("1. Tabel perkalian modulo n")
    print("2. Mencari nilai sigma x")
    print("3. Mencari nilai n!")
    print("4. Total dan rata-rata suatu data")
    print("5. keluar")
def tabel_modulo_n():
    while True :
        n = int(input("Masukkan angka antara 1 sampai 10 : "))
        if 0<n<=10:
            break
        print("Angka tidak valid. Ulang masukkan angka")
    print("Tabel perkalian modulo", n)
    for i in range(n):
        for j in range(n):
            print((i*j)%n, end=" ")
        print()
def sigma_x():
    while True:
        batas_bawah = int(input("Masukkan batas bawah: "))
        batas_atas = int(input("Masukkan batas atas: "))
        if batas_atas >= batas_bawah:
            break
        print("Batas atas >= batas bawah")
    total = 0
    for x in range(batas_bawah, batas_atas+1):
        total += x
    print("Sigma x = ", total)
def faktorial():
    while True:
        n = int(input("Masukkan nilai n >= 0: "))
        if n>=0:
            break
        print("n harus >=0")
    hasil = 1
    for i in range(1, n+1):
        hasil *= i
    print("n! = ", hasil)
def total_rata_rata():
    while True:
        n = int(input("Masukkan banyak data : "))
        if n>0:
            break
        print("n harus lebih dari 0")
    data = []
    for i in range(n):
        nilai = float(input(f"Masukkan data ke-{i+1}: "))
        data.append(nilai)
    total = 0
    for x in data:
        total += x
    rata = total/n
    print("| Data ke- | Nilai |")
    for i in range(n):
        print(f"|     {i+1}    |  {data[i]}  |")
    print(f"Total = {total}")
    print(f"Rata-rata = {rata}")
while True:
    menu()
    pilihan = int(input("Masukkan pilihan menu (1-5): "))
    if pilihan == 1:
        tabel_modulo_n()
    elif pilihan == 2:
        sigma_x()
    elif pilihan == 3:
        faktorial()
    elif pilihan == 4:
        total_rata_rata()
    elif pilihan == 5:
        print("Selesai")
        break
    else :
        print("Pilihan tidak valid. Masukkan angka 1-5: ")

