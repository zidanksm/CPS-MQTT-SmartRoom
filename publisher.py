import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883

def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Berhasil terhubung ke Broker (Kode: {rc})\n")
    
    # =========================================================
    # AREA UBAH KODE UNTUK SKENARIO PENGUJIAN (Sudah Diperbarui)
    # =========================================================
    
    # [UJI 1] Skenario 5 (Wildcard #) -> DINONAKTIFKAN
    # client.subscribe("smartroom/#", qos=2)

    # [UJI 2] Skenario 4 (Wildcard +) -> DIAKTIFKAN
    # HANYA menangkap data sensor (suhu & kelembapan), kontrol lampu TIDAK AKAN MASUK
    client.subscribe("smartroom/sensor/+", qos=1)
    
    print("Berhasil subscribe ke topik dengan Wildcard (+).")
    # =========================================================

def on_message(client, userdata, msg):
    print(f"-> DATA MASUK! Topik: {msg.topic}")
    print(f"   Payload: {msg.payload.decode()} | QoS: {msg.qos}\n")

# Inisialisasi Client dengan API versi terbaru (Version 2)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="SmartRoom_Monitor")
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

print("=== SUBSCRIBER SMART ROOM AKTIF (Menunggu Data...) ===")
client.loop_forever()