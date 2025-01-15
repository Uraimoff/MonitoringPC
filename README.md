```markdown
# PC Network Status Monitor & Custom Lock Screen

A powerful and elegant Python program that monitors your PC's network connectivity, sends notifications to your phone via Pushbullet, and provides a secure, customizable lock screen interface with a keyword-password system.

---

## Features

- **Network Status Monitor**:
  - Checks if your PC is connected to the internet.
  - Sends a **Pushbullet notification** with the timestamp and PC name when the network comes online.

- **Custom Lock Screen**:
  - Full-screen, tamper-resistant Tkinter-based lock screen.
  - Randomly generated keywords requiring corresponding passcodes to unlock.
  - Secure: Overrides default close button behavior to prevent premature exit.

- **Startup Integration**:
  - Automatically starts on system boot by adding the script to the Windows startup folder.

---

## How It Works

### **Password Check Mechanism**
The lock screen generates a **random keyword** from a predefined list, such as:

```python
{"keyword": "lemon", "passcode": "melon"}
```

1. The user is presented with the keyword (e.g., `lemon`) on the lock screen.
2. They must enter the correct passcode (`melon`) to unlock.
3. If the passcode matches:
   - The lock screen closes.
   - The user regains access to their desktop.
4. If the passcode is incorrect:
   - An error message appears.
   - The user must try again until they succeed.

---

## Installation

Follow these steps to set up the program on your PC.

### 1. **Clone the Repository**
```bash
git clone https://github.com/Uraimoff/MonitoringPC.git
cd pc-network-lock-screen
```

### 2. **Install Required Libraries**
Ensure Python 3.11 or higher is installed. Install the dependencies:

```bash
pip install pushbullet.py requests
```

### 3. **Configure Pushbullet**
1. Sign in to [Pushbullet](https://www.pushbullet.com/).
2. Go to **Settings** > **Create Access Token**.
3. Replace `API_KEY` in the code with your token.

---

## Automatic Startup Configuration

To make the program start automatically when your PC boots up:

### **1. Add the Program to Startup**
1. Press `Win + R`, type `shell:startup`, and hit Enter.
2. Create a `.vbs` file in the Startup folder with the following content:

```vbscript
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "C:\path\to\your\run_pc_status.bat", 0, False
```

Replace `C:\path\to\your\run_pc_status.bat` with the full path to your batch file.

### **2. Create the Batch File**
1. In the same directory as the Python script, create `run_pc_status.bat`:
   ```batch
   @echo off
   cd /d "C:\path\to\your\script"
   python pc_status.py
   ```
   Replace `C:\path\to\your\script` with the full path to the folder containing `pc_status.py`.

2. Save the batch file in the same directory as the `.py` script.

---

## Customization

### **Modify the Lock Screen Keywords**
To add or update keywords and passcodes, edit the `keyword_passcode_list` in the `pc_status.py` file:

```python
keyword_passcode_list = [
    {"keyword": "lemon", "passcode": "melon"},
    {"keyword": "apple", "passcode": "banana"},
    {"keyword": "orange", "passcode": "grape"}
]
```

### **Change Lock Screen Design**
Edit the Tkinter components in `pc_status.py` to adjust the design:
- **Background color**: Update `root.configure(bg="black")`.
- **Font style**: Adjust `font` properties in labels and buttons.

---

## Usage

1. Run the program using the batch file or execute the Python script directly:
   ```bash
   python pc_status.py
   ```
2. The program will:
   - Send a Pushbullet notification when the PC connects to the internet.
   - Display a lock screen where you must enter the correct passcode for the given keyword.

3. To stop the script during testing, press `Ctrl+C` in the terminal or kill the process in Task Manager.

---

## Example Workflow

1. **Network Status Notification**:
   - The PC connects to the internet.
   - Pushbullet sends a notification:  
     > *Your PC WIN-SADIKOFF is online at 2025-01-12 14:23:45.*

2. **Lock Screen Interaction**:
   - The screen displays:  
     > *Keyword: lemon*  
   - You enter the passcode: `melon`.
   - If correct, the desktop unlocks. If not, an error prompts you to retry.

---

## Troubleshooting

- **Pushbullet API Key Issues**:
  - Ensure you’ve copied the correct Access Token.
  - Verify Pushbullet is set up on your phone and PC.

- **Script Doesn’t Start on Boot**:
  - Double-check the `.vbs` file path and contents.
  - Ensure the `.bat` file points to the correct Python script.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

We welcome contributions! Feel free to fork the repository, make improvements, and submit a pull request.

---

## Author

Developed by **Your Name**. Reach out at [your.email@example.com](mailto:your.email@example.com) or via [GitHub Issues](https://github.com/username/pc-network-lock-screen/issues).

```

### **Key Highlights of the `README.md`**
1. **Clear Structure**: Organized into sections like Features, Installation, and Usage.
2. **Visual Appeal**: Markdown elements like headings, lists, and code blocks improve readability.
3. **Comprehensive Instructions**: Covers everything from setup to customization.
4. **Professional Tone**: Suitable for public GitHub repositories.
