from pynput import keyboard
import time
import pyautogui
import pywhatkit
import json
import os

CONFIG_FILE = "config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return None

def save_config(phone_number):
    config = {"phone_number": phone_number}
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

def get_phone_number():
    config = load_config()
    if config and "phone_number" in config:
        return config["phone_number"]
    
    while True:
        phone_number = input("\nEnter your WhatsApp number (with country code, e.g., +1234567890): \n")
        if phone_number.startswith('+') and phone_number[1:].isdigit():
            save_config(phone_number)
            return phone_number
        print("Invalid phone number format. Please try again.")

def send_to_whatsapp(image_path):
    phone_number = get_phone_number()
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Screenshot file not found at {image_path}")
        
        abs_image_path = os.path.abspath(image_path)
        
        print(f"Attempting to send image from: {abs_image_path}")
        pywhatkit.sendwhats_image(phone_number, abs_image_path, "Test", 10, True, 5)
        print(f"Screenshot sent successfully to {phone_number}")

    except Exception as e:
        print(f"Error while sending screenshot: {str(e)}")

def take_and_send_screenshot():
    screenshot_filename = "screenshot.png"
    # Delete existing screenshot if it exists
    if os.path.exists(screenshot_filename):
        try:
            os.remove(screenshot_filename)
            print(f"Deleted existing screenshot: {screenshot_filename}")
        except Exception as e:
            print(f"Error deleting existing screenshot: {str(e)}")
    try:            
        print("Taking screenshot...")
        screenshot = pyautogui.screenshot(screenshot_filename)
        screenshot_path = os.path.abspath(screenshot_filename)
        print(f"Screenshot taken and saved at: {screenshot_path}")
        
        send_to_whatsapp(screenshot_path)
    except Exception as e:
        print(f"Error taking or sending screenshot: {str(e)}")


def on_activate_h():
    print('<ctrl>+<alt>+h pressed')
    take_and_send_screenshot()



def main():
    print("Welcome to the Screenshot Sender!")
    phone_number = get_phone_number()
    print(f"Using WhatsApp number: {phone_number}")
    print("Press Ctrl+alt+h to take a screenshot and send it via WhatsApp.")
    with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+h': on_activate_h}) as h:
        h.join()


if __name__ == "__main__":
    main()
