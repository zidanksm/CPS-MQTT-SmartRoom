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

### Sensor Suhu

```json
{
  "sensor": "suhu",
  "value": 25.68,
  "unit": "C"
}
```

### Sensor Kelembapan

```json
{
  "sensor": "kelembapan",
  "value": 61.43,
  "unit": "%"
}
```

### Aktuator Lampu

```json
{
  "device": "lampu_utama",
  "command": "ON"
}
```

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
### Install Python Dependency

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
+------------------+
| subscriber.py    |
| (Listening Mode) |
+--------+---------+
         |
         |
         v
+------------------+
| Mosquitto Broker |
+--------+---------+
         ^
         |
         |
+--------+---------+
| publisher.py     |
| (Streaming Mode) |
+------------------+
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
## 📸 Matriks Skenario Pengujian

Pengujian sistem mengacu pada lima skenario yang ditetapkan pada modul praktikum MQTT. Implementasi yang dikembangkan menggunakan **satu program Publisher** yang mempublikasikan seluruh data Smart Room secara kontinu dengan variasi **QoS 0, QoS 1, dan QoS 2**, serta **satu program Subscriber** yang menyediakan tiga mode *subscription* (topik spesifik, wildcard `+`, dan wildcard `#`). Dengan rancangan tersebut, beberapa skenario praktikum dapat divalidasi dalam satu proses pengujian sehingga seluruh kebutuhan praktikum tetap terpenuhi melalui **tiga kali pengujian**.

| Skenario Praktikum | Implementasi pada Sistem | Status |
| :--- | :--- | :---: |
| **Skenario 1**<br>Komunikasi Dasar Publisher–Broker–Subscriber | Tervalidasi melalui **Menu 1**, di mana Publisher mengirim data dan Subscriber menerima data pada topik `smartroom/sensor/temperature`. | ✅ |
| **Skenario 2**<br>Pengujian Quality of Service (QoS 0, 1, dan 2) | Diamati selama proses **Streaming Mode** Publisher yang mengirim seluruh topik menggunakan QoS berbeda pada setiap siklus pengiriman. | ✅ |
| **Skenario 3**<br>Subscription Topik Spesifik | Tervalidasi melalui **Menu 1**, sehingga Subscriber hanya menerima data dari topik `smartroom/sensor/temperature`. | ✅ |
| **Skenario 4**<br>Penggunaan Wildcard `+` | Tervalidasi melalui **Menu 2** dengan *subscription* `smartroom/sensor/+` sehingga Subscriber menerima data suhu dan kelembapan secara bersamaan. | ✅ |
| **Skenario 5**<br>Penggunaan Wildcard `#` | Tervalidasi melalui **Menu 3** dengan *subscription* `smartroom/#` sehingga seluruh data Smart Room diterima secara simultan. | ✅ |

> **Catatan:** Implementasi sistem hanya memerlukan **tiga kali eksekusi pengujian** karena Publisher melakukan *streaming* seluruh topik secara simultan dengan variasi QoS 0, QoS 1, dan QoS 2, sedangkan Subscriber menyediakan tiga mode *subscription* (topik spesifik, wildcard `+`, dan wildcard `#`). Dengan demikian, seluruh skenario praktikum dapat tervalidasi tanpa memerlukan lima proses pengujian yang terpisah.

---
---

---

## 🖼️ Hasil Pengujian Sistem

Implementasi sistem berhasil memvalidasi seluruh skenario praktikum MQTT melalui **tiga kali proses pengujian**, di mana beberapa skenario dapat direalisasikan dalam satu eksekusi karena Publisher melakukan *streaming* seluruh topik secara simultan dan Subscriber menyediakan beberapa mode *subscription*.

### 1️⃣ Pengujian Topik Spesifik (`smartroom/sensor/temperature`)
**Merepresentasikan Skenario 1 (Komunikasi Dasar) dan Skenario 3 (Subscription Topik Spesifik).**

<img width="1867" height="1032" alt="Screenshot 2026-06-10 182438" src="https://github.com/user-attachments/assets/3c4c21a5-a695-4dd7-b7d5-01fffd8ca615" />

**Hasil Pengujian**

Subscriber hanya menerima data pada topik `smartroom/sensor/temperature` meskipun Publisher secara simultan mengirimkan data suhu, kelembapan, dan status lampu. Hasil ini menunjukkan bahwa Mosquitto Broker berhasil melakukan *topic filtering* sesuai mekanisme **Publish-Subscribe** MQTT.

