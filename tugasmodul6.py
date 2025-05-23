titik = []
for i in range(3):
    x = float((input(f"Masukkan nilai x untuk titik ke-{i+1}: ")))
    y = float((input(f"Masukkan nilai y untuk titik ke-{i+1}: ")))
    titik.append([x,y])
a = (titik[0][0]-titik[1][0])**2+(titik[0][1]-titik[1][1])**2
b = (titik[1][0]-titik[2][0])**2+(titik[1][1]-titik[2][1])**2
c = (titik[2][0]-titik[0][0])**2+(titik[2][1]-titik[0][1])**2
if a==b or b==c or a==c:
    print("Ketiga titik membentuk segitiga sama kaki")
else :
    print("Ketiga titik tidak membentuk segitiga sama kaki")