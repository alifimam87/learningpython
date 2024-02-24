#Celcius to Reamur, Fahrenheit, Kelvin

dataC = float(input ("Masukan suhu Celcius : "))
CtR = (4 / 5) * dataC
print("Hasil Konversi Celcius ke Reamur adalah : ", CtR)

CtF = (9 / 5) * dataC + 32
print("Hasil Konversi Celcius ke Fahrenheit adalah : ", CtF)

CtK = dataC + 273
print("Hasil Konversi Celcius ke Kelvin adalah : ", CtK)



#Kelvin to Fahrenheit
# K-> C -> F
dataK = float(input("Masukan suhu Kelvin: "))
KtoF = ((dataK - 273) * 9 / 5 ) + 32
print("Hasil Konversi Kelvin to Fahrenheit adalah : ", KtoF)

#Fahrenheit to Kelvin
# F -> C -> K
dataF = float(input("Masukkan suhu Fahrenheit: "))
FtoK = (5 / 9 * (dataF -  32)) + 273
print("Hasil Konersi Fahrenheit ke Kelvin adalah : ", FtoK)