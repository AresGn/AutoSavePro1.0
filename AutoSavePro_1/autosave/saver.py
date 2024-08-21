import pyautogui
import time
from datetime import datetime

def save_active_window():
    # Simule Ctrl+S sans interruption
    pyautogui.hotkey('ctrl', 's')
    return f"Sauvegarde effectuée le {datetime.now().strftime('%Y-%m-%d à %H:%M:%S')}"

def auto_save(interval, callback):
    while True:
        result = save_active_window()
        callback(result)
        time.sleep(interval * 60)  # Convertit les minutes en secondes