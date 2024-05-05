# konversi-Gambar-menjadi-ASCII
contoh kode Python yang mengonversi gambar menjadi seni ASCII dan mencetaknya sebagai animasi di terminal. 
Untuk menjalankan kode Python yang mengonversi gambar menjadi seni ASCII dan mencetaknya sebagai animasi di terminal, 

berikut adalah beberapa persiapan yang perlu Anda lakukan:

1. Instalasi Python: Pastikan Anda memiliki Python terinstal di komputer Anda. Kunjungi situs resmi Python di https://www.python.org untuk mengunduh dan menginstal Python sesuai dengan sistem operasi Anda.

2. Instalasi library PIL: Kode ini menggunakan library PIL (Python Imaging Library) untuk memanipulasi gambar. Pastikan Anda telah menginstal library PIL atau versi yang lebih baru yang dikenal sebagai Pillow. Anda dapat menginstalnya dengan menggunakan pip, yaitu menjalankan perintah pip install pillow di terminal atau command prompt.

3. Persiapan gambar: Pastikan Anda memiliki gambar yang ingin Anda konversi menjadi seni ASCII. Sesuaikan path file gambar pada kode dengan path file gambar yang ingin Anda gunakan. Dalam kode yang Anda berikan, path file gambar ditentukan oleh image_path = "/home/image/Logo1.png". Pastikan path file gambar tersebut sesuai dengan lokasi file gambar yang ada di komputer Anda.

4. Menjalankan kode: Setelah semua persiapan di atas selesai, Anda dapat menjalankan kode dengan menjalankan file Python tersebut. Jalankan perintah python nama_file.py di terminal atau command prompt, dengan nama_file.py adalah nama file Python yang berisi kode tersebut. Misalnya, jika Anda menyimpan kode dalam file ascii_art.py, jalankan perintah python ascii_art.py. Kode akan mulai dijalankan dan Anda akan melihat animasi seni ASCII yang dihasilkan dari gambar.


Berikut adalah penjelasan singkat tentang setiap bagian kode:

1. Impor library yang diperlukan:
   time: Digunakan untuk mengontrol jeda antara frame animasi.
   os: Digunakan untuk membersihkan layar terminal.
   PIL: Modul Python Imaging Library, digunakan untuk memanipulasi gambar.
   
2. Tentukan karakter-karakter ASCII:
   ASCII_CHARS: Daftar karakter ASCII yang akan digunakan untuk merepresentasikan intensitas piksel gambar.
   
3. Fungsi resize_image(image, new_width): Mengubah ukuran gambar ke lebar yang diinginkan sambil menjaga rasio aspek.
   image: Gambar yang akan diubah ukurannya.
   new_width: Lebar baru yang diinginkan untuk gambar.
4. Fungsi grayify(image): Mengonversi gambar menjadi skala abu-abu.
   image: Gambar yang akan diubah menjadi skala abu-abu.

5. Fungsi pixels_to_ascii(image): Mengonversi setiap piksel gambar menjadi karakter ASCII berdasarkan intensitasnya.
   image: Gambar yang akan diubah menjadi karakter ASCII.
   
7. Buka file gambar:
   image_path: Path file gambar yang akan dibuka.
   image: Membuka gambar menggunakan PIL.
   
9. Konversi gambar ke ASCII:
   resized_image: Mengubah ukuran gambar sesuai lebar yang diinginkan.
   gray_image: Mengonversi gambar menjadi skala abu-abu.
   ascii_str: Mengonversi piksel gambar menjadi karakter ASCII.

10. Cetak ASCII art sebagai animasi:
   ascii_width: Lebar gambar ASCII.
   ascii_str_len: Panjang string karakter ASCII.
   num_frames: Jumlah frame animasi.
   delay: Waktu jeda antara frame.
   Melakukan loop untuk setiap frame animasi.
   Membersihkan layar terminal menggunakan os.system untuk sistem operasi yang berbeda.
   Membentuk ASCII art untuk setiap frame dengan menggabungkan karakter ASCII dari string ascii_str.
   Mengubah warna karakter pada setiap frame dengan menggunakan kode escape ANSI.
   Mencetak ASCII art dan menunggu selama jeda waktu sebelum beralih ke frame berikutnya.
