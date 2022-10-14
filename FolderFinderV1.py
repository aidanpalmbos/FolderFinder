import os
import subprocess

print("Hello " + os.getlogin())
print("Input new folder: ")

while(True):

    file = input()

    if "-" in file:
        secondSet= file[0:file.find("-")]
        firstSet = secondSet[:-3]

    else:
        firstSet = file[:-3]
        secondSet = file

    file_path = "Z:\\Adv_Jobs\\" + str(firstSet) + "xxx\\" + str(secondSet) + "\\" + file

    print("Opening: " + file_path)

    try:
        subprocess.run(['explorer', os.path.normpath(file_path)])
    except:
        print("subprocess.run did not work. Make sure you typed in the file correctly. If you did, something unrelated went wrong.")

    print(" ")
    print("Input another folder: ")
