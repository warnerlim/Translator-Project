from openai import OpenAI
from apikeys import apikey

# Set your OpenAI API key
client = OpenAI(api_key = apikey)

def translate_text(text, model="gpt-4o"): # Prompt for translation purposes
    """
    Translates a given text from Japanese to English using the specified OpenAI model.
    """
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": 
                f"""
                You are a translator tasked with translating Japanese text to English. Your goal is to accurately translate each segment and maintain the structure and order provided in the original text. Ensure that you do not skip any segment, and follow the format shown in the example below.

                Example:
                これは例文です\nThis is an example sentence.\n

                Your task:
                1. Translate each segment accurately and completely.
                2. Maintain the order and structure of the segments as in the original text.
                3. Ensure that each Japanese segment is followed by its corresponding English translation.
                4. Make sure the number of Japanese segments matches the number of English segments. If there are 75 Japanese segments, there must be 75 English segments.
                5. Input format: なんか女の子の話するとねチャット欄に女の子増えるの何とかだわよ\nありがとうですわよつって\nんー\nんー\n死者誤入しないんかい\n死者誤入して73\
                Text to translate:
                {text}
                """,
            }
        ],
        model=model,
        max_tokens=4096,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content

def read_file_in_chunks(file_path, chunk_lines=300): # Reads file at a chunk of 300 lines per interval
    """
    Generator to read a file in chunks of specified size.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            lines = []
            for _ in range(chunk_lines):
                line = file.readline()
                if not line:
                    break
                lines.append(line)
            if not lines:
                break
            yield ''.join(lines)

def split_text(translated_text):
    lines = translated_text.strip().split('\n\n') # Splits the text because it looks like this, JP Text\nEng Text\n\nJP Text\nEng Text\n\n
    translation_map = {} # Hashmap
    for block in lines:
        parts = block.strip().split('\n')
        japanese_text = parts[0]
        english_text = ""
        for part in parts:
            if any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in part):
                english_text = part
        translation_map[japanese_text] = english_text
    return translation_map

def map_original_array(original_array, map):
    # Step 4: Map the original array to English translations
    translated_array = [map.get(jp, "") for jp in original_array]
    return translated_array

def process_subtitle_line(line):
    if "English translation: " in line:
        return line.replace("English translation: ", "")
    else:
        return line

def process_translation(lines_to_translate):
    unique_japanese_set = set(lines_to_translate) # Uses a hashset so I can remove repetitive text 
    combined_text = "\n".join(unique_japanese_set) # Combines array of JP text back to string
    translated_text = translate_text(combined_text) # Translates text
    edited_lines = process_subtitle_line(translated_text) # Removes problem when GPT returns English Translation: [english translation here]
    translation_map = split_text(edited_lines) # Splits text into hashmap, JP text as keys, ENG text as values
    translated_array = map_original_array(lines_to_translate, translation_map) # Compares original JP text array and finds equal value in the hashmap, returns ENG text array 
    return translated_array

def translate_file(file_path, output_path):
    """
    Translate the content of a file from Japanese to English and save the result to another file.
    """
    with open(output_path, 'w', encoding='utf-8') as output_file:
        lines_number = 1
        lines_timing = []
        lines_to_translate = []

        for chunk in read_file_in_chunks(file_path): # Splits file into chunks of 75 translations each time, to prevent overloading of token usage in input text.
            lines = chunk.splitlines(True)
            line_number = 0
            for line in lines:          
                if line_number % 4 == 1:
                    lines_timing.append(line.strip()) # Appends all timings from the text file to array
                elif line_number % 4 == 2:
                    lines_to_translate.append(line.strip()) # Appends all JP text from the text file to array

                line_number += 1 # Counter
            
            translated_lines = process_translation(lines_to_translate) # Translator function

            for i in range(len(lines_timing)):
                output_file.write(str(lines_number) + "\n") # Writes subtitle number, for SRT Formatting
                output_file.write(lines_timing[i] + "\n") # Timings go here
                output_file.write(translated_lines[i] + "\n") # Translated lines go here
                output_file.write("\n") # New line for formatting purposes
                lines_number += 1
            lines_to_translate.clear() # Clears current chunk of text to allow next chunk to be translated
            lines_timing.clear() # Clears current chunk so it aligns with current translation
