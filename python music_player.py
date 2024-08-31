import os
import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Initialize the GUI application
root = tk.Tk()
root.title("Music Player")
root.geometry("400x250")

current_music = None
is_paused = False
current_track_label = tk.Label(root, text="No track playing", font=("Arial", 12))
current_track_label.pack(pady=5)

def select_folder():
    global current_music
    folder_path = filedialog.askdirectory()
    if folder_path:
        play_music(folder_path)

def play_music(folder_path):
    global current_music
    music_files = [f for f in os.listdir(folder_path) if f.endswith('.mp3') or f.endswith('.wav')]
    if music_files:
        current_music = os.path.join(folder_path, music_files[0])
        pygame.mixer.music.load(current_music)
        pygame.mixer.music.play()
        update_track_label(os.path.basename(current_music))
    else:
        print("No music files found in the selected folder.")

def stop_music():
    pygame.mixer.music.stop()
    update_track_label("No track playing")

def pause_music():
    global is_paused
    if is_paused:
        pygame.mixer.music.unpause()
        update_track_label(os.path.basename(current_music))
        is_paused = False
    else:
        pygame.mixer.music.pause()
        update_track_label("Paused")
        is_paused = True

def update_track_label(track_name):
    current_track_label.config(text=f"Current Track: {track_name}")

def set_volume(value):
    volume = int(value) / 100
    pygame.mixer.music.set_volume(volume)

# Create GUI elements
select_button = tk.Button(root, text="Select Folder", command=select_folder)
select_button.pack(pady=10)

play_button = tk.Button(root, text="Play", command=lambda: play_music(os.path.dirname(current_music)))
play_button.pack(pady=10)

pause_button = tk.Button(root, text="Pause/Resume", command=pause_music)
pause_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack(pady=10)

volume_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Volume", command=set_volume)
volume_slider.set(100)  # Set default volume to maximum
volume_slider.pack(pady=10)

# Run the GUI loop
root.mainloop()
