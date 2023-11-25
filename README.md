# Video Processing CLI

This project provides a command-line tool for generating and embedding subtitles into videos, with additional options for audio processing and text to speech conversion.

## Features

- Generate subtitles from the audio within a video or from a separate audio file.
- Embed subtitles directly into the video.
- Convert text to speech and overlay or replace the existing audio track in the video.
- Adjust the volume of the original video audio.
- Control the speed of the generated text-to-speech audio.

## Installation

Clone the repository and install the required Python dependencies:

```bash
git clone https://github.com/siinghd/auto-subtitle-tts
cd auto-subtitle-tts
pip install -r requirements.txt
```

`ffmpeg` must also be installed on your system for video and audio processing.

## Usage

Use the CLI with the following command pattern:

```bash
python3 ./src/cli.py --video VIDEO_PATH [options]
```

Options:
- `--video VIDEO_PATH`: Path to the video file.
- `--audio AUDIO_PATH`: Path to an alternative audio file (optional).
- `--text TEXT_PATH`: Path to a text file for text-to-speech conversion (optional).
- `--volume_factor VOLUME`: Float value to adjust the volume of the video's original audio (optional, default is 1). 1=max volume, 0 mute
- `--speed SPEED`: Integer value to control the speed percentage of the text-to-speech audio (optional, default is 5).
- `--apikey API_KEY`: IBM TTS service API key if using text-to-speech features (optional).
- `--url SERVICE_URL`: IBM TTS service URL if using text-to-speech features (optional).

Examples:

Generate subtitles from a video's audio:

```bash
python3 ./src/cli.py --video path/to/video.mp4
```
Generate subtitles from a custom audio:

```bash
python3 ./src/cli.py --video path/to/video.mp4 --audio path/to/audio.mp3 --volume_factor=0 (volume_factor=0.2 = original audio of the video will be less audiable)
```
Overlay text-to-speech audio onto a video with a custom speed and volume adjustment:

```bash
python3 ./src/cli.py --video path/to/video.mp4 --text path/to/textfile.txt --speed 120 --apikey yourapikey --url yourserviceurl
```

## Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
