# Pertemuan 07 Fungsi Python

**Nama:** Eka Elsanti  
**NIM:** 2225250059  
**Kelas:** 3A  

---

## Tujuan
Menggunakan fungsi, parameter, return value, dan scope untuk membuat program modular yang dapat digunakan kembali serta lebih mudah diuji.

---

## Cara Menjalankan
Jalankan perintah berikut di terminal:
```bash
python praktik/utilitas_matematika.py

```

---

## Struktur Fungsi

* `luas_persegi_panjang(p, l)`: Menerima parameter panjang (`p`) dan lebar (`l`), mengembalikan hasil perkalian luas persegi panjang.
* `luas_segitiga(a, t)`: Menerima parameter alas (`a`) dan tinggi (`t`), mengembalikan hasil perhitungan $0.5 \times a \times t$.
* `jumlah_n(n)`: Menerima parameter bilangan bulat `n`, menghitung akumulasi penjumlahan dari 1 hingga `n` menggunakan perulangan, dan mengembalikan totalnya.
* `faktorial(n)`: Menerima parameter bilangan bulat `n`, menghitung hasil perkalian faktorial dari 1 hingga `n` menggunakan perulangan, dan mengembalikan hasilnya.
* `tampilkan_menu()`: Menampilkan pilihan daftar operasi matematika ke layar.

---

## Hasil Pengujian

| Operasi | Input | Hasil Diharapkan | Hasil Aktual | Status |
| --- | --- | --- | --- | --- |
| Luas persegi panjang | $p=8, l=5$ | 40.0 | 40.0 | Sesuai |
| Luas segitiga | $a=10, t=6$ | 30.0 | 30.0 | Sesuai |
| Jumlah 1..n | $n=10$ | 55 | 55 | Sesuai |
| Faktorial | $n=5$ | 120 | 120 | Sesuai |
| Faktorial | $n=0$ | 1 | 1 | Sesuai |

---

## Refleksi

Setelah memisahkan kode menjadi fungsi, rumus matematika tidak perlu ditulis berulang kali pada program utama. Program menjadi lebih rapi karena logika perhitungan terisolasi di dalam fungsi masing-masing, sehingga jika terjadi kesalahan rumus, perbaikan hanya perlu dilakukan pada fungsi terkait tanpa mengubah alur utama program.