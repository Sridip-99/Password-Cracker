import zipfile

def crack_zip(zip_file_path, wordlist_path):
    zip_file = zipfile.ZipFile(zip_file_path)

    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            password = line.strip()
            try:
                zip_file.extractall(pwd=bytes(password, 'utf-8'))
                print(f"[✅] Password found: {password}")
                return
            except:
                print(f"[❌] Tried: {password}")
                continue

    print("[-] Password not found in wordlist.")

# Example usage
crack_zip("test.zip", "rockyou.txt")