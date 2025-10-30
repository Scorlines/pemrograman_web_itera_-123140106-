
# Personal Dashboard - To Do List

**Nama** : Muhammad Fadhel  
**NIM**  : 123140106  
**Mata Kuliah**: Pemrograman Web  
**Pertemuan**: 2  

---

## Deskripsi Singkat
Aplikasi **Personal Dashboard** sederhana berbentuk *To Do List* yang memungkinkan pengguna menambah, mengedit, menandai selesai, dan menghapus tugas.  
Semua data tersimpan secara lokal menggunakan **localStorage**, sehingga tidak hilang ketika halaman direfresh.

File utama:
- `index.html` — struktur halaman utama  
- `script.js` — logika dan interaksi aplikasi  
- `style.css` — desain dan tampilan antarmuka

---

## Cara Menjalankan
1. Clone repository:
   ```bash
   git clone https://github.com/<username>/pemrograman_web_itera_123140106.git
   ```
2. Buka folder:
   ```bash
   cd muhammadfadhel_123140106_pertemuan2
   ```
3. Jalankan aplikasi dengan membuka `index.html` di browser (cukup klik dua kali).

> Tidak perlu server, karena aplikasi berjalan sepenuhnya di sisi klien (client-side).

---

## Fitur Aplikasi
- Menambah tugas baru  
- Mengedit tugas  
- Menghapus tugas  
- Menandai tugas selesai  
- Menyimpan dan memuat tugas dari **localStorage**  
- Loading data secara asinkron (simulasi `async/await`)

---

## Screenshot
> Tambahkan tangkapan layar aplikasi kamu di folder `screenshots/`

Contoh:
- `screenshots/main.png` – tampilan utama aplikasi  
- `screenshots/list.png` – contoh daftar tugas setelah ditambahkan

---

## Implementasi Fitur ES6+
| Fitur | Implementasi |
|-------|---------------|
| **let** dan **const** | Digunakan untuk deklarasi variabel dan konstanta |
| **Arrow Functions** | ≥ 3 fungsi menggunakan `()=>{}` seperti `renderTasks`, `createTaskElement`, `addTask` |
| **Template Literals** | Digunakan untuk menampilkan daftar tugas dengan sintaks `` `...${task}...` `` |
| **Async/Await** | Digunakan dalam fungsi `getTasksAsync()` untuk simulasi pemuatan data asinkron |
| **Classes** | Menggunakan `class Task` dan `class TaskManager` untuk struktur dan manajemen data |

---

## Struktur Folder
```
pemrograman_web_itera_123140106/
├─ muhammadfadhel_123140106_pertemuan4/
│  ├─ index.html
│  ├─ script.js
│  ├─ style.css
│  ├─ README.md
│  └─ screenshots/
│     ├─ main.png
│     └─ list.png
```


## Saran Pengembangan (Opsional)
- Ganti `prompt()` edit dengan input langsung di dalam elemen list (inline edit).  
- Tambahkan animasi transisi saat tambah/hapus tugas.  
- Buat filter “Semua / Aktif / Selesai”.  
- Tambahkan tema gelap (*dark mode*) dengan toggle dan simpan di `localStorage`.  

---

## Commit & Pengumpulan
- **Nama repository:** `pemrograman_web_itera_123140106`  
- **Folder pertemuan:** `muhammadfadhel_123140106_pertemuan4`  
- **Contoh commit message:**  
  ```
  feat: add personal dashboard - pertemuan 2
  ```

---
