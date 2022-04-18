import os
import sys

input = sys.argv
folders = int(input[1].replace("--folders=", ""))
files = int(input[2].replace("--files=", ""))
file_size = int(input[3].replace("--filesize=", "")) * 1000
path1 = os.path.join(os.getcwd(), "output")

os.makedirs(path1)
os.chdir(path1)

for i in range(1, folders + 1):
    path = os.path.join(path1, "folder" + str(i))
    os.makedirs(path)
    os.chdir(path)

    for k in range(1, files + 1):
        f = open("file" + str(k), "wb")
        f.seek(file_size)
        f.write(b"\0")
        f.close()
