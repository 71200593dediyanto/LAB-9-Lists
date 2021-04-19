# Dedi Yanto
# 71200593
# Universitas Kristen Duta Wacana
# Prodi Teknik Informatika
# List

'''
Buatlah sebuah program yang dapat menampilkan list bilang ganjil dan
bilangan genap dari angka-angka yang telah diinputkan oleh user, 
banyaknya data yang akan di inputkan ditentukan oleh user. Output 
dari bilangan ganjil harus dari yang terkecil, dan bilangan genap 
harus dari yang terbesar. Output dari program tidak boleh mengandung 
bilangan yang sama.

'''

'''
Input:
input 1 : 4
data 1 : ...
data 2 : ...
data 3 : ...
data 4 : ...

Proses:
6
data ke 1 = 5
data ke 2 = 2
.... (sampai)
data ke 6 = 3
kumpulan data = [5,2,...,6]

a = [1,2,3,2]
1/2 = 1
2/2 = 0
3/2 = 1
2/2 = 0
Output:

bilangan ganjil = [1,3]
bilangan genap = [2]
'''

# Source Code
banyak = int(input('Masukkan banyak data : '))
lst = []
ganjil = []
genap = []

for i in range(banyak):
    data = int(input('Masukkan data '+'ke-'+str(i+1)+': '))
    lst.append(data)

for i in lst:
    if i%2 != 0:
        if ganjil.count(i) == 1:
            continue
        else:
            ganjil.append(i)
    elif i == 0:
        continue
    else:
        if genap.count(i) == 1:
            continue
        else:
            genap.append(i)

ganjil.sort()
genap.sort()
genap.reverse()

print('List bilangan ganjil dari yang terkecil adalah',ganjil)
print('List bilangan genap dari yang terbesar adalah',genap)
