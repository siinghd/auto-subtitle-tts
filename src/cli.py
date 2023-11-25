# Import necessary modules for the script's functionality
import argparse
from subtitle_generator import generate_subtitles
from subtitle_editor import edit_subtitles
from text_to_audio import text_to_speech_ibm, text_to_speech_elevenlabs

def main():
    # Set up an argument parser for command-line options
    parser = argparse.ArgumentParser(description="Video Processing CLI")
    
    # Add command-line arguments for the video, audio, and text file paths, as well as IBM API credentials
    parser.add_argument('--video', help='Path to the video file')
    parser.add_argument('--audio', help='Path to an audio file', default=None)
    parser.add_argument('--text', help='Path to a text file', default=None)
    parser.add_argument('--start_time', help='Cut the video from start time', default=None)
    parser.add_argument('--end_time', help='Cut the video to end time', default=None)
    parser.add_argument('--volume_factor', help='Volume of the video original audio', default=1)
    parser.add_argument('--speed', help='Speed of the text to speech audio', default=0)
    parser.add_argument('--apikey', help='IBM TTS service API key OR elevenlabs.io API key', required=False, default='')
    parser.add_argument('--url', help='IBM TTS service URL or elevenlabs.io service URL', required=False, default='')
    parser.add_argument('--service_tts', help='IBM TTS service or Elevenlabs.io service | IBM | ELABS', required=False, default='IBM')
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    
    # Check the combination of arguments and call the appropriate functions
    
    # If a video is provided without audio or text, generate subtitles from the video's audio
    if args.video and not args.audio and not args.text:
        generate_subtitles(args.video, None, None, args.volume_factor,args.start_time,args.end_time)
        
    # If a video and audio are provided without text, generate subtitles from the provided audio
    elif args.video and args.audio and not args.text:
        generate_subtitles(args.video, args.audio, None, args.volume_factor,args.start_time,args.end_time)
        
    # If a video and text are provided, convert the text to speech, then generate subtitles from this audio
    elif args.video and args.text:
        # Determine the path for the output audio file by replacing the text file extension with '.mp3'
        output_audio_path = args.text.replace('.txt', '.mp3')
        
        # Read the content of the provided text file
        with open(args.text, 'r') as file:
            text_content = file.read()
        
        # Convert the text content to speech using IBM Watson TTS service
        if args.service_tts == 'IBM':
            text_to_speech_ibm(text_content, output_audio_path, args.apikey, args.url, speed=args.speed)
        else:
            text_to_speech_elevenlabs(text_content, output_audio_path, args.apikey, args.url, speed=args.speed)
        # Generate subtitles for the video using the audio generated from the text
        generate_subtitles(args.video, output_audio_path, None, args.volume_factor,args.start_time,args.end_time)
        
        # Generate only the audio file
    elif args.text:
        # Determine the path for the output audio file by replacing the text file extension with '.mp3'
        output_audio_path = args.text.replace('.txt', '.mp3')
        
        # Read the content of the provided text file
        with open(args.text, 'r') as file:
            text_content = file.read()
        
        # Convert the text content to speech using IBM Watson TTS service
        if args.service_tts == 'IBM':
            text_to_speech_ibm(text_content, output_audio_path, args.apikey, args.url, speed=args.speed)
        else:
            text_to_speech_elevenlabs(text_content, output_audio_path, args.apikey, args.url, speed=args.speed)
        


# Entry point for the script, ensuring it only runs when executed directly
if __name__ == "__main__":
    main()
