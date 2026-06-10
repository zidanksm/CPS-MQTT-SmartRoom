import paho.mqtt.client as mqtt
from datetime import datetime

BROKER = "localhost"
PORT = 1883

print("="*65)
print("     CPS SUBSCRIBER - INTERACTIVE WILDCARD TESTING      ")
print("="*65)
print("Pilih Filter Skenario Penerimaan Data:")
print("[1] Skenario 1 & 3 : Topik Spesifik (Hanya Pantau Data Suhu)")
print("[2] Skenario 4     : Wildcard (+) - Pantau Semua Jenis Sensor")
print("[3] Skenario 5     : Wildcard (#) - Pantau Seluruh Data Ruangan")
print("="*65)

pilihan = input("Masukkan pilihan Anda (1/2/3): ")

# Pemetaan otomatis berdasarkan kriteria penugasan praktikum
if pilihan == '1':
    topic_target = "smartroom/sensor/temperature"
    mode_desc = "Topik Spesifik (Suhu)"
elif pilihan == '2':
    topic_target = "smartroom/sensor/+"
    mode_desc = "Single-Level Wildcard (+)"
elif pilihan == '3':
    topic_target = "smartroom/#"
    mode_desc = "Multi-Level Wildcard (#)"
else:
    print("[ERROR] Opsi salah!")
    exit()

def get_timestamp():
    return datetime.now().strftime("%H:%M:%S.%f")[:-3]

def on_connect(client, userdata, flags, rc, properties=None):
    print(f"\n[INFO] Terhubung ke Broker lokal (Result Code: {rc})")
    client.subscribe(topic_target, qos=2)
    print(f"[INFO] Mode Aktif : {mode_desc}")
    print(f"[INFO] Mendengarkan pada Target: '{topic_target}'\n" + "="*65)

def on_message(client, userdata, msg):
    time_received = get_timestamp()
    print(f"[{time_received}] DATA MASUK!")
    print(f" ├─ Topic : {msg.topic}")
    print(f" ├─ QoS   : {msg.qos}")
    print(f" └─ Data  : {msg.payload.decode()}\n")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="SmartRoom_Monitor")
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()