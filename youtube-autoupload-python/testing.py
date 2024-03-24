# from moviepy.editor import AudioFileClip, ImageClip, concatenate_videoclips, CompositeVideoClip
# from moviepy.video.fx.all import fadein, fadeout

# # File paths
# image_path = 'C:\\Automate\\AI-Automation-Video-Generating\\AI-Automation\\youtube-autoupload-python\\DataLibrary\\Images\\Love\\alia.jpg'
# audio_path = 'C:\\Automate\\AI-Automation-Video-Generating\\AI-Automation\\youtube-autoupload-python\\DataLibrary\\audio\\Love\\your_song.mp3'

# # Video (Image Clip) with fade-in and fade-out
# img_clip = ImageClip(image_path).set_duration(10)  # Image clip with 10 seconds duration
# img_clip = fadein(img_clip, 1).fadeout(1)  # Apply fade-in and fade-out effects to the image clip

# # Audio with fade-in and fade-out
# audio_clip = AudioFileClip(audio_path).subclip(0, 10)  # Audio matched to the duration of the video
# audio_clip = audio_clip.audio_fadein(1).audio_fadeout(1)  # Apply fade-in and fade-out effects to the audio clip

# # Setting the audio to the video
# final_clip = CompositeVideoClip([img_clip]).set_audio(audio_clip)  # Use CompositeVideoClip to ensure effects apply

# # Save the final video
# output_path = 'C:\\Automate\\AI-Automation-Video-Generating\\AI-Automation\\youtube-autoupload-python\\DataLibrary\\test_output.mp4'
# final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=24)

# from moviepy.editor import ImageClip

# # Minimal example to test functionality
# image_path = 'C:\\Automate\\AI-Automation-Video-Generating\\AI-Automation\\youtube-autoupload-python\\DataLibrary\\Images\\Love\\alia.jpg'
# output_path = 'C:\\Automate\\AI-Automation-Video-Generating\\AI-Automation\\youtube-autoupload-python\\DataLibrary\\test_output.mp4'

# img_clip = ImageClip(image_path).set_duration(5)  # No effects, just plain video
# img_clip.write_videofile(output_path, codec='libx264', fps=24)

# from moviepy.editor import ImageClip

# # Test with a very basic setup
# img_clip = ImageClip('C:\\A   utomate\\AI-Automation-Video-Generating\\AI-Automation\\youtube-autoupload-python\\DataLibrary\\Images\\Love\\alia.jpg').set_duration(5)
# img_clip.write_videofile('C:\\Automate\\AI-Automation-Video-Generating\\AI-Automation\\youtube-autoupload-python\\DataLibrary\\test_output.mp4', codec='libx264', fps=24)

from moviepy.editor import *

image_clip = ImageClip('C:\\Automate\\AI-Automation-Video-Generating\\AI-Automation\\youtube-autoupload-python\\DataLibrary\\Images\\Love\\alia.jpg').set_duration(10)
audio_clip = AudioFileClip('C:\\Automate\\AI-Automation-Video-Generating\\AI-Automation\\youtube-autoupload-python\\DataLibrary\\audio\\Love\\your_song.mp3').subclip(0, 10)
# Play the audio to confirm it's working
print("Playing audio for confirmation...")
audio_clip.preview()  # This should play the audio out loud

video_clip = image_clip.set_audio(audio_clip)
video_clip.write_videofile('C:\\Automate\\AI-Automation-Video-Generating\\AI-Automation\\youtube-autoupload-python\\DataLibrary\\test_output.mp4', codec='libx264', audio_codec='aac',fps=25, verbose=True, logger="bar")
