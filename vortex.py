import time
import os
import sys
import requests
from stem import Signal
from stem.control import Controller
from colorama import Fore, Style, init

init(autoreset=True)

# Configuration Constants
CONTROL_PORT = 9051
SOCKS_PORT = 9050
PROXIES = {
    'http': f'socks5h://127.0.0.1:{SOCKS_PORT}',
    'https': f'socks5h://127.0.0.1:{SOCKS_PORT}'
}

def clear():
    os.system('clear')

def banner():
    clear()
    # The "Rat hiding in a hole" ASCII art
    print(f"""{Fore.RED}
       _     _
      (o)___(o)     {Fore.WHITE}Tool: VORTEX-IP
       (     )      {Fore.WHITE}Created by: Mr. 3L4CK
        (www)       {Fore.WHITE}Status: {Fore.GREEN}Active
    {Fore.RED}     \_/        
    {Fore.YELLOW}  ---[ ]---     {Fore.WHITE}"This Tool Only for Educational purpose"
    """)

def get_ip():
    try:
        return requests.get('https://api.ipify.org', proxies=PROXIES, timeout=10).text.strip()
    except:
        return "Connection Error"

def save_log(ip_address):
    with open("log.txt", "a") as f:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] IP: {ip_address}\n")

def rotate_circuit():
    try:
        with Controller.from_port(port=CONTROL_PORT) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
            return True
    except:
        return False

def auto_tor():
    print(f"\n{Fore.CYAN}[*] Starting Auto Rotation (20s interval)...")
    try:
        while True:
            rotate_circuit()
            time.sleep(3) # Wait for circuit build
            current_ip = get_ip()
            print(f"{Fore.GREEN}[+] New IP: {current_ip}")
            time.sleep(17)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Stopping Auto Tor...")

def main():
    while True:
        banner()
        print(f"{Fore.WHITE}[1] Auto Tor (Rotate every 20s)")
        print(f"{Fore.WHITE}[2] Change New Circuit (Manual)")
        print(f"{Fore.WHITE}[3] Save Current IP to log.txt")
        print(f"{Fore.WHITE}[4] Exit")
        
        choice = input(f"\n{Fore.YELLOW}vortex@3L4CK ~> {Fore.WHITE}")

        if choice == '1':
            auto_tor()
        elif choice == '2':
            print(f"{Fore.BLUE}[*] Requesting new circuit...")
            if rotate_circuit():
                time.sleep(3)
                print(f"{Fore.GREEN}[+] Success! IP: {get_ip()}")
            else:
                print(f"{Fore.RED}[!] Failed to connect to Tor.")
            input("\nPress Enter to continue...")
        elif choice == '3':
            ip = get_ip()
            save_log(ip)
            print(f"{Fore.GREEN}[+] IP {ip} saved to log.txt")
            input("\nPress Enter to continue...")
        elif choice == '4':
            print(f"{Fore.RED}[!] Shutting down...")
            sys.exit()
        else:
            print(f"{Fore.RED}[!] Invalid choice.")
            time.sleep(1)

if __name__ == "__main__":
    main()
