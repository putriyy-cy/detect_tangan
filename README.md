# ✋ Real-Time Hand Detection System with YOLOv5 & Flask

Sistem ini merupakan aplikasi deteksi tangan secara real-time menggunakan YOLOv5 dan kamera live, yang diintegrasikan dengan Flask untuk tampilan web. Cocok untuk pengembangan sistem interaksi berbasis gesture, keamanan, atau kontrol tanpa sentuhan (touchless).

---

## 🚀 Fitur Unggulan

- 🔍 **Deteksi Tangan Real-Time**  
  Menggunakan YOLOv5 yang telah dilatih pada dataset tangan untuk pendeteksian akurat dan cepat.

- 📸 **Capture dan Simpan Output**  
  Gambar hasil deteksi disimpan otomatis ke folder `static`.

---

## 🛠 Teknologi & Tools

| Teknologi | Deskripsi |
|-----------|-----------|
| Python 3.x | Bahasa pemrograman utama |
| YOLOv5 | Model deteksi objek |
| Flask | Framework web ringan |
| OpenCV | Pengolahan video dan gambar |
| PyTorch | Library deep learning untuk YOLOv5 |

---

## 📁 Struktur Proyek

```bash
.
├── app.py                # Endpoint utama Flask
├── detect.py             # Logika deteksi tangan
├── yolov5/               # Model YOLOv5 custom
├── static/
│   └── result.jpg        # Output hasil deteksi
├── templates/
│   └── index.html        # Antarmuka pengguna
└── requirements.txt      # Daftar dependensi Python
