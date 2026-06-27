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


```

🛠️ Gereksinimler

· Python 3.6+
· Internet bağlantısı

📝 Lisans

MIT License - Detaylar için LICENSE dosyasına bakın.

⚠️ Uyarı

Bu araç yalnızca eğitim ve güvenlik testleri amacıyla kullanılmalıdır. Yetkisiz kullanımdan kullanıcı sorumludur.

```
## 🚀 Kurulum

```bash
# Repoyu klonla
git clone  https://github.com/kadrbequit/-p-osint-.git
cd -p-osint-

# Bağımlılıkları yükle
pip install -r requirements.txt

#temel kullanım 
python  İp_osint.py 8.8.8.8
#json çıktısı 
python   İp_osint.py 8.8.8.8 --json
#yardım
python   İp_osint.py --help




# örnek çıktı

   ██╗██████╗     ██████╗ ███████╗██╗███╗   ██╗████████╗
   ██║██╔══██╗    ██╔══██╗██╔════╝██║████╗  ██║╚══██╔══╝
   ██║██████╔╝    ██████╔╝███████╗██║██╔██╗ ██║   ██║   
   ██║██╔═══╝     ██╔══██╗╚════██║██║██║╚██╗██║   ██║   
   ██║██║         ██║  ██║███████║██║██║ ╚████║   ██║   
   ╚═╝╚═╝         ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
          Pycrafttools IP OSINT Tool 

════════════════════════════════════════════════════════════
🎯 Hedef IP: 8.8.8.8
🕐 Zaman: 2024-01-15 14:30:25
════════════════════════════════════════════════════════════

▶ 📍 Coğrafi Konum Bilgileri
────────────────────────────────────────
  🌐 IP Adresi: 8.8.8.8
  🏳️ Ülke: 🇺🇸 United States
  📍 Bölge/Şehir: California / Mountain View
  🗺️ Koordinat: 37.4223, -122.0841
  🕐 Zaman Dilimi: America/Los_Angeles
  🏢 ISP: Google LLC
  🔢 AS Numarası: AS15169

▶ 📡 Ping Testi
────────────────────────────────────────
  📶 Durum: ✅ Erişilebilir
  ⏱️ TTL: 118
  ⏱️ Ortalama RTT: 12.5ms

▶ 🔍 Reverse DNS
────────────────────────────────────────
  🏷️ Hostname: dns.google

▶ 🔌 Port Taraması (Yaygın Portlar)
────────────────────────────────────────
  ⏳ Taranıyor...
  ✅ Port 53 (DNS) - AÇIK
  ✅ Port 443 (HTTPS) - AÇIK

▶ 🔒 SSL Sertifika Bilgisi
────────────────────────────────────────
  🔐 SSL Aktif (Port 443)
  🏷️ Ortak Ad: *.google.com
  🏢 Düzenleyen: Google Trust Services LLC
  📅 Başlangıç: 2024-01-10 00:00:00
  📅 Bitiş: 2024-04-10 23:59:59

▶ 🚫 Kara Liste Kontrolü
────────────────────────────────────────
  ▸ Spamhaus: ✅ TEMİZ
  ▸ SpamCop: ✅ TEMİZ
  ▸ CBL: ✅ TEMİZ
  ▸ SORBS: ✅ TEMİZ

  ✅ IP adresi hiçbir kara listede bulunmuyor!

▶ ⚠️ Tehdit İstihbaratı
────────────────────────────────────────
  📊 Abuse Score: 0/100
  📈 Risk Seviyesi: TEMİZ
  📝 Toplam Rapor: 0

📊 ANALİZ ÖZETİ
────────────────────────────────────────
  ▸ Konum: United States
  ▸ ISP: Google LLC
  ▸ ASN: AS15169
  ▸ Hostname: dns.google
  ▸ Risk Skoru: 0/100
  ▸ Risk Seviyesi: TEMİZ
  ▸ Açık Portlar: 2
  ▸ Kara Liste: 0 liste

  ✅ Analiz tamamlandı!
  📁 Sonuçlar JSON olarak kaydedildi: 8.8.8.8_report.json
