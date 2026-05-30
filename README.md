# 🔐 Password Manager Encryption

> **Python Programming Internship Project** | Secure password storage with encryption & GUI

---

## 🎓 Internship Details

| Field | Information |
|-------|-------------|
| **Internship Name** | Python Programming Internship |
| **Intern Name** | Sakshi Sorte |
| **Intern ID** | CITS1852 |

*Technologies Learned** | Python, Tkinter, Cryptography, File Handling, Git/GitHub |

---

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/platform-cross--platform-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg)

---

## 📑 Table of Contents

- [About](#-about)
- [Internship Details](#-internship-details)
- [Features](#-features)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Advantages](#-advantages)
- [Conclusion](#-conclusion)
- [Repository](#-repository)
- [Contact](#-contact)

---

## 🧭 About

The **Password Manager Encryption** project is a Python-based desktop application designed to securely store and manage passwords using encryption techniques. Built during a Python Programming Internship, this project demonstrates strong security practices while providing a simple, user-friendly GUI interface for saving and managing passwords safely.

---

## 🖼️ Demo

![Password Manager Screenshot](Screenshot.png)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔒 **Secure Storage** | Passwords are encrypted before storage |
| 🧩 **Cryptography** | Uses `cryptography.fernet` for strong encryption |
| 🎲 **Password Generator** | Generates strong random passwords automatically |
| 🖥️ **GUI Interface** | User-friendly Tkinter desktop interface |
| 💾 **Easy Management** | Save, view, and manage passwords effortlessly |
| 🛡️ **Secure File Handling** | Encrypted files prevent unauthorized access |

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| **Language** | Python 3.x |
| **GUI Framework** | Tkinter (built-in) |
| **Encryption** | `cryptography` (Fernet) |
| **Modules** | `os`, `random`, `string`, `messagebox` |
| **IDE** | VS Code |
| **Version Control** | GitHub |

### Key Modules Used

```python
from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import os
import random
import string
```

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package manager)

### Step-by-Step Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/password-manager-encryption.git
   cd password-manager-encryption
   ```

2. **Install required library:**
   ```bash
   pip install cryptography
   ```

3. **Run the program:**
   ```bash
   python password_manager.py
   ```

---

## 🚀 Usage

1. **Launch the application:**
   ```bash
   python password_manager.py
   ```

2. **The program will:**
   - Generate or load a secret encryption key (`secret.key`)
   - Display the GUI interface for password management

3. **Features you can use:**
   - 🔐 **Add Password:** Enter website/username/password and save
   - 🎲 **Generate Password:** Create strong random passwords
   - 📋 **View Passwords:** See your stored (encrypted) passwords
   - 💾 **Save Securely:** All passwords stored in encrypted format

---

## ⚙️ How It Works

1. The program generates or loads a secret encryption key (`secret.key`)
2. Passwords entered by the user are **encrypted** using Fernet symmetric encryption
3. Encrypted passwords are **stored securely** in a file
4. Users can manage and save passwords safely
5. Random strong passwords can be generated using `random` + `string` modules

---

## 📁 Project Structure
password-manager-encryption/
├── README.md # This file (professional documentation)
├── password_manager.py # Main application script
├── Screenshot.png # Application screenshot (GUI demo)
├── secret.key # Encryption key (auto-generated)
└── requirements.txt # Dependencies (optional)


---

## ✅ Advantages

| Advantage | Impact |
|-----------|--------|
| 🔒 **Improves Password Security** | Prevents unauthorized access to sensitive data |
| 🎯 **Easy to Use** | Intuitive GUI requires no technical expertise |
| 🛡️ **Prevents Password Theft** | Encryption makes stolen data useless |
| 💾 **Supports Encrypted Storage** | Passwords stored in unreadable format |
| 📚 **Learning Value** | Great for understanding cybersecurity & encryption concepts |

---

## 🎯 Conclusion

The **Password Manager Encryption** project was successfully developed using Python during the Python Programming Internship. This project helps users securely store and manage passwords using encryption techniques.

**Key Learnings:**
- Python programming & GUI development (Tkinter)
- File handling & secure storage practices
- Cryptography & encryption concepts (Fernet symmetric encryption)
- Cybersecurity fundamentals
- Version control with Git & GitHub

---

## 📂 Repository

**GitHub Repository:** [password-manager-encryption](https://github.com/<your-username>/password-manager-encryption)

---

