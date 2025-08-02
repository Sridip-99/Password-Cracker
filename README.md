# 🔐 Password Cracker (ZIP & PDF)

This project demonstrates how to ethically crack password-protected ZIP and PDF files using Python and wordlists. It includes a basic ZIP cracker and a **multi-threaded PDF cracker** for faster performance.

Before starting this project go to your browser & search for-
````
rockyou.txt github
```` 
download it then move the `rockyou.txt` file to the working directory of this project, where the other files exists.\
Now, let's start the project:

> ⚠️ **For educational and ethical use only.** Do **not** use this tool for unauthorized or malicious purposes.

---

## 📁 Project Structure
```bash
Password_cracker/
├── test.pdf                    # Password-protected PDF
├── test.zip                    # Password-protected ZIP
├── rockyou.txt                 # Wordlist file containing possible passwords
├── README.md                   # Project documentation (this file)
├── zip_cracker.py              # Script to brute-force ZIP passwords
└── pdf_cracker_threaded.py     # Multi-threaded script to crack PDF passwords
```
---
## 🚀 Usage
### 1. 🔓 Crack a ZIP File

````
python zip_cracker.py
````

> *zip_cracker.py*

![ZIP file cracker](https://raw.githubusercontent.com/Sridip-99/Password-Cracker/refs/heads/main/snapshots/Screenshot%202025-08-02%20213155.png "ZIP file cracker.py.")

### 📌 Make sure:
* Your ZIP file is named `test.zip`
* already a `test.zip` is given

---

### 2. 🔓 Crack a PDF File (Multi-threaded)

#### 🔧 Requirements:
* ✅ Install Required Library:

````
pip install pikepdf
````
then run this code:

````
python pdf_cracker_threaded.py
````

> *pdf_cracker_threaded.py*

![PDF file cracker](https://raw.githubusercontent.com/Sridip-99/Password-Cracker/refs/heads/main/snapshots/Screenshot%202025-08-02%20213219.png "PDF file cracker.py.")

### 📌 Make sure:
* Your PDF is named `test.pdf`
* already a `test.pdf` is given

---
## 🧠 How It Works

#### 1. ZIP Cracker
Reads passwords from the wordlist one by one.\
Attempts to extract the ZIP file using each password.\
Stops when the correct password is found.

#### 2. PDF Cracker (Multi-threaded)
Utilizes ThreadPoolExecutor to try many passwords concurrently.\
Uses pikepdf to check if the PDF can be opened with each password.\
Stops all threads once a valid password is found.

```bash
✅ Example Output

[❌] Tried: admin
[❌] Tried: 123456
[✅] Password found: chocolate1
```

---
## 🔒 Legal & Ethical Notice
This tool is intended for:\
Learning and demonstration\
Ethical hacking and authorized testing\
Recovering your own forgotten passwords\
⚠️ Do not use this for illegal or unauthorized purposes.

---
## 📬 Author
Made with ❤️ by [Sridip](https://sridiptah99.netlify.app)\
[GitHub](https://github.com/Sridip-99) | [LinkedIn](https://www.linkedin.com/in/sridip-tah99)\
If you like this, ⭐ the repo and feel free to contribute!
