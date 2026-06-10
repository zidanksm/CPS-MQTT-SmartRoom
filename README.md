# 🏢 Cyber-Physical System for Smart Room Monitoring & Control
### MQTT-Based Publish-Subscribe Architecture using Python and Eclipse Mosquitto

Cyber-Physical Systems require deterministic communication and reliable data exchange to maintain synchronization between cyber components and physical processes.

Repositori ini berisi implementasi platform Smart Room Monitoring & Control berbasis Cyber-Physical System (CPS) menggunakan protokol MQTT, bahasa pemrograman Python, dan Eclipse Mosquitto Broker sebagai pusat komunikasi berbasis publish-subscribe.

---

## 📌 Badges & Technologies
![Python Version](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MQTT Protocol](https://img.shields.io/badge/MQTT-v5.0%20%2F%20v3.1.1-660066?style=for-the-badge&logo=mqtt&logoColor=white)
![Broker](https://img.shields.io/badge/Eclipse_Mosquitto-v2.x-3C5280?style=for-the-badge&logo=eclipse-mosquitto&logoColor=white)
![Platform](https://img.shields.io/badge/Windows-x64-0078D4?style=for-the-badge&logo=windows&logoColor=white)

---

## 📖 Daftar Isi (Table of Contents)
1. [Deskripsi Proyek](#-deskripsi-proyek)
2. [Arsitektur Siber-Fisik (CPS Closed-Loop)](#-arsitektur-siber-fisik-cps-closed-loop)
3. [Manajemen Topik & Matriks QoS](#-manajemen-topik--matriks-qos)
4. [Prasyarat Sistem](#-prasyarat-sistem)
5. [Panduan Instalasi & Pengaturan](#-panduan-instalasi--pengaturan)
6. [Cara Menjalankan Simulasi](#-cara-menjalankan-simulasi)
7. [Matriks Skenario & Analisis Pengujian](#-matriks-skenario--analisis-pengujian)
8. [Struktur Repositori](#-struktur-repositori)

---

## 📝 Deskripsi Proyek
Platform ini mensimulasikan lingkungan Smart Room dengan memetakan entitas fisik berupa suhu ruangan, kelembapan, dan status aktuator lampu ke dalam ruang siber secara real-time melalui komunikasi MQTT. Sistem menerapkan paradigma Cyber-Physical System (CPS) yang mengintegrasikan proses sensing, komunikasi jaringan, dan monitoring secara kontinu dalam satu siklus closed-loop.

Implementasi ini mengadopsi beberapa karakteristik utama Cyber-Physical System yang meliputi sinkronisasi temporal, komunikasi berbasis publish-subscribe, serta integrasi antara representasi fisik dan ruang siber secara kontinu:

* **Determinisme Waktu (Temporal Constraints):** Pencatatan log waktu diperinci hingga tingkat **milidetik (milliseconds)** untuk validasi sinkronisasi temporal data fisik saat mengalir di ruang siber.
* **Interaktivitas Jaringan:** Komponen *Subscriber* bertindak sebagai kontroler dinamis yang dilengkapi dengan antarmuka menu teks interaktif untuk mengubah parameter filter topik tanpa perlu memodifikasi kode program.
* **Streaming Data Paralel:** Sisi *Publisher* mengadopsi metode *Streaming Mode* kontinu untuk memancarkan seluruh parameter sensor siber-fisik secara simultan guna membuktikan aspek *concurrency*.

---

## 🔄 Arsitektur Siber-Fisik (CPS Closed-Loop)
Sistem komunikasi ini merepresentasikan siklus umpan balik (*closed-loop system*) yang terintegrasi:

```text
[ PHYSICAL PLANT ] ──(Sensing via JSON)──> [ MQTT BROKER ] ──(Routing)──> [ CYBER CONTROLLER ]
  (Kamar Pintar)                             (Mosquitto)                   (Interactive Sub)
        ▲                                                                          │
        └─────────────────(Actuation / QoS 2 Command)──────────────────────────────┘
```
```text
+----------------------+
| Physical Plant       |
|----------------------|
| Temperature Sensor   |
| Humidity Sensor      |
| Lamp Actuator        |
+----------+-----------+
           |
           | Publish JSON
           v
+----------------------+
| Eclipse Mosquitto    |
| MQTT Broker          |
+----------+-----------+
           |
           | Routing
           v
+----------------------+
| Cyber Controller     |
| subscriber.py        |
+----------------------+
```

  - Physical Plant: Entitas fisik kamar pintar yang memancarkan parameter termal lingkungan.

  - Sensing & Telemetry: publisher.py melakukan digitalisasi dan serialisasi besaran analog menjadi objek terstruktur (JSON Payload).

  - Cyber Network: Mosquitto Broker mengelola tabel routing data siber dan menjaga keandalan paket berdasarkan tingkat QoS.

  - Cyber Controller: subscriber.py menangkap, melakukan parsing JSON, dan menganalisis aliran data masuk untuk kebutuhan monitoring ataupun keputusan aktuasi sakelar.

---

## Spesifikasi Kontrak Data (JSON Schema Payload)
Data dikirim dalam representasi objek terstruktur JavaScript Object Notation (JSON) demi interoperabilitas sistem:

Sensor Suhu: {"sensor": "suhu", "value": 25.68, "unit": "C"}

Sensor Kelembapan: {"sensor": "kelembapan", "value": 61.43, "unit": "%"}

Aktuator Lampu: {"device": "lampu_utama", "command": "ON"}

---

## ⚙️ Manajemen Topik & Matriks QoS
Penentuan tingkat Quality of Service (QoS) disesuaikan secara logis berdasarkan karakteristik kekritisan data (data criticality) pada sistem siber-fisik:


| No | Entitas Fisik     | Topik MQTT                     | Level QoS | Justifikasi Karakteristik Data                                                                                                                                                                                             |
| -- | ----------------- | ------------------------------ | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1  | Sensor Suhu       | `smartroom/sensor/temperature` | QoS 0     | **At Most Once.** Data dikirim secara periodik dan kontinu. Kehilangan satu sampel data tidak akan mengganggu stabilitas kontrol sistem siber.                                                                             |
| 2  | Sensor Kelembapan | `smartroom/sensor/humidity`    | QoS 1     | **At Least Once.** Menjamin data kelembapan lingkungan tersampaikan ke pusat siber minimal satu kali melalui mekanisme handshake paket `PUBACK`.                                                                           |
| 3  | Aktuator Lampu    | `smartroom/control/lamp`       | QoS 2     | **Exactly Once.** Bersifat *safety-critical*. Instruksi sakelar fisik harus dieksekusi tepat satu kali untuk menghindari kondisi desinkronisasi status fisik yang dapat menyebabkan perilaku sistem yang tidak diinginkan. |

---

## 💻 Prasyarat Sistem
Sebelum mengeksekusi program, pastikan lingkungan lokal Anda memenuhi spesifikasi berikut:

  - Sistem Operasi: Windows 10/11 (Arsitektur x64)

  - Bahasa Pemrograman: Python versi 3.11 atau yang lebih baru

  - Message Broker: Eclipse Mosquitto versi 2.x

  - Library Python: Paho-MQTT versi 2.1.0+ (Menggunakan spesifikasi API Callback versi terbaru)

---

## 🛠️ Panduan Instalasi & Pengaturan

1. Kloning Repositori
Buka Terminal/CMD Anda, arahkan ke direktori lokal, lalu jalankan perintah:
```bash
git clone [https://github.com/username-kamu/CPS-MQTT-SmartRoom.git](https://github.com/username-kamu/CPS-MQTT-SmartRoom.git)
cd CPS-MQTT-SmartRoom
```
2. Instalasi Dependensi Jaringan Siber
### Install dependency

```bash
Instal library MQTT client resmi untuk Python melalui pip:
```
```bash
pip install paho-mqtt
```

3. Konfigurasi & Menjalankan Mosquitto Broker
Pastikan layanan (service) Mosquitto Broker telah aktif berjalan di komputer lokal Anda pada port 1883. Untuk mematikan atau menyalakannya kembali di Windows, gunakan perintah administrator berikut:
```bash
# Menyalakan Mosquitto Service
net start mosquitto
```
Verifikasi broker telah aktif:
```bash
netstat -ano | findstr 1883
```
---

## 🚀 Cara Menjalankan Simulasi
Sistem ini diuji paling optimal menggunakan fitur terminal terintegrasi pada Visual Studio Code dengan memanfaatkan mekanisme Split Terminal demi menampilkan visualisasi data secara berdampingan.

```text
Subscriber
↓

Waiting...

↓

Publisher Start

↓

Broker Route

↓

Subscriber Receive
```

Langkah Eksekusi:
1. Terminal Kiri (Cyber Controller): Jalankan entitas subscriber terlebih dahulu untuk mendengarkan jaringan:

  ```bash
  python subscriber.py
  ```
  Terminal akan memunculkan pilihan menu interaktif (1/2/3). Pilih skenario wildcard yang ingin Anda uji.

2. Terminal Kanan (Physical Plant): Jalankan simulator lingkungan fisik publisher:

  ```bash
  python publisher.py
  ```
  Publisher akan langsung otomatis berada dalam Streaming Mode dan memancarkan seluruh topik data.

---
## 📸 Matriks Skenario & Analisis Pengujian
📑 Ringkasan Pemenuhan Skenario Tugas Praktikum:

    | **Skenario Praktikum**                                              | **Implementasi pada Sistem**                                                                                                            | **Status**  |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **Skenario 1 – Komunikasi Dasar Publisher–Broker–Subscriber**       | Tervalidasi pada pengujian **Menu 1** melalui komunikasi pada topik `smartroom/sensor/temperature`.                                     | ✅ Terpenuhi |
| **Skenario 2 – Pengujian Quality of Service (QoS 0, QoS 1, QoS 2)** | Diamati melalui proses *Streaming Mode* Publisher yang mengirim seluruh topik menggunakan QoS berbeda pada setiap siklus pengiriman.    | ✅ Terpenuhi |
| **Skenario 3 – Subscription Topik Spesifik**                        | Tervalidasi pada pengujian **Menu 1**, di mana Subscriber hanya menerima data dari topik `smartroom/sensor/temperature`.                | ✅ Terpenuhi |
| **Skenario 4 – Penggunaan Single-Level Wildcard (`+`)**             | Tervalidasi pada pengujian **Menu 2** dengan *subscription* `smartroom/sensor/+` sehingga Subscriber menerima data suhu dan kelembapan. | ✅ Terpenuhi |
| **Skenario 5 – Penggunaan Multi-Level Wildcard (`#`)**              | Tervalidasi pada pengujian **Menu 3** dengan *subscription* `smartroom/#` sehingga seluruh data Smart Room diterima secara bersamaan.   | ✅ Terpenuhi |

---
## 🖼️ Bukti Visual Dokumentasi Hasil Running
  1. Skenario 1 & 3: Pengujian Target Topik Spesifik (Hanya Jalur Sensor Suhu)
    
     <img width="1867" height="1032" alt="Screenshot 2026-06-10 182438" src="https://github.com/user-attachments/assets/3c4c21a5-a695-4dd7-b7d5-01fffd8ca615" />

  Analisis Teknis: Pada kondisi pengujian ini, komponen Subscriber memilih opsi menu 1 (smartroom/sensor/temperature). Meskipun Publisher memancarkan data sensor  kelembapan dan perintah kontrol lampu secara masif (seperti yang terlihat pada log terminal kanan), broker secara cerdas menyaring data tersebut sehingga Subscriber hanya menerima pesan dari kluster temperatur dengan tingkat keandalan QoS 0.

2. Skenario 4: Pengujian Penyaringan Kluster Sensor (Single-Level Wildcard +)
  
   <img width="1868" height="1034" alt="Screenshot 2026-06-10 182251" src="https://github.com/user-attachments/assets/089c3b65-4009-465c-80e3-d61959898bb4" />

    Analisis Teknis: Pada kondisi pengujian ini, Subscriber memilih opsi menu 2 (smartroom/sensor/+). Berdasarkan aturan arsitektur pola routing tree MQTT, karakter wildcard + mengisolasi pencarian hanya pada satu tingkat folder folder. Log terminal siber membuktikan bahwa data smartroom/sensor/temperature (QoS 0) dan smartroom/sensor/humidity (QoS 1) berhasil ditangkap secara bergantian, sementara data aktuasi lampu (smartroom/control/lamp) sepenuhnya disaring keluar dari sistem karena berada pada struktur cabang hierarki yang berbeda.

3. Skenario 5: Pengujian Menangkap Seluruh Data Ruangan (Multi-Level Wildcard #)

    <img width="1869" height="1037" alt="Screenshot 2026-06-10 182129" src="https://github.com/user-attachments/assets/7ada4018-942d-4fe9-8013-0ddc9cbc9216" /> 

    Analisis: Pada kondisi pengujian ini, Subscriber memilih opsi menu 3 (smartroom/#). Sesuai dengan spesifikasi pola routing MQTT, wildcard # bersifat multi-level yang mampu menangkap seluruh data tanpa batasan tingkatan hierarki folder di bawah node utama. Log terminal siber membuktikan bahwa seluruh aliran data, baik sensor suhu (QoS 0), kelembapan (QoS 1), hingga perintah kontrol lampu (QoS 2), berhasil diterima secara paralel, simultan, dan lengkap.

---

## 📂 Struktur Repositori
Berikut adalah susunan struktur file proyek tugas yang rapi dan terorganisir di dalam direktori repositori:
```text
CPS-MQTT-SmartRoom/
│
├── publisher.py       # Simulator Lingkungan Fisik & Pengirim Data JSON (Streaming Mode)
├── subscriber.py      # Dashboard Pemantau Siber Berbasis Antarmuka Menu Interaktif
├── README.md          # Dokumentasi Teknis Utama Proyek Platform (Markdown Masterpiece)
└── Laporan_Praktikum_CPS_MQTT.pdf  # Dokumen Resmi Pelaporan Akademik Praktikum
```

