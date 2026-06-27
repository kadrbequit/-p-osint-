# # 🕵️ IP OSINT Tool

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Basit, hızlı ve renkli bir IP adresi analiz aracı. Tek bir komutla IP adresi hakkında detaylı bilgi edinin!

## ✨ Özellikler

- 🌍 **Coğrafi Konum**: Ülke, şehir, koordinatlar, zaman dilimi
- 🏢 **ISP & ASN**: Servis sağlayıcı ve Otonom Sistem numarası
- 🔍 **Reverse DNS**: Hostname ve alias bilgileri
- 📋 **Whois**: Domain kayıt bilgileri
- 🚫 **Kara Liste**: Spamhaus, SpamCop, CBL, SORBS kontrolleri
- ⚠️ **Tehdit İstihbaratı**: AbuseIPDB ile risk skoru
- 🔌 **Port Taraması**: Yaygın portların durumu
- 🔒 **SSL Sertifika**: HTTPS sertifika bilgileri
- 📡 **Ping Testi**: Bağlantı durumu ve gecikme
- 🎨 **Renkli Çıktı**: Okunması kolay, renkli terminal çıktısı
- 💾 **JSON Çıktısı**: Sonuçları JSON formatında kaydetme

## 🚀 Kurulum

```bash
# Repoyu klonla
git clone  https://github.com/kadrbequit/-p-osint-.git
cd ip-osint

# Bağımlılıkları yükle
pip install -r requirements.txt

#temel kullanım 
python ip_osint.py 8.8.8.8
#json çıktısı 
python ip_osint.py 8.8.8.8 --json
#yardım
python ip_osint.py --help




