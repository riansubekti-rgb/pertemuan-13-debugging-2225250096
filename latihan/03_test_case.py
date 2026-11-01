# Latihan 3 - Pengujian Test Case Batas Kelulusan
def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

print("T1 (75):", status_lulus(75))
print("T2 (60):", status_lulus(60))
print("T3 (59):", status_lulus(59))