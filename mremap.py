from pynput import mouse, keyboard

# Initialize the keyboard controller to send commands
kb_controller = keyboard.Controller()

def on_click(x, y, button, pressed):
    if pressed:
        # Map back side button (Button.x1) to Copy
        if button == mouse.Button.x1:
            kb_controller.press(keyboard.Key.ctrl)
            kb_controller.press('c')
            kb_controller.release('c')
            kb_controller.release(keyboard.Key.ctrl)
            print("Action: Copy")

        # Map forward side button (Button.x2) to Paste
        elif button == mouse.Button.x2:
            kb_controller.press(keyboard.Key.ctrl)
            kb_controller.press('v')
            kb_controller.release('v')
            kb_controller.release(keyboard.Key.ctrl)
            print("Action: Paste")

# Setup the listener
with mouse.Listener(on_click=on_click) as listener:
    listener.join()