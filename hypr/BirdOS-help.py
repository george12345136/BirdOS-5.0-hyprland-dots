import tkinter as tk
from tkinter import filedialog, messagebox
import platform
import webbrowser
import os
import distro 
import subprocess
import glob


BIRDOS_VERSION = "BirdOS 3.0"
DEVELOPER_WEBSITE_URL = "https://github.com/george12345136"

def get_wm_or_de():
    """Attempts to determine the Window Manager or Desktop Environment on Linux."""
    
    de_name = os.environ.get('XDG_CURRENT_DESKTOP')
    if de_name:
        return de_name.replace(':', '/').strip() 

    session_type = os.environ.get('XDG_SESSION_DESKTOP')
    if session_type:
        return session_type.strip()
    return "Unknown WM/DE (Variables unset)"


class SimpleInfoApp:
    def __init__(self, master):
        self.master = master
        master.title("System/BirdOS Information")

        os_name = platform.system()
        wm_or_de = get_wm_or_de()
        
        if os_name == "Linux":
            try:
                os_name = distro.name(pretty=True)
            except NameError:
                pass 
        
        info_text = (
            f"You are using {os_name} in {wm_or_de} with {BIRDOS_VERSION}\n"
        )

        self.label = tk.Label(
            master,
            text=info_text,
            font=('Helvetica', 16),
            padx=20,
            pady=20,
            justify=tk.CENTER
        )
        self.label.pack(expand=True, fill=tk.Y)

        button_frame = tk.Frame(master)
        button_frame.pack(fill=tk.X, pady=10)

        self.developer_button = tk.Button(
            button_frame,
            text="Developer Website",
            command=self.open_website
        )
        self.developer_button.pack(side=tk.LEFT, padx=10)

        self.close_button = tk.Button(
            button_frame,
            text="Close Window",
            bg="red",        
            fg="white",           
            command=master.quit
        )
        self.close_button.pack(side=tk.RIGHT, padx=10)

    def open_website(self):
        """Opens the specified URL in the default web browser."""
        try:
            webbrowser.open(DEVELOPER_WEBSITE_URL)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open website: {e}")

if __name__ == "__main__":
    try:
        import distro
    except ImportError:
        distro = None 
        
    root = tk.Tk()
    app = SimpleInfoApp(root)
    root.mainloop()