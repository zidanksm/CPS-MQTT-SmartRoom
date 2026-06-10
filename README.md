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
3. [Spesifikasi Kontrak Data (JSON Payload Schema)](#-spesifikasi-kontrak-data-json-payload-schema)
4. [Manajemen Topik & Matriks QoS](#️-manajemen-topik--matriks-qos)
5. [Prasyarat Sistem](#-prasyarat-sistem)
6. [Panduan Instalasi & Pengaturan](#️-panduan-instalasi--pengaturan)
7. [Cara Menjalankan Simulasi](#-cara-menjalankan-simulasi)
8. [Matriks Skenario Pengujian](#-matriks-skenario-pengujian)
9. [Hasil Pengujian Sistem](#️-hasil-pengujian-sistem)
10. [Hasil Implementasi](#-hasil-implementasi)
11. [Struktur Repositori](#-struktur-repositori)
12. [Kesimpulan](#-kesimpulan)
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

## 📄 Spesifikasi Kontrak Data (JSON Payload Schema)

Seluruh data pada sistem dikirim menggunakan format **JavaScript Object Notation (JSON)** sebagai media pertukaran data antara Publisher dan Subscriber. Penggunaan JSON memungkinkan representasi data yang terstruktur, ringan, mudah diproses, serta mendukung interoperabilitas antar komponen pada sistem Cyber-Physical System (CPS).

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

Pastikan seluruh perangkat lunak pendukung telah terpasang sebelum menjalankan simulasi Smart Room Monitoring & Control.

### 1. Clone Repository

Unduh repositori ke komputer lokal menggunakan perintah berikut:

```bash
git clone https://github.com/username-kamu/CPS-MQTT-SmartRoom.git
cd CPS-MQTT-SmartRoom
```

### 2. Install Python Dependency

Instal library **Paho-MQTT** sebagai MQTT Client untuk Python:

```bash
pip install paho-mqtt
```

### 3. Menjalankan Eclipse Mosquitto Broker

Pastikan **Eclipse Mosquitto Broker** telah terinstal dan berjalan pada **port 1883**.

Menjalankan service Mosquitto pada Windows:

```bash
net start mosquitto
```

Verifikasi bahwa broker telah aktif:

```bash
netstat -ano | findstr 1883
```

Apabila broker berhasil berjalan, sistem siap digunakan untuk proses komunikasi berbasis **MQTT Publish–Subscribe**.

> **Catatan:** Pastikan **Mosquitto Broker telah aktif** sebelum menjalankan **Publisher** maupun **Subscriber** agar proses komunikasi MQTT dapat berlangsung dengan normal.

---

## 🚀 Cara Menjalankan Simulasi

Simulasi direkomendasikan menggunakan **Visual Studio Code Split Terminal** atau dua terminal terpisah sehingga aktivitas Publisher dan Subscriber dapat diamati secara **real-time**.

### Langkah 1 — Jalankan Subscriber

Pada terminal pertama, jalankan:

```bash
python subscriber.py
```

Program akan menampilkan menu *subscription* berikut:

```text
1. smartroom/sensor/temperature
2. smartroom/sensor/+
3. smartroom/#
```

Pilih mode *subscription* sesuai skenario pengujian yang akan dilakukan. Subscriber dijalankan terlebih dahulu agar seluruh pesan yang dipublikasikan Publisher dapat langsung diterima dan diamati.

### Langkah 2 — Jalankan Publisher

Pada terminal kedua, jalankan:

```bash
python publisher.py
```

Publisher akan memasuki **Continuous Streaming Mode** dan secara periodik mempublikasikan seluruh data Smart Room menggunakan **JSON Payload** pada beberapa topik MQTT dengan variasi **QoS 0**, **QoS 1**, dan **QoS 2**.

Selama proses simulasi berlangsung, **Mosquitto Broker** akan melakukan proses **topic routing**, **topic filtering**, dan pengiriman pesan berdasarkan **Quality of Service (QoS)** yang telah ditentukan sehingga komunikasi antara Publisher dan Subscriber berlangsung sesuai mekanisme **Publish–Subscribe MQTT**.

### Alur Eksekusi

```text
Start Mosquitto Broker
           │
           ▼
Run subscriber.py
(Select Menu 1 / 2 / 3)
           │
           ▼
Run publisher.py
(Streaming Mode)
           │
           ▼
MQTT Broker Routing
           │
           ▼
Subscriber Receives Data
```

Selama simulasi berlangsung, data akan diteruskan oleh Mosquitto Broker sesuai mekanisme **topic filtering**, **hierarchical topic**, dan **Quality of Service (QoS)** yang diterapkan pada sistem Smart Room.

---

## 📸 Matriks Skenario Pengujian

Pengujian sistem mengacu pada **lima skenario praktikum MQTT** yang ditetapkan pada modul pembelajaran. Implementasi yang dikembangkan menggunakan **satu program Publisher** yang secara kontinu mempublikasikan seluruh data Smart Room dengan variasi **Quality of Service (QoS 0, QoS 1, dan QoS 2)** serta **satu program Subscriber** yang menyediakan tiga mode *subscription*, yaitu **topik spesifik**, **single-level wildcard (`+`)**, dan **multi-level wildcard (`#`)**.

Dengan arsitektur tersebut, beberapa skenario praktikum dapat divalidasi secara bersamaan dalam satu proses eksekusi sehingga seluruh kebutuhan pengujian berhasil direalisasikan melalui **tiga kali proses pengujian** tanpa mengurangi cakupan evaluasi terhadap fitur-fitur MQTT yang diimplementasikan.

| **Skenario Praktikum** | **Implementasi pada Sistem** | **Status** |
| :--- | :--- | :---: |
| **Skenario 1 – Komunikasi Dasar Publisher–Broker–Subscriber** | Tervalidasi pada **Menu 1**, di mana Publisher mengirim data dan Subscriber menerima data sesuai mekanisme *publish-subscribe* pada topik `smartroom/sensor/temperature`. | ✅ Terpenuhi |
| **Skenario 2 – Pengujian Quality of Service (QoS 0, QoS 1, QoS 2)** | Diamati selama proses **Streaming Mode**, di mana Publisher mengirim seluruh topik menggunakan QoS yang berbeda pada setiap siklus pengiriman. | ✅ Terpenuhi |
| **Skenario 3 – Subscription Topik Spesifik** | Tervalidasi pada **Menu 1**, sehingga Subscriber hanya menerima data dari topik `smartroom/sensor/temperature` sesuai mekanisme *topic filtering*. | ✅ Terpenuhi |
| **Skenario 4 – Penggunaan Single-Level Wildcard (`+`)** | Tervalidasi pada **Menu 2** melalui *subscription* `smartroom/sensor/+`, sehingga Subscriber menerima seluruh data sensor yang berada pada satu tingkat hierarki. | ✅ Terpenuhi |
| **Skenario 5 – Penggunaan Multi-Level Wildcard (`#`)** | Tervalidasi pada **Menu 3** melalui *subscription* `smartroom/#`, sehingga seluruh data Smart Room diterima tanpa batasan tingkat hierarki topik. | ✅ Terpenuhi |

> **Catatan:** Meskipun modul praktikum mendefinisikan **lima skenario pengujian**, implementasi sistem hanya memerlukan **tiga kali eksekusi** karena Publisher mempublikasikan seluruh topik beserta variasi **QoS 0, QoS 1, dan QoS 2** secara simultan, sedangkan Subscriber menyediakan tiga mode *subscription* yang mampu merepresentasikan seluruh mekanisme **topic filtering** dan **wildcard subscription** pada protokol MQTT. Dengan demikian, seluruh skenario praktikum tetap tervalidasi tanpa memerlukan lima proses pengujian yang terpisah.

### 📊 Pemetaan Implementasi terhadap Skenario Praktikum MQTT

```text
                    publisher.py
             (Streaming All MQTT Topics)
                         │
                         │
                         ▼
            Eclipse Mosquitto Broker
                         │
     ┌───────────────────┼───────────────────┐
     │                   │                   │
     ▼                   ▼                   ▼
  Menu 1              Menu 2              Menu 3
Topic Specific      Wildcard (+)        Wildcard (#)
temperature         sensor/+            smartroom/#
     │                   │                   │
     ▼                   ▼                   ▼
Skenario 1 & 3      Skenario 4          Skenario 5

             ──────────────────────────────────►
              QoS 0 • QoS 1 • QoS 2 diamati
            selama Publisher berada pada
                 Continuous Streaming Mode
                   (Merepresentasikan
                     Skenario 2)
```

---

## 🖼️ Hasil Pengujian Sistem

Implementasi sistem berhasil memvalidasi seluruh skenario praktikum MQTT melalui **tiga kali proses pengujian**. Hal ini dimungkinkan karena **Publisher** secara kontinu mempublikasikan seluruh data Smart Room menggunakan variasi **QoS 0**, **QoS 1**, dan **QoS 2**, sedangkan **Subscriber** menyediakan tiga mode *subscription* berupa **topik spesifik**, **single-level wildcard (`+`)**, dan **multi-level wildcard (`#`)**. Dengan rancangan tersebut, seluruh skenario praktikum dapat direpresentasikan tanpa memerlukan lima proses pengujian yang terpisah.

---

### 1️⃣ Pengujian Topik Spesifik (`smartroom/sensor/temperature`)

**Merepresentasikan Skenario 1 (Komunikasi Dasar Publisher–Broker–Subscriber) dan Skenario 3 (Subscription Topik Spesifik).**

<img width="1867" height="1032" alt="Screenshot 2026-06-10 182438" src="https://github.com/user-attachments/assets/3c4c21a5-a695-4dd7-b7d5-01fffd8ca615" />

#### Hasil Pengujian

Subscriber hanya menerima data pada topik `smartroom/sensor/temperature` meskipun Publisher secara bersamaan mempublikasikan data suhu, kelembapan, dan status lampu. Mosquitto Broker berhasil melakukan proses **topic filtering** sehingga hanya paket yang sesuai dengan topik *subscription* yang diteruskan kepada Subscriber.

#### Analisis

Hasil tersebut menunjukkan bahwa mekanisme **Publish–Subscribe** MQTT berjalan dengan baik, di mana proses routing pesan sepenuhnya ditentukan oleh topik yang dilanggan tanpa dipengaruhi oleh topik lain yang dipublikasikan secara simultan.

> **Kesimpulan:** Implementasi komunikasi dasar MQTT dan *subscription* topik spesifik berhasil direalisasikan sesuai mekanisme **Publish–Subscribe**.

---

### 2️⃣ Pengujian Quality of Service (QoS 0, QoS 1, dan QoS 2)

**Merepresentasikan Skenario 2 (Quality of Service MQTT).**

#### Hasil Pengujian

Selama proses **Continuous Streaming Mode**, Publisher mempublikasikan data suhu menggunakan **QoS 0**, data kelembapan menggunakan **QoS 1**, dan data kontrol lampu menggunakan **QoS 2**. Setiap proses pengiriman menampilkan informasi tingkat QoS pada log Publisher sehingga implementasi masing-masing mekanisme dapat diamati secara langsung.

#### Analisis

Implementasi **QoS 0 (At Most Once)** digunakan untuk data yang dikirim secara periodik tanpa jaminan pengiriman, **QoS 1 (At Least Once)** memastikan pesan diterima minimal satu kali melalui mekanisme *acknowledgement*, sedangkan **QoS 2 (Exactly Once)** menjamin pesan dikirim tepat satu kali sehingga sesuai digunakan pada data kontrol aktuator.

> **Catatan:** Pengujian QoS diamati melalui log Publisher selama proses *Streaming Mode* sehingga tidak memerlukan dokumentasi visual terpisah. Variasi **QoS 0**, **QoS 1**, dan **QoS 2** telah dipublikasikan secara simultan pada setiap siklus pengiriman.

> **Kesimpulan:** Implementasi **Quality of Service (QoS 0, QoS 1, dan QoS 2)** berhasil direalisasikan sesuai karakteristik tingkat keandalan pada protokol MQTT.

---

### 3️⃣ Pengujian Single-Level Wildcard (`smartroom/sensor/+`)

**Merepresentasikan Skenario 4 (Single-Level Wildcard `+`).**

<img width="1868" height="1034" alt="Screenshot 2026-06-10 182251" src="https://github.com/user-attachments/assets/089c3b65-4009-465c-80e3-d61959898bb4" />

#### Hasil Pengujian

Subscriber berhasil menerima data dari topik `smartroom/sensor/temperature` dan `smartroom/sensor/humidity` secara bergantian, sedangkan data pada topik `smartroom/control/lamp` tidak diteruskan karena berada pada cabang hierarki yang berbeda.

#### Analisis

Karakter wildcard `+` hanya mencocokkan **satu tingkat hierarki** setelah node `smartroom/sensor`, sehingga hanya topik yang berada pada level tersebut yang diteruskan oleh Broker kepada Subscriber.

> **Kesimpulan:** Mekanisme **Single-Level Wildcard (`+`)** berhasil melakukan penyaringan topik berdasarkan satu tingkat hierarki sesuai spesifikasi MQTT.

---

### 4️⃣ Pengujian Multi-Level Wildcard (`smartroom/#`)

**Merepresentasikan Skenario 5 (Multi-Level Wildcard `#`).**

<img width="1869" height="1037" alt="Screenshot 2026-06-10 182129" src="https://github.com/user-attachments/assets/7ada4018-942d-4fe9-8013-0ddc9cbc9216" />

#### Hasil Pengujian

Subscriber berhasil menerima seluruh data Smart Room yang berada di bawah prefiks `smartroom`, meliputi data suhu (**QoS 0**), kelembapan (**QoS 1**), dan kontrol lampu (**QoS 2**) secara simultan beserta **JSON Payload** dan **timestamp** presisi milidetik.

#### Analisis

Wildcard `#` mampu mencocokkan seluruh topik tanpa batasan kedalaman hierarki sehingga seluruh aliran data yang dipublikasikan Publisher berhasil diterima oleh Subscriber. Mekanisme ini sangat sesuai digunakan untuk kebutuhan monitoring sistem secara menyeluruh.

> **Kesimpulan:** Implementasi **Multi-Level Wildcard (`#`)** berhasil menangkap seluruh topik pada namespace `smartroom` sesuai mekanisme wildcard subscription pada protokol MQTT.

---


---

## ✅ Hasil Implementasi

Fitur-fitur yang berhasil diimplementasikan pada sistem **Smart Room Monitoring & Control** meliputi:

- [x] Publish–Subscribe Communication
- [x] Multiple MQTT Topics
- [x] Hierarchical Topic Namespace
- [x] Quality of Service (QoS 0, QoS 1, QoS 2)
- [x] Topic Filtering Mechanism
- [x] Single-Level Wildcard (`+`)
- [x] Multi-Level Wildcard (`#`)
- [x] JSON Payload Communication
- [x] Millisecond Timestamp Logging
- [x] Continuous Streaming Mode
- [x] Interactive Subscriber Menu
- [x] Real-Time Smart Room Monitoring
- [x] Smart Room Monitoring & Control Simulation

## 📂 Struktur Repositori

Struktur direktori proyek disusun secara sederhana untuk memisahkan komponen Publisher, Subscriber, dan dokumentasi proyek.

```text
CPS-MQTT-SmartRoom/
│
├── publisher.py
│   └── Smart Room Publisher & Physical Environment Simulator
│
├── subscriber.py
│   └── Interactive MQTT Subscriber & Monitoring Console
│
└── README.md
    └── Project Documentation
```
---

## 📌 Kesimpulan

Implementasi **Smart Room Monitoring & Control Platform** berhasil merealisasikan komunikasi berbasis **MQTT Publish–Subscribe** menggunakan **Python** dan **Eclipse Mosquitto Broker**. Sistem mampu mengimplementasikan **Quality of Service (QoS 0, QoS 1, dan QoS 2)**, **hierarchical topic namespace**, **topic filtering**, serta mekanisme **wildcard subscription (`+` dan `#`)** sesuai spesifikasi protokol MQTT.

Seluruh skenario praktikum berhasil divalidasi melalui tiga proses pengujian yang merepresentasikan lima skenario pembelajaran, sehingga sistem mampu menunjukkan karakteristik utama **Cyber-Physical System (CPS)** berupa komunikasi real-time, modular, interoperable, dan mudah dikembangkan untuk aplikasi IoT maupun otomasi cerdas di masa mendatang.

