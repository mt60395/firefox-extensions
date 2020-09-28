#!/usr/bin/env python3
import webbrowser
ff = webbrowser.get('firefox')

def get(extension):
	ff.open("https://addons.mozilla.org/firefox/downloads/file/" + extension)

extensions = [
        '3629683',  # uBlock Origin
        '3625427',  # HTTPS Everywhere
        '3630305',  # Cookie Auto Delete
        '704003',   # History Auto Delete
        '3548655',  # Facebook Container
        '3628130',  # DDG Privacy Essentials
        '3539177',  # Decentraleyes
        '3586373',  # CanvasBlocker
        '3638157',  # Chameleon
        '3637558',  # User Agent Switcher
        '3641200',  # Universal Bypass
]

if __name__ == "__main__":
        for ext in extensions:
                get(ext)
