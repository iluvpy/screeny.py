from pynput import keyboard

"""
this is the KeyListener class, 
i use this here instead of the in-built Qt API
because here the keys are global
"""
class KeyListener:
    def __init__(self) -> None:
        self.keys = {}
        self.listener = keyboard.Listener(
            on_press=self.on_press, 
            on_release=self.on_release)
        
    def listen(self) -> None:
        self.listener.start()

    def get_string_key(self, key) -> str:
        return str(key).replace("Key.", "") 

    def on_press(self, key) -> None:
        # get the string version of the key and remove 
        str_key = self.get_string_key(key)
        self.keys[str_key] = True # pressed
    
    def on_release(self, key) -> None:
        str_key = self.get_string_key(key)
        self.keys[str_key] = False # not pressed
    
    def is_pressed(self, key: str):
        return self.keys.get(key, False)