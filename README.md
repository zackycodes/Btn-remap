# 🖱️ Btn-remap
A lightweight Python utility that transforms your mouse's side buttons into powerful productivity shortcuts.
By default, this script maps your auxiliary mouse buttons to Copy and Paste commands.  

## ✨ Features 
* Zero GUI: Runs silently in the background with minimal overhead. 
* Instant Mapping: Converts Button.x1 (Back) to Ctrl+C and Button.x2 (Forward) to Ctrl+V.
* Real-time Feedback: Prints the action to the console whenever a trigger occurs.

## 🛠️ How It Works

The script utilizes a mouse.Listener to intercept click events.
When it detects the specific side button inputs (x1 or x2), it uses the keyboard.Controller to simulate the corresponding keystrokes. 
* Button.x1 -> Key.ctrl + c
* Button.x2 -> Key.ctrl + v 

## ⚙️ Customization
You can easily modify the script to perform different actions (like Ctrl+Z or Alt+Tab) by changing the keys inside the kb_controller.press() functions.


## 🚀 Getting Started

### Prerequisites
* You will need Python installed on your system and the pynput library. 
Use:
`Bashpip install pynput`

### Usage
- Clone this repository.
- Run the script: `Bashpython main.py`
- Use your mouse side buttons to copy and paste text or files instantly.

## NOTE
Depending on your OS (especially macOS and Linux), you may need to grant "Accessibility" or "Root" permissions to your terminal for the script to listen to system-wide mouse events.
