from faster_whisper import WhisperModel
import datetime

def seconds_to_srt_time(seconds):
    td = datetime.timedelta(seconds=seconds)
    time_str = str(td)
    if '.' in time_str:
        time_str = time_str[:-3].replace('.', ',')
    else:
        time_str += ',000'
    return time_str

def whisper_function():
    # Initialize the Whisper model
    model = WhisperModel("large-v2", device="cuda", compute_type="float16")

    # Transcribe the audio file
    segments, _ = model.transcribe(audio="input_audio.mp3", hallucination_silence_threshold=5, condition_on_previous_text=False, vad_filter=True)
    segment_list = list(segments)

    # Open the text file with UTF-8 encoding to handle Japanese characters
    with open("raw_text.txt", "a", encoding="utf-8") as f:
        # Add transcribed segments to the txt file
        for i, segment in enumerate(segment_list, 1):
            start_time = seconds_to_srt_time(segment.start)
            end_time = seconds_to_srt_time(segment.end)
            text = f"{i}\n{start_time} --> {end_time}\n{segment.text}\n\n"

            f.write(text)