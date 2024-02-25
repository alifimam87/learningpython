#Operasi Komporasi

data = float(input("Masukkan data : "))
VarA = float(input("Masukan variabel A : "))
VarB = float(input("Masukan variabel B : "))
VarC = float(input("Masukan variabel C : "))

#Lebih besar dari (>)
print(' ========= lebih besar dari (>)=========')
hasil = data>VarA
print(data, '>', VarA, '=', hasil)
hasil = data>VarB
print(data, '>', VarB, '=', hasil)
hasil = data>VarC
print(data, '>', VarC, '=', hasil)

#Lebih kecil dari (<)
print(' ========= lebih kecil dari (<)=========')
hasil = data<VarA
print(data, '<', VarA, '=', hasil)
hasil = data<VarB
print(data, '<', VarB, '=', hasil)
hasil = data>VarC
print(data, '<', VarC, '=', hasil)


#Lebih besar sama dengan dari (>=)
print(' ========= lebih besar sama dengan dari (>=)=========')
hasil = data>=VarA
print(data, '>=', VarA, '=', hasil)
hasil = data>=VarB
print(data, '>=', VarB, '=', hasil)
hasil = data>=VarC
print(data, '>=', VarC, '=', hasil)

#Lebih kecil sama dengan dari (<=)
print(' ========= lebih kecil sama dengan dari (<=)=========')
hasil = data<=VarA
print(data, '<=', VarA, '=', hasil)
hasil = data<=VarB
print(data, '<=', VarB, '=', hasil)
hasil = data<=VarC
print(data, '<=', VarC, '=', hasil)

#Sama dengan (==)
print(' ========= sama dengan (==)=========')
hasil = data==VarA
print(data, '==', VarA, '=', hasil)
hasil = data==VarB
print(data, '==', VarB, '=', hasil)
hasil = data==VarC
print(data, '==', VarC, '=', hasil)

#Tidak Sama dengan (!=)
print(' ========= tidak sama dengan (!=)=========')
hasil = data!=VarA
print(data, '!=', VarA, '=', hasil)
hasil = data!=VarB
print(data, '!=', VarB, '=', hasil)
hasil = data!=VarC
print(data, '!=', VarC, '=', hasil)

# 'is' sebagai komparasi object identity
# kalau is untuk variabel, kalau == untuk literal

x = 5
y = 5

print('nilai x =', x, 'id', hex(id(x)))
print('nilai y =', y, 'id', hex(id(y)))

hasil = x is y
print ('x is y = ', hasil)
hasil = x is not y
print ('x is not y = ', hasil)