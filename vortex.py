import time
import os
import sys
import subprocess
import requests
from stem import Signal
from stem.control import Controller
from colorama import Fore, Style, init

init(autoreset=True)

# Configuration
CONTROL_PORT = 9051
SOCKS_PORT = 9050
PROXIES = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}

def clear():
    os.system('clear')

def banner():
    clear()
    print(f"""{Fore.RED}
         _   _
        (q\_/p)     {Fore.CYAN}--- VORTEX-IP ---
         \_ " _/    {Fore.WHITE}Created by: Mr. 3L4CK
         / _ \      {Fore.WHITE}Status: {Fore.GREEN}Active
        / / \ \ 
    ___(_/---\_)_________________________________
    
    {Fore.YELLOW}[!] This Tool Only for Educational purpose [!]
    """)

def setup_tor():
    """স্বয়ংক্রিয়ভাবে Tor কনফিগার করার জন্য"""
    print(f"{Fore.YELLOW}[*] Configuring Tor Engine...")
    config = "ControlPort 9051\nCookieAuthentication 1\nSocksPort 9050\nMaxCircuitDirtiness 20"
    with open("torrc", "w") as f:
        f.write(config)
    print(f"{Fore.GREEN}[+] Tor Configured! Now run 'tor -f torrc' in another tab.")
    time.sleep(3)

def update_tool():
    """গিটহাব থেকে সরাসরি আপডেট করার জন্য"""
    print(f"{Fore.YELLOW}[*] Checking for updates...")
    try:
        subprocess.run(["git", "pull", "origin", "main"], check=True)
        print(f"{Fore.GREEN}[+] Update Successful! Restarting...")
        time.sleep(2)
        os.execv(sys.executable, ['python'] + sys.argv)
    except:
        print(f"{Fore.RED}[!] Update failed. Make sure git is installed.")
        time.sleep(2)

def get_ip():
    try:
        return requests.get('https://api.ipify.org', proxies=PROXIES, timeout=10).text.strip()
    except:
        return None

def rotate():
    try:
        with Controller.from_port(port=CONTROL_PORT) as con:
            con.authenticate()
            con.signal(Signal.NEWNYM)
            return True
    except:
        return False

def main_menu():
    while True:
        banner()
        print(f"{Fore.WHITE}[1] Auto Tor (20s Rotation)")
        print(f"{Fore.WHITE}[2] Change New Circuit")
        print(f"{Fore.WHITE}[3] Save log.txt")
        print(f"{Fore.WHITE}[4] Auto-Setup Tor Config")
        print(f"{Fore.WHITE}[5] Update Tool")
        print(f"{Fore.WHITE}[0] Exit")
        
        choice = input(f"\n{Fore.RED}3L4CK@Vortex ~> {Fore.WHITE}")

        if choice == '1':
            print(f"\n{Fore.GREEN}[*] Auto-rotation started...")
            try:
                while True:
                    if rotate():
                        time.sleep(5)
                        print(f"{Fore.BLUE}[+] New IP: {get_ip()}")
                        time.sleep(15)
                    else:
                        print(f"{Fore.RED}[!] Error: Tor is not running!")
                        break
            except KeyboardInterrupt: pass
        elif choice == '2':
            if rotate():
                print(f"{Fore.GREEN}[+] Circuit Changed!")
            else:
                print(f"{Fore.RED}[!] Failed. Start Tor first.")
            time.sleep(2)
        elif choice == '3':
            ip = get_ip()
            with open("log.txt", "a") as f:
                f.write(f"{time.ctime()} : {ip}\n")
            print(f"{Fore.GREEN}[+] IP saved to log.txt")
            time.sleep(2)
        elif choice == '4':
            setup_tor()
        elif choice == '5':
            update_tool()
        elif choice == '0':
            sys.exit()

if __name__ == "__main__":
    main_menu()

