# OBD-II EMS Data Logger (Bluetooth)

Project ini adalah aplikasi berbasis Python untuk membaca dan merekam data dari *Engine Management System* (ECU/EMS) kendaraan secara *real-time* menggunakan adapter ELM327 via koneksi Bluetooth. Data yang terekam akan otomatis diekspor ke dalam format `.csv` untuk analisis lebih lanjut.

## 🚀 Fitur Utama
- **Koneksi Serial Bluetooth:** Terhubung langsung ke adapter ELM327 melalui komunikasi COM Port manual.
- **Live Monitoring:** Membaca data dinamis mesin kendaraan seperti:
  - Putaran Mesin (RPM)
  - Kecepatan Kendaraan (Speed)
  - Suhu Cairan Pendingin Engine (*Coolant Temperature*)
- **Auto Data Logging:** Menyimpan seluruh riwayat pemantauan sensor ke dalam file tabel `hasil_log_ems.csv` secara otomatis menggunakan library Pandas.

## 🛠️ Prasyarat & Library
Sebelum menjalankan, pastikan telah menginstal:
- Python 3.11 / 3.12
- Library pendukung: `pip install obd pandas matplotlib`
- Perangkat keras: Adapter OBD-II ELM327 Bluetooth & Kendaraan yang mendukung OBD-II (misal: Toyota Avanza atau sejenisnya).

## 💻 Cara Menjalankan
1. Pasang adapter ELM327 ke port OBD-II mobil, putar kunci kontak ke posisi **ON**.
2. Hubungkan Bluetooth laptop dengan adapter. Cek nomor *Outgoing COM Port* di pengaturan Windows.
3. Sesuaikan variabel `port_bluetooth` di dalam file `logger.py` dengan nomor COM Port kamu.
4. Jalankan perintah: `python obd_logger/logger.py`
5. Tekan `Ctrl + C` di terminal untuk menghentikan perekaman dan menyimpan file CSV.
