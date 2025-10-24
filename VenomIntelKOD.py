#!/usr/bin/env python3
import os
import sys
import subprocess
import itertools
import time
from time import sleep

# Renkli Yazilar
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RED = "\033[91m"
BOLD = "\033[1m"
WHITE = "\033[97m"
RESET = "\033[0m"
MENU_WHITE = WHITE + BOLD
MATRIX = GREEN + BOLD

def show_banner():
    os.system("clear")
    print(f"""{RED}{BOLD}
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣶⣶⣶⣶⣶⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⢰⣿⣿⣿⣿⣿⣿⣿⣿⠿⢃⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡈⠻⢿⣿⠿⣿⣿⣿⠇⣴⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣶⡆⠀⠀⠀⠀⠉⠀⢿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠙⢛⣉⣍⡛⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣄⣉⠛⣛⡉⠁⠀⠀⣀⣤⣶⣦⣤⣀⣶⠄⣿⣿⣿⣿⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠇⠀⠀⣸⠛⠉⠉⠙⣿⣿⣿⡆⢿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⠟⠀⠀⠀⠁⠀⠀⠀⠀⢸⣿⣿⣿⣮⡻⢿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⢋⣩⣭⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⣠⣶⡾⣿⣟⠛⣋⠁⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠛⣩⣤⣶⣤⣄⡀⠀⢀⣼⣿⠟⠁⣩⣿⣿⢿⣿⡿⣽⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⢧⣾⣿⣿⣿⣿⣿⣿⡄⠻⠿⠁⢠⣾⣿⠟⣡⣾⣿⠛⢮⡛⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⢳⣾⣶⡄⠀⠈⢿⢸⣿⣿⣿⡟⣩⣶⣿⣿⣿⣷⣄⢿⡿⢫⣾⣿⣿⠏⣠⣼⡿⠾⣻⣽⣤⣶⡶⣦⣄⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣤⣴⣾⡿⠃⠈⠛⢿⣦⣀⣈⠈⢿⣿⡏⣼⣿⣿⣿⣿⣿⠿⣛⣂⣀⡛⢿⠟⣡⣾⣿⡿⢁⣾⣿⣿⣿⣿⡷⢹⣿⣿⣿⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⣼⡿⠋⠉⠀⠀⠀⠀⠀⠹⢿⣼⢧⡈⠻⠀⣿⣿⣿⣿⢋⣴⣿⣿⣿⣿⣿⣷⣄⢿⡟⠋⠀⣾⣿⣿⡿⠉⠩⠷⠿⣿⣿⣿⣿⡿⣫⣶⣷⣄⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⠋⠀⢠⣶⣶⣶⣾⣿⣿⣿⣿⣷⡄⣶⣶⣆⣿⣿⣿⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⠁⣀⣤⣶⣜⢿⠁⢸⣷⡄⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣧⣄⠀⠀
⠀⠀⠀⠀⣿⡇⠀⢰⣯⣿⠉⠉⢩⣍⣉⣉⣭⣭⣥⣭⣍⣻⣥⣭⣭⣜⠿⣿⣿⣿⣿⣿⣿⣿⠿⢓⠸⢿⣿⣿⡟⠀⠀⠀⢻⣧⣀⡀⠀⠈⠐⣿⣿⣿⣿⣿⣿⣿⣿⡄
⠀⠀⢀⣼⠿⠁⠀⢸⣿⡇⠀⢸⣿⠿⠟⠿⠿⠿⠿⢿⣿⣟⠛⠛⣻⣥⣴⣶⣄⠉⠛⠿⠟⢱⣿⣿⣿⡄⣀⠈⠀⠀⠀⠀⠈⠉⠛⠁⠀⠀⠀⣹⣿⣿⣿⣿⣿⣿⣿⡇
⣠⡴⠟⠛⠁⠀⠀⢸⣿⡇⠀⣿⣿⠀⠀⢠⣼⣻⣿⣿⣿⣿⣿⣿⠾⣿⠿⠛⠁⣀⣴⣿⣷⠈⣛⠻⠟⠁⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃
⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⢿⣿⡇⢀⣾⣿⡃⠉⠙⠛⠋⠁⠀⠀⠀⠀⠀⣟⡛⠻⣿⡁⠀⣿⣇⠀⠀⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡿⠟⠿⠁⠀⢤⣤⣶⠆
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⢸⣿⡇⠸⣿⣿⡇⠀⠀⠀⣤⠾⠻⣿⣿⣶⣿⣿⣿⣦⠻⠃⠀⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇⠀⠀⠀⢠⣼⣿⡿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠃⢸⣶⠁⢐⡿⠏⠀⠀⠀⢠⣶⣿⣷⠘⠿⠿⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠋⠀⠀⠀⠀⣀⣼⣿⡿⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠜⠉⠀⠀⠀⢻⣧⠘⣿⣦⠀⠀⢠⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⢀⣿⣿⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡏⠀⠘⣿⣧⠀⣾⣿⣿⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠛⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠟⠀⠀⠀⣼⣿⠆⣿⣿⣿⣿⣿⢿⣿⣥⣴⣶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠋⠀⢹⣿⣿⡟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣠⣤⣤⣤⣤⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠈⣿⣿⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⠎⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣋⡉⠉⠛⠉⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣿⣿⣿⣿⣿⠟⠉⢼⣿⣿⣦⣆⢀⣠⣴⣦⣤⡴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠙⠛⠿⠿⠿⠿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

:::      .::..,:::::::::.    :::.    ...     .        :   ::::::.    :::.::::::::::::.,::::::   :::     
';;,   ,;;;' ;;;;''''`;;;;,  `;;; .;;;;;;;.  ;;,.    ;;;  ;;;`;;;;,  `;;;;;;;;;;;'''';;;;''''   ;;;     
 \[[  .[[/    [[cccc   [[[[[. '[[,[[     \[[,[[[[, ,[[[[, [[[  [[[[[. '[[     [[      [[cccc    [[[     
  Y$c.$$'     $$''''   $$$ 'Y$c$$$$$,     $$$$$$$$$$$'$$$ $$$  $$$ 'Y$c$$     $$      $$''''    $$'     
   Y88P       888oo,__ 888    Y88'888,_ _,88P888 Y88' 888o888  888    Y88     88,     888oo,__ o88oo,.__
    MP        ''''YUMMMMMM     YM  'YMMMMMP' MMM  M'  'MMMMMM  MMM     YM     MMM     'YUMMM'' '''YUMMM


{RESET}""")

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
    sleep(1)
    os.system("clear")

