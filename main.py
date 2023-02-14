import subprocess
import os
from pytube import YouTube

ACTUAL_DIR = os.getcwd()

def downloadAudio(link):
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    destination = '.'

    out_file = video.download(output_path=destination)

    base, ext = os.path.splitext(out_file)

    new_file = base + '.mp3'

    os.rename(out_file, new_file)

    converMp3ToWav(new_file)

    print(f'{yt.title} has been successfully downloaded')


def converMp3ToWav(path):
    sound = getAudioNameFromAudioPath(path)
    print(sound)
    destination = sound.replace('.mp3', '.wav')

    subprocess.call(['ffmpeg', '-i', sound,destination])

def getAudioNameFromAudioPath(audioPath):
    audioName = audioPath.replace(f'{ACTUAL_DIR}/', '')
    return audioName

urls = [
    'https://youtu.be/dWrppMcbtd0',
    'https://youtu.be/CW-aFR1UZj4',
    'https://youtu.be/BZt6m1LAwR4',
    'https://youtu.be/OZHEO7HGhTQ',
    'https://youtu.be/GmKO-ekc_EM',
    'https://youtu.be/iI8mUCYUBgk',
    'https://youtu.be/sTOWpLpKjSI',
    'https://youtu.be/bhIvPGbSUgA',
    'https://youtu.be/lZMz3SITQNs'
]

for url in urls:
    downloadAudio(url)

print('\nDone!')
