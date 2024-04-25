"""
Buatlah fungsi sederhana yang dapat menghitung subtotal dari pembelanjaan seorang customer. Fungsi tersebut akan menerima parameter berupa list of dictionary dengan struktur dictionary sebagai berikut:
nama: string
jumlah: int
harga: int

Fungsi akan mengembalikan nilai berupa total harga yang harus dibayarkan oleh seorang customer.

"""
barang = [
    {
        'nama': "pena",
        'jumlah': 5,
        'harga': 7000
    },
    {
        'nama': "pensil",
        'jumlah': 8,
        'harga': 2000
    }
]
"""
def total_harga(jumlah, harga):
    total = barang['jumlah']
    harga = barang['harga']
    total_harga = 0
    for total in barang:
        print(total)
        for harga in barang:
            print(harga)
            total_harga = total * harga
"""

for i in barang:
    total_harga = i['jumlah'] * i['harga']
print("Total harga masing-masing barang: %d" % (total_harga))