---

### 2️⃣ Pengujian Quality of Service (QoS 0, QoS 1, dan QoS 2)
**Merepresentasikan Skenario 2 (Perbandingan Quality of Service).**

<img width="1867" height="1032" alt="Screenshot 2026-06-10 182438" src="https://github.com/user-attachments/assets/3c4c21a5-a695-4dd7-b7d5-01fffd8ca615" />

**Hasil Pengujian**

Selama proses *Streaming Mode*, Publisher mempublikasikan data suhu menggunakan **QoS 0**, data kelembapan menggunakan **QoS 1**, dan data kontrol lampu menggunakan **QoS 2**. Log Publisher menampilkan label `[QoS 0]`, `[QoS 1]`, dan `[QoS 2]` pada setiap siklus pengiriman sehingga implementasi variasi **Quality of Service** dapat diamati secara langsung sesuai karakteristik masing-masing tingkat keandalan.

> **Catatan:** Pengujian QoS tervalidasi melalui log Publisher yang muncul selama proses streaming sehingga tidak memerlukan dokumentasi visual terpisah. Screenshot yang digunakan merupakan proses eksekusi yang sama dengan pengujian komunikasi dasar.

---

### 3️⃣ Pengujian Single-Level Wildcard (`smartroom/sensor/+`)
**Merepresentasikan Skenario 4 (Wildcard `+`).**

<img width="1868" height="1034" alt="Screenshot 2026-06-10 182251" src="https://github.com/user-attachments/assets/089c3b65-4009-465c-80e3-d61959898bb4" />

**Hasil Pengujian**

Subscriber berhasil menerima data dari topik `smartroom/sensor/temperature` dan `smartroom/sensor/humidity` secara bergantian. Data pada topik `smartroom/control/lamp` tidak diteruskan karena berada pada cabang hierarki yang berbeda, sehingga membuktikan bahwa wildcard `+` hanya mencocokkan **satu tingkat hierarki** setelah node `smartroom/sensor`.

---

### 4️⃣ Pengujian Multi-Level Wildcard (`smartroom/#`)
**Merepresentasikan Skenario 5 (Wildcard `#`).**

<img width="1869" height="1037" alt="Screenshot 2026-06-10 182129" src="https://github.com/user-attachments/assets/7ada4018-942d-4fe9-8013-0ddc9cbc9216" />

**Hasil Pengujian**

Subscriber berhasil menerima seluruh data Smart Room yang berada di bawah prefiks `smartroom`, meliputi data suhu (**QoS 0**), kelembapan (**QoS 1**), dan kontrol lampu (**QoS 2**) secara simultan beserta payload JSON dan *timestamp* presisi milidetik. Hasil ini membuktikan bahwa wildcard `#` mampu menangkap seluruh topik pada semua tingkat hierarki sehingga sesuai untuk proses monitoring sistem secara menyeluruh.

---

## ✅ Hasil Implementasi

Seluruh fitur utama sistem berhasil diimplementasikan dan diuji, meliputi:

- ✅ Publish-Subscribe Communication
- ✅ Multiple MQTT Topics
- ✅ Quality of Service (QoS 0, QoS 1, QoS 2)
- ✅ Topic Filtering
- ✅ Single-Level Wildcard (`+`)
- ✅ Multi-Level Wildcard (`#`)
- ✅ JSON Payload Communication
- ✅ Millisecond Timestamp Logging
- ✅ Continuous Streaming Mode
- ✅ Interactive Subscriber Menu
- ✅ Smart Room Monitoring & Control Simulation

## 📂 Struktur Repositori

Struktur direktori proyek disusun secara sederhana untuk memisahkan komponen Publisher, Subscriber, dan dokumentasi proyek.

```text
CPS-MQTT-SmartRoom/
│
├── publisher.py      # Smart Room Publisher & Physical Environment Simulator
├── subscriber.py     # Interactive MQTT Subscriber & Monitoring Console
└── README.md         # Project Documentation
```
---

## 📌 Kesimpulan

Implementasi Smart Room Monitoring & Control Platform berhasil merealisasikan komunikasi berbasis MQTT menggunakan pola Publish–Subscribe dengan dukungan variasi Quality of Service (QoS), hierarki topik terstruktur, serta mekanisme wildcard subscription. Seluruh skenario praktikum berhasil divalidasi sehingga sistem mampu merepresentasikan konsep dasar Cyber-Physical System secara interaktif, real-time, dan modular.

