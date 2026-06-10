# 🏢 Smart Room Monitoring & Control via MQTT

Proyek ini merupakan implementasi **Smart Room Monitoring & Control** menggunakan protokol **MQTT** dengan **Eclipse Mosquitto Broker** sebagai pusat komunikasi. Sistem mensimulasikan proses monitoring lingkungan ruangan dan kontrol perangkat menggunakan arsitektur **Publish–Subscribe**.

Terdapat dua komponen utama:

- **Publisher** → Mengirim data sensor dan kontrol perangkat.
- **Subscriber** → Menerima dan menampilkan data berdasarkan topik yang dipilih.

---

## 📋 Prasyarat

### 1. Python

Pastikan Python **3.10 atau lebih baru** telah terinstal.

```bash
python --version
```

### 2. Library `paho-mqtt`

Install library MQTT untuk Python:

```bash
pip install paho-mqtt
```

### 3. Eclipse Mosquitto Broker

Broker Mosquitto harus berjalan sebelum Publisher dan Subscriber dijalankan.

### Instalasi Mosquitto

| Sistem Operasi | Perintah |
|---|---|
| Ubuntu / Debian | `sudo apt install mosquitto mosquitto-clients` |
| macOS (Homebrew) | `brew install mosquitto` |
| Windows | Download dari https://mosquitto.org/download/ |

### Menjalankan Mosquitto Broker

#### Windows

```bash
net start mosquitto
```

#### Linux

```bash
sudo systemctl start mosquitto
```

atau

```bash
mosquitto -v
```

> Broker berjalan secara default pada `localhost` dengan port `1883`.

---

## 🚀 Cara Menjalankan Program

> **Penting:** Jalankan Subscriber terlebih dahulu sebelum Publisher agar seluruh pesan dapat diterima dengan baik.

### Langkah 1 — Jalankan Subscriber

Buka terminal pertama kemudian jalankan:

```bash
python subscriber.py
```

Program akan menampilkan menu berikut:

```text
1. smartroom/sensor/temperature
2. smartroom/sensor/+
3. smartroom/#
```

Pilih mode subscription sesuai skenario pengujian yang ingin dilakukan.

---

### Langkah 2 — Jalankan Publisher

Buka terminal kedua kemudian jalankan:

```bash
python publisher.py
```

Publisher akan mulai mengirim data Smart Room secara periodik ke topik MQTT berikut:

| Topik | Data | QoS |
|---|---|---|
| `smartroom/sensor/temperature` | Data suhu ruangan | 0 |
| `smartroom/sensor/humidity` | Data kelembapan ruangan | 1 |
| `smartroom/control/lamp` | Status kontrol lampu | 2 |

---

### Langkah 3 — Menghentikan Program

Tekan `CTRL + C` pada masing-masing terminal untuk menghentikan Publisher maupun Subscriber.

---

## 🎯 Penjelasan Mode Subscription

| Pilihan | Subscription | Keterangan |
|---|---|---|
| `1` | `smartroom/sensor/temperature` | Hanya menerima data suhu |
| `2` | `smartroom/sensor/+` | Menerima seluruh data sensor (suhu dan kelembapan) |
| `3` | `smartroom/#` | Menerima seluruh data Smart Room |

---

## 🧪 Pemetaan Skenario Praktikum

| Skenario Praktikum | Implementasi |
|---|---|
| Skenario 1 – Komunikasi Dasar Publisher–Subscriber | Menu 1 |
| Skenario 2 – QoS 0, QoS 1, dan QoS 2 | Publisher |
| Skenario 3 – Subscription Topik Spesifik | Menu 1 |
| Skenario 4 – Wildcard `+` | Menu 2 |
| Skenario 5 – Wildcard `#` | Menu 3 |

---

## 📸 Hasil Pengujian

### 1. Topik Spesifik (`smartroom/sensor/temperature`)

![Topik Spesifik](MASUKKAN_LINK_GAMBAR_1)

Subscriber hanya menerima data dari topik:

```text
smartroom/sensor/temperature
```

---

### 2. Wildcard Single-Level (`smartroom/sensor/+`)

![Wildcard Plus](MASUKKAN_LINK_GAMBAR_2)

Subscriber menerima data:

```text
smartroom/sensor/temperature
smartroom/sensor/humidity
```

Namun tidak menerima:

```text
smartroom/control/lamp
```

---

### 3. Wildcard Multi-Level (`smartroom/#`)

![Wildcard Hash](MASUKKAN_LINK_GAMBAR_3)

Subscriber menerima seluruh data Smart Room:

```text
smartroom/sensor/temperature
smartroom/sensor/humidity
smartroom/control/lamp
```

---

## 📂 Struktur File

```text
.
├── publisher.py      # Simulasi pengirim data Smart Room
├── subscriber.py     # Penerima dan monitoring data MQTT
└── README.md         # Dokumentasi proyek
```

---

## ❗ Troubleshooting

### Gagal terhubung ke broker

- Pastikan Mosquitto Broker sudah berjalan.
- Pastikan port `1883` tidak digunakan aplikasi lain.
- Periksa konfigurasi firewall.

### Modul `paho-mqtt` tidak ditemukan

Install ulang library:

```bash
pip install paho-mqtt
```

### Subscriber tidak menerima pesan

- Pastikan Subscriber dijalankan sebelum Publisher.
- Pastikan Broker aktif.
- Pastikan pilihan subscription sesuai dengan topik yang dikirim Publisher.

---

## 👨‍💻 Author

**Zidan Kusuma Putra Wanda**  
NIM: **235150307111002**  
Fakultas Ilmu Komputer  
Universitas Brawijaya
