#latihan logika dan komparasi

#+++++++3---------10+++++++

inputUser = float(input("Masukan angka yang bernilai\nkurang dari 3 \natau\n lebih besar dari 10\n : "))

#Kurang dari 3
IsKurangDari = inputUser < 3
print('Kurang dari tiga:', IsKurangDari)

#Lebihdari 10
IsLebihDari = inputUser > 10
print('Lebih dari sepuluh:', IsLebihDari)

#Gabung
IsCorrect = IsLebihDari or IsKurangDari
print ('Angka yang anda masukkan : ', IsCorrect)


#--------3+++++++++10-------
#Irisan
inputUser = float(input("Masukan angka yang bernilai lebih dari 3 dan\n kurang dari 10\n : "))

#Lebih dari 3
LebihDari = inputUser > 3
print('Lebih dari tiga : ', LebihDari)

#Kurang dari 10
KurangDari = inputUser < 10
print('Kurang dari sepuluh', KurangDari)

#Gabung
IsCorrect = LebihDari and KurangDari
print('Anda yang anda masukkan', IsCorrect)


#----0++++++5------8+++++11-----
inputUser = float(input("Masukan nilai : dengan ketentuan : \n a. Nilai Lebih dari 0 dan kurang dari 5 \n b. Nilai lebih dari 8 dan kurang dari 11 \n : "))

fasenol = inputUser > 0
faselima = inputUser < 5
fasedelapan = inputUser > 8
fasesebelas = inputUser < 11

print("Apakah nilai lebih dari nol : ", fasenol)
print("Apakah nilai kurang dari lima : ", faselima)
print("Apakah nilai lebih dari delapan : ", fasedelapan)
print("Apakah nilai kurang dari sebelas : ", fasesebelas)

jangkauan = (fasenol and faselima) or (fasedelapan and fasesebelas)
print("Angka yang anda masukkan masuk dalam jangkauan", jangkauan)


#++++0------5++++++8-----11-----
inputUser = float(input("Masukan nilai : dengan ketentuan : \n a. Nilai kurang dari 0 dan lebih dari 5 \n b. Nilai kurang dari 8 dan lebih dari 11 \n : "))

fasenol = inputUser < 0
faselima = inputUser > 5
fasedelapan = inputUser < 8
fasesebelas = inputUser > 11

print("Apakah nilai kurang dari nol : ", fasenol)
print("Apakah nilai lebih dari lima : ", faselima)
print("Apakah nilai kurang dari delapan : ", fasedelapan)
print("Apakah nilai lebih dari sebelas : ", fasesebelas)

jangkauan = (fasenol or fasesebelas) or (faselima and fasedelapan)
print("Angka yang anda masukkan masuk dalam jangkauan", jangkauan)
