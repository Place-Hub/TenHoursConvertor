import moviepy.editor

def get_file_name(file):
    if str(file).endswith('.mp4'):
        return str(file).replace(".mp4", "")
    if str(file).endswith('.mp3'):
        return str(file).replace(".mp4", "")
        
def convertor_replyer(file, max_time):
    if str(file).endswith(".mp4"):
        
        clip = moviepy.editor.VideoFileClip(file)
        clip_list = []
        i=0
        while i+clip.duration < max_time:
            clip_list.append(clip)
            i+=clip.duration
            print((i/max_time)*100,"%")
        print("100%")
        moviepy.editor.concatenate_videoclips(clip_list).write_videofile(get_file_name(file)+"[10].mp4", codec='libx264')
    if str(file).endswith(".mp3"):
        clip = moviepy.editor.AudioFileClip(file)
        clip_list = []
        i=0
        while i+clip.duration < max_time:
            clip_list.append(clip)
            i+=clip.duration
            print((i/max_time)*100,"%")
        print("100%")
        moviepy.editor.concatenate_audioclips(clip_list).write_videofile(get_file_name(file)+"[10].mp3", codec='libx264')

#def convertor_mp3_to_mp4(file):
#    moviepy.editor.VideoFileClip(file).audio.write_audiofile(get_file_name+".mp3")

def convertor_mp4_to_mp3(file):
    moviepy.editor.VideoFileClip(file).audio.write_audiofile(get_file_name(file)+".mp3")

convertor_mp4_to_mp3("3s.mp4")