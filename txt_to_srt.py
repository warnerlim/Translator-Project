def convert_txt_to_srt(txt_file_path, srt_file_path):
    with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
        content = txt_file.read()

    with open(srt_file_path, 'w', encoding='utf-8') as srt_file:
        srt_file.write(content)