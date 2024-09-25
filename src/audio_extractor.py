from moviepy.editor import VideoFileClip
import time

def extract_audio(video_file, audio_file):
    print(f"Attempting to open video file: {video_file}")
    video = VideoFileClip(video_file)
    print("Video file opened successfully.")
    
    # Simulate the extraction process
    print("Extracting audio...")
    audio = video.audio
    audio.write_audiofile(audio_file, codec='pcm_s16le')
    print("Audio extraction complete.")
    
    video.close()
