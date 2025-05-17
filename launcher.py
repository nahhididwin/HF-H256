# launcher.py
import os
import subprocess

REPO_URL = "https://github.com/..."
FOLDER_NAME = "..."

# Xóa folder cũ nếu có
if os.path.exists(FOLDER_NAME):
    print("[*] Removing old bot folder...")
    subprocess.run(["rm", "-rf", FOLDER_NAME])

# Clone repo
print("[*] Cloning GitHub repo...")
subprocess.run(["git", "clone", REPO_URL])

# Cài thư viện
print("[*] Installing dependencies...")
subprocess.run(["pip", "install", "-r", f"{FOLDER_NAME}/requirements.txt"])

# Chạy bot
print("[*] Launching bot...")
os.chdir(FOLDER_NAME)
subprocess.run(["python", "main.py"])
