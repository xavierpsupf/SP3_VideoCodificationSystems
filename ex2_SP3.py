import subprocess

# EXERSICE 2 SP3:

# This file it has to be executed after executing the "SP3_fle" because the videos
# "BigBuckBunny_mp4_video_480p_VP8.webm" and "BigBuckBunny_mp4_video_480p_VP9.webm" are needed!


def video_comparison(input_file_vp8, input_file_vp9, output_file):
    # Set ffmpeg command for video concatenation
    ffmpeg_cmd = (
        f'ffmpeg -i {input_file_vp8} -i {input_file_vp9} '
        f'-filter_complex "[0:v][1:v]hstack=inputs=2[v];[0:a][1:a]amerge=inputs=2[a]" '
        f'-map "[v]" -map "[a]" -c:v libvpx -b:v 2M -c:a libvorbis {output_file}.webm'
    )

    try:
        # Run ffmpeg command using subprocess
        subprocess.run(ffmpeg_cmd, shell=True, check=True)
        print(f'Video comparison exported successfully: {output_file}.webm')
    except subprocess.CalledProcessError as e:
        print(f'Error exporting video comparison: {e}')


vp8_input_video = 'BigBuckBunny_mp4_video_480p_VP8.webm'
vp9_input_video = 'BigBuckBunny_mp4_video_480p_VP9.webm'
output_video_comparison = 'VP8_VP9_output_video_comparison'
video_comparison(vp8_input_video, vp9_input_video, output_video_comparison)
