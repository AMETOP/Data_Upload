import os
import time
import subprocess

file_path = "file.json"
remote_repository = "https://github.com/DrDoXi/Test_Git_automation.git"

while True:
    previous_modification_time = os.path.getmtime(file_path)
    time.sleep(2)
    current_modification_time = os.path.getmtime(file_path)
    if current_modification_time != previous_modification_time:
        subprocess.run(["git", "add", file_path])
        subprocess.run(["git", "commit", "-m", "Automatic commit"])
        subprocess.run(["git", "push", "-u", remote_repository, "HEAD"])
