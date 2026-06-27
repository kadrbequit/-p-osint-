import requests
import json
import socket
import ipaddress
import argparse
import sys
import os
from datetime import datetime
from colorama import init, Fore, Back, Style, just_fix_windows_console
import whois
import dns.resolver
from tabulate import tabulate


init(autoreset=True)
just_fix_windows_console()


BANNER = f"""
{Fore.CYAN}{Style.BRIGHT}
   ██╗██████╗     ██████╗ ███████╗██╗███╗   ██╗████████╗
   ██║██╔══██╗    ██╔══██╗██╔════╝██║████╗  ██║╚══██╔══╝
   ██║██████╔╝    ██████╔╝███████╗██║██╔██╗ ██║   ██║   
   ██║██╔═══╝     ██╔══██╗╚════██║██║██║╚██╗██║   ██║   
   ██║██║         ██║  ██║███████║██║██║ ╚████║   ██║   
   ╚═╝╚═╝         ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
{Fore.YELLOW}          PyCraftTools IP OSINT Tool 
{Fore.GREEN}     GitHub: https://github.com/kadrbequit/-p-osint-.git
{Style.RESET_ALL}
"""

class IPOSINT:
 
    
    def __init__(self, ip_address):
        self.ip = ip_address
        self.results = {}
        self.colors = {
            'info': Fore.CYAN,
            'success': Fore.GREEN,
            'warning': Fore.YELLOW,
            'danger': Fore.RED,
            'highlight': Fore.MAGENTA,
            'dim': Fore.LIGHTBLACK_EX,
            'reset': Style.RESET_ALL
        }
        self.validate_ip()
        
    def validate_ip(self):
        """IP adresini doğrula"""
        try:
            ipaddress.ip_address(self.ip)
        except ValueError:
            print(f"{Fore.RED}❌ Geçersiz IP adresi: {self.ip}{Style.RESET_ALL}")
            sys.exit(1)
            
    def print_header(self, title, color=Fore.CYAN):
        """Başlık yazdır"""
        print(f"\n{color}{Style.BRIGHT}┌{'─' * 50}┐")
        print(f"│ {title.center(48)} │")
        print(f"└{'─' * 50}┘{Style.RESET_ALL}\n")
        
    def print_section(self, title, color=Fore.YELLOW):
        """Bölüm başlığı yazdır"""
        print(f"\n{color}{Style.BRIGHT}▶ {title}{Style.RESET_ALL}")
        print(f"{color}{'─' * 40}{Style.RESET_ALL}")
        
    def print_result(self, key, value, color=Fore.WHITE):
        """Sonuç yazdır"""
        if value and value != 'N/A' and value != '':
            print(f"  {Fore.CYAN}▸ {key}:{Style.RESET_ALL} {color}{value}{Style.RESET_ALL}")
            
    def get_ip_info(self):
        """ip-api.com ile temel IP bilgileri"""
        self.print_section("📍 Coğrafi Konum Bilgileri", Fore.GREEN)
        
        try:
            url = f"http://ip-api.com/json/{self.ip}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,asname,reverse,mobile,proxy,hosting"
            response = requests.get(url, timeout=10)
            data = response.json()
            
            if data.get('status') == 'success':
                
                flag = self.get_country_flag(data.get('countryCode', ''))
                
                print(f"  {Fore.CYAN}🌐 IP Adresi:{Style.RESET_ALL} {Fore.WHITE}{self.ip}{Style.RESET_ALL}")
                print(f"  {Fore.CYAN}🏳️ Ülke:{Style.RESET_ALL} {Fore.WHITE}{flag} {data.get('country', 'N/A')}{Style.RESET_ALL}")
                print(f"  {Fore.CYAN}📍 Bölge/Şehir:{Style.RESET_ALL} {Fore.WHITE}{data.get('regionName', 'N/A')} / {data.get('city', 'N/A')}{Style.RESET_ALL}")
                print(f"  {Fore.CYAN}📮 Posta Kodu:{Style.RESET_ALL} {Fore.WHITE}{data.get('zip', 'N/A')}{Style.RESET_ALL}")
                print(f"  {Fore.CYAN}🗺️ Koordinat:{Style.RESET_ALL} {Fore.WHITE}{data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}{Style.RESET_ALL}")
                print(f"  {Fore.CYAN}🕐 Zaman Dilimi:{Style.RESET_ALL} {Fore.WHITE}{data.get('timezone', 'N/A')}{Style.RESET_ALL}")
                print(f"  {Fore.CYAN}🏢 ISP/Organizasyon:{Style.RESET_ALL} {Fore.WHITE}{data.get('isp', 'N/A')}{Style.RESET_ALL}")
                print(f"  {Fore.CYAN}🔢 AS Numarası:{Style.RESET_ALL} {Fore.WHITE}{data.get('as', 'N/A')}{Style.RESET_ALL}")
                print(f"  {Fore.CYAN}📱 Mobil:{Style.RESET_ALL} {Fore.WHITE}{'✅ Evet' if data.get('mobile') else '❌ Hayır'}{Style.RESET_ALL}")
                print(f"  {Fore.CYAN}🔒 Proxy:{Style.RESET_ALL} {Fore.WHITE}{'⚠️ Evet' if data.get('proxy') else '✅ Hayır'}{Style.RESET_ALL}")
                print(f"  {Fore.CYAN}☁️ Hosting:{Style.RESET_ALL} {Fore.WHITE}{'✅ Evet' if data.get('hosting') else '❌ Hayır'}{Style.RESET_ALL}")
                
                # Google Maps linki
                lat = data.get('lat')
                lon = data.get('lon')
                if lat and lon:
                    print(f"  {Fore.CYAN}🗺️ Harita:{Style.RESET_ALL} {Fore.BLUE}https://www.google.com/maps?q={lat},{lon}{Style.RESET_ALL}")
                
                self.results['geo'] = data
                
            else:
                print(f"  {Fore.RED}❌ Hata: {data.get('message', 'Bilinmeyen hata')}{Style.RESET_ALL}")
                
        except requests.exceptions.Timeout:
            print(f"  {Fore.RED}❌ Bağlantı zaman aşımı!{Style.RESET_ALL}")
        except Exception as e:
            print(f"  {Fore.RED}❌ Hata: {str(e)}{Style.RESET_ALL}")
            
    def get_country_flag(self, country_code):
        """Ülke kodundan bayrak emojisi oluştur"""
        if not country_code:
            return ''
        return ''.join([chr(ord(ch) + 127397) for ch in country_code.upper()])
        
    def reverse_dns(self):
        """Reverse DNS sorgusu"""
        self.print_section("🔍 Reverse DNS", Fore.MAGENTA)
        
        try:
            hostname = socket.gethostbyaddr(self.ip)[0]
            aliases = socket.gethostbyaddr(self.ip)[1]
            
            print(f"  {Fore.CYAN}🏷️ Hostname:{Style.RESET_ALL} {Fore.GREEN}{hostname}{Style.RESET_ALL}")
            if aliases:
                print(f"  {Fore.CYAN}🔗 Aliases:{Style.RESET_ALL} {Fore.WHITE}{', '.join(aliases[:3])}{Style.RESET_ALL}")
                
            self.results['reverse_dns'] = {'hostname': hostname, 'aliases': aliases}
            
        except socket.herror:
            print(f"  {Fore.YELLOW}⚠️ PTR kaydı bulunamadı{Style.RESET_ALL}")
        except Exception as e:
            print(f"  {Fore.RED}❌ Hata: {str(e)}{Style.RESET_ALL}")
            
    def get_whois(self):
        """Whois bilgisi"""
        self.print_section("📋 Whois Bilgileri", Fore.BLUE)
        
        try:
            
            try:
                domain = socket.gethostbyaddr(self.ip)[0]
                if domain:
                    w = whois.whois(domain)
                    
                    print(f"  {Fore.CYAN}🌐 Domain:{Style.RESET_ALL} {Fore.GREEN}{domain}{Style.RESET_ALL}")
                    print(f"  {Fore.CYAN}🏢 Registrar:{Style.RESET_ALL} {Fore.WHITE}{w.registrar or 'N/A'}{Style.RESET_ALL}")
                    
                    if w.creation_date:
                        print(f"  {Fore.CYAN}📅 Oluşturulma:{Style.RESET_ALL} {Fore.WHITE}{w.creation_date}{Style.RESET_ALL}")
                    if w.expiration_date:
                        print(f"  {Fore.CYAN}⏰ Bitiş Tarihi:{Style.RESET_ALL} {Fore.WHITE}{w.expiration_date}{Style.RESET_ALL}")
                    
                    if w.name_servers:
                        ns = w.name_servers[:3]
                        print(f"  {Fore.CYAN}🔄 Name Servers:{Style.RESET_ALL} {Fore.WHITE}{', '.join(ns)}{Style.RESET_ALL}")
                    
                    self.results['whois'] = {'domain': domain, 'data': w}
                else:
                    print(f"  {Fore.YELLOW}⚠️ Domain bilgisi bulunamadı{Style.RESET_ALL}")
                    
            except:
                print(f"  {Fore.YELLOW}⚠️ Whois sorgulanamadı{Style.RESET_ALL}")
                
        except Exception as e:
            print(f"  {Fore.RED}❌ Hata: {str(e)}{Style.RESET_ALL}")
            
    def check_blacklists(self):
        """Kara liste kontrolü"""
        self.print_section("🚫 Kara Liste Kontrolü", Fore.RED)
        
        blacklists = {
            'zen.spamhaus.org': 'Spamhaus',
            'bl.spamcop.net': 'SpamCop',
            'cbl.abuseat.org': 'CBL',
            'dnsbl.sorbs.net': 'SORBS'
        }
        
        reversed_ip = '.'.join(reversed(self.ip.split('.')))
        listed_count = 0
        
        for bl, name in blacklists.items():
            try:
                query = f"{reversed_ip}.{bl}"
                dns.resolver.resolve(query, 'A')
                status = f"{Fore.RED}⚠️ LISTELENMİŞ{Style.RESET_ALL}"
                listed_count += 1
            except dns.resolver.NXDOMAIN:
                status = f"{Fore.GREEN}✅ TEMİZ{Style.RESET_ALL}"
            except:
                status = f"{Fore.YELLOW}❓ SORGULANAMADI{Style.RESET_ALL}"
                
            print(f"  {Fore.CYAN}▸ {name}:{Style.RESET_ALL} {status}")
            
        if listed_count == 0:
            print(f"\n  {Fore.GREEN}✅ IP adresi hiçbir kara listede bulunmuyor!{Style.RESET_ALL}")
        else:
            print(f"\n  {Fore.RED}⚠️ IP adresi {listed_count} kara listede bulunuyor!{Style.RESET_ALL}")
            
        self.results['blacklists'] = {'listed_count': listed_count}
        
    def check_threat_intel(self):
        
        self.print_section("⚠️ Tehdit İstihbaratı", Fore.YELLOW)
        
        
        try:
            
            url = f"https://api.abuseipdb.com/api/v2/check"
            headers = {
                'Accept': 'application/json'
            }
            params = {
                'ipAddress': self.ip,
                'maxAgeInDays': '90'
            }
            
            response = requests.get(url, headers=headers, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if 'data' in data:
                    abuse_data = data['data']
                    score = abuse_data.get('abuseConfidenceScore', 0)
                    
                   
                    if score >= 80:
                        risk_color = Fore.RED
                        risk_level = "KRİTİK"
                    elif score >= 50:
                        risk_color = Fore.YELLOW
                        risk_level = "YÜKSEK"
                    elif score >= 20:
                        risk_color = Fore.YELLOW
                        risk_level = "ORTA"
                    elif score > 0:
                        risk_color = Fore.GREEN
                        risk_level = "DÜŞÜK"
                    else:
                        risk_color = Fore.GREEN
                        risk_level = "TEMİZ"
                    
                    print(f"  {Fore.CYAN}📊 Abuse Score:{Style.RESET_ALL} {risk_color}{score}/100{Style.RESET_ALL}")
                    print(f"  {Fore.CYAN}📈 Risk Seviyesi:{Style.RESET_ALL} {risk_color}{risk_level}{Style.RESET_ALL}")
                    print(f"  {Fore.CYAN}📝 Toplam Rapor:{Style.RESET_ALL} {Fore.WHITE}{abuse_data.get('totalReports', 0)}{Style.RESET_ALL}")
                    
                    if abuse_data.get('lastReportedAt'):
                        print(f"  {Fore.CYAN}🕐 Son Rapor:{Style.RESET_ALL} {Fore.WHITE}{abuse_data.get('lastReportedAt')[:10]}{Style.RESET_ALL}")
                    
                    self.results['threat'] = {
                        'score': score,
                        'level': risk_level,
                        'reports': abuse_data.get('totalReports', 0)
                    }
                    
        except Exception as e:
            print(f"  {Fore.YELLOW}⚠️ Tehdit istihbaratı sorgulanamadı: {str(e)}{Style.RESET_ALL}")
            
    def port_scan(self):
        """Basit port taraması"""
        self.print_section("🔌 Port Taraması (Yaygın Portlar)", Fore.CYAN)
        
        
        common_ports = {
            21: 'FTP',
            22: 'SSH',
            23: 'Telnet',
            25: 'SMTP',
            53: 'DNS',
            80: 'HTTP',
            110: 'POP3',
            143: 'IMAP',
            443: 'HTTPS',
            3306: 'MySQL',
            3389: 'RDP',
            5900: 'VNC',
            8080: 'HTTP-Alt'
        }
        
        open_ports = []
        timeout = 1.5
        
        print(f"  {Fore.YELLOW}⏳ Taranıyor...{Style.RESET_ALL}")
        
        for port, service in common_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            
            try:
                result = sock.connect_ex((self.ip, port))
                if result == 0:
                    open_ports.append((port, service))
                    print(f"  {Fore.GREEN}✅ Port {port} ({service}) - AÇIK{Style.RESET_ALL}")
                sock.close()
            except:
                sock.close()
                
        if not open_ports:
            print(f"  {Fore.YELLOW}⚠️ Açık port bulunamadı{Style.RESET_ALL}")
            
        self.results['ports'] = open_ports
        
    def get_ssl_info(self):
        """SSL sertifika bilgisi (HTTPS portu varsa)"""
        self.print_section("🔒 SSL Sertifika Bilgisi", Fore.MAGENTA)
        
        try:
            import ssl
            
            for port in [443, 8443]:
                try:
                    context = ssl.create_default_context()
                    conn = context.wrap_socket(
                        socket.socket(socket.AF_INET, socket.SOCK_STREAM),
                        server_hostname=self.ip
                    )
                    conn.settimeout(5)
                    conn.connect((self.ip, port))
                    
                    cert = conn.getpeercert()
                    conn.close()
                    
                    if cert:
                        print(f"  {Fore.CYAN}🔐 SSL Aktif (Port {port}){Style.RESET_ALL}")
                        
                        
                        subject = dict(cert.get('subject', []))
                        issuer = dict(cert.get('issuer', []))
                        
                        print(f"  {Fore.CYAN}🏷️ Ortak Ad:{Style.RESET_ALL} {Fore.WHITE}{subject.get('commonName', 'N/A')}{Style.RESET_ALL}")
                        print(f"  {Fore.CYAN}🏢 Düzenleyen:{Style.RESET_ALL} {Fore.WHITE}{issuer.get('organizationName', 'N/A')}{Style.RESET_ALL}")
                        print(f"  {Fore.CYAN}📅 Başlangıç:{Style.RESET_ALL} {Fore.WHITE}{cert.get('notBefore', 'N/A')}{Style.RESET_ALL}")
                        print(f"  {Fore.CYAN}📅 Bitiş:{Style.RESET_ALL} {Fore.WHITE}{cert.get('notAfter', 'N/A')}{Style.RESET_ALL}")
                        
                        self.results['ssl'] = {'port': port, 'cert': cert}
                        break
                        
                except:
                    continue
                    
            if 'ssl' not in self.results:
                print(f"  {Fore.YELLOW}⚠️ SSL sertifikası bulunamadı{Style.RESET_ALL}")
                
        except Exception as e:
            print(f"  {Fore.YELLOW}⚠️ SSL bilgisi alınamadı: {str(e)}{Style.RESET_ALL}")
            
    def ping_test(self):
        """Ping testi"""
        self.print_section("📡 Ping Testi", Fore.GREEN)
        
        try:
            import subprocess
            import platform
            
            
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, '2', '-W', '2', self.ip]
            
            result = subprocess.run(command, capture_output=True, text=True, timeout=5)
            
            if result.returncode == 0:
           
                import re
                
               
                ttl_match = re.search(r'ttl=(\d+)', result.stdout, re.IGNORECASE)
                ttl = ttl_match.group(1) if ttl_match else 'N/A'
                
                
                if platform.system().lower() == 'windows':
                    avg_match = re.search(r'Ortalama = (\d+)ms', result.stdout)
                else:
                    avg_match = re.search(r'avg\s+=\s+([\d.]+)', result.stdout)
                    
                avg_rtt = avg_match.group(1) if avg_match else 'N/A'
                
                print(f"  {Fore.CYAN}📶 Durum:{Style.RESET_ALL} {Fore.GREEN}✅ Erişilebilir{Style.RESET_ALL}")
                print(f"  {Fore.CYAN}⏱️ TTL:{Style.RESET_ALL} {Fore.WHITE}{ttl}{Style.RESET_ALL}")
                print(f"  {Fore.CYAN}⏱️ Ortalama RTT:{Style.RESET_ALL} {Fore.WHITE}{avg_rtt}ms{Style.RESET_ALL}")
                
                self.results['ping'] = {'status': 'reachable', 'ttl': ttl, 'rtt': avg_rtt}
            else:
                print(f"  {Fore.RED}❌ Erişilemiyor{Style.RESET_ALL}")
                self.results['ping'] = {'status': 'unreachable'}
                
        except Exception as e:
            print(f"  {Fore.YELLOW}⚠️ Ping testi yapılamadı: {str(e)}{Style.RESET_ALL}")
            
    def print_summary(self):
        """Özet bilgileri göster"""
        self.print_header("📊 ANALİZ ÖZETİ", Fore.CYAN)
        
        
        stats = [
            ["📍 Konum", self.results.get('geo', {}).get('country', 'N/A')],
            ["🏢 ISP", self.results.get('geo', {}).get('isp', 'N/A')],
            ["🔢 ASN", self.results.get('geo', {}).get('as', 'N/A')],
            ["🏷️ Hostname", self.results.get('reverse_dns', {}).get('hostname', 'N/A')],
            ["📊 Risk Skoru", f"{self.results.get('threat', {}).get('score', 0)}/100"],
            ["⚠️ Risk Seviyesi", self.results.get('threat', {}).get('level', 'N/A')],
            ["🔌 Açık Portlar", len(self.results.get('ports', []))],
            ["🚫 Kara Liste", f"{self.results.get('blacklists', {}).get('listed_count', 0)} liste"]
        ]
        
        for key, value in stats:
            if value and value != 'N/A':
                print(f"  {Fore.CYAN}▸ {key}:{Style.RESET_ALL} {Fore.WHITE}{value}{Style.RESET_ALL}")
                
        print(f"\n  {Fore.GREEN}✅ Analiz tamamlandı!{Style.RESET_ALL}")
        print(f"  {Fore.DIM}📁 Sonuçlar JSON olarak kaydedildi: {self.ip}_report.json{Style.RESET_ALL}")
        
    def save_results(self):
        """Sonuçları JSON olarak kaydet"""
        try:
            filename = f"{self.ip}_report.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"  {Fore.YELLOW}⚠️ Sonuçlar kaydedilemedi: {str(e)}{Style.RESET_ALL}")
            
    def run(self):
        """Tüm analizi çalıştır"""
        
        print(BANNER)
        print(f"{Fore.DIM}{'═' * 60}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🎯 Hedef IP: {Fore.WHITE}{self.ip}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🕐 Zaman: {Fore.WHITE}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")
        print(f"{Fore.DIM}{'═' * 60}{Style.RESET_ALL}")
        
        
        self.get_ip_info()
        self.ping_test()
        self.reverse_dns()
        self.get_whois()
        self.port_scan()
        self.get_ssl_info()
        self.check_blacklists()
        self.check_threat_intel()
        
        
        self.print_summary()
        self.save_results()

def main():
    parser = argparse.ArgumentParser(
        description="IP OSINT Tool - Basit ve Etkili IP Analiz Aracı",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Örnek Kullanımlar:
  python ip_osint.py 8.8.8.8
  python ip_osint.py 192.168.1.1
  python ip_osint.py --help
        """
    )
    
    parser.add_argument('ip', help='Analiz edilecek IP adresi')
    parser.add_argument('-j', '--json', action='store_true', 
                       help='Sadece JSON çıktısı göster')
    
    args = parser.parse_args()
    
    
    tool = IPOSINT(args.ip)
    
    if args.json:
        
        tool.validate_ip()
        tool.get_ip_info()
        tool.reverse_dns()
        tool.get_whois()
        tool.check_blacklists()
        tool.check_threat_intel()
        print(json.dumps(tool.results, indent=2, ensure_ascii=False))
    else:
        tool.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}⚠️ Kullanıcı tarafından durduruldu.{Style.RESET_ALL}")
        sys.exit(0)
