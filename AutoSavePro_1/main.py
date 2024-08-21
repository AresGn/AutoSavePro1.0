import tkinter as tk
from autosave.gui import AutoSaveGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoSaveGUI(root)
    root.mainloop()