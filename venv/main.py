import tkinter as tk
import requests
import re
import subprocess
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs


def handle_submit(user_submitted_url):
    base_source_url = find_base_source_url(user_submitted_url)
    combine_video_and_audio(base_source_url + "/")


def find_base_source_url(url):
    data = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.137 Safari/537.36 Vivaldi/2.7.1628.33"})
    prettified_page = bs(data.content).prettify()
    end_index = re.search("data-url=\"", prettified_page).span()[1]

    return prettified_page[end_index:].split("\"")[0]


def combine_video_and_audio(base_source_url):
    video_url = find_video(base_source_url)
    print("result:" + video_url)
    video = urlopen(video_url)
    with open("video.mp4", 'wb') as f:
        f.write(video.read())

    audio_url = find_audio(base_source_url)
    if (audio_url != ""):
        audio = urlopen(audio_url)
        with open("audio.mp4", 'wb') as f:
            f.write(audio.read())
        subprocess.call('ffmpeg -i video.mp4 -i audio.mp4 -c copy output.mp4', shell=False)


def find_video(base_source_url):
    resolutions = ["DASH_1080.mp4", "DASH_1080", "DASH_720.mp4", "DASH_720", "DASH_480.mp4", "DASH_480", "DASH_360.mp4",
                   "DASH_360", "DASH_240.mp4", "DASH_240"]
    for resolution in resolutions:
        videoUrl = base_source_url + resolution
        request = requests.head(videoUrl)
        print("video url: " + videoUrl)
        if request.status_code == 200:
            return videoUrl
    return ""


def find_audio(url):
    options = ["audio", "DASH_audio.mp4"]
    for option in options:
        audioUrl = url + option
        request = requests.head(audioUrl)
        if request.status_code == 200:
            return audioUrl

    return ""


def set_up_gui():
    window = tk.Tk(className='Sup faggot')
    window.geometry("300x50")
    tk.Label(window, text="plebbit url").grid(row=0)
    e1 = tk.Entry(window)

    e1.grid(row=0, column=1, pady=10)

    tk.Button(window, text='download', command=lambda: handle_submit(e1.get())).grid(row=0, column=2, pady, padx=10)

    window.mainloop()


def run():
    set_up_gui()


run()
