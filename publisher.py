import paho.mqtt.client as mqtt
import time
import random
import json
from datetime import datetime

BROKER = "localhost"
PORT = 1883

# Inisialisasi Client (Menggunakan Paho API v2)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="SmartRoom_Publisher")
client.connect(BROKER, PORT, 60)

# ==================== PERBAIKAN UTAMA ====================
# Memulai network loop di background agar library paho-mqtt 
# bisa memproses jabat tangan (handshake) paket QoS 1 & QoS 2
client.loop_start() 
# =========================================================

def get_timestamp():
    # Waktu presisi milidetik untuk aspek determinisme waktu CPS
    return datetime.now().strftime("%H:%M:%S.%f")[:-3]

print("="*65)
print("   CPS PUBLISHER - ALL SCENARIOS ACTIVE (STREAMING MODE)   ")
print("="*65)
print("[INFO] Mengirim data ke broker secara berkala...\n")

try:
    while True:
        # Simulasi nilai besaran fisik dunia nyata
        temp = round(random.uniform(20.0, 35.0), 2)
        hum = round(random.uniform(40.0, 80.0), 2)
        lamp_status = random.choice(["ON", "OFF"])

        # Format JSON standar IoT (Materi Parsing JSON Kuliah CPS)
        payload_temp = json.dumps({"sensor": "suhu", "value": temp, "unit": "C"})
        payload_hum = json.dumps({"sensor": "kelembapan", "value": hum, "unit": "%"})
        payload_lamp = json.dumps({"device": "lampu_utama", "command": lamp_status})

        now = get_timestamp()

        # [SKENARIO 1 & 3]: Distribusi data ke beberapa topik berbeda
        # [SKENARIO 2]: Variasi tingkat keandalan data (QoS 0, QoS 1, QoS 2)
        
        # 1. Topik Suhu (QoS 0 - At Most Once / Periodik berkala)
        client.publish("smartroom/sensor/temperature", payload_temp, qos=0)
        print(f"[{now}] [QoS 0] Sent -> smartroom/sensor/temperature | {payload_temp}")
        
        # 2. Topik Kelembapan (QoS 1 - At Least Once / Terjamin sampai)
        client.publish("smartroom/sensor/humidity", payload_hum, qos=1)
        print(f"[{now}] [QoS 1] Sent -> smartroom/sensor/humidity  | {payload_hum}")
        
        # 3. Topik Kontrol Lampu (QoS 2 - Exactly Once / Safety-Critical Actuation)
        client.publish("smartroom/control/lamp", payload_lamp, qos=2)
        print(f"[{now}] [QoS 2] Sent -> smartroom/control/lamp       | {payload_lamp}")

        print("-" * 65)
        time.sleep(3) # Periode sampling loop fisik
        
except KeyboardInterrupt:
    print("\n[INFO] Publisher dimatikan.")
    client.loop_stop()  # Menghentikan network loop di background secara bersih
    client.disconnect()
