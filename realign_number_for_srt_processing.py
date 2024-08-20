
# Ask user for the starting line number
while True:
    try:
        input_line_number = int(input("Enter beginning of line number that needs to be edited here: "))
        break  # Exit the loop if input is successfully converted to integer
    except ValueError:
        print("Please enter a valid integer.")

# Ask user for the number adjustment
while True:
    try:
        number_adjustment = int(input("Enter number adjustment: "))
        break  # Exit the loop if input is successfully converted to integer
    except ValueError:
        print("Please enter a valid integer.")

# File path to your text file
file_path = "raw_english_text.txt"

# Function to upscale the modified integer (assuming upscale means replacing the line)
def upscale_integer(original_line, modified_integer):
    return original_line.replace(original_line.split()[0], str(modified_integer))

# Open the file for reading and writing
with open(file_path, 'r+', encoding='utf-8') as file:
    lines = file.readlines()
    # Iterate over every 4th line starting from line number, for some reason you need to -1. idk why
    for i in range(input_line_number - 1, len(lines), 4):
        try:
            # Get the integer from the line and adjust
            current_integer = int(lines[i].strip())
            modified_integer = current_integer + number_adjustment
            
            # Upscale the result in the original line format
            lines[i] = upscale_integer(lines[i], modified_integer)
            
        except ValueError:
            print(f"Error processing line {i}: {lines[i].strip()} is not an integer.")

    # Go to the beginning of the file and write all the modified lines
    file.seek(0)
    file.writelines(lines)
    file.truncate()

print("Modification complete.")