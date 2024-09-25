import speech_recognition as sr
from pydub import AudioSegment
import time

def audio_to_text(audio_file):
    """
    Convert audio to text using the SpeechRecognition library.
    
    Parameters:
    - audio_file: str, path to the audio file.

    Returns:
    - list: Transcribed text as a list of lines.
    """
    recognizer = sr.Recognizer()
    
    print(f"Starting transcription for audio file: {audio_file}")
    
    # Get the duration of the audio file
    audio = AudioSegment.from_wav(audio_file)
    duration_ms = len(audio)  # Duration in milliseconds
    print(f"Audio duration: {duration_ms / 1000:.2f} seconds")
    
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        print("Audio data recorded.")

    # Attempt to use Sphinx for offline recognition
    try:
        print("Recognizing audio using PocketSphinx...")
        start_time = time.time()
        text = recognizer.recognize_sphinx(audio_data)  # Removed timeout
        
        # Simulate progress
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time >= 5:  # Adjust this value as needed
                break
            percentage = (elapsed_time / (duration_ms / 1000)) * 100
            print(f"Progress: {percentage:.2f}%")
            time.sleep(1)  # Update every second
            
        print("Recognition complete.")
        return text.splitlines()  # Return notes as a list of lines
    except sr.UnknownValueError:
        return ["Could not understand audio"]
    except sr.RequestError as e:
        return [f"Could not request results from speech recognition service; {e}"]
    except Exception as e:
        return [f"An error occurred during recognition: {str(e)}"]