def clear_screen():
    os.system("clear")

def wait_for_enter():
    input(f"\033[1m\033[97m\nAna menuye donmek icin Enter basin...{RESET}")
    clear_screen()

def sherlok(username):
    clear_screen()
    print(f"{GREEN}[+] Sherlock ile username taramasi baslatiliyor...{RESET}")
    os.system(f"sherlock --verbose {username}")
    wait_for_enter()

def holehe(email):
    clear_screen()
    print(f"{GREEN}[+] Holehe ile e-posta kontrolu baslatiliyor...{RESET}")
    os.system(f"holehe {email}")
    wait_for_enter()

def socialscan(target):
    clear_screen()
    print(f"{GREEN}[+] SocialScan ile tarama baslatiliyor...{RESET}")
    os.system(f"socialscan {target}")
    wait_for_enter()
   
def whatsmyname(username):
    clear_screen()
    print(f"{GREEN}[+] WhatsMyName ile username kontrolu baslatiliyor...{RESET}")
    subprocess.run(["xdg-open", "https://whatsmyname.app/"])
    wait_for_enter()

def waybackmachine(url):
    clear_screen()
    print(f"{GREEN}[+] WaybackMachine ile tarama baslatiliyor...{RESET}")
    subprocess.run(["xdg-open", f"https://web.archive.org/web/*/{url}"])
    wait_for_enter()


