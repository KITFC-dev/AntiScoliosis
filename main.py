# im under the water, please help me

import tkinter as tk
from tkinter import messagebox
import pygetwindow as gw
import pygame
import time
import threading
import plyer
import sys
from plyer.platforms.win.notification import Notification
import os
import ctypes

notification = Notification()


def get_resource_path(relative_path):
    """Get the absolute path to a resource file."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def get_resource_path_ico(relative_path):
    """Get the absolute path to a resource file."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# Get the path to the alerr.mp3 file
sound_file = get_resource_path("alerr.mp3")
icon_file = get_resource_path_ico('icon.ico')

def func():
    pass

def custom_message_box(title, message, width, height):
    # Create a new window
    window = tk.Toplevel()
    window.title(title)

    # Create a label with the message
    label = tk.Label(window, text=message)
    label.pack(padx=10, pady=10)

    # Set the size of the window
    window.geometry(f"{width}x{height}")

    # Center the window on the screen
    window.update_idletasks()
    window.geometry(f"+{window.winfo_screenwidth() // 2 - width // 2}+{window.winfo_screenheight() // 2 - height // 2}")

    # Run the window's event loop
    window.mainloop()


def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()


def close_win():
    time.sleep(7)
    ctypes.windll.user32.LockWorkStation()

def hide_all_windows():
    windows = gw.getAllTitles()
    for window in windows:
        if window != "Program Manager":
            win = gw.getWindowsWithTitle(window)[0]
            win.minimize()

def loop():
    try:
        secondss = interval_entry.get()
        seconds = float(secondss)
        minutes = seconds * 60
        if minutes <= float(0):
            raise ValueError("not positive number")
        if minutes > 0:
            time.sleep(float(minutes))
            win_thread = threading.Thread(target=close_win)
            win_thread.start()
            hide_all_windows()
            play_sound(sound_file)
            plyer.notification.notify(title='TIME FOR BREAKKK', message='LEAVE NOWW', app_name='SilentAlr')
            messagebox.showinfo("LEAVE NOW", "TIME FOR BREAK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            pygame.time.wait(17000)

            pygame.quit()


    except ValueError as ve:
        custom_message_box("ERROR", f"{ve}", 900, 900)
    except Exception as e:
        custom_message_box("ERROR", f"{e}", 900, 900)
    finally:
        pygame.quit()
        time.sleep(3)
        sys.exit()

def start():
    loop_thread = threading.Thread(target=loop)
    loop_thread.start()


root = tk.Tk()
root.title("AntiScoliosis")
root.iconbitmap(icon_file)
root.geometry("400x400")
# root.iconbitmap("")
root.minsize(400, 400)
root.maxsize(400, 400)
menu = tk.Menu(root)
root.config(menu=menu)
main_menu = tk.Menu(menu, tearoff=0)
main_menu.add_command(label="PH 1", command=func)
main_menu.add_command(label="PH 2", command=func)
main_menu.add_command(label="PH 3", command=func)
menu.add_cascade(label="PLACEHOLDER", menu=main_menu)

main_logo = tk.Label(root, font=("Lucida Console", 20, "bold"), text="AntiScoliosis")
main_logo.pack(padx=50, pady=30)

interval_text = tk.Label(text="Enter interval (in minutes)", font=("Microsoft JhengHei", 10))
interval_text.pack()
interval_entry = tk.Entry(root)
interval_entry.pack()

start_button = tk.Button(text="Start Timer", command=start)
start_button.pack(pady=10)


if __name__ == "__main__":
    root.mainloop()

# I hear the crystal raindrops fall
# On the window down the hall
# And it becomes the morning dew
# And, darling, when the morning comes
# And I see the morning sun
# I want to be the one with you

# Just the two of us
# We can make it if we try
# Just the two of us
# Just the two of us
# Just the two of us
# Building big castles way on high
# Just the two of us
# You and I
