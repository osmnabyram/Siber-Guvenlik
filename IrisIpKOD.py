#!/usr/bin/env python3

import os
import time
import sys
import itertools  # Spinner icin gerekli

# Renk Kodlari
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RED = "\033[91m"
MAGENTA = "\033[1;30m"
CYAN = "\033[96m"
MATRIX = GREEN + BOLD
MENU_WHITE = WHITE + BOLD

# Tool Kontrolu
def install_requirements():
    if os.system("which nmap > /dev/null 2>&1") != 0:
        os.system("sudo apt-get install -y nmap")
    if os.system("which nikto > /dev/null 2>&1") != 0:
        os.system("sudo apt-get install -y nikto")

# Yuklenme Animasyonu
def loading_animation():
    os.system("clear")
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    print(f"{MENU_WHITE}Sistem aciliyor ", end="", flush=True)
    for _ in range(20):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.15)
        sys.stdout.write("\b")
    print(f" {MAGENTA}Hosgeldiniz{RESET}\n")
    time.sleep(1)
    os.system("clear")

# ASCII Banner
def show_banner():
    os.system("clear")
    print(MENU_WHITE + r"""
                                     
""" + RESET)

    print(RED + r"""
                           +*#+#*############*#*%*                            
                      +**##%%@@@@@@@@@@@@@@@@@@@@%%##***                       
                   **##%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*#*+                   
                **#%%@%@%@@@@%%##************##%%@@@@@%@#@%#*#*                
             ***%#@@%@%%@##***#######****########***##@%@@%@%%#*#*              
          +*#*%%@@%@%%#*#%#########****###%%%#######%%###%%@%@@%%*#*+        
       +*##%@%@@%@%###%%%%#######****++++*##**#######%%%%##*%@%@@%@###*      
     *#*%%@%@@%%#*#%%%%%%###%######+=--=--=+######%###%%%%%%%*%%%@%@@###**   
   ##*%%@@%@@#*#%%%%%%%%%##%%%####+==+===+==*#####%###%%%%%%%%%%*#@@%@@%%*#* 
 **#%%%@%@%##%@@@@@@@@@@@%%%%%%###*+++*%+*++*####%%%#%%@@@@@@@@@@%##%%%@%%%#*+
*#%%%%@####@@@@@@@@@@@@@@%#%%%%###*===+++===####%%%%%%@@@@@@@@@@@@@%####@%%%#**
###%#*#%###@@@@@@@@@@@@@@%%%%%%%%###+=====+###%%%%%%%@@@@@@@@@@@@@@###%%#*#%%%#
*#####**#*###%%@@@@@@@@@@@%%%%%%%%###########%%%%%%%%@@@@@@@@@@%%%#******#####*
  +***++*+##%##**##%@@@@@@@%#%%%%%%%######%%%%%%%%#%@@@@@@%%####%%%*#+*++**+   
          +*****##%*#**#%@@@%##%%%%%%%%%#%%%%%%%#%@@@%%#*###%##***++           
               +***###%###*#%%%##%#%%%%%%%%%%##%%%#**###%##***+                
                   ++**##%%%%####*##########*#*###%%%##***#+                   
                      +***##%%%%%%%%######%%%%%%%%%#****                       
                          ******##############**+**#*                          
                              +*****######*****+          
""" + RESET)

