## Description
This program performs two primary functions:
1. **Network Status Monitor**: It checks if your PC is connected to the internet and sends a notification to your phone via Pushbullet with the current timestamp.
2. **Custom Lock Screen**: Displays a full-screen Tkinter-based lock screen with a randomly generated keyword and passcode. The user must enter the correct passcode to unlock the screen.
## Features
- Sends Pushbullet notifications when the PC connects to the internet.
- Displays a customizable lock screen with:
  - Full-screen mode and restricted close functionality.
  - Randomly selected keywords and corresponding passcodes.
- Logs user input in a separate JSON file.
## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pc-status-lock-screen.git
   ```
   cd pc-status-lock-screen
   ```bash
pip install -r requirements.txt
```
Run the program:
```bash
python pc_status.py
```
## Customization
- **Add Keywords/Passcodes**: Modify the `keyword_passcode_list` array in `pc_status.py`.
- **Change Pushbullet Device**: Ensure your phone is linked to Pushbullet and adjust API settings if needed.
- **Modify UI**: Update the Tkinter `Frame` and `Label` properties to change the lock screen appearance.
# checkMyPCOnline
# MonitoringPC
