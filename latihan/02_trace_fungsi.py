# Latihan 2 - Menelusuri Fungsi[cite: 41]
def hitung_diskon(total, persen):
    diskon = total * persen / 100
    return total - diskon

print("Total setelah diskon:", hitung_diskon(200000, 10))