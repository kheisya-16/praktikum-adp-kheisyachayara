n = int(input("Masukkan jumlah baris (minimal 4) : "))
while n<4 :
    print("Jumlah baris minimal 4!")
    n = int(input("Masukkan jumlah baris (minimal 4) : "))
boom = 0
for i in range(n) :
    for j in range(n):
        if n%2!=0 and i==n//2 and j==n//2 :
                print("HORE", end=" "*3)
        elif i==j :
                print("1", end=" "*6)
        elif i+j==n-1 :
             print("2", end=" "*6)
        else :
            print("BOOM", end=" "*3)
            boom +=1
    print()
print(f"Total boom yang muncul adalah {boom}")
