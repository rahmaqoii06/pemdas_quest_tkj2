print("====================")
print("rumus bangun datar")
print("====================\n")

print("1. persegi\n")

sisi = int(input("Masukan nilai sisi: "))
luas_p = sisi * sisi
print("luas persegi adalah: ", luas_p)

print("2. persegi panjang")

panjang = int(input("Masukan nilai panjang: "))
lebar = int(input("Masukan nilai lebar: "))
luas_pp = panjang * lebar

print("luas persegi panjang adalah: ", luas_pp)

print("3.segitiga")

alas = int(input("Masukan nilai alas: "))
tinggi = int(input("Masukan nilai tinggi: "))
luas_s = alas * tinggi / 2 # or 1/2 * alas * tinggi
print("luas segitiga adalah", luas_s)