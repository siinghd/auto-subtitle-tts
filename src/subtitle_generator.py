# Import necessary libraries
import moviepy.editor as mp  # For video and audio processing
import whisper  # OpenAI's Whisper model for transcription
import os  # For interacting with the file system
from datetime import timedelta  # For representing time intervals
import srt  # Library for handling SRT subtitle files
import subprocess  # For executing shell commands

# Function to generate an SRT content from the transcription segments
def generate_srt(segments):
    subtitles = []
    # Loop through each segment to create subtitle entries
    for i, segment in enumerate(segments, start=1):
        subtitles.append(srt.Subtitle(index=i,
                                      start=segment['start'],
                                      end=segment['end'],
                                      content=segment['text']))
    # Compile the subtitle entries into the SRT format
    return srt.compose(subtitles)

# Function to extract audio from the video file
def extract_audio(video_path):
    # Load the video file
    video = mp.VideoFileClip(video_path)
    # Construct the audio file path by replacing video extension with '.wav'
    audio_path = video_path.rsplit('.', 1)[0] + '.wav'
    # Write the audio to the file
    video.audio.write_audiofile(audio_path, codec='pcm_s16le')
    return audio_path

# Function to perform transcription without timestamps
def transcribe(audio_path):
    # Load the Whisper model
    model = whisper.load_model("small.en")
    # Transcribe the audio file
    result = model.transcribe(audio_path)
    return result['text']

# Function to perform transcription with timestamps
def transcribe_with_timestamps(audio_path):
    # Load the Whisper model
    model = whisper.load_model("base")
    # Transcribe the audio file with verbose output disabled
    result = model.transcribe(audio_path, verbose=False)
    
    segments = []
    # Extract segments with text and timing information
    for segment in result['segments']:
        if segment['text'] and segment['start'] is not None and segment['end'] is not None:
            segments.append({
                'start': timedelta(seconds=segment['start']),
                'end': timedelta(seconds=segment['end']),
                'text': segment['text']
            })
    return segments

# Function to embed subtitles into the video and adjust audio volume
def embed_subtitles(video_path, srt_path, output_video_path, additional_audio_path, fontname='Arial', volume_factor=0.5):
    command = [
        'ffmpeg',  # Call ffmpeg
        '-i', video_path,  # Input video file
        '-i', additional_audio_path,  # Additional audio file
        # Apply audio volume filter and mix additional audio with original audio
        '-filter_complex', f"[0:a]volume={volume_factor}[a1]; [1:a][a1]amix=inputs=2[a]",
        # Apply subtitles with custom style
        '-vf', f"subtitles={srt_path}:force_style='Alignment=10,MarginV=10,FontName={fontname}'",
        # Map video and audio streams to output
        '-map', '0:v',
        '-map', '[a]',
        # Set video codec and quality
        '-c:v', 'libx264',
        '-crf', '23',
        '-preset', 'veryfast',
        # Set audio codec and bitrate
        '-c:a', 'aac',
        '-b:a', '192k',
        # Specify output video file
        output_video_path
    ]
    # Execute the ffmpeg command
    subprocess.run(command, check=True)
    
# Function to generate subtitles and embed them into the video
def generate_subtitles(video_path, audio_path=None, srt_path=None, volume_factor=0.5):
    # Check if the video file exists
    if not os.path.exists(video_path):
        print(f"Error: The video file {video_path} does not exist.")
        return
    
    # Use existing audio file if it's provided and exists
    if audio_path and os.path.exists(audio_path):
        print(f"Using existing audio file: {audio_path}")
    else:
        # Extract audio from the video if no audio file is provided
        print("Extracting audio from video...")
        audio_path = extract_audio(video_path)
    
    # Use existing SRT file if it's provided and exists
    if srt_path and os.path.exists(srt_path):
        print(f"Using existing subtitles file: {srt_path}")
    else:
        # Transcribe audio and generate SRT content if no SRT file is provided
        print("Transcribing audio and generating subtitles...")
        segments = transcribe_with_timestamps(audio_path)
        srt_content = generate_srt(segments)
        srt_path = audio_path.rsplit('.', 1)[0] + '.srt'
        with open(srt_path, 'w') as file:
            file.write(srt_content)
    
    print(f"Subtitles saved to {srt_path}")
    
    # Construct the output video file path
    output_video_path = 'sub_' + os.path.basename(video_path)
    # Embed subtitles into the video if the output video doesn't already exist
    if not os.path.exists(output_video_path):
        print("Embedding subtitles into video...")
        embed_subtitles(video_path, srt_path, output_video_path, audio_path, volume_factor=volume_factor)
        print(f"Video with subtitles saved to {output_video_path}")
    else:
        # Notify the user if the output video file already exists
        print(f"The output video file {output_video_path} already exists.")
