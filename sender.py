import os
import time
from datetime import datetime
from PIL import Image
import pyautogui
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the receiver URLs from the .env file
receiver_urls_env = os.getenv("RECEIVER_URLS", "")

if not receiver_urls_env:
    raise ValueError("RECEIVER_URLS is not set in the .env file. Provide at least one URL.")

# Split URLs into a list (handles single or multiple URLs)
RECEIVER_URLS = [url.strip() for url in receiver_urls_env.split(",") if url.strip()]

if not RECEIVER_URLS:
    raise ValueError("No valid URLs found in RECEIVER_URLS.")

# Screenshot capturing function
def capture_screenshot():
    screenshot = pyautogui.screenshot()
    filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    screenshot.save(filename)
    print(f"Screenshot saved as {filename}")
    return filename

# File upload function
def send_screenshot_via_http(filename, server_url):
    with open(filename, 'rb') as file:
        try:
            response = requests.post(
                server_url,
                files={'file': file},
                timeout=10  # Timeout for network requests
            )
            print(f"Sent to {server_url}. Response: {response.json()}")
        except Exception as e:
            print(f"Failed to send file {filename} to {server_url}: {e}")

# Scheduler task
def take_and_send_screenshot():
    filename = capture_screenshot()
    for server_url in RECEIVER_URLS:
        send_screenshot_via_http(filename, server_url)
    os.remove(filename)  # Clean up the local screenshot file

# Run periodically
if __name__ == '__main__':
    while True:
        take_and_send_screenshot()
        time.sleep(20)  # Wait 20 seconds before taking the next screenshot
