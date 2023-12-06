import tkinter as tk
from tkinter import filedialog
import subprocess

from functions_previous_labs import mp3_video_converter


# EXERCISE 3 SP3:

class VideoToAudioConverterGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("MP4 to MP3 Converter")

        self.input_label = tk.Label(master, text="Select a MP4 video file:")
        self.input_label.pack()

        self.input_button = tk.Button(master, text="Select MP4 Video", command=self.choose_video_file)
        self.input_button.pack()

        self.output_label = tk.Label(master, text="Save as an MP3 audio file:")
        self.output_label.pack()

        self.output_button = tk.Button(master, text="Select Output Folder", command=self.choose_output_folder)
        self.output_button.pack()

        self.convert_button = tk.Button(master, text="Convert", command=self.convert_video_to_audio)
        self.convert_button.pack()

        self.video_file = ""
        self.output_folder = ""

    def choose_video_file(self):
        self.video_file = filedialog.askopenfilename(filetypes=[("MP4 video files", "*.mp4")])

    def choose_output_folder(self):
        self.output_folder = filedialog.askdirectory()

    def convert_video_to_audio(self):
        if not self.video_file or not self.output_folder:
            tk.messagebox.showerror("Error", "Select a video file and output folder.")
            return

        input_video = self.video_file
        output_audio = f"{self.output_folder}/output_audio.mp3"

        try:
            mp3_video_converter(input_video, output_audio)
            tk.messagebox.showinfo("Success", "The conversion has been completed successfully.")
        except subprocess.CalledProcessError:
            tk.messagebox.showerror("Error", "There was a problem converting video to audio.")


root = tk.Tk()
converter = VideoToAudioConverterGUI(root)
root.mainloop()
