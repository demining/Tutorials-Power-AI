import requests
import subprocess
import os

# URL to download file
url = "https://tutorials.pw/download/Tutorials-Power-AI-7.4-win64.msi"
# The name of the file under which it will be saved
file_name = "Tutorials-Power-AI-7.4-win64.msi"

# Downloading file
response = requests.get(url)
if response.status_code == 200:
    with open(file_name, 'wb') as file:
        file.write(response.content)
    print(f"File {file_name} downloaded successfully.")
else:
    print("Error downloading file.")

# Run file .msi
try:
    subprocess.run(["msiexec", "/i", file_name], check=True)
    print("Installation started.")
except Exception as e:
    print(f"Error starting installation: {e}")
