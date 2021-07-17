def tambah (X,Y):
    return X + Y

def kurang (x,y):
    return x - y

def kali (x,y):
    return x*y

def bagi (x,y):
    return x/y

print ('Menu Operasi :\n1. penjumlahan \n2. pengurangan \n3. perkalian \n4. pembagian')

operasi = int(input('silahkan masukan operasi pilihan anda (dalam angka):'))
x = int (input('masukan angka pertama: '))
y = int (input ('masukan angka kedua:'))

if operasi == 1:
    print (tambah(x,y))
elif operasi == 2:
    print (kurang (x,y))
elif operasi == 3:
    print (kali (x,y))
elif operasi == 4:
    print (bagi(x,y))