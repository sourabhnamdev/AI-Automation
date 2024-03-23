from moviepy.editor import VideoFileClip, AudioFileClip

try:
    video = VideoFileClip("C:\\Automate\\AI-Automation-Video-Generating\\youtube-autoupload-python\\DataLibrary\\TempFiles\\5_images_video.mp4")
    audio = AudioFileClip("C:\\Automate\\AI-Automation-Video-Generating\\youtube-autoupload-python\\DataLibrary\\audio\\Love\\your_song.mp3")
    final = video.set_audio(audio)
    final.write_videofile("C:\\Automate\\AI-Automation-Video-Generating\\youtube-autoupload-python\\test_output.mp4", codec="libx264", audio_codec="aac")
finally:
    video.close()
    audio.close()
