# Tugas Praktikum CPS: Implementasi MQTT - Smart Room

Sistem *Cyber Physical System* (CPS) ini menggunakan protokol MQTT untuk memantau sensor dan mengendalikan aktuator ruangan secara *real-time*.

## Prasyarat
1. Mosquitto Broker berjalan di `localhost:1883`.
2. Python library terinstal: `pip install paho-mqtt`

## Cara Menjalankan
1. Buka Terminal 1, jalankan: `python subscriber.py`
2. Buka Terminal 2, jalankan: `python publisher.py`