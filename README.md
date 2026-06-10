# 🏢 Cyber-Physical System: Smart Room Monitoring & Control Platform

Beneath the cyber-physical loop, timing and reliability dictate system safety. Repositori ini berisi implementasi sistem **Cyber-Physical Systems (CPS)** untuk platform *Smart Room Monitoring & Control* menggunakan protokol **MQTT**, bahasa pemrograman **Python**, dan **Eclipse Mosquitto Broker**. 

Proyek ini mengintegrasikan representasi data fisik lingkungan nyata ke dalam ruang siber secara interaktif, paralel (*concurrent*), dan dinamis.

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
Proyek ini dirancang untuk mensimulasikan lingkungan kamar pintar (*Smart Room*) di mana entitas fisik (suhu, kelembapan, status sakelar) dipetakan secara *real-time* ke dalam ruang siber melalui arsitektur jaringan terdistribusi berbasis **Publish-Subscribe**. 

Berbeda dengan sistem simulasi IoT standar, platform ini mengadopsi prinsip ketat perangkat lunak **Cyber-Physical Systems (CPS)**:
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
Physical Plant: Entitas fisik kamar pintar yang memancarkan parameter termal lingkungan.

Sensing & Telemetry: publisher.py melakukan digitalisasi dan serialisasi besaran analog menjadi objek terstruktur (JSON Payload).

Cyber Network: Mosquitto Broker mengelola tabel routing data siber dan menjaga keandalan paket berdasarkan tingkat QoS.

Cyber Controller: subscriber.py menangkap, melakukan parsing JSON, dan menganalisis aliran data masuk untuk kebutuhan monitoring ataupun keputusan aktuasi sakelar.

---

## ⚙️ Manajemen Topik & Matriks QoS
Penentuan tingkat Quality of Service (QoS) disesuaikan secara logis berdasarkan karakteristik kekritisan data (data criticality) pada sistem siber-fisik:
No,Entitas Fisik,Topik MQTT,Level QoS,Justifikasi Karakteristik Data
1,Sensor Suhu,smartroom/sensor/temperature,QoS 0,At Most Once. Bersifat periodik kontinu. Kehilangan satu sampel data (data loss) tidak akan mengganggu stabilitas kontrol sistem siber.
2,Sensor Kelembapan,smartroom/sensor/humidity,QoS 1,At Least Once. Menjamin data kelembapan lingkungan tersampaikan ke pusat siber minimal satu kali melalui mekanisme handshake paket PUBACK.
3,Aktuator Lampu,smartroom/control/lamp,QoS 2,Exactly Once. Bersifat Safety-Critical. Instruksi sakelar fisik wajib dieksekusi tepat satu kali untuk menghindari kondisi desinkronisasi status fisik yang berbahaya.
