# Kasus 3: Penanganan Exception File I/O dan Validasi Data
import os

def baca_nilai_file(nama_file):
    try:
        if not os.path.exists(nama_file):
            raise FileNotFoundError(f"File {nama_file} tidak ditemukan.")
        with open(nama_file, "r") as f:
            isi = f.readlines()
        return [int(x.strip()) for x in isi if x.strip().isdigit()]
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return []
    except ValueError:
        print("Error: Terdapat data non-integer di dalam file.")
        return []

if __name__ == "__main__":
    hasil = baca_nilai_file("data_kosong.txt")
    print("Data terbaca:", hasil)