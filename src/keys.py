

class KeyCode(int):
    def __init__(self) -> None:
        super().__init__()

class KeyHandler:
    def __init__(self) -> None:
        self.keys = {}
    
    def press(self, key: KeyCode) -> None:
        self.keys[key] = True
    
    def release(self, key: KeyCode) -> None:
        self.keys[key] = False
    
    def is_pressed(self, key: KeyCode) -> None:
        return self.keys.get(key, False)