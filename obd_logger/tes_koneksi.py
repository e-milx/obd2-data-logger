import obd

# Ganti "COM4" dengan nomor port Outgoing 
port_bluetooth = "COM4" 
print(f"Sedang mencoba terhubung ke {port_bluetooth}...")

#baudrate Bluetooth yang lambat
connection = obd.OBD(port_bluetooth, baudrate=38400) 

if connection.is_connected():
    print("Mantap! Berhasil terhubung ke ECU mobil.")
    
    #RPM
    response = connection.query(obd.commands.RPM)
    print(f"Putaran Mesin: {response.value}")
else:
    print("Gagal terhubung. Cek kembali nomor COM Port dan pastikan mesin minimal di posisi ON.")