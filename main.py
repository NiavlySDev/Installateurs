import tkinter as tk
from tkinter import ttk

import Params
import api

# Dictionary of installers, mapping their names to Params values.
INSTALLERS = {
    "Discord": Params.DISCORD,
    "Epic Games": Params.EPIC,
    "Ninite": Params.NINITE,
    "OBS Studio": Params.OBS,
    "Opera": Params.OPERA,
    "Rockstar Games": Params.ROCKSTAR,
    "Ubisoft Connect": Params.UBISOFT,
    "Xbox": Params.XBOX,
    "Jetbrains": Params.JETBRAINS,
    "LabyMod": Params.LABYMOD,
    "GitHub": Params.GITHUB,
    "BlockBench": Params.BLOCKBENCH,
    "Mcreator": Params.MCREATOR,
}

# Create the main window
root = tk.Tk()
root.title("Installer Manager")

# Set dark theme styles
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#2E2E2E", foreground="white")
style.configure("TButton", background="#444444", foreground="white")
style.configure("TFrame", background="#2E2E2E")
root.configure(bg="#2E2E2E")


# Function to create buttons for each installer
def create_buttons(installer_name):
    def confirm_action(action, *args):
        confirm_window = tk.Toplevel(root)
        confirm_window.title("Validation")
        confirm_window.configure(bg="#2E2E2E")

        def execute_action():
            action(*args)
            confirm_window.destroy()

        confirm_label = ttk.Label(confirm_window, text="Action effectuée avec succès !", style="TLabel")
        confirm_label.pack(padx=10, pady=10)

        confirm_button = ttk.Button(confirm_window, text="OK", command=confirm_window.destroy, style="TButton")
        confirm_button.pack(pady=10)

        # Trigger the action once the confirmation window opens
        execute_action()

    installer_frame = ttk.Frame(root)
    installer_frame.pack(fill="x", pady=5)

    label = ttk.Label(installer_frame, text=installer_name, width=20, style="TLabel")
    label.grid(row=0, column=0, padx=5)

    install_button = ttk.Button(installer_frame, text="Installer",
                                command=lambda: confirm_action(api.download, INSTALLERS[installer_name]),
                                style="TButton")
    install_button.grid(row=0, column=1, padx=5)

    delete_button = ttk.Button(installer_frame, text="Supprimer", command=lambda: confirm_action(api.deleteAll),
                               style="TButton")
    delete_button.grid(row=0, column=2, padx=5)


# Dynamically create sections for each installer
for name in INSTALLERS.keys():
    create_buttons(name)

# Start the tkinter main loop
root.mainloop()
