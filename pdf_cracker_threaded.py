import pikepdf
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

found = False
lock = threading.Lock()

def try_password(pdf_path, password):
    global found
    if found:
        return None

    password = password.strip()
    try:
        with pikepdf.open(pdf_path, password=password):
            with lock:
                found = True
            print(f"[✅] Password found: '{password}'")
            return password
    except pikepdf._qpdf.PasswordError:
        print(f"[❌] Tried: '{password}'")
        return None
    except Exception as e:
        print(f"[⚠️] Error with '{password}': {e}")
        return None

def crack_pdf_multithreaded(pdf_path, wordlist_path, max_workers=10):
    global found
    found = False

    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
        passwords = file.readlines()

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(try_password, pdf_path, pwd) for pwd in passwords]

        for future in as_completed(futures):
            result = future.result()
            if result:
                return result

    print("[-] Password not found in wordlist.")
    return None

# Example usage
crack_pdf_multithreaded("test.pdf", "rockyou.txt", max_workers=15)
