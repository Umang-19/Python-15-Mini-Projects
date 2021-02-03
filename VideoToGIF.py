from moviepy.editor import *

clip = VideoFileClip("PythonHub.mp4")

clip.write_gif("newfile.gif")