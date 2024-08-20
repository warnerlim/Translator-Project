from ytdlp import yt_download_dlp
from jp2engtxt import whisper_function
from gpt4translate import translate_file
from txt_to_srt import convert_txt_to_srt
import os

def download_video():
    url = input("Enter YouTube link here: ")
    yt_download_dlp(video_url=url)
    print("Video download completed.")

def transcribe_audio():
    whisper_function()
    print("Audio transcription completed.")

def translate_transcription():
    input_file_path = 'raw_text.txt'
    output_file_path = 'raw_english_text2.txt'
    translate_file(input_file_path, output_file_path)
    print("Translation completed.")

def srt_converter():
    txt_file_path = 'raw_english_text.txt'
    srt_file_path = 'output.srt'
    convert_txt_to_srt(txt_file_path, srt_file_path)

def apply_subtitles():
    input_file = 'input.mp4'
    output_file = 'output_video.mp4'
    subtitle_file = 'output.srt'
    font_file = 'OpenSans-Regular.ttf'
    command = (
        f'ffmpeg -i {input_file} -vf "subtitles={subtitle_file}:'
        f'force_style=\'Alignment=2,FontName={font_file},FontSize=24,PrimaryColour=&HFFFFE0&\'" '
        f'-c:a copy {output_file}'
    )
    os.system(command)

if __name__ == "__main__":
    while True:
        print("\nSelect an option:")
        print("1. Download video")
        print("2. Transcribe audio")
        print("3. Translate text")
        print("4. Convert txt to SRT file")
        print("5. Subtitle video")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            download_video()
        elif choice == '2':
            transcribe_audio()
        elif choice == '3':
            translate_transcription()
        elif choice == '4':
            srt_converter()
        elif choice == '5':
            apply_subtitles()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")