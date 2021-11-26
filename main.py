import baseController

choice = "s"
while (choice.lower() == "s"):
    baseController.baseControllerMain()
    choice = str(input("Continuar?(s/n): "))