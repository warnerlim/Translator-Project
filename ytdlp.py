from yt_dlp import *

def yt_download_dlp(video_url):

    # Set options for downloading audio only
    audio_opts = {
        'format': 'bestaudio',
        'outtmpl': 'input_audio.mp3',
    }

    opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': 'input.mp4',
    }

    # Download audio
    with YoutubeDL(audio_opts) as ydl:
        ydl.download([video_url])

    # Download video
    with YoutubeDL(opts) as ydl:
        ydl.download([video_url])

    print("Download complete. Video and audio are saved separately.")