# Kasus 2: Bug Perhitungan Rata-rata
def rata_rata(data):
    total = sum(data)
    return total / 5  # Bug: pembagi di-hardcode dengan angka 5[cite: 41]

if __name__ == "__main__":
    print("Rata-rata [80, 90, 70]:", rata_rata([80, 90, 70]))