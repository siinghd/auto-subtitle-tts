# Video Processing CLI

This project provides a command-line tool for generating and embedding subtitles into videos, with additional options for audio processing and text-to-speech conversion using IBM Watson or ElevenLabs services.

## Features

- Generate subtitles from the audio within a video or from a separate audio file.
- Embed subtitles directly into the video.
- Convert text to speech and overlay or replace the existing audio track in the video.
- Cut the video to a specified duration using start and end times.
- Adjust the volume of the original video audio.
- Control the speed of the generated text-to-speech audio (IBM only for now).

## Installation

Clone the repository and install the required Python dependencies:

```bash
git clone https://github.com/siinghd/auto-subtitle-tts
cd auto-subtitle-tts
pip install -r requirements.txt
```

`ffmpeg` and `moviepy` must also be installed on your system for video and audio processing.

## Usage

Use the CLI with the following command pattern:

```bash
python3 ./src/cli.py --video VIDEO_PATH [options]
```

Options:
- `--video VIDEO_PATH`: Path to the video file.
- `--audio AUDIO_PATH`: Path to an alternative audio file (optional).
- `--text TEXT_PATH`: Path to a text file for text-to-speech conversion (optional).
- `--start_time START_TIME`: Start time to cut the video, format 'hh:mm:ss' or seconds (optional).
- `--end_time END_TIME`: End time to cut the video, format 'hh:mm:ss' or seconds (optional).
- `--volume_factor VOLUME`: Float value to adjust the volume of the video's original audio (optional, default is 1).
- `--speed SPEED`: Integer value to control the speed percentage of the text-to-speech audio (optional, default is 0 negative supported,IBM ONLY FOR NOW).
- `--apikey API_KEY`: IBM TTS service API key or ElevenLabs API key, depending on the selected service (optional).
- `--url SERVICE_URL`: IBM TTS service URL or ElevenLabs service URL, depending on the selected service (optional).
- `--service_tts SERVICE`: Select between 'IBM' or 'ELABS' for the text-to-speech service (optional, default is 'IBM').

Examples:

Generate subtitles from a video's audio:

```bash
python3 ./src/cli.py --video path/to/video.mp4
```

Generate subtitles and cut the video with custom audio:

```bash
python3 ./src/cli.py --video path/to/video.mp4 --audio path/to/audio.mp3 --start_time 00:00:30 --end_time 00:02:30
```

Overlay text-to-speech audio onto a video with custom speed and service:

```bash
python3 ./src/cli.py --video path/to/video.mp4 --text path/to/textfile.txt --speed -10 --apikey yourapikey --url yourserviceurl --service_tts ELABS
```

Convert a text file to speech without video:

```bash
python3 ./src/cli.py --text path/to/textfile.txt --apikey yourapikey --url yourserviceurl --service_tts IBM
```

## Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
