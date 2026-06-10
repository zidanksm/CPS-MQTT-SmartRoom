# 🏢 Cyber-Physical System: Smart Room Monitoring via MQTT

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MQTT](https://img.shields.io/badge/MQTT-660066?style=for-the-badge&logo=mqtt&logoColor=white)
![Mosquitto](https://img.shields.io/badge/Eclipse_Mosquitto-3C5280?style=for-the-badge&logo=eclipse-mosquitto&logoColor=white)

Repositori ini berisi implementasi sistem **Cyber-Physical Systems (CPS)** untuk *Smart Room Monitoring* menggunakan protokol MQTT. Proyek ini mendemonstrasikan komunikasi *real-time* dan *concurrency* antara entitas fisik (sensor/aktuator) dan entitas siber (aplikasi pemantau).

## 🎯 Fitur dan Skenario Pengujian
Sistem ini dirancang untuk memenuhi seluruh skenario komunikasi IoT dan CPS pada tugas praktikum:
- **Variasi Quality of Service (QoS):**
  - `QoS 0` (Fire and Forget): Digunakan untuk sensor suhu (toleransi data *loss*).
  - `QoS 1` (At least once): Digunakan untuk sensor kelembapan.
  - `QoS 2` (Exactly once): Digunakan untuk kontrol lampu (*safety-critical actuation*).
- **Format Data Standar Industri:** Pengiriman *payload* menggunakan format **JSON** terstruktur.
- **Pengujian Wildcard Topic:**
  - `+` (Single-level): Menangkap spesifik data sensor saja (`smartroom/sensor/+`).
  - `#` (Multi-level): Menangkap seluruh lalu lintas data ruangan (`smartroom/#`).

## ⚙️ Arsitektur Topik MQTT
Struktur hierarki topik dirancang untuk merepresentasikan *feedback loop* pada CPS:
| Entitas | Topik MQTT | QoS | Deskripsi |
| :--- | :--- | :--- | :--- |
| **Sensor Suhu** | `smartroom/sensor/temperature` | 0 | Mengirim data suhu secara periodik |
| **Sensor Kelembapan** | `smartroom/sensor/humidity` | 1 | Mengirim data kelembapan terjamin |
| **Aktuator Lampu** | `smartroom/control/lamp` | 2 | Menerima instruksi sakelar lampu secara presisi |

## 🚀 Cara Menjalankan Program

### Prasyarat (Prerequisites)
1. Instal [Eclipse Mosquitto](https://mosquitto.org/download/) dan pastikan *service* berjalan di `localhost:1883`.
2. Instal *library* Python yang dibutuhkan:
   ```bash
   pip install paho-mqtt
