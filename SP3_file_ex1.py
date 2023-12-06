import subprocess

# EXERCISE 1 SP3:


class VideoConverter:
    def __init__(self):
        pass

    @staticmethod
    def change_video_resolution(input_path, output_path, new_resolution):
        command = [
            'ffmpeg',
            '-i', input_path,
            '-vf', f'scale={new_resolution}',
            '-c:a', 'copy',
            output_path
        ]

        subprocess.run(command)

    @staticmethod
    def vp8_converter(input_path, output_path):
        command = [
            'ffmpeg',
            '-i', input_path,
            '-c:v', 'libvpx',
            '-c:a', 'libvorbis',
            output_path
        ]

        subprocess.run(command)

    @staticmethod
    def vp9_converter(input_path, output_path):
        command = [
            'ffmpeg',
            '-i', input_path,
            '-c:v', 'libvpx-vp9',
            '-c:a', 'libvorbis',
            output_path
        ]

        subprocess.run(command)

    @staticmethod
    def h265_converter(input_path, output_path):
        command = [
            'ffmpeg',
            '-i', input_path,
            '-c:v', 'libx265',
            '-c:a', 'aac',
            output_path
        ]

        subprocess.run(command)

    @staticmethod
    def av1_converter(input_path, output_path):
        command = [
            'ffmpeg',
            '-i', input_path,
            '-c:v', 'libaom-av1',
            '-c:a', 'libvorbis',
            output_path
        ]

        subprocess.run(command)


vc_instance = VideoConverter()

input_video = 'BigBuckBunny_mp4_video.mp4'  # Change this with a shorter video (highly recommended).

# First, we will convert the "BigBuckBunny_mp4_video" to four different types of RESOLUTION (720p,
# 480p, 360x240 and 160x120):

output_video_720p = 'BigBuckBunny_mp4_video_720p.mp4'
resolution720p = '1280x720'  # 720p = 1280x720
vc_instance.change_video_resolution(input_video, output_video_720p, resolution720p)

output_video_480p = 'BigBuckBunny_mp4_video_480p.mp4'
resolution480p = '640x480'
vc_instance.change_video_resolution(input_video, output_video_480p, resolution480p)

output_video_360x240 = 'BigBuckBunny_mp4_video_360x240.mp4'
resolution360x240 = '360x240'
vc_instance.change_video_resolution(input_video, output_video_360x240, resolution360x240)

output_video_160x120 = 'BigBuckBunny_mp4_video_160x120.mp4'
resolution160x120 = '160x120'
vc_instance.change_video_resolution(input_video, output_video_160x120, resolution160x120)

# Now, we will select the "BigBuckBunny_mp4_video_480p.mp4" video, and we will convert it to 4 four different
# types of CODECS (VP8, VP9, h265 and AV1):

# VERY IMPORTANT!!! To execute this part of the code, I HIGHLY recommend to do it with a very short
# video (not with 10 minutes long video), because otherwise it takes a VERY long time to execute the
# code!!!

output_video_vp8 = 'BigBuckBunny_mp4_video_480p_VP8.webm'
vc_instance.vp8_converter(output_video_480p, output_video_vp8)

output_video_vp9 = 'BigBuckBunny_mp4_video_480p_VP9.webm'
vc_instance.vp9_converter(output_video_480p, output_video_vp9)

output_video_h265 = 'BigBuckBunny_mp4_video_480p_h265.mp4'
vc_instance.h265_converter(output_video_480p, output_video_h265)

output_video_AV1 = 'BigBuckBunny_mp4_video_480p_AV1.mkv'
vc_instance.av1_converter(output_video_480p, output_video_AV1)
