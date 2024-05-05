import time
import os
from PIL import Image

# Tentukan karakter-karakter ASCII untuk merepresentasikan gambar
ASCII_CHARS = '#@$ '

# Ubah ukuran gambar ke lebar yang diinginkan sambil menjaga rasio aspek
def resize_image(image, new_width=50):
    width, height = image.size
    ratio = height / float(width / new_width)
    new_height = int(ratio * new_width / 55.5)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Konversi setiap piksel ke skala abu-abu
def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

# Peta setiap piksel ke karakter ASCII berdasarkan intensitasnya
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // 64]
    return ascii_str

# Buka file gambar
image_path = "/home/image/Logo1.png"
image = Image.open(image_path)

# Konversi gambar ke ASCII
resized_image = resize_image(image)
gray_image = grayify(resized_image)
ascii_str = pixels_to_ascii(gray_image)

# Cetak ASCII art animasi
ascii_width = resized_image.width
ascii_str_len = len(ascii_str)
num_frames = 60  # Jumlah frame animasi
delay = 0.5  # Waktu jeda antara frame (detik)

for frame in range(num_frames):
    os.system('cls' if os.name == 'nt' else 'clear')  # Membersihkan layar terminal
    ascii_art = ""
    for i in range(0, ascii_str_len, ascii_width):
        frame_ascii = ascii_str[i:i + ascii_width]
        if frame % 2 == 0:
            # Ganti warna karakter pada frame genap
            frame_ascii = '\033[91m' + frame_ascii  # Warna merah
        else:
            # Ganti warna karakter pada frame ganjil
            frame_ascii = '\033[94m' + frame_ascii  # Warna biru
        ascii_art += frame_ascii + "\n"
    print(ascii_art)
    time.sleep(delay)
