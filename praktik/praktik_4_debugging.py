def hitung_rata_rata_awal(nilai):
    return sum(nilai) / 5  # Bug: pembagi statis 5

def status_awal(nilai):
    if nilai > 60:         # Bug: batas 60 keliru
        return "Lulus"
    return "Tidak lulus"

def nilai_tertinggi_awal(nilai):
    tertinggi = 0          # Bug: inisialisasi awal 0
    for x in nilai:
        if x < tertinggi:  # Bug: arah operator salah (<)
            tertinggi = x
    return tertinggi


def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0.0
    return sum(nilai) / len(nilai)  # Perbaikan: pembagi dinamis

def status(nilai):
    if nilai >= 60:                 # Perbaikan: operator inklusif >=
        return "Lulus"
    return "Tidak lulus"

def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None
    tertinggi = nilai[0]            # Perbaikan: inisialisasi elemen pertama
    for x in nilai[1:]:
        if x > tertinggi:           # Perbaikan: arah operator >
            tertinggi = x
    return tertinggi


if __name__ == "__main__":

    while True:
        print("Pilih Target Pengujian:")
        print("1. Rata-Rata")
        print("2. Status Kelulusan")
        print("3. Nilai Tertinggi")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()
        print("-" * 50)

        if pilihan == "1":
            # Input manual untuk Rata-rata
            raw = input("Masukkan daftar nilai (pisahkan dengan spasi, contoh: 80 60 90 70): ")
            try:
                daftar = [float(x) for x in raw.split()]
            except ValueError:
                print("❌ Error: Masukkan angka yang valid!\n")
                continue
            
            if not daftar:
                print("❌ Daftar nilai tidak boleh kosong.\n")
                continue

            expected = sum(daftar) / len(daftar)
            
            # Actual Awal & Akhir
            act_awal = hitung_rata_rata_awal(daftar)
            act_akhir = hitung_rata_rata(daftar)
            
            stat_awal = "PASS" if act_awal == expected else "FAIL"
            stat_akhir = "PASS" if act_akhir == expected else "FAIL"

            print(f"\n[HASIL UJI RATA-RATA]")
            print(f"Input         : {daftar}")
            print(f"Expected      : {expected:.1f}")
            print(f"Actual Awal   : {act_awal:.1f}  -> Status: {stat_awal}")
            print(f"Actual Akhir  : {act_akhir:.1f}  -> Status: {stat_akhir}\n")

        elif pilihan == "2":
            # Input manual untuk Status Kelulusan
            raw = input("Masukkan nilai untuk uji status (contoh: 60 atau 59): ")
            try:
                val = float(raw)
            except ValueError:
                print("❌ Error: Masukkan angka yang valid!\n")
                continue

            expected = "Lulus" if val >= 60 else "Tidak lulus"
            
            act_awal = status_awal(val)
            act_akhir = status(val)
            
            stat_awal = "PASS" if act_awal == expected else "FAIL"
            stat_akhir = "PASS" if act_akhir == expected else "FAIL"

            print(f"\n[HASIL UJI STATUS KELULUSAN]")
            print(f"Input         : {val}")
            print(f"Expected      : {expected}")
            print(f"Actual Awal   : {act_awal}  -> Status: {stat_awal}")
            print(f"Actual Akhir  : {act_akhir}  -> Status: {stat_akhir}\n")

        elif pilihan == "3":
            # Input manual untuk Nilai Tertinggi
            raw = input("Masukkan daftar nilai (pisahkan dengan spasi, contoh: 80 60 90 70): ")
            try:
                daftar = [float(x) for x in raw.split()]
            except ValueError:
                print("❌ Error: Masukkan angka yang valid!\n")
                continue
            
            if not daftar:
                print("❌ Daftar nilai tidak boleh kosong.\n")
                continue

            expected = max(daftar)
            
            act_awal = nilai_tertinggi_awal(daftar)
            act_akhir = nilai_tertinggi(daftar)
            
            stat_awal = "PASS" if act_awal == expected else "FAIL"
            stat_akhir = "PASS" if act_akhir == expected else "FAIL"

            print(f"\n[HASIL UJI NILAI TERTINGGI]")
            print(f"Input         : {daftar}")
            print(f"Expected      : {expected}")
            print(f"Actual Awal   : {act_awal}  -> Status: {stat_awal}")
            print(f"Actual Akhir  : {act_akhir}  -> Status: {stat_akhir}\n")

        elif pilihan == "4":
            print("Keluar dari program!")
            break
        else:
            print("❌ Pilihan tidak valid. Silakan masukkan angka 1 sampai 4.\n")