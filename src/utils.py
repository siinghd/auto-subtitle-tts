import moviepy.editor as mp  # For video and audio processing

def cut_video(video_path, start_time, end_time, output_video_path):
    # Load the video clip
    video = mp.VideoFileClip(video_path)
    video_duration = video.duration

    # Convert start and end times to seconds
    start_time_seconds = convert_to_seconds(start_time)
    end_time_seconds = convert_to_seconds(end_time) if end_time else video_duration

    # Check if the start and end times are within the video duration
    if start_time_seconds < 0 or start_time_seconds > video_duration:
        raise ValueError(f"Start time {start_time} is out of range for the video duration {video_duration:.2f} seconds.")
    if end_time_seconds < start_time_seconds or end_time_seconds > video_duration:
        raise ValueError(f"End time {end_time} is out of range for the video duration {video_duration:.2f} seconds.")

    # Cut the clip to the user-specified portion
    cut_clip = video.subclip(start_time_seconds, end_time_seconds)
    
    # Write the result to the output file
    cut_clip.write_videofile(output_video_path, codec='libx264', audio_codec='aac')

    # Close the video file to release resources
    video.close()

def convert_to_seconds(time_str):
    # This function converts a time string in hh:mm:ss format to seconds.
    if isinstance(time_str, str):
        h, m, s = time_str.split(':')
        print(h,m,s)
        return int(h) * 3600 + int(m) * 60 + int(s)
    return time_str

def loop_video_to_audio_length(video_path, audio_path, output_video_path):
    # Load the audio to get its duration
    audio_clip = mp.AudioFileClip(audio_path)
    audio_duration = audio_clip.duration
    
    # Load the video to get its duration
    video_clip = mp.VideoFileClip(video_path)
    video_duration = video_clip.duration
    
    # Calculate how many times to loop the video
    loop_count = int(audio_duration // video_duration) + 1
    
    # Create a list of the video clip repeated
    final_clip = mp.concatenate_videoclips([video_clip] * loop_count)
    
    # Set the final video's audio to be the audio clip
    final_clip = final_clip.set_audio(audio_clip)
    
    # Write the result to the output file path
    final_clip.write_videofile(output_video_path, codec='libx264', audio_codec='aac')
    
    # Close the clips to release resources
    audio_clip.close()
    video_clip.close()
    final_clip.close()
    
def check_audio_video_length(video_path, audio_path):
    # Load the video and get its duration
    video_clip = mp.VideoFileClip(video_path)
    video_duration = video_clip.duration
    video_clip.close()  # Close the video clip to release resources

    # Load the audio and get its duration
    audio_clip = mp.AudioFileClip(audio_path)
    audio_duration = audio_clip.duration
    audio_clip.close()  # Close the audio clip to release resources

    # Compare the durations
    if audio_duration > video_duration:
        return True  # Audio is longer than the video
    else:
        return False  # Audio is not longer than the video