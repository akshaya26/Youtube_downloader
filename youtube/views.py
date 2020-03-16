from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
from pytube  import YouTube # for video
import moviepy.editor as mp #used to convert video to audio
import os
import re

#Each time an audio or video request is generated below function is called.
#for audio the actual videofile is downloaded and then converted to audio using moiepy.editor and renamed as .mp3

def download(request):

    if (request.method=="POST"):
        print("video")
        # link is the name of input type url
        link = request.POST.get('link','nolink')

        print(link)

        # obtaining downloads path
        save_path=os.path.expanduser("~") + '/Downloads'

        try:
            ob = YouTube(link)
        except:
            print('error')

        # returns title of video
        print(ob.title)

        # returns all streams of video and audio. from that first videostram is chosen
        mp4 = ob.streams.first()
        print(mp4)
        print(str(ob.title))

        #video is saved with titleof video to specified path.However saved filename contains spaces.Below block is to create an
        #  _ seperated filename
        # lst = str(ob.title).split()
        # print(lst)
        # name = ""
        # for i in range(int(len(lst))):
        #     name = name + lst[i] + "_"
        # print(name)

        #check if youtube_downloader file already exists

        filelst=[]


        #filenames to be saved as youtube_downloader(1).mp4,youtube_downloader(2).mp4
        for file in os.listdir(save_path):
            if (file.startswith("youtube_downloader") and file.endswith(".mp4")):
                filelst.append(file)
        print(filelst)
        if (len(filelst) == 0):
            name = "youtube_downloader(0)"
        else:
            repeatregex = re.compile(r'\([0-9]+\)')
            repeatval = repeatregex.search(filelst[-1])
            count = repeatval.group()
            if (count == None):
                name = "youtube_downloader(1)"
            else:
                filecount = re.compile(r'[\d]+').search(count).group()
                name = "youtube_downloader(" + str(int(filecount) + 1) + ")"





            #dowloads video altered filename to specified output path
        mp4.download(output_path = save_path,filename = name)
        print("File downloaded")

        #if request is generated for .mp3 download
        if(request.POST.get('type')=="audio"):
            print("audio")
            path = save_path + '\\' + name + ".mp4" #file name
            newname = os.path.join(save_path, name + ".mp3") #.mp3 file
            audio = mp.AudioFileClip(path)
            audio.write_audiofile(newname)
            #for deleteing the actual download .mp4 file
            os.remove(path)

    return render(request,'youtube/youtube_index.html')