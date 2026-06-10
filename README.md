# 🏢 Smart Room Monitoring & Control via MQTT

Implementasi sistem **Smart Room Monitoring & Control** menggunakan protokol **MQTT**, bahasa pemrograman **Python**, dan **Eclipse Mosquitto Broker**.

Sistem mensimulasikan komunikasi antara sensor dan perangkat dalam sebuah ruangan pintar menggunakan arsitektur **Publish–Subscribe**, dengan dukungan:

- 🌡️ Monitoring suhu ruangan
- 💧 Monitoring kelembapan ruangan
- 💡 Kontrol status lampu
- 📡 MQTT Topic Filtering
- 🔄 MQTT Wildcard Subscription (`+` dan `#`)
- ⚙️ Quality of Service (QoS 0, QoS 1, QoS 2)

---

## 📋 Prasyarat

Pastikan perangkat telah memenuhi kebutuhan berikut.

### Python

Minimal Python 3.10

```bash
python --version
```

### Library MQTT

Install library yang diperlukan:

```bash
pip install paho-mqtt
```

### Eclipse Mosquitto Broker

Install Mosquitto sesuai sistem operasi:

| Sistem Operasi | Instalasi |
|---|---|
| Ubuntu/Debian | `sudo apt install mosquitto mosquitto-clients` |
| macOS | `brew install mosquitto` |
| Windows | https://mosquitto.org/download/ |

---

## 🚀 Menjalankan Program

### Langkah 1 — Jalankan Mosquitto Broker

#### Linux/macOS

```bash
mosquitto -v
```

atau

```bash
sudo systemctl start mosquitto
```

#### Windows

```bash
net start mosquitto
```

Broker akan berjalan pada:

```text
localhost:1883
```

---

## 💡 Rekomendasi Pengujian

Disarankan menggunakan **Visual Studio Code Split Terminal** atau dua terminal terpisah.

Dengan cara ini aktivitas Publisher dan Subscriber dapat diamati secara bersamaan secara real-time.

```text
┌─────────────────────┬─────────────────────┐
│     Subscriber      │      Publisher      │
├─────────────────────┼─────────────────────┤
│ Data diterima       │ Data dikirim        │
│ Topic filtering     │ JSON publishing     │
│ Wildcard matching   │ QoS monitoring      │
└─────────────────────┴─────────────────────┘
```

---

## ▶️ Langkah 2 — Jalankan Subscriber

Buka terminal pertama:

```bash
python subscriber.py
```

Program akan menampilkan menu:

```text
=========================================================
 CPS SUBSCRIBER - INTERACTIVE WILDCARD TESTING
=========================================================

[1] Topik Spesifik
    smartroom/sensor/temperature

[2] Wildcard (+)
    smartroom/sensor/+

[3] Wildcard (#)
    smartroom/#

Masukkan pilihan Anda:
```

Pilih salah satu mode subscription.

---

## ▶️ Langkah 3 — Jalankan Publisher

Buka terminal kedua:

```bash
python publisher.py
```

Publisher akan mulai mengirim data secara periodik.

Contoh output:

```text
[QoS 0] Sent:
smartroom/sensor/temperature

[QoS 1] Sent:
smartroom/sensor/humidity

[QoS 2] Sent:
smartroom/control/lamp
```

---

## 📡 Topik MQTT yang Digunakan

| Topik | Data | QoS |
|---|---|---|
| `smartroom/sensor/temperature` | Suhu Ruangan | 0 |
| `smartroom/sensor/humidity` | Kelembapan Ruangan | 1 |
| `smartroom/control/lamp` | Status Lampu | 2 |

---

## 🎯 Mode Subscription

### Mode 1 — Topik Spesifik

Subscription:

```text
smartroom/sensor/temperature
```

Menerima:

```text
✔ Data suhu
```

---

### Mode 2 — Wildcard Single-Level

Subscription:

```text
smartroom/sensor/+
```

Menerima:

```text
✔ smartroom/sensor/temperature
✔ smartroom/sensor/humidity
```

Tidak menerima:

```text
✘ smartroom/control/lamp
```

---

### Mode 3 — Wildcard Multi-Level

Subscription:

```text
smartroom/#
```

Menerima:

```text
✔ smartroom/sensor/temperature
✔ smartroom/sensor/humidity
✔ smartroom/control/lamp
```

---

## 🧪 Keterkaitan dengan Skenario Praktikum

| Skenario | Implementasi |
|---|---|
| Komunikasi Dasar Publisher–Subscriber | Mode 1 |
| QoS 0, QoS 1, QoS 2 | Publisher |
| Topik Spesifik | Mode 1 |
| Wildcard `+` | Mode 2 |
| Wildcard `#` | Mode 3 |

---

## 🔄 Alur Eksekusi Program

```text
Start Mosquitto Broker
          │
          ▼
Run subscriber.py
          │
          ▼
Pilih Mode 1 / 2 / 3
          │
          ▼
Run publisher.py
          │
          ▼
Publisher Mengirim Data
          │
          ▼
Mosquitto Broker
          │
          ▼
Subscriber Menampilkan Data
```

---

## 📂 Struktur File

```text
.
├── publisher.py
├── subscriber.py
└── README.md
```

---

## ❗ Troubleshooting

### Tidak dapat terhubung ke broker

Pastikan Mosquitto sudah berjalan:

```bash
net start mosquitto
```

atau

```bash
sudo systemctl start mosquitto
```

---

### Modul paho-mqtt tidak ditemukan

Install ulang:

```bash
pip install paho-mqtt
```

---

### Subscriber tidak menerima pesan

Periksa hal berikut:

- Broker aktif
- Subscriber dijalankan terlebih dahulu
- Topik subscription sesuai
- Port MQTT menggunakan `1883`

---

## ✅ Hasil yang Diharapkan

Jika seluruh langkah berhasil dilakukan:

- Publisher dapat mengirim data secara periodik.
- Subscriber menerima data sesuai topik yang dipilih.
- QoS 0, QoS 1, dan QoS 2 dapat diamati pada proses pengiriman.
- Wildcard `+` dan `#` bekerja sesuai spesifikasi MQTT.
- Seluruh skenario praktikum berhasil dijalankan.
