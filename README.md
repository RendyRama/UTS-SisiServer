# Anggota Kelompok

Muhammad Arif Aldafa (A11.2022.14221)

Muhammad Rendy Ramadhan (A11.2022.14590)

# Sistem Inventaris

Proyek ini adalah aplikasi manajemen inventaris yang dirancang untuk memudahkan pengelolaan stok barang, pelacakan persediaan, dan aksesibilitas informasi inventaris secara real-time. Aplikasi ini diimplementasikan menggunakan Docker Compose untuk memudahkan penyebaran dan pengelolaan layanan.

# Fitur

1. Dashboard Ringkasan Sistem (Kategori, Item, Suppliers, Laporan stok minimal) 
2. Manajemen Kategori (Create, Edit, Delete)
3. Manajemen Item (Create, Edit, Delete)
4. Manajemen Suppliers (Create, Edit, Delete)


# Teknologi
1. Django
2. PostgreSQL
3. Tailwind CSS
4. Docker

# Cara Menjalankan Proyek

1. Pastikan Anda memiliki Docker dan Docker Compose terinstal di komputer Anda.
2. Clone Repository ini
3. Hapus folder postgres_data (jika ada)
4. Jalankan perintah berikut untuk membangun dan menjalankan kontainer:
    <pre>docker compose up -d --build</pre>

5. Terapkan Migrasi
   
   Buat migrasi
   <pre>docker exec uts_test manage.py makemigrations</pre>

   Lalu, terapkan migrasi
   <pre>docker exec uts_test python manage.py migrate</pre>

6. Mulai ulang kontainer docker
   <pre>docker compose restart</pre>

7. Membuat Superuser (Akses Admin)
   <pre>docker exec -it uts_test python manage.py createsuperuser</pre>

8. Akses Aplikasi

   * Untuk mengakses dashboard, Anda dapat mengunjungi http://localhost:8000.
   * Tidak dapat mengelola kategori, item, dan suppliers sebelum membuat admin untuk manajemen inventaris

9. Membuat Admin Manajemen Inventaris

   * Pilih admin di bilah navigasi
   * Masuk menggunakan kredensial superuser yang baru Anda buat.
   * Dari panel admin, Anda dapat mengelola admin untuk manajemen inventaris.
