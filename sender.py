import os
import time
from datetime import datetime
from PIL import Image
import pyautogui
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the server URL from the .env file
SERVER_URL = os.getenv("SERVER_URL")

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
                files={'file': file}
            )
            print(f"Server response: {response.json()}")
        except Exception as e:
            print(f"Failed to send file {filename}: {e}")
        finally:
            os.remove(filename)  # Clean up local copy

# Scheduler task
def take_and_send_screenshot():
    filename = capture_screenshot()
    send_screenshot_via_http(filename, SERVER_URL)

# Run periodically
if __name__ == '__main__':
    while True:
        take_and_send_screenshot()
        time.sleep(30)  # Wait 60 seconds