# Ana Menu
def show_menu():
    print(f"\n{BOLD}{MAGENTA}[TEMEL TARAMA SECENEKLERI]{RESET}")
    print(f"{WHITE}[1] Hizli Tarama")
    print(f"[2] Standart Servis Tarama")
    print(f"[3] OS Tespiti")
    print(f"[4] Tum Portlari Tarama")
    print(f"[5] Guvenlik Zaafiyet Taramasi{RESET}")
    
    print(f"\n{BOLD}{MAGENTA}[OZEL TARAMA YONTEMLERI]{RESET}")
    print(f"{WHITE}[6] Ozel Port Taramasi (Kullanici Tanimli)")
    print(f"[7] Detayli Bilgi Toplama")
    print(f"[8] Firewall Taramasi")
    print(f"[9] Sessiz Tarama")
    print(f"[10] Sessiz Tarama v2")
    print(f"[11] Sinyalsiz Tarama")
    print(f"[12] TCP Disindaki Aciklari Arar{RESET}")
    
    print(f"\n{BOLD}{MAGENTA}[EKSTRALAR]{RESET}")
    print(f"{WHITE}[13] Ping Atma)")
    print(f"[14] Tek Seferde Fazla Bilgi")
    print(f"[15] Firewall Bypass")
    print(f"[16] Yol Gosterme")
    print(f"[17] Narin Bilgi Toplama")
    print(f"[18] Zaafiyet Taramasi")
    print(f"[19] HTTPS Sifrelemesi")
    print(f"[20] Ozel Port Taramasi (Kullanici Tanimli){RESET}")
    
    print(f"\n{RED}[21] Cikis{RESET}")

# Nikto Taramasi
def run_nikto(ip):
    print(MATRIX + "\n--- Nikto Zaafiyet Taramasi Basliyor ---\n" + RESET)
    os.system(f"nikto -h {ip}")
    print(MATRIX + "\n--- Tarama Bitti ---\n" + RESET)

# Ana Fonksiyon
def main():
    install_requirements()
    loading_animation()  # <-- Animasyonu burada cagiyoruz
    
    while True:
        show_banner()
        show_menu()
        try:
            choice = int(input(MENU_WHITE + "Seciminiz (1-21): " + RESET))
        except ValueError:
            print(MATRIX + "Lutfen gecerli bir sayi girin!" + RESET)
            time.sleep(1)
            continue

        if choice == 21:
            print(MAGENTA + "Cikis yapiliyor..." + RESET)
            break

        if choice < 1 or choice > 21:
            print(MATRIX + "Gecersiz secim! Lutfen 1-21 arasinda bir sayi girin." + RESET)
            time.sleep(1)
            continue

        if choice != 18 and choice != 21:  
            ip = input(MENU_WHITE + "Hedef IP veya Host: " + RESET)

        commands = {
            1: f"nmap --top-ports 100 {ip}",
            2: f"nmap -sV {ip}",
            3: f"nmap -O {ip}",
            4: f"nmap -p- {ip}",
            5: f"nmap --script vuln {ip}",
            6: "custom",
            7: f"nmap -sV -O --version-all {ip}",
            8: f"nmap -sA {ip}",
            9: f"nmap -sF {ip}",
            10: f"nmap -sX {ip}",
            11: f"nmap -sN {ip}",
            12: f"nmap -sO {ip}",
            13: f"nmap -sn {ip}",
            14: f"nmap -A {ip}",
            15: f"nmap -f {ip}",
            16: f"nmap --traceroute {ip}",
            17: f"nmap --script=http-enum {ip}",
            19: f"nmap --script=ssl-enum-ciphers {ip}"
        }

        if choice == 18:
            ip = input(MENU_WHITE + "Hedef IP veya Host: " + RESET)
            run_nikto(ip)
        elif choice == 6 or choice == 20:
            ports = input(MENU_WHITE + "Taranacak port araligi (orn: 1-1000): " + RESET)
            print(MATRIX + "\n--- Nmap Taramasi Basliyor ---\n" + RESET)
            os.system(f"nmap -p {ports} {ip}")
            print(MATRIX + "\n--- Tarama Bitti ---\n" + RESET)
        else:
            print(MATRIX + "\n--- Nmap Taramasi Basliyor ---\n" + RESET)
            os.system(commands[choice])
            print(MATRIX + "\n--- Tarama Bitti ---\n" + RESET)

        input(MENU_WHITE + "\nDevam etmek icin Enter'a basin..." + RESET)


if __name__ == "__main__":
    main()
