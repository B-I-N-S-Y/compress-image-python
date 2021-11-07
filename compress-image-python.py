#refer: https://understandingdata.com/python-for-seo/how-to-compress-images-in-python/
#refer: https://www.runoob.com/python/os-walk.html
# python3 -m pip install --upgrade pip
# python3 -m pip install pillow

from PIL import Image
import PIL
import os
import glob
import time


gogopath = os.getcwd()



images = [file for file in os.listdir() if file.endswith(('jpeg', 'png' )) or "example" in file]
print(images)


def compress_images(directory=False, quality=30):
    # 1. If there is a directory then change into it, else perform the next operations inside of the 
    # current working directory:
    if directory:
        os.chdir(directory)

    # 2. Extract all of the .png and .jpeg files:
    files = os.listdir()

    # 3. Extract all of the images:
    images = [file for file in files if file.endswith(('jpeg', 'png'))]

    # 4. Loop over every image:
    for image in images:
        print(image)

        # 5. Open every image:
        img = Image.open(image)

        # 5. Compress every image and save it with a new name:
        img.save("Compressed_"+image, optimize=True, quality=quality)


#compress_images(directory="/Users/sy/Downloads/HADA Comestic/Lotion/ Botanical Skin 500ml",quality=10)

for root, dirs, files in os.walk(".", topdown=False):
    for name in dirs:
        
        directory = os.path.join(root,name)
        print(directory)
        compress_images(directory=directory,quality=30)
        os.chdir(gogopath)

