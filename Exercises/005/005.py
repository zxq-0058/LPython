"""
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""
import shutil

from PIL import Image
import os


# 有关文件系统的操作,使用os
# 如何获得一个目录下面的所有文件是关键
Path = './imgs'
images = os.listdir(Path)
W = 1136
H = 640
MAX_SIZE = (W, H)
# 注意:图片的尺寸和分辨率都是描述图片的清晰度
def Pictures_Resize():
    for image in images:
        image = Path + '/' + image #获得完整图片名字
        img = Image.open(f"{image}") #打开图片
        # img = img.resize((W, H))
        img.thumbnail(MAX_SIZE)
        img.save(f"{image}", 'jpeg') #保存

    print("Finished!")

Pictures_Resize()


