IrisIp:
Hedef IP/host üzerinde ağ keşfi ve zafiyet taramaları yapmak için Nmap ve Nikto gibi araçları kullanan menü tabanlı bir araçtır.

Özellikler :
- Port tarama: açık portları ve servisleri tespit etmek için.
- Servis/versiyon tespiti: hangi servislerin hangi sürümde çalıştığını öğrenmek için.
- İşletim sistemi tespiti: hedefin olası işletim sistemini belirlemek için.
- Zafiyet tarama: Nmap script'leri ve Nikto ile bilinen açıklıkları araştırmak için.
- Traceroute / firewall tespiti: ağ yolunu ve olası engelleyicileri analiz etmek için.

 <img width="1920" height="1080" alt="Screenshot_2025-10-24_19_20_13" src="https://github.com/user-attachments/assets/3431f133-2478-4721-a392-da97ca5473b1" />
 
 -------------------------------
 
NetSpider:
Aircrack-ng araç setini kullanarak kablosuz ağları tarayan, monitör moda alan ve WPA/WPA2 handshake yakalama süreçlerini otomatikleştiren bir betiktir.

Özellikler :
- Adaptör kontrolü ve monitör modu: paket yakalamak ve dinleme için.
- Ağ keşfi (airodump): çevredeki SSID/BSSID ve kanalları listelemek için.
- Deauthentication saldırısı: hedef istemcilerden handshake almak amacıyla bağlantıları koparmak için.
- Handshake yakalama ve .cap dosyası oluşturma: parola kırma için gerekli veriyi toplamak amacıyla.
- Bruteforce entegrasyonu: yakalanan handshake üzerinde parola denemeleri yapmak için.
  
<img width="1920" height="1080" alt="Screenshot_2025-10-24_19_20_16" src="https://github.com/user-attachments/assets/6b9a0a47-e849-43d0-8b37-7a00f29e060b" />

-------------------------------

Owl:
Çalıştırıldığında kullanıcının anonim/izinli test ortamını başlatmaya yönelik görevleri otomatikleştiren kısa bir başlatıcıdır. ASCII sanat ve başlatma animasyonu gösterir; OpenVPN yapılandırmasını ve Tor servislerini ayrı terminallerde başlatmayı otomatikleştirir.

Özellikler :
- Başlatma animasyonu ve ASCII sanat: kullanıcıya görsel geri bildirim ve hoş geldiniz ekranı sunmak için.
- OpenVPN oturumu başlatma: belirli bir .ovpn yapılandırmasını kullanarak VPN bağlantısı açmak için (sudo gerekebilir).
- Tor servisini başlatma: ağ trafiğini Tor üzerinden yönlendirmek amacıyla Tor'u çalıştırmak için.
- Terminal otomasyonu (gnome-terminal): OpenVPN ve Tor komutlarını ayrı GUI terminallerinde otomatik başlatmak için.
- Zamanlama/delays: hizmetlerin sıralı başlatılması için bekleme süreleri kullanmak.

  <img width="1920" height="1080" alt="Screenshot_2025-10-24_19_20_24" src="https://github.com/user-attachments/assets/67da6147-8cea-4b2d-9344-f0ff5ec72d34" />

-------------------------------
QuiteCat:
Metasploit’in exploit/multi/handler modülünü kullanarak ters bağlantıları yakalamayı ve Meterpreter oturumlarını yönetmeyi kolaylaştıran bir arayüzdür.

Özellikler (ne için):
- LHOST/LPORT yönetimi: dinleyici ayarlarını yapılandırmak için.
- msfconsole başlatma/handler yönetimi: reverse shell/meterpreter oturumlarını yakalamak için.
- Meterpreter cheat-sheet: oturum esnasında sık kullanılan komutları hızlıca uygulamak için rehber.
- Otomasyon kısayolları: farklı payload/handler senaryolarını hızlandırmak için.

<img width="1920" height="1080" alt="Screenshot_2025-10-24_19_20_31" src="https://github.com/user-attachments/assets/ea9661c2-be17-400d-b8ac-1a34b36c3f65" />

-------------------------------

Scamp:
Yerelde bir TCP dinleyicisi kurup bağlanan istemcilerden gelen verileri (ör. keylogger çıktıları) alıp gösteren basit bir ağ dinleme aracıdır.

Özellikler :
- Soket dinleme: belirtilen HOST:PORT üzerinden gelen bağlantıları kabul etmek için.
- Veri yakalama ve gösterim: bağlantıdan gelen metinsel verileri canlı görüntülemek için.
- Keylogger simülasyonu/entegrasyonu: test ortamında tuş vuruşu verilerini almak için.
- Basit durum animasyonu/loglama: dinleme durumunu ve bağlantı aktivitelerini izlemek için.

<img width="1920" height="1080" alt="Screenshot_2025-10-24_19_20_33" src="https://github.com/user-attachments/assets/00c4496a-517f-4198-a307-d1a5c5921fe5" />

-------------------------------

VenomIntel:
OSINT toplama görevlerini kolaylaştırmak için Sherlock, Holehe, Photon vb. araçları tek bir menü altında birleştiren bir bilgi toplama aracıdır.

Özellikler :
- Username taraması (Sherlock): bir kullanıcı adının birçok platformda kullanılıp kullanılmadığını kontrol etmek için.
- E-posta sorgulama (Holehe): bir e-postanın hangi servis/hesaplarda kayıtlı olduğunu tespit etmek için.
- Web tarama/crawl (Photon): hedef web sitelerinin içerik ve yapı bilgilerini toplamak için.
- Ek entegrasyonlar (SpiderFoot, Shodan, Maltego): daha derin altyapı ve istihbarat sorgulamaları başlatmak için kısayollar.
- Wayback (geçmiş sürümler): URL'lerin geçmişteki hallerini incelemek ve değişiklikleri takip etmek için.

  <img width="1920" height="1080" alt="Screenshot_2025-10-24_19_20_36" src="https://github.com/user-attachments/assets/cdf4f768-0b1a-4c7f-ac83-0ca2cdfe4ae6" />

