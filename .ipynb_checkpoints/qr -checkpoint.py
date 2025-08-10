import os
from PIL import Image

print("Current working directory:", os.getcwd())

logo_path = r"C:\Users\chouh\OneDrive\Scans\Qr Generative\logo.png"

if os.path.exists(logo_path):
    logo = Image.open(logo_path).resize((50, 50))

else:
    print(f"Error: logo file not found at {logo_path}")

