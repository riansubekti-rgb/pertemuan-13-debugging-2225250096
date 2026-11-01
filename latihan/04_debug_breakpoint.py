# Latihan 4 - Simulasi Debugger Breakpoint
def akumulasi_nilai(daftar_nilai):
    total = 0
    for n in daftar_nilai:
        total += n
    return total

if __name__ == "__main__":
    nilai_mhs = [75, 80, 85, 90]
    hasil = akumulasi_nilai(nilai_mhs)
    print("Akumulasi total:", hasil)