██████╗  █████╗ ██████╗ ███████╗ ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██████╔╝███████║██████╔╝███████╗ ██╔═══╝ ██╔══██║██╔══██╗╚════██║ ██║     ██║  ██║██║  ██║███████║ ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ PRIVACY ABUSE REPORTING SYSTEM
Copy code

<p align="center">
  <img src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif" width="500">
</p>

---

## 🕵️ PARS — Privacy Abuse Reporting System

**PARS** is an open-source, cross-platform tool designed to combat **privacy abuse**,  
**non-consensual sexual content**, **deepfake impersonation**, and **doxxing** on Telegram.

This project focuses on **ethical reporting**, **evidence generation**, and **user safety**  
without automating or abusing Telegram systems.

---

## 🚨 What This Tool Does

- Analyzes reported Telegram content
- Classifies violation type
- Generates professional abuse reports
- Creates PDF evidence files
- Supports bulk / silent reporting
- Prepares ready-to-send email reports
- Works on mobile (Termux) and desktop systems

---

## ❌ What This Tool Does NOT Do

- ❌ Does NOT hack Telegram
- ❌ Does NOT send reports automatically
- ❌ Does NOT scrape private data
- ❌ Does NOT bypass Telegram security

**All actions are user-controlled and ethical.**

---

## ⚙️ Technologies Used

### Programming Languages
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

### Frameworks & Tools
![Flask](https://img.shields.io/badge/Flask-black?logo=flask)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)

---

## 💻 Supported Operating Systems

![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)
![Windows](https://img.shields.io/badge/Windows-0078D6?logo=windows)
![Android](https://img.shields.io/badge/Android-3DDC84?logo=android&logoColor=black)
![Termux](https://img.shields.io/badge/Termux-000000)

---

## 📸 Screenshots

### Web Interface
![Web UI](screenshots/web_ui.png)

### Bulk / Silent Reporting
![Bulk](screenshots/bulk_result.png)

### CLI Mode
![CLI](screenshots/cli.png)

---

## 📁 Project Structure
Pars/ ├── core/        → classification & legal mapping ├── ui/          → web interface (Flask) ├── report/      → PDF / statistics generator ├── screenshots/ → project screenshots ├── Evidence/    → generated reports (gitignored) ├── cli.py └── README.md
Copy code

---

# ▶️ How To Run (By Platform)

---

## 📱 Android (Termux)

```bash
pkg install python git -y
pip install flask
git clone https://github.com/MRAvarvokiranshare/Pars.git
cd Pars
python ui/web_ui.py
Open in browser:
Copy code

http://127.0.0.1:5000
🐧 Linux
Copy code
Bash
sudo apt install python3 python3-pip git -y
pip3 install flask
git clone https://github.com/MRAvarvokiranshare/Pars.git
cd Pars
python3 ui/web_ui.py
🪟 Windows (PowerShell)
Copy code
Powershell
git clone https://github.com/MRAvarvokiranshare/Pars.git
cd Pars
pip install flask
python ui\web_ui.py
🖥 CLI Mode (All Platforms)
Copy code
Bash
python cli.py
⚖️ Legal & Ethical Disclaimer
This project is provided for educational and ethical purposes only.
Do NOT submit false abuse reports
Do NOT target innocent users
Do NOT use for harassment or political abuse
You are solely responsible for how you use this software.
📜 License
MIT License
⭐ Support the Project
If you believe in fighting digital abuse and protecting privacy, please ⭐ star this repository.
