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

def hitung_total(benda):
    harga_per_barang = 0
    total_harga = 0
    for i in benda:
        harga_per_barang = i['jumlah'] * i['harga']
        total_harga = total_harga + harga_per_barang
    return total_harga
print(hitung_total(barang))