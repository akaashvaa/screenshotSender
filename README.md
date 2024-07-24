# Screenshot Sender

Screenshot Sender is a Python-based utility that allows you to take a screenshot using a global hotkey combination and send it to a predefined WhatsApp number. This tool is useful for quickly sharing screenshots without needing to manually attach and send them through WhatsApp.

## Features

- Take a screenshot using a global hotkey combination (`Ctrl + Alt + h`).
- Automatically send the screenshot to a predefined WhatsApp number.
- Configurable phone number stored in a local configuration file.

## Requirements

- Python
- PIP

## Installation

1. **Clone the repository:**

   - git clone `https://github.com/akaashvaa/ss_to_whatsapp.git`
   - cd ss_to_whatsapp

2. **Create and activate a virtual environment:**

   ```
   python -m venv venv
   source venv/bin/activate # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:

   ```
   python main.py
   ```

2. Press
   `
Ctrl + Alt + h`
   to take a screenshot and send it to the configured WhatsApp number.

$$**NOTE**$$

<center>
For the initial setup, it will prompt you to enter the WhatsApp number where you want to send the screenshots. This number will be saved in a configuration file (`config.json`) for future use.

Replace `+1234567890` with your desired WhatsApp number, including the country code.

</center>

## Acknowledgements

- [PyWhatKit](https://github.com/Ankit404butfound/PyWhatKit) for WhatsApp automation.
- [PyAutoGUI](https://pyautogui.readthedocs.io/) for screenshot functionality.
- [Pynput](https://pynput.readthedocs.io/) for global hotkey detection.

## License

[MIT License](LICENSE)
