import boto3
import os
from moviepy.editor import VideoFileClip

def convert_video_to_audio(bucket_name, file_key):
    try:
        # Initialize S3 client
        s3 = boto3.client('s3')

        # Initialize SNS client
        sns = boto3.client('sns')

        # Download the video from S3 to a temporary file
        local_video_path = '/tmp/temp_video.mp4'
        s3.download_file(bucket_name, file_key, local_video_path)

        # Use MoviePy to convert video to audio
        local_audio_path = '/tmp/temp_audio.mp3'
        clip = VideoFileClip(local_video_path)
        clip.audio.write_audiofile(local_audio_path)

        # Upload the audio file to another S3 bucket
        audio_bucket_name = 'audio-bucket-lambda-s3'
        audio_file_key = f"audio/{file_key.split('/')[-1].split('.')[0]}.mp3"
        s3.upload_file(local_audio_path, audio_bucket_name, audio_file_key)

        # Clean up temporary files
        os.remove(local_video_path)
        os.remove(local_audio_path)

        sns.publish(
            TopicArn='arn:aws:sns:us-east-1:112463047312:video-to-audio-email-topic', 
            Message='Video converted to audio and saved to S3.'
        )

        print("Video converted to audio and saved to S3.")
    except Exception as e:
        print(f"Error converting video to audio: {e}")

# Fetch environment variables passed from ECS task
bucket_name = "event-driven-arch-videos"
file_key = "local_path_to_download_video.mp4"

# Convert video to audio
convert_video_to_audio(bucket_name, file_key)
