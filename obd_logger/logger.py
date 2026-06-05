import obd
import time
import pandas as pd

# 1. Setup Koneksi
port_bluetooth = "COM4" # Sesuaikan dengan port kamu
connection = obd.OBD(port_bluetooth)

if not connection.is_connected():
    print("Gagal terhubung ke kendaraan.")
    exit()

print("Koneksi berhasil. Mulai merekam data EMS...")

# 2. Siapkan tempat penampungan data
data_log = []
waktu_mulai = time.time()

try:
    # 3. Looping untuk mengambil data terus-menerus
    # Tekan Ctrl+C di terminal untuk menghentikan rekaman
    while True:
        waktu_berjalan = round(time.time() - waktu_mulai, 2)
        
        # Ambil data sensor
        rpm = connection.query(obd.commands.RPM).value
        speed = connection.query(obd.commands.SPEED).value
        coolant_temp = connection.query(obd.commands.COOLANT_TEMP).value
        
        # Ekstrak angka saja (hilangkan satuan seperti 'rpm' atau 'kph')
        rpm_val = rpm.magnitude if rpm else 0
        speed_val = speed.magnitude if speed else 0
        temp_val = coolant_temp.magnitude if coolant_temp else 0
        
        # Tampilkan di layar
        print(f"Waktu: {waktu_berjalan}s | RPM: {rpm_val} | Speed: {speed_val} km/h | Suhu: {temp_val} C")
        
        # Simpan ke memori sementara
        data_log.append({
            "Time (s)": waktu_berjalan,
            "RPM": rpm_val,
            "Speed (km/h)": speed_val,
            "Coolant Temp (C)": temp_val
        })
        
        # Beri jeda sedikit agar ECU tidak nge-hang karena dibrondong permintaan
        time.sleep(0.5) 

except KeyboardInterrupt:
    # 4. Simpan ke CSV saat script dihentikan (Ctrl+C)
    print("\nPerekaman dihentikan. Menyimpan data...")
    df = pd.DataFrame(data_log)
    df.to_csv("hasil_log_ems.csv", index=False)
    print("Data berhasil disimpan ke 'hasil_log_ems.csv'. Siap dianalisis!")