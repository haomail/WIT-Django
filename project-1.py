"""
Buatlah fungsi sederhana yang dapat menghitung subtotal dari pembelanjaan seorang customer. Fungsi tersebut akan menerima parameter berupa list of dictionary dengan struktur dictionary sebagai berikut:
nama: string
jumlah: int
harga: int
Fungsi akan mengembalikan nilai berupa total harga yang harus dibayarkan oleh seorang customer.
"""
belanja = [
    {
        'nama': "Kemeja",
        'jumlah': 2,
        'harga': 100000
    },
    {
        'nama': "Blouse",
        'jumlah': 3,
        'harga': 150000
    },
    {
        'nama': "Celana kain",
        'jumlah': 2,
        'harga': 120000
    }
]

def hitung_total(barang):
    harga_per_barang = 0
    total_harga = 0
    for i in barang:
        harga_per_barang = i['jumlah'] * i['harga']
        total_harga = total_harga + harga_per_barang
    return total_harga
print(f"Total harga yang harus dibayarkan: Rp.{hitung_total(belanja)},-")