# 🏢 Smart Room Monitoring & Control via MQTT

Implementasi sistem **Smart Room Monitoring & Control** menggunakan protokol **MQTT** dengan **Eclipse Mosquitto Broker** dan **Python**.

Sistem terdiri dari dua komponen utama:

- **Publisher** → Mengirim data sensor dan kontrol perangkat.
- **Subscriber** → Menerima dan menampilkan data berdasarkan topik yang dipilih.

Fitur yang diimplementasikan:

- Publish–Subscribe MQTT
- Quality of Service (QoS 0, QoS 1, QoS 2)
- Topic Filtering
- Single-Level Wildcard (`+`)
- Multi-Level Wildcard (`#`)
- Real-Time Monitoring

---

## 📋 Prasyarat

### Python

Pastikan Python **3.10 atau lebih baru** telah terinstal.

```bash
python --version
```

### Library MQTT

Install library yang diperlukan:

```bash
pip install paho-mqtt
```

### Eclipse Mosquitto Broker

Install Mosquitto Broker:

| Sistem Operasi | Perintah |
|---|---|
| Ubuntu/Debian | `sudo apt install mosquitto mosquitto-clients` |
| macOS | `brew install mosquitto` |
| Windows | Download dari https://mosquitto.org/download/ |

Menjalankan broker:

#### Windows

```bash
net start mosquitto
```

#### Linux

```bash
sudo systemctl start mosquitto
```

Broker berjalan pada:

```text
localhost:1883
```

---

## 🚀 Cara Menjalankan Program

> Jalankan **Subscriber terlebih dahulu**, kemudian jalankan **Publisher**.

### Langkah 1 — Jalankan Subscriber

Buka terminal pertama:

```bash
python subscriber.py
```

Program akan menampilkan menu:

```text
1. smartroom/sensor/temperature
2. smartroom/sensor/+
3. smartroom/#
```

Pilih salah satu mode subscription.

---

### Langkah 2 — Jalankan Publisher

Buka terminal kedua:

```bash
python publisher.py
```

Publisher akan mengirim data Smart Room secara periodik.

Topik yang digunakan:

| Topik | Data | QoS |
|---|---|---|
| `smartroom/sensor/temperature` | Data suhu | 0 |
| `smartroom/sensor/humidity` | Data kelembapan | 1 |
| `smartroom/control/lamp` | Status lampu | 2 |

---

### Langkah 3 — Menghentikan Program

Tekan:

```bash
CTRL + C
```

pada terminal Publisher maupun Subscriber.

---

## 🎯 Penjelasan Mode Subscription

| Pilihan | Subscription | Keterangan |
|---|---|---|
| `1` | `smartroom/sensor/temperature` | Hanya menerima data suhu |
| `2` | `smartroom/sensor/+` | Menerima data suhu dan kelembapan |
| `3` | `smartroom/#` | Menerima seluruh data Smart Room |

---

## 🧪 Pemetaan Skenario Praktikum

| Skenario | Implementasi |
|---|---|
| Komunikasi Dasar Publisher–Subscriber | Menu 1 |
| QoS 0, QoS 1, QoS 2 | Publisher |
| Subscription Topik Spesifik | Menu 1 |
| Wildcard `+` | Menu 2 |
| Wildcard `#` | Menu 3 |

---

## 📸 Hasil Pengujian

### Topik Spesifik

*(Tambahkan screenshot pengujian topik spesifik di sini)*

### Wildcard `+`

*(Tambahkan screenshot pengujian wildcard + di sini)*

### Wildcard `#`

*(Tambahkan screenshot pengujian wildcard # di sini)*

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

### Gagal terhubung ke broker

Pastikan Mosquitto Broker sudah berjalan:

```bash
net start mosquitto
```

atau

```bash
sudo systemctl start mosquitto
```

### Modul `paho-mqtt` tidak ditemukan

Install ulang:

```bash
pip install paho-mqtt
```

### Subscriber tidak menerima pesan

- Pastikan Broker aktif.
- Jalankan Subscriber sebelum Publisher.
- Pastikan topik subscription sesuai.

---

