import os.path

def fileChecker(dirName):
    if os.path.isdir(os.path.expanduser("~/Desktop/YoutubeDumper/{0}".format(dirName))):
        return True
    else:
        return False

def fileCreator(dirName):
    print("~/Desktop/{0}".format(dirName))
    os.mkdir(os.path.expanduser("~/Desktop/YoutubeDumper/{0}".format(dirName)))

def rootChecker():
    if os.path.isdir(os.path.expanduser("~/Desktop/YoutubeDumper/")):
        return True
    else:
        os.mkdir(os.path.expanduser("~/Desktop/YoutubeDumper/"))

def rootCreator():
    os.mkdir(os.path.expanduser("~/Desktop/YoutubeDumper/"))