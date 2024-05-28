from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
import os

# object creation
music = tk.Tk()
music.title("Hassan's Music Player")
music.geometry("500x300")
music.resizable(False, False)

# initialized the pygame
pygame.mixer.init()

# to store the songs in variable
songs = []
current_song = ""
pause = False
is_playing = False


# load the songs
def load_songs():
    global current_song
    music.directory = filedialog.askdirectory()

    for song in os.listdir(music.directory):
        name, ext = os.path.splitext(song)
        if ext == ".mp3" or ext == ".flac":
            songs.append(song)

    for song in songs:
        song_list.insert("end", song)
    song_list.select_set(0)
    current_song = songs[song_list.curselection()[0]]


# create the function for play
def play_music():
    global current_song, pause
    if not pause:
        pygame.mixer.music.load(os.path.join(music.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        pause = False


# pause the music
def pause_music():
    global pause
    pygame.mixer.music.pause()
    pause = True


# next song
def next_music():
    global current_song, pause
    try:
        song_list.select_clear(0, END)
        song_list.select_set(songs.index(current_song) + 1)
        current_song = songs[song_list.curselection()[0]]
        play_music()
    except:
        pass


# previous music
def prev_music():
    global current_song, pause
    try:
        song_list.select_clear(0, END)
        song_list.select_set(songs.index(current_song) - 1)
        current_song = songs[song_list.curselection()[0]]
        play_music()
    except:
        pass


# create the function to play a song on double-click
def play_selected_song(event):
    global current_song
    selected_index = song_list.curselection()
    if selected_index:
        current_song = songs[selected_index[0]]
        play_music()


# update current song on list selection
def on_song_select(event):
    global current_song
    selected_index = song_list.curselection()
    if selected_index:
        current_song = songs[selected_index[0]]
        play_music()


# Create a function to toggle play/pause
def toggle_play_pause():
    global is_playing
    if is_playing:
        pause_music()
        play_pause_button.config(image=play)  # Change button image to "Play"
    else:
        play_music()
        play_pause_button.config(image=paused)  # Change button image to "Pause"
    is_playing = not is_playing

def about():
    messagebox.showinfo('About', "\n \n    Coded by: \n\n Shaik Hassan Ahmed")

# create the menu bar
menubar = Menu(music)
music.config(menu=menubar)
# create the menu detail
organized_menu = Menu(menubar, tearoff=False)
organized_menu.add_command(label="import", command=load_songs)
menubar.add_cascade(label="music", menu=organized_menu)

# another menu bar
about_menu = Menu(menubar, tearoff=0,bg="black",fg="white")
menubar.add_cascade(label="About", command=about)
# to create the frame to display the song
song_list = Listbox(background="black", width=100, height=15, fg="white")
song_list.pack()
song_list.bind("<<ListboxSelect>>", on_song_select)
song_list.bind("<<ListboxDoubleClick>>", play_selected_song)
# Bind list selection event
# get the button from the image
play = PhotoImage(file=r"Buttons/play.png")
paused = PhotoImage(file=r"Buttons/pause.png")
nxt = PhotoImage(file=r"Buttons/next.png")
prev = PhotoImage(file=r"Buttons/previous.png")
stop = PhotoImage(file=r"Buttons/stop.png")
# put into the frame
control_frame = Frame(music)
control_frame.pack()

# create the button in the frame
play_button = Button(control_frame, image=play, borderwidth=0, command=play_music)
stop_button = Button(control_frame, image=stop, borderwidth=0, command=pause_music)
pause_button = Button(control_frame, image=paused, borderwidth=0, command=pause_music)
next_button = Button(control_frame, image=nxt, borderwidth=0, command=next_music)
prev_button = Button(control_frame, image=prev, borderwidth=0, command=prev_music)
play_pause_button = Button(control_frame, image=play, borderwidth=0, command=toggle_play_pause)


# to display the button in the frame
play_pause_button.grid(row=0, column=0, padx=10, pady=10)
play_button.grid(row=0, column=0, padx=10, pady=10)
stop_button.grid(row=0, column=1, padx=10, pady=10)
prev_button.grid(row=0, column=2, padx=10, pady=10)
next_button.grid(row=0, column=3, padx=10, pady=10)

music.mainloop()