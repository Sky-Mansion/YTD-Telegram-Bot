from lib.downloader.__main__ import YouTube
from lib.marge.stefnk import merge

def download_video_and_audio(video_url, resolution_choice):
    yt = YouTube(video_url)
    video_stream = yt.streams.filter(file_extension='mp4', res=resolution_choice, only_video=True).first()
    video_stream.download(filename='video.mp4')

 
    audio_stream = yt.streams.filter(only_audio=True).first()
    if audio_stream:
        audio_stream.download(filename='audio.mp3')
    else:
        print("No audio stream available for the selected resolution.")



video_url = 'https://youtu.be/TjvrbPqfBxI?si=PYOAh-on2n4-ylJc'


resolution_choice = '144p'


download_video_and_audio(video_url, resolution_choice)


merge('video.mp4', 'audio.mp3', 'output_video.mp4')
