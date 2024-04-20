#input
pembeli=input("input Nama Pembeli : Mikael Sena")
no_hp=input("input No. Handphone: 08123456789")
Jurusan=input("input Jurusan [SBY/BL/LMP]:")
#proses
if Jurusan=="SBY":
    namajurusan="Surabaya"
    harga=300000
elif Jurusan=="BL":
    namajurusan="Bali"
    harga=350000
else :
    namajurusan="Lampung"
    harga=5000000

#input Jumlah Beli
jumlah=int(input("Masukan Jumlah Beli: "))

#Proses Potongan
if jumlah>=3 :
    potongan=(jumlah*harga)*0.1
    total=(jumlah*harga)-potongan
else : 
    potongan=0
    total=(jumlah*harga)-potongan
#Cetak Hasil
print("_________________________________________")
print("         PENJUALAN TIKET BUS")
print("               XYZ")
print("_________________________________________")
print("Nama Pembeli : "+str(pembeli))
print("No. Handphone : "+str(no_hp))
print("Kode Jurusan yang dipilih :"+str(Jurusan))
print("Harga : ",+(harga))
print("Jumlah Beli : ",+(jumlah))
print("_________________________________________")
print("potongan yang didapat : ",+(potongan))
print("Total Bayar : ",+(total))
ubay=int(input("Masukkan Uang Bayar : "))
uangkembali=ubay-total
print("Uang Kembali : ",+uangkembali)