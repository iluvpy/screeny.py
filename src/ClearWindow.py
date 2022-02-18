from tkinter import Tk 

class ClearWindow(Tk):

    def __init__(self, w: int, h: int) -> None:
        super().__init__()
        self.geometry(f"{w}x{h}")
        self.title("window")
        self.attributes("-alpha", 0.5) # add transparency
        self.overrideredirect(True) # remove title bar 
    def open(self):
        self.mainloop()