import sys
import os
from ytdlp import yt_download_dlp
from jp2engtxt import whisper_function
from gpt4translate import translate_file

def download_file(url):
    yt_download_dlp(video_url=url)
    print("Downloading file with input: " + url)
    
def transcribe_audio():
    whisper_function()
    print("Audio transcription completed.")

def translate_files():
    input_file_path = 'raw_text.txt'
    output_file_path = 'raw_english_text.txt'
    translate_file(input_file_path, output_file_path)
    print("Translation completed.")

def delete_file():
    file_paths = ["input_audio.mp3", "input.mp4"]
    for file_path in file_paths:
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    return "Deleting file..."

def upload_file():
    return "Uploading file..."

def main(action, input_data=None):
    if action == 'Download':
        return download_file(input_data)
    elif action == 'Transcribe':
        return transcribe_audio()
    elif action == 'Translate':
        return translate_files()
    elif action == 'Delete':
        return delete_file()
    elif action == 'Upload':
        return upload_file()
    else:
        return "Invalid action"

if __name__ == "__main__":
    action = sys.argv[1]
    input_data = sys.argv[2] if len(sys.argv) > 2 else None  # Capture the input if provided
    result = main(action, input_data)