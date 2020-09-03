import os
import imageio
from moviepy.editor import *
from moviepy.audio.tools.cuts import find_audio_period
from moviepy.video.tools.cuts import find_video_period
import time

if not os.path.exists("3inPlm.webm"):
    os.system("youtube-dl -f 'bestvideo' ATcqaqwQXF0 -o 3inPlm")  

clip = (VideoFileClip("./3inPlm.webm", audio=False)
    .subclip((1,25.7),(1,27)))    

clip.write_gif('3inPlm.gif')
