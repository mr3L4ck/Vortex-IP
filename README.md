<h1 align="center">VORTEX-IP ROTATOR</h1>

<p align="center">
  <img src="https://img.shields.io/badge/MADE%20IN-BANGLADESH-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/TOOL-IP%20CHANGER-green?style=for-the-badge">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0-blue">
  <img src="https://img.shields.io/badge/Maintained%3F-yes-brightgreen">
  <img src="https://img.shields.io/badge/License-MIT-yellow">
</p>

<p align="center">
  <b>Created by: Mr. 3L4CK</b><br>
  <i>"This Tool Only for Educational purpose"</i>
</p>

---

### 🔗 ABOUT TOOL :
Vortex-IP is a professional CLI tool developed for Linux to automate the Tor network identity. It helps users to change their public IP address automatically at specific intervals (every 20 seconds) to maintain anonymity.

### 🔗 AVAILABLE ON :
* **Termux**
* **Linux**

### 🔗 TESTED ON :
* **Termux (Android)**
* **Kali Linux**
* **Ubuntu**
* **Debian**
* **Arch Linux**
 
### 🔗 REQUIREMENTS :
* **Internet Connection**
* **Tor Service**
* **Python 3.x**
* **Storage Permission**

### 🔗 FEATURES :
* **[+]** Auto Rotate IP every 20 seconds!
* **[+]** Manual Circuit Change option!
* **[+]** Professional ASCII Banner!
* **[+]** Save IP History to `log.txt`!
* **[+]** Easy to use CLI Interface!

### 🔗 INSTALLATION :

```bash
pkg update && pkg upgrade
pkg install tor python git -y
pip install stem requests[socks] colorama
git clone https://github.com/mr3L4ck/Vortex-IP
cd Vortex-IP
tor -f torrc
python3 vortex.py

