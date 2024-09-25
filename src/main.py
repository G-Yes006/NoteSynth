from audio_extractor import extract_audio
from speech_to_text import audio_to_text
from note_generator import generate_notes
import os

def main(video_file):
    """
    Main function to extract audio from a video file, convert it to text,
    and generate notes.

    Parameters:
    - video_file: str, path to the video file.
    """
    audio_file = os.path.join(os.path.dirname(__file__), "extracted_audio.wav")
    extract_audio(video_file, audio_file)
    transcribed_text = audio_to_text(audio_file)
    notes = generate_notes(transcribed_text)
    return notes

if __name__ == "__main__":
    # Use the converted video file
    video_path = os.path.join(os.path.dirname(__file__), "sample.mp4")
    notes = main(video_path)
    print("Generated Notes:")
    for note in notes:
        print("-", note)
