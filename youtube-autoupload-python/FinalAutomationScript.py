import os
import random
from moviepy.editor import AudioFileClip, concatenate_videoclips, ImageClip
import inspect
import traceback
# from EffectAndTransitionAndUtilityOthers.VideoEffects import VideoEffects  # Your custom class
from EffectAndTransitionAndUtilityOthers.VideoTransitions import VideoTransitions  # Your custom class

# def get_effect_methods():
#     # List all public methods from the VideoEffects class that are actual effects
#     print("Getting effect methods from VideoEffects class.")
#     methods = [method_name for method_name, method_obj in inspect.getmembers(VideoEffects, predicate=inspect.isfunction) if not method_name.startswith('_')]
#     print(f"Effect methods found: {methods}")
#     return methods

def get_transition_methods():
    # List all public methods from the VideoTransitions class that are actual transitions
    print("Getting transition methods from VideoTransitions class.")
    methods = [method_name for method_name, method_obj in inspect.getmembers(VideoTransitions, predicate=inspect.isfunction) if not method_name.startswith('_')]
    print(f"Transition methods found: {methods}")
    return methods

# Define the size to which all images will be resized
width, height = 1200, 2000

class VideoCreator:
    def __init__(self, root_dir='C:\\Automate\\AI-Automation-Video-Generating\\AI-Automation\\youtube-autoupload-python\\DataLibrary'):
        print("Initializing VideoCreator...")
        self.root_dir = root_dir
        self.categories = ['Love']  # Adjust as necessary
        self.selected_category = None
        self.images = []
        self.song = None
        print("VideoCreator initialized.")

    def select_random_files(self):
        try:
            print("Selecting random files...")
            self.selected_category = random.choice(self.categories)
            print(f"Selected category: {self.selected_category}")
            
            # For images
            image_category_path = os.path.join(self.root_dir, 'Images', self.selected_category)
            # image_files = [f for f in os.listdir(image_category_path) if os.path.isfile(os.path.join(image_category_path, f))]
            image_files = [os.path.join(image_category_path, f) for f in os.listdir(image_category_path) if os.path.isfile(os.path.join(image_category_path, f))]
            self.images = random.sample(image_files, min(len(image_files), 10))
            print(f"Selected images: {self.images}")
            
            # For music
            music_category_path = os.path.join(self.root_dir, 'audio', self.selected_category)
            music_files = [f for f in os.listdir(music_category_path) if os.path.isfile(os.path.join(music_category_path, f))]
            self.song = os.path.join(music_category_path, random.choice(music_files))
            print(f"Selected song: {self.song}")
        except Exception as e:
            print(f"Error selecting files: {e}")
    
    def apply_transitions(self, images):
        print("Applying transitions...")
        final_clips = []
        transition_methods = get_transition_methods()

        # Create ImageClips and store in a list for transition application
        # In apply_transitions method:
        image_clips = []  # Set each image duration to 6 seconds
        for img in images:
            if img:  # Ensure the image is not None
                img_clip = ImageClip(img).set_duration(4)  # Set each image duration
                img_clip = img_clip.resize(newsize=(width, height))  # Resize the clip
                image_clips.append(img_clip)
                
        # Apply fade in and fade out transitions between consecutive clips
        for i in range(len(image_clips) - 1):
            if image_clips[i] is not None and image_clips[i + 1] is not None:  # Ensure neither clip is None
                print(f"Applying fade transition between clip {i} and clip {i + 1}")
                # Use the static method to add fading transitions between clips
                transition_clip = VideoTransitions.add_fadein_and_fadeout(image_clips[i], image_clips[i + 1])
                final_clips.append(transition_clip)

        # If there's a remaining clip without a pair, just append it as it is
        if len(image_clips) > len(final_clips):
            final_clips.append(image_clips[-1])  # Add the last clip without transition

        # Combine all clips into one video
        combined_clip = concatenate_videoclips(final_clips,method="compose")
        for clip in image_clips:  # Close individual clips if they're not needed anymore
            clip.close()
        print("Transitions applied.")
        return combined_clip

    # def apply_effects_transitions(self, images):
    #     print("Applying effects and transitions...")
    #     final_clips = []

    #     effect_methods = get_effect_methods()
    #     transition_methods = get_transition_methods()

    #     for i, image_path in enumerate(images):
    #         print(f"Applying effects to image {i}: {image_path}")
    #         effect_method = random.choice(effect_methods)
    #         video_effect_instance = VideoEffects(image_path)
    #         effect_func = getattr(video_effect_instance, effect_method)
    #         image_clip_with_effect = effect_func()
    #         final_clips.append(image_clip_with_effect)

    #     final_video_clips = [final_clips[0]]
    #     for i in range(1, len(final_clips)):
    #         print(f"Applying transition between clip {i-1} and clip {i}")
    #         transition_method = random.choice(transition_methods)
    #         transition_func = getattr(VideoTransitions, transition_method)
    #         transition_clip = transition_func(final_video_clips[-1], final_clips[i])
    #         final_video_clips.append(transition_clip)

    #     combined_clip = concatenate_videoclips(final_video_clips)
    #     print("Effects and transitions applied.")
    #     return combined_clip

    def create_video(self):
        # audio = None  # Initialize audio variable
        try:
            print("Creating video...")
            edited_images = self.apply_transitions(self.images)
            total_video_duration = min(60, edited_images.duration)  # seconds, but not exceeding the actual video duration
            # Load and set the audio of the final video cli
            audio_clip = AudioFileClip(self.song).subclip(0, total_video_duration)  # Use only the first 60 seconds of the audio or the actual video duration
            print("Playing audio for confirmation...")
            # audio_clip.preview()
            final_clip = edited_images.set_audio(audio_clip)
            final_clip.set_audio(audio_clip)

            # final_clip.preview()
            print("Video creation successful.")
        except Exception as e:
            print(f"Error creating video: {e}")
        return final_clip

    def save_video(self, video_clip, count):
        try:
            if not video_clip:
                print("No video clip to save.")
                return

            print("Saving video...")
            # Modify the filename to include the count
            filename = f"output_video_{count}.mp4"
            save_path = os.path.join(self.root_dir, 'Generated Videos', self.selected_category, filename)
            # Ensure the directory exists before trying to save
            print(f"Does the final video have audio? {'No' if video_clip.audio is None else 'Yes'}")
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            video_clip.write_videofile(save_path, codec='libx264', audio_codec='aac', fps=24)
            print(f"Video saved successfully at {save_path}.")
        except Exception as e:
            traceback.print_exc()  # This provides more details than just printing the error
            print(f"Error saving video: {e}")
        finally:
            if video_clip:  # Ensure to close the video clip if it exists
                video_clip.close()  

if __name__ == "__main__":
    for i in range(5):  # 'i' will go from 0 to 4
        print(f"Script iteration started. Iteration: {i+1}")
        video_creator = VideoCreator()
        video_creator.select_random_files()
        final_clip = None  # Initialize final_clip to ensure it's defined
        if video_creator.song and video_creator.images:
            final_clip = video_creator.create_video()
        if final_clip:
            video_creator.save_video(final_clip, i+1)  # Pass 'i+1' as the count to save_video
        print(f"Script iteration finished. Iteration: {i+1}")


