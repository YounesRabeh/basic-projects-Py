from pytube import YouTube, streams
import os
from urllib.parse import urlparse, parse_qs
from contextlib import suppress
from pathlib import Path

SAVE_PATH = "/home/YOUNES/Desktop/YOUNES/Python Projects/basic-projects-Py/YouTubeDownloader/Downloads"

# TODO: audio, streams , recent one, overwrite, dim options
# add the file name , the audio , the over write, 
def main(my_link, _res, _file_name, _only_audio):
    global yt
    try:
        yt = YouTube(my_link)
        if _file_name == "":
            _file_name = yt.title
        the_video = yt.streams.filter(res=_res, progressive=True, only_audio=_only_audio).first()
        the_video.download(SAVE_PATH)
        print(yt.title)
        #my_path = Path(f'Downloads/{yt.title}').absolute()
        #print(my_path)
        #os.rename(my_path, _file_name + '.mp4')

    except:
        print("Some Error!")
        #exit()

    print('Task Completed!') 

# add the export settings, quality, frames , audio or mute, play list, shorts

def get_yt_id(url, ignore_playlist=False):
    query = urlparse(url)
    if query.hostname == 'youtu.be': return query.path[1:]
    if query.hostname in {'www.youtube.com', 'youtube.com', 'music.youtube.com'}:
        if not ignore_playlist:
            # use case: get playlist id not current video in playlist
            with suppress(KeyError):
                return parse_qs(query.query)['list'][0]
        if query.path == '/watch': return parse_qs(query.query)['v'][0]
        if query.path[:7] == '/watch/': return query.path.split('/')[1]
        if query.path[:7] == '/embed/': return query.path.split('/')[2]
        if query.path[:3] == '/v/': return query.path.split('/')[2]
    # returns None for invalid YouTube url    