from PIL import Image
import json
from yoloOld import YOLO
import os
yoloOld = YOLO()
path = './dataHomework/val/val/'
objectid = 1
resultDic = {}

while True:
    img = input('Input image filename:')
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        continue
    else:
        r_image = yoloOld.detect_image(image)
        r_image.show()
        r_image.save("img.jpg")