def photon(url):
    clear_screen()
    print(f"{GREEN}[+] Photon ile web taramasi baslatiliyor...{RESET}")
    os.system(f"photon -u {url} --wayback")
    wait_for_enter()

def spiderfoot():
    clear_screen()
    print(f"{GREEN}[+] SpiderFoot web arayuzu aciliyor...{RESET}")
    os.system("spiderfoot -l 127.0.0.1:5001")
    print(f"{RED}Konsolda calisiyor! Tarayiciyla `http://127.0.0.1:5001` acin.{RESET}")
    wait_for_enter()

def shodan():
    clear_screen()
    print(f"{GREEN}[+] Shodan websitesi aciliyor...{RESET}")
    subprocess.run(["xdg-open", "https://www.shodan.io"])
    wait_for_enter()

def maltego():
    clear_screen()
    print(f"{GREEN}[+] Maltego baslatiliyor...{RESET}")
    os.chdir(os.path.expanduser("~/Downloads/maltego_4.10.0/bin"))
    os.system("./maltego")
    wait_for_enter()
    
def face_and_storage():
    clear_screen()
    print(f"{GREEN}[+] PYM aciliyor...{RESET}")
    subprocess.run(["xdg-open", "https://pimeyes.com/"])
    subprocess.run(["xdg-open", "https://yandex.com/images/"])
    subprocess.run(["xdg-open", "https://mega.io/"])
    wait_for_enter()

def osint_framework():
    clear_screen()
    print(f"{GREEN}[+] OSINT Framework websitesi aciliyor...{RESET}")
    subprocess.run(["xdg-open", "https://osintframework.com/"])
    wait_for_enter()

def menu():
    clear_screen()
    show_banner()
    print(f"{WHITE}1) Username Tarama (Sherlock){RESET}")
    print(f"{WHITE}2) E-posta Kontrol (Holehe){RESET}")
    print(f"{WHITE}3) SocialScan Tarama (S+H){RESET}")
    print(f"{WHITE}4) WhatsMyName{RESET}")
    print(f"{WHITE}5) Photon Web Tarama{RESET}")
    print(f"{WHITE}6) SpiderFoot Baslat{RESET}")
    print(f"{WHITE}7) Shodan{RESET}")
    print(f"{WHITE}8) Maltego{RESET}")
    print(f"{WHITE}9) PYM{RESET}")
    print(f"{WHITE}10) WaybackMachine{RESET}")
    print(f"""{RED}{BOLD}
0)Cikis{RESET}""")

def main():
    loading_animation()
    while True:
        menu()
        choice = input(f"\n{GREEN}Seciminiz (0-10): {RESET}")

        if choice == "0":
            clear_screen()
            print(f"{RED}Cikis yapiliyor...{RESET}")
            break
        elif choice == "1":
            username = input(f"{WHITE}Username: {RESET}")
            sherlok(username)
        elif choice == "2":
            email = input(f"{WHITE}E-posta: {RESET}")
            holehe(email)
        elif choice == "3":
            target = input(f"{WHITE}Username/E-posta: {RESET}")
            socialscan(target)
        elif choice == "4":
            username = input(f"{WHITE}Username: {RESET}")
            whatsmyname(username)
        elif choice == "5":
            url = input(f"{WHITE}Website URL: {RESET}")
            photon(url)
        elif choice == "6":
            spiderfoot()
        elif choice == "7":
            shodan()
        elif choice == "8":
            maltego()
        elif choice == "9":
            face_and_storage()
        elif choice == "10":
            url = input(f"{WHITE}Website URL: {RESET}")
            waybackmachine(url)
        else:
            clear_screen()
            print(f"{RED}Hatali girdi!{RESET}")

        sleep(1)

if __name__ == "__main__":
    if os.getuid() != 0:
        print(f"{RED}[!] Root yetkisi gerekli! (sudo){RESET}")
        sys.exit(1)
    main()
