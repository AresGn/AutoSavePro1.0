import tkinter as tk
from tkinter import ttk, scrolledtext
from autosave.saver import auto_save
import threading
import pyautogui

class AutoSaveGUI:
    def __init__(self, master):
        self.master = master
        master.title("AutoSavePro")
        master.geometry("400x300")

        self.label = ttk.Label(master, text="Intervalle de sauvegarde (minutes):")
        self.label.pack(pady=5)

        self.interval = ttk.Combobox(master, values=[1, 3, 9, 15])
        self.interval.pack(pady=5)
        self.interval.current(0)  # Sélectionne par défaut la première valeur

        self.start_button = ttk.Button(master, text="Démarrer", command=self.start_auto_save)
        self.start_button.pack(pady=5)

        self.log_area = scrolledtext.ScrolledText(master, height=10)
        self.log_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.auto_save_thread = None

    def log(self, message):
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)

    def start_auto_save(self):
        try:
            interval = int(self.interval.get())
            if self.auto_save_thread is None or not self.auto_save_thread.is_alive():
                self.auto_save_thread = threading.Thread(target=auto_save, args=(interval, self.log), daemon=True)
                self.auto_save_thread.start()
                self.start_button.config(state='disabled')
                self.log(f"AutoSave démarré avec un intervalle de {interval} minutes")
                self.check_active_window()
            else:
                self.log("AutoSave est déjà en cours d'exécution")
        except ValueError:
            self.log("Veuillez sélectionner un intervalle valide")

    def check_active_window(self):
        active_window = pyautogui.getActiveWindow()
        if active_window:
            self.log(f"Application active : {active_window.title}")
        else:
            self.log("Aucune application active détectée")
        self.master.after(6000, self.check_active_window)  # Vérifie toutes les 2 minutes

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoSaveGUI(root)
    root.mainloop()
