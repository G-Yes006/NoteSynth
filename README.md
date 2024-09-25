# NoteSynth

NoteSynth is a simple Python application that extracts audio from video files and generates notes from the audio content.

## Features
- Extract audio from video files
- Convert audio to text using speech recognition (offline using PocketSphinx)
- Generate notes from transcribed text
- Simulated progress updates during transcription

## Requirements
- Python 3.x
- Required packages listed in `requirements.txt`

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd NoteSynth
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Requirements
The following packages are required and listed in `requirements.txt`:
- **moviepy**: For video processing and extracting audio.
- **SpeechRecognition**: For converting audio to text.
- **pydub**: For handling audio files and getting their duration.
- **pocketsphinx**: Offline speech recognition engine used by the SpeechRecognition library.
- **ffmpeg**: Required by `moviepy` and `pydub` for handling video/audio processing.
  
   You can install `ffmpeg` using the following:
   - **Ubuntu**: 
     ```bash
     sudo apt install ffmpeg
     ```
   - **Windows**: Download and install `ffmpeg` from [ffmpeg.org](https://ffmpeg.org/download.html).

## How to Use

1. Place the video file in the `src` directory (e.g., `sample2.mp4`).
2. Run the application:
   ```bash
   python3 src/main.py
   ```

3. The extracted audio will be processed, and notes will be generated from the transcribed text.

## Additional Commands
To cut the first 30 seconds of a video, use the following `ffmpeg` command:
```bash
ffmpeg -i input_video.mp4 -ss 00:00:00 -t 00:00:30 -c copy output_video.mp4
```