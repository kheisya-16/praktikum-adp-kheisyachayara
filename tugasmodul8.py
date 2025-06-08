praktikan = {}
with open('data_praktikan.txt','r') as file:
    for line in file:
        nim, nama, pretest, postest, tugas = line.strip().split(',')
        praktikan[nim]= {'nama':nama,
                         'pretest': int(pretest),
                         'postest': int(postest),
                         'tugas': int(tugas)
                         }
with open('data_nilai_akhir.txt','w') as file:
    file.write('NIM, Nama, Pretest, Postest, Tugas, Total nilai\n')
    for nim,data in praktikan.items():
        nilai_akhir = 0.35*data['pretest']+0.35*data['postest']+0.3*data['tugas']
        praktikan[nim]['nilai akhir']= nilai_akhir
        file.write(f"{nim},{data['nama']},{data['pretest']},{data['postest']},{data['tugas']},{nilai_akhir:.2f}\n")
nilaiakhir =[data['nilai akhir']for data in praktikan.values()]
maks = max(nilaiakhir)
min = min(nilaiakhir)
for nim,data in praktikan.items():
    if data['nilai akhir']==maks:
        tertinggi = (nim,data['nama'],data['nilai akhir'])
    if data['nilai akhir']==min:
        terendah = (nim,data['nama'],data['nilai akhir'])
rata_rata = sum(nilaiakhir)/len(nilaiakhir)
bawah_ratarata = 0
for x in nilaiakhir:
    if x<rata_rata:
        bawah_ratarata +=1
print(f"Nilai tertinggi : {tertinggi}")
print(f"Nilai terendah : {terendah}")
print(f"Rata-rata nilai : {rata_rata:.2f}")
print(f"Banyak yang di bawah rata-rata : {bawah_ratarata}")