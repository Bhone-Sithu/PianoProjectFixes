import os
import requests

# List of note names
notes = [
    "A0", "C1", "Ds1", "Fs1", "A1", "C2", "Ds2", "Fs2", "A2", "C3",
    "Ds3", "Fs3", "A3", "C4", "Ds4", "Fs4", "A4", "C5", "Ds5", "Fs5",
    "A5", "C6", "Ds6", "Fs6", "A6", "C7", "Ds7", "Fs7", "A7", "C8"
]

# Base URL for the piano samples
base_url = "https://tonejs.github.io/audio/salamander/"

# Directory to save the files
download_dir = "piano_samples"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Function to download a file
def download_file(note):
    file_url = f"{base_url}{note}.mp3"
    file_path = os.path.join(download_dir, f"{note}.mp3")

    response = requests.get(file_url)
    with open(file_path, "wb") as file:
        file.write(response.content)

# Download all notes
for note in notes:
    print(f"Downloading {note}.mp3...")
    download_file(note)
    print(f"{note}.mp3 downloaded!")

print("All files downloaded!")