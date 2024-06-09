[python]: Here's a cleaned-up version of your GitHub README:

# Screentime-Code

This project is designed for use with a Mac and an Apple device. Feel free to fork it and make modifications for other devices.

## How to Use

### Initial Setup

1. **Enable Necessary Permissions on Mac:**
    - Go to `System Preferences` > `Privacy & Security`
    - Select `Accessibility` and enable Terminal.
    - Select `Input Monitoring` and enable Terminal.

2. **Prepare the Environment:**
    - Ensure that the Terminal is running in the same folder as the program.
    - Install the required Python package by running:
      ```bash
      pip install pynput
      ```

3. **Install Keypad App:**
    - Download and install the Keypad - Bluetooth Keyboard app from the [Mac App Store](https://apps.apple.com/ca/app/keypad-bluetooth-keyboard/id1491684442?mt=12).
    - Follow the instructions to connect your Mac to your iPhone.

### Setting Up Screen Time

Make sure you have your Screen Time limits already set up. Once locked, the only way to unlock it is by checking the code in the `.txt` file, which will reveal the code.

### Running the Program

1. On your iPhone, navigate to the Screen Time lock password screen.
2. On your Mac, open Terminal and run the following command:
   ```bash
   python Screentime-Password.py
   ```
3. Switch to the Keypad app you installed and click the keyboard icon.

The program will wait 5 seconds and then type a random 4-digit code twice. After it finishes typing, the code will be saved to a `.txt` file in the same folder as the program.

### Storing the Code

- You can store the `.txt` file on a USB drive and give it to someone else.
- Alternatively, use an app like Cold Turkey to lock the `.txt` file until a certain date.
- If you feel confident, you could delete the file completely and never look back.

This setup aims to help you manage your screen time addiction effectively.

---

Feel free to reach out if you have any questions or suggestions. Happy coding!
