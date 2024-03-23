from moviepy.editor import concatenate_videoclips, CompositeVideoClip
from moviepy.video.fx.all import fadein, fadeout
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate

class VideoTransitions:

    @staticmethod
    def add_fadein_and_fadeout(video1, video2, duration=1):
        # Apply fadeout to the end of the first clip and fadein to the start of the second clip
        first_clip = fadeout(video1, duration)
        second_clip = fadein(video2, duration)
        # Concatenate the clips with overlapping fades
        return concatenate_videoclips([first_clip, second_clip], padding=-duration, method="compose")

    
    # @staticmethod
    # def wipe_transition(video1, video2, duration=1):
    #     if video1 is None or video2 is None:
    #         raise ValueError("One of the video clips is None")

    #     # Define the custom effect function
    #     def custom_wipe(get_frame, t):
    #         frame = get_frame(t)
    #         wipe_length = int(min(t / duration, 1) * video2.size[0])
    #         new_frame = video2.get_frame(t)
    #         if t < duration:
    #             frame[:, :wipe_length] = new_frame[:, :wipe_length]
    #         return frame

    #     # Apply custom wipe effect to the second video over its duration
    #     second_clip_wipe = video2.fl(custom_wipe)
    #     second_clip_wipe = second_clip_wipe.set_start(video1.duration - duration).set_duration(video2.duration)

    #     # Combine the first video with the modified second video
    #     return CompositeVideoClip([video1, second_clip_wipe.set_pos('center')], size=video1.size)


    #     # Apply custom wipe effect to the second video over its duration
    #     second_clip_wipe = video2.fl(custom_wipe, apply_to=['mask', 'video'])
    #     second_clip_wipe = second_clip_wipe.set_start(video1.duration - duration).set_duration(duration)
    
    # @staticmethod
    # def slide_transition(video1, video2, direction='left', duration=1):
    #     # Here, 'translate' should be replaced by actual sliding logic if not available as is.
    #     # This is a simplistic representation assuming such a function exists.
    #     if direction == 'left':
    #         final_clip = video1.set_end(duration).set_position(('right',0))
    #         return CompositeVideoClip([final_clip, video2.set_position(('left', 0))], size=video1.size)
    #     # Add logic for other directions if necessary

    # @staticmethod
    # def dissolve_transition(video1, video2, duration=1):
    #     first_clip = video1.crossfadeout(duration)
    #     second_clip = video2.crossfadein(duration)
    #     return concatenate_videoclips([first_clip, second_clip], padding=-duration, method="compose")
    
    # @staticmethod
    # def zoom_transition(video1, video2, duration=1, zoom_factor=4):
    #     # Zoom in on the end of the first clip
    #     final_frame = video1.to_ImageClip(video1.duration)
    #     zoom_in = final_frame.resize(lambda t: 1 + zoom_factor * (1 - t / duration))  # Zoom in
    #     zoom_in = zoom_in.set_duration(duration)

    #     # Zoom out from the start of the second clip
    #     start_frame = video2.to_ImageClip(0)
    #     zoom_out = start_frame.resize(lambda t: 1 + zoom_factor * (t / duration))  # Zoom out
    #     zoom_out = zoom_out.set_duration(duration)

    #     # Combine the two clips
    #     final_clip = concatenate_videoclips([video1, zoom_in, zoom_out, video2], method="compose")
    #     return final_clip


    # @staticmethod
    # def spin_transition(video1, video2, duration=1, spin_cycles=2):
    #     # Spin out the first clip
    #     spin_out = video1.fl_time(lambda t: rotate(video1, t/duration * 360 * spin_cycles))
    #     spin_out = spin_out.set_end(duration)

    #     # Spin in the second clip
    #     spin_in = video2.fl_time(lambda t: rotate(video2, (1 - t/duration) * 360 * spin_cycles))
    #     spin_in = spin_in.set_start(video1.duration).set_duration(duration)

    #     # Combine the two clips
    #     final_clip = concatenate_videoclips([video1, spin_out, spin_in, video2], method="compose")
    #     return final_clip

    # @staticmethod
    # def heartbeat_transition(video1, video2, duration=1, beat_times=2):
    #     # Define the heartbeat effect
    #     def heartbeat_effect(clip, times, duration):
    #         beats = []
    #         for i in range(times):
    #             beat_duration = duration / (2 * times)
    #             # Create a heartbeat effect by increasing and decreasing the size.
    #             # Note: MoviePy's resize effect is applied to the entire clip and does not accept 'apply_to'.
    #             beat_increase = clip.fx(resize, lambda t: 1 + 0.1 if (t // beat_duration) % 2 == 0 else 1)
    #             beat_decrease = clip.fx(resize, lambda t: 1 - 0.1 if (t // beat_duration) % 2 == 1 else 1)
    #             # Set duration for each part of the heartbeat.
    #             beat_increase.set_duration(beat_duration)
    #             beat_decrease.set_duration(beat_duration)
    #             # Add the increase and decrease effects alternatively.
    #             beats.append(beat_increase)
    #             beats.append(beat_decrease)
    #         # Combine all beats into a single clip.
    #         return concatenate_videoclips(beats, method="chain")

    #     # Apply heartbeat to the end of the first clip and start of the second.
    #     heartbeat_end = heartbeat_effect(video1.subclip(max(0, video1.duration - duration), video1.duration), beat_times, duration)
    #     heartbeat_start = heartbeat_effect(video2.subclip(0, min(duration, video2.duration)), beat_times, duration)

    #     # Combine the two clips with heartbeat effects applied at their junction.
    #     final_clip = concatenate_videoclips([video1, heartbeat_end, heartbeat_start, video2], method="compose")
    #     return final_clip



    


