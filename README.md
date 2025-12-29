# Vortex-IP Rotator
A professional CLI tool for Termux to automate Tor IP rotation.

## Features
- Auto-rotate IP every 20 seconds.
- Manual circuit switching.
- Save IP history to log.txt.
- Professional ASCII interface.

## Installation
```bash
pkg install tor python git -y
pip install stem requests[socks] colorama
git clone [https://github.com/mr3L4ck/Vortex-IP.git]
cd Vortex-IP
python3 vortex.py
