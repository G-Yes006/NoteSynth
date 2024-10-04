import speech_recognition as sr
from pydub import AudioSegment
import time
import re

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
        
        # Process the text and add icons
        sentences = break_into_sentences(text)
        return add_icons_to_notes(sentences)  # Return notes with icons

    except sr.UnknownValueError:
        return ["Could not understand audio"]
    except sr.RequestError as e:
        return [f"Could not request results from speech recognition service; {e}"]
    except Exception as e:
        return [f"An error occurred during recognition: {str(e)}"]

def break_into_sentences(text):
    """
    Breaks a block of text into sentences for easier processing.
    
    Parameters:
    - text: str, the transcribed text to break into sentences.
    
    Returns:
    - list of str: The text split into individual sentences.
    """
    # Use regex to split text into sentences.
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return [sentence.strip() for sentence in sentences if sentence]

def add_icons_to_notes(sentences):
    """
    Adds relevant icons (emojis) to each sentence based on its content.
    
    Parameters:
    - sentences: list of str, the transcribed text as a list of sentences.

    Returns:
    - list of str: Sentences with added icons.
    """
    icons = {
        "reminder": "🔔",  # Reminder related
        "idea": "💡",      # New ideas
        "action": "✅",    # Action items
        "warning": "⚠️",  # Warnings or cautions
        "question": "❓",  # Questions or doubts
        "information": "ℹ️",  # General info
        "important": "⭐", # Important points
    }

    enhanced_notes = []
    for sentence in sentences:
        # Match keywords to assign relevant icons
        if any(keyword in sentence.lower() for keyword in ["remind", "remember"]):
            icon = icons["reminder"]
        elif any(keyword in sentence.lower() for keyword in ["idea", "thought"]):
            icon = icons["idea"]
        elif any(keyword in sentence.lower() for keyword in ["action", "complete", "done"]):
            icon = icons["action"]
        elif any(keyword in sentence.lower() for keyword in ["warning", "caution"]):
            icon = icons["warning"]
        elif any(keyword in sentence.lower() for keyword in ["what", "how", "why"]):
            icon = icons["question"]
        elif any(keyword in sentence.lower() for keyword in ["info", "information", "details"]):
            icon = icons["information"]
        elif any(keyword in sentence.lower() for keyword in ["important", "priority"]):
            icon = icons["important"]
        else:
            # Default or random icon
            icon = random.choice(list(icons.values()))
        
        # Add the icon and format as a bullet point
        enhanced_notes.append(f"{icon} {sentence}")

    return enhanced_notes
