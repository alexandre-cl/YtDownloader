from pytube import YouTube
import fileController

import os

def baseControllerMain():
    inputedType = '0'
    dirNames = {
    'vid' : 'Yt-Videos',
    'aud' : 'Yt-Audios'
    }
    while (inputedType != "1" and inputedType != "2"):
        os.system('cls')
        inputedType = str(input("1-Vídeo \n2-Áudio\n> "))


    if(inputedType == "1"):
        dirNameController = "vid"
    elif(inputedType == "2"):
        dirNameController = "aud"

    fileController.rootChecker()
    fileExist = fileController.fileChecker(dirNames.get(dirNameController))

    if(fileExist == False):
        fileController.fileCreator(dirNames.get(dirNameController))
    else:
        print("File " + dirNames.get(dirNameController) + " already exist in the system.")

    link = input("Link:  ")
    yt = YouTube(link)
    pathFile = os.path.expanduser("~/Desktop/YoutubeDumper/{0}".format(dirNames.get(dirNameController)))
    if(type == '1'):
        ys = yt.streams.get_highest_resolution()
        print("Baixando...")
        ys.download(pathFile)
        print("Download completo!!")
    else:
        t = yt.streams.filter(only_audio=True)
        print("Baixando...")
        t[0].download(pathFile)
        print("Download completo!!")