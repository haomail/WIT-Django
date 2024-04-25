"""
SOAL:
Buatlah program untuk menghitung harga barang setelah dikurangi diskon.
Di dalam program akan ada variable harga asli sebesar 123,000 dan diskon sebesar 23%. 
Kemudian, lakukan perhitungan sehingga didapatkan harga setelah diskon.
Simpan kode program Anda dalam sebuah file script Python sehingga program Anda dapat dijalankan di dalam komputer lokal.
Ketika dijalankan, program akan mengeluarkan hasil sebagai berikut: 
Harga asli = Rp.123.000,-
Diskon = 23%
Harga barang setelah diskon = Rp. 94.710,-
"""
harga_asli = 123000
diskon = 0.23
harga_diskon = harga_asli - (harga_asli * diskon)
print(f"Harga asli: Rp.{harga_asli},-")
print(f"Diskon: {int(diskon * 100)}%")
print(f"Harga diskon: Rp.{int(harga_diskon)},-")
