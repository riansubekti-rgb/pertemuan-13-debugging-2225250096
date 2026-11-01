# Pertemuan 13 Debugging dan Testing
Nama: Rian Subekti  
NIM: 2225250096  
Kelas: 3F  

## Kasus
Praktik 4 menginvestigasi program pengolahan nilai mahasiswa yang memiliki beberapa *logical error* pada fungsi perhitungan rata-rata, penentuan status kelulusan batas (60), serta pencarian nilai tertinggi.

## Test Case
| ID | Target | Input | Expected | Actual Awal | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| T1 | rata-rata | `[80, 60, 90, 70]` | `75.0` | `60.0` (dibagi 5) | **FAIL** |
| T2 | rata-rata | `[100, 80]` | `90.0` | `36.0` (dibagi 5) | **FAIL** |
| T3 | status | `60` | `Lulus` | `Tidak lulus` | **FAIL** |
| T4 | status | `59` | `Tidak lulus` | `Tidak lulus` | **PASS** |
| T5 | tertinggi | `[80, 60, 90, 70]` | `90` | `0` (salah inisialisasi) | **FAIL** |

## Bug Report
1. **B01 (Fungsi `hitung_rata_rata`)**
   - **Gejala:** Nilai rata-rata salah ketika panjang list tidak sama dengan 5.
   - **Lokasi:** `praktik/praktik_4_debugging.py` pada baris `sum(nilai) / 5`.
   - **Akar Penyebab:** Pembagi di-*hardcode* dengan angka statis `5` alih-alih menggunakan jumlah elemen list aktual `len(nilai)`.
   - **Perbaikan:** Mengubah pembagi menjadi `len(nilai)` serta menambahkan validasi list kosong.

2. **B02 (Fungsi `status`)**
   - **Gejala:** Mahasiswa dengan nilai tepat `60` dinyatakan "Tidak lulus".
   - **Lokasi:** `praktik/praktik_4_debugging.py` pada baris `if nilai > 60:`.
   - **Akar Penyebab:** Penggunaan operator perbandingannya kurang inklusif (`>` alih-alih `>=`).
   - **Perbaikan:** Mengubah operator perbandingan menjadi `>=`.

3. **B03 (Fungsi `nilai_tertinggi`)**
   - **Gejala:** Selalu mengembalikan angka `0`.
   - **Lokasi:** `praktik/praktik_4_debugging.py` pada fungsi `nilai_tertinggi()`.
   - **Akar Penyebab:** Inisialisasi awal variabel `tertinggi = 0` dan arah operator pembanding `x < tertinggi` keliru.
   - **Perbaikan:** Menginisialisasi `tertinggi = nilai[0]` dan mengubah operator menjadi `x > tertinggi`.

## Retest
| ID | Target | Input | Expected | Actual Akhir | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| T1 | rata-rata | `[80, 60, 90, 70]` | `75.0` | `75.0` | **PASS** |
| T2 | rata-rata | `[100, 80]` | `90.0` | `90.0` | **PASS** |
| T3 | status | `60` | `Lulus` | `Lulus` | **PASS** |
| T4 | status | `59` | `Tidak lulus` | `Tidak lulus` | **PASS** |
| T5 | tertinggi | `[80, 60, 90, 70]` | `90` | `90` | **PASS** |

## Cara Menjalankan
python3 praktik/praktik_4_debugging.py

## Refleksi 
Teknik debugging yang paling membantu bagi saya adalah **pengujian menggunakan *test case* terstruktur (T1–T5) dan membandingkan *Expected Result* dengan *Actual Result***. 

Alasannya karena dengan mendefinisikan *test case* terutama pengujian pada nilai batas (seperti angka 60 untuk status kelulusan) kita bisa langsung melihat celah kesalahan logika secara spesifik. Hal ini membuat proses pelacakan akar masalah (seperti pembagi statis atau arah operator perbandingan) menjadi jauh lebih cepat dan terarah dibandingkan harus menebak-nebak letak error di dalam baris kode.

## Sumber
Bahan_Ajar_Pertemuan_13_Debugging_Tracing_Testing_VSCode_GitHub