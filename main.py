import moviepy.editor

def get_file_name(file):
    retourn=""
    for arg in range(len(str(file).split("/")[len(str(file).split("/"))-1].split("."))-2):
        retourn+=str(file).split("/")[len(str(file).split("/"))-1].split(".")[arg]+"."
    return retourn+str(file).split("/")[len(str(file).split("/"))-1].split(".")[len(str(file).split("/")[len(str(file).split("/"))-1].split("."))-2]

def convertor_replyer(file, max_time, types):
    if str(types).startswith("audio"):
        clip = moviepy.editor.AudioFileClip(file)
        clip_list = []
        i=0
        while i+clip.duration < max_time:
            clip_list.append(clip)
            i+=clip.duration
            print((i/max_time)*100,"%")
        print("100%")
        moviepy.editor.concatenate_audioclips(clip_list).write_audiofile(get_file_name(file)+"[10h].mp3")
    else:
        clip = moviepy.editor.VideoFileClip(file)
        clip_list = []
        i=0
        while i+clip.duration < max_time:
            clip_list.append(clip)
            i+=clip.duration
            print((i/max_time)*100,"%")
        print("100%")
        moviepy.editor.concatenate_videoclips(clip_list).write_videofile(get_file_name(file)+"[10h].mp4", codec='libx264')

def convertor_mp4_to_mp3(file):
    moviepy.editor.VideoFileClip(file).audio.write_audiofile(get_file_name(file)+".mp3")

import youtube_dl
def youtube_video_downloader(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


#command excutor
import argparse
from distutils.util import strtobool
parser = argparse.ArgumentParser(description="make 10 hours of any video or audio")
import_group = parser.add_mutually_exclusive_group()
import_group.add_argument("-y", "--youtube", help="import from youtube url")
import_group.add_argument("-f", "--file", help="import from file")
parser.add_argument("-a", "--audio", action='store_true' , help="export audio")
args = parser.parse_args()

import os
if __name__ == "__main__":
    if args.youtube:
        files_list = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files_list:
            if not f.endswith(".py"):
                os.remove(f)
        youtube_video_downloader(args.youtube)
        files_list = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files_list:
            if not str(f).endswith(".py"):
                print(str(f))
                if args.audio == True:
                    convertor_replyer(f, 36000, "audio")
                else:
                    convertor_replyer(f, 36000, "video")
    if args.file:
        files_list = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files_list:
            if args.file == f:
                if args.audio == True:
                    convertor_replyer(f, 36000, "audio")
                else:
                    convertor_replyer(f, 36000, "video")