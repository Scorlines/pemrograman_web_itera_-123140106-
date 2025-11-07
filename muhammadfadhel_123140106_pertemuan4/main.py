"""
Program Pengelolaan Data Nilai Mahasiswa - Versi Simple
========================================================
Author: Praktikum Pengweb
Date: 7 November 2025
"""

# Data mahasiswa (list kosong, akan diisi saat input)
data_mahasiswa = []

# Fungsi hitung nilai akhir (30% UTS + 40% UAS + 30% Tugas)
def hitung_nilai_akhir(uts, uas, tugas):
    return round((uts * 0.3) + (uas * 0.4) + (tugas * 0.3), 2)

# Fungsi tentukan grade
def tentukan_grade(nilai):
    if nilai >= 80:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"

# Fungsi tampilkan tabel
def tampilkan_tabel(data):
    if not data:
        print("\nBelum ada data mahasiswa. Silakan tambah data terlebih dahulu.")
        return
    
    print("\n" + "="*90)
    print("DATA NILAI MAHASISWA".center(90))
    print("="*90)
    print(f"{'No':<5}{'Nama':<20}{'NIM':<10}{'UTS':<8}{'UAS':<8}{'Tugas':<8}{'Akhir':<10}{'Grade'}")
    print("-"*90)
    
    for i, mhs in enumerate(data, 1):
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        grade = tentukan_grade(nilai_akhir)
        print(f"{i:<5}{mhs['nama']:<20}{mhs['nim']:<10}{mhs['nilai_uts']:<8}{mhs['nilai_uas']:<8}{mhs['nilai_tugas']:<8}{nilai_akhir:<10}{grade}")
    
    print("="*90)

# Fungsi cari nilai tertinggi
def cari_tertinggi(data):
    if not data:
        return None, None
    
    tertinggi = None
    nilai_max = 0
    
    for mhs in data:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        if nilai_akhir > nilai_max:
            nilai_max = nilai_akhir
            tertinggi = mhs
    
    return tertinggi, nilai_max

# Fungsi cari nilai terendah
def cari_terendah(data):
    if not data:
        return None, None
    
    terendah = None
    nilai_min = 999
    
    for mhs in data:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        if nilai_akhir < nilai_min:
            nilai_min = nilai_akhir
            terendah = mhs
    
    return terendah, nilai_min

# Fungsi tambah mahasiswa baru
def tambah_mahasiswa():
    print("\n=== TAMBAH MAHASISWA BARU ===")
    nama = input("Nama: ")
    nim = input("NIM: ")
    
    try:
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        tugas = float(input("Nilai Tugas: "))
        
        mahasiswa_baru = {
            "nama": nama,
            "nim": nim,
            "nilai_uts": uts,
            "nilai_uas": uas,
            "nilai_tugas": tugas
        }
        
        data_mahasiswa.append(mahasiswa_baru)
        print("\nData berhasil ditambahkan!")
        
    except ValueError:
        print("Error: Nilai harus berupa angka!")

# Fungsi filter berdasarkan grade
def filter_grade(data, grade_cari):
    if not data:
        print("\nBelum ada data mahasiswa.")
        return
    
    print(f"\n=== MAHASISWA DENGAN GRADE {grade_cari} ===")
    hasil = []
    
    for mhs in data:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        grade = tentukan_grade(nilai_akhir)
        
        if grade == grade_cari:
            hasil.append(mhs)
    
    if hasil:
        tampilkan_tabel(hasil)
    else:
        print(f"Tidak ada mahasiswa dengan grade {grade_cari}")

# Fungsi hitung rata-rata kelas
def hitung_rata_rata(data):
    if not data:
        return None
    
    total = 0
    for mhs in data:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        total += nilai_akhir
    
    return round(total / len(data), 2)

# Program utama
def main():
    while True:
        print("\n" + "="*50)
        print("PROGRAM PENGELOLAAN NILAI MAHASISWA")
        print("="*50)
        print("1. Tampilkan Semua Data")
        print("2. Tambah Mahasiswa Baru")
        print("3. Cari Nilai Tertinggi")
        print("4. Cari Nilai Terendah")
        print("5. Filter Berdasarkan Grade")
        print("6. Hitung Rata-rata Kelas")
        print("7. Keluar")
        print("="*50)
        
        pilihan = input("Pilih menu (1-7): ")
        
        if pilihan == "1":
            tampilkan_tabel(data_mahasiswa)
            
        elif pilihan == "2":
            tambah_mahasiswa()
            
        elif pilihan == "3":
            mhs, nilai = cari_tertinggi(data_mahasiswa)
            if mhs:
                print(f"\nNilai Tertinggi: {mhs['nama']} ({mhs['nim']}) = {nilai}")
            else:
                print("\nBelum ada data mahasiswa.")
            
        elif pilihan == "4":
            mhs, nilai = cari_terendah(data_mahasiswa)
            if mhs:
                print(f"\nNilai Terendah: {mhs['nama']} ({mhs['nim']}) = {nilai}")
            else:
                print("\nBelum ada data mahasiswa.")
            
        elif pilihan == "5":
            grade = input("Masukkan grade (A/B/C/D/E): ").upper()
            filter_grade(data_mahasiswa, grade)
            
        elif pilihan == "6":
            rata = hitung_rata_rata(data_mahasiswa)
            if rata:
                print(f"\nRata-rata Nilai Kelas: {rata}")
                print(f"Grade Rata-rata: {tentukan_grade(rata)}")
            else:
                print("\nBelum ada data mahasiswa.")
            
        elif pilihan == "7":
            print("\nTerima kasih!")
            break
            
        else:
            print("\nPilihan tidak valid!")

if __name__ == "__main__":
    main()
