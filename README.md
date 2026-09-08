# 🏦 ATM Python

A beginner Python ATM simulation project built to practice fundamental programming concepts, modular programming, file handling, and basic Git workflow. 🐍💻

## 📌 About

This project is a simple ATM simulation built using Python.

The project allows users to log in using a bank account number and PIN, then perform several basic banking transactions. 💳

The main goal of this project is to practice writing a structured Python program and gradually improve the project through refactoring and modular programming. 🚀

## ✨ Features

* 🔐 Login with account number and PIN
* 💰 Check balance
* 💵 Cash deposit
* 🏧 Cash withdrawal
* 🔑 Change PIN
* 💸 Transfer money between accounts
* 📜 Transaction history
* 💾 Store customer data using text files
* 📝 Store transaction history using text files
* ⚠️ Input validation and basic error handling

## 📂 Project Structure

```text
ATM-PYTHON/
├── main.py
├── data_nasabah.txt
├── data_transaksi.txt
├── .gitignore
└── modules/
    ├── login.py
    ├── menu_atm.py
    ├── pause.py
    ├── cek_saldo.py
    ├── setor_tunai.py
    ├── tarik_tunai.py
    ├── ganti_pin.py
    ├── transfer.py
    ├── catat_transaksi.py
    └── riwayat_transaksi.py
```

### 🧩 Main Files

* `main.py` — Entry point of the program. Loads customer data and starts the login process.
* `data_nasabah.txt` — Stores customer account data.
* `data_transaksi.txt` — Stores transaction history.
* `.gitignore` — Prevents unnecessary Python files such as `__pycache__` from being tracked by Git.

### 🔧 Modules

Each module is responsible for a specific part of the ATM system.

* `login.py` — Handles account and PIN verification.
* `menu_atm.py` — Displays the main ATM menu and connects each transaction feature.
* `cek_saldo.py` — Handles balance checking.
* `setor_tunai.py` — Handles cash deposits.
* `tarik_tunai.py` — Handles cash withdrawals.
* `ganti_pin.py` — Handles PIN changes.
* `transfer.py` — Handles money transfers.
* `catat_transaksi.py` — Records transactions.
* `riwayat_transaksi.py` — Displays transaction history.
* `pause.py` — Provides a pause between menus.

## 🧠 Concepts Used

This project applies several fundamental Python concepts:

* 📦 Variables and data types
* 🔀 `if`, `elif`, and `else`
* 🔁 `while` and `for` loops
* 🎯 `match-case`
* 🧩 Functions
* 📚 Modules and imports
* 🛡️ `try-except`
* 📁 File handling
* 🔤 String manipulation
* 📋 Lists
* ⚙️ Basic data processing
* 🌿 Git and GitHub workflow

## ▶️ How to Run

Make sure Python is installed on your computer. 🐍

Clone the repository, open the project directory, and run:

```bash
python main.py
```

## 🗃️ Data Format

Customer data is stored in `data_nasabah.txt` using the following format:

```text
rekening|pin|nama|saldo
```

Example:

```text
123456789|1234|Arya|2000000
```

Transaction data is stored in `data_transaksi.txt` and uses `|` as a separator.

## 📈 Learning Progress

This project is part of my learning journey in Python programming. 🐍📚

The project started as a simple ATM program and is gradually being improved through:

* 🔨 Refactoring
* 🧩 Modular programming
* 🛡️ Error handling
* 💾 File handling
* 🌿 Git and GitHub workflow

Every improvement is part of the learning process. 🚀

## 📝 Notes

This project is created for learning purposes and is not intended to represent a real banking system.

PINs and customer data are stored as plain text, so this implementation should not be used for a real banking application. ⚠️

---

⭐ **Built as part of my Python learning journey.**
