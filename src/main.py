from audio_extractor import extract_audio
from speech_to_text import audio_to_text
from note_generator import generate_notes
import os
import uuid

def main(video_file):
    """
    Main function to extract audio from a video file, convert it to text,
    and generate notes.

    Parameters:
    - video_file: str, path to the video file.
    """
    # Ensure the 'audio' directory exists
    audio_dir = os.path.join(os.path.dirname(__file__), "../audio")
    os.makedirs(audio_dir, exist_ok=True)

    # Generate a unique filename for the audio output
    unique_id = uuid.uuid4()
    audio_file = os.path.join(audio_dir, f"extracted_audio_{unique_id}.wav")
    
    extract_audio(video_file, audio_file)
    transcribed_text = audio_to_text(audio_file)
    notes = generate_notes(transcribed_text)
    
    # Optionally clean up the audio file after processing
    os.remove(audio_file)
    
    return notes

if __name__ == "__main__":
    # Ask user for video file input
    video_path = input("Please provide the path to the video file: ")
    
    if os.path.exists(video_path):
        notes = main(video_path)
        print("Generated Notes:")
        for note in notes:
            print("-", note)
    else:
        print(f"The file {video_path} does not exist.")
