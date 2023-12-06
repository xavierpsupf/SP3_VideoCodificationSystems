import subprocess


# FUNCTIONS FOR EXERCISE 3 SP3:

# This is a modified function of the "mp2_video_converter" function from lab 2:
def mp3_video_converter(input_video, output_audio):  # Function to convert a video into a .mp3 audio file.
    subprocess.run(["ffmpeg", "-i", input_video, "-q:a", "0", "-map", "a", output_audio])
