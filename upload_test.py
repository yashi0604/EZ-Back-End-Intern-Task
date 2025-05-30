import requests

url = "http://127.0.0.1:5000/ops/upload"
file_path = "Yashi IOT presentation.pptx"  # Change this to your actual file path

with open(file_path, 'rb') as f:
    files = {'file': f}
    response = requests.post(url, files=files)

print(response.status_code)
print(response.json())
