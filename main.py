import baseController
import os


choice = "s"
while (choice.lower() == "s"):
    baseController.baseControllerMain()
    choice = str(input("Continuar?(s/n): "))
path = os.path.expanduser("~/Desktop/YoutubeDumper/")
path = os.path.realpath(path)
os.startfile(path)