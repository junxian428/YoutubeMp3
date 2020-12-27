import youtube_dl
import subprocess
def run():
    video_url=input('Please Enter Youtube URL:')
    video_info = youtube_dl.YoutubeDL().extract_info(video_url,download=False)
    filename= f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
        'postprossors':[{
          'key':'FFmpegExtractAudio',
          'preferredcodec':'mp3',
          'preferredquality':'192',
        }]
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    subprocess.call(['open',filename])
if __name__=='__main__':
    run()
