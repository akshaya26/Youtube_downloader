from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
from pytube  import YouTube # for video
import moviepy.editor as mp #used to convert video to audio
import os
import re
import youtube_dl

#Each time an audio or video request is generated below function is called.
#for audio the actual videofile is downloaded and then converted to audio using moiepy.editor and renamed as .mp3

def download(request):

    if (request.method=="POST"):
        print("video")
        # link is the name of input type url
        link = request.POST.get('link','nolink')

        print(link)



        # simulate: skip_download: extract_flat:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'forceurl': True,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])








#*******************************************
        # obtaining downloads path
        # save_path =os.path.join(os.path.join(os.path.expanduser('~')),'Downloads')
        #
        # try:
        #     ob = YouTube(link)
        # except:
        #     print('error')
        #
        # # returns title of video
        # print(ob.title)
        #
        # # returns all streams of video and audio. from that first videostram is chosen
        # mp4 = ob.streams.first()
        #
        #
        # print(str(ob.title))
        #
        # #check if youtube_downloader file already exists(Not required when in production)
        #
        # # filelst=[]
        #
        #
        # #filenames to be saved as youtube_downloader(1).mp4,youtube_downloader(2).mp4
        # # for file in os.listdir(save_path):
        # #     if (file.startswith("youtube_downloader") and file.endswith(".mp4")):
        # #         filelst.append(file)
        # # print(filelst)
        # # if (len(filelst) == 0):
        # #     name = "youtube_downloader(0)"
        # # else:
        # #     repeatregex = re.compile(r'\([0-9]+\)')
        # #     repeatval = repeatregex.search(filelst[-1])
        # #     count = repeatval.group()
        # #     if (count == None):
        # #         name = "youtube_downloader(1)"
        # #     else:
        # #         filecount = re.compile(r'[\d]+').search(count).group()
        # #         name = "youtube_downloader(" + str(int(filecount) + 1) + ")"
        # #dowloads video altered filename to specified output path
        # #mp4.download(output_path = save_path,filename = name)
        #
        #
        # print("File downloaded")
        # # print(save_path + name)
        #
        # #if request is generated for .mp3 download
        #
        # # if(request.POST.get('type')=="audio"):
        # #     print("audio")
        # #     path = save_path + '\\' + name + ".mp4" #file name
        # #     newname = os.path.join(save_path, name + ".mp3") #.mp3 file
        # #     audio = mp.AudioFileClip(path)
        # #     audio.write_audiofile(newname)
        # #     #for deleteing the actual download .mp4 file
        # #     os.remove(path)
        return render(request, 'youtube/youtube_index.html', {'val': True, 'buttonval': False})

    # return render(request,'youtube/youtube_index.html',{'downloadlink' : mp4.url,'val': True,'buttonval':False})

    return render(request,'youtube/youtube_index.html',
                  {'buttonval':True})


def downloadspage(request):
    return HttpResponse("download")
