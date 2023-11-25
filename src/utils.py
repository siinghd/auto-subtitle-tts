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