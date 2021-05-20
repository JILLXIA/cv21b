'''
predict.py有几个注意点
1、该代码无法直接进行批量预测，如果想要批量预测，可以利用os.listdir()遍历文件夹，利用Image.open打开图片文件进行预测。
具体流程可以参考get_dr_txt.py，在get_dr_txt.py即实现了遍历还实现了目标信息的保存。
2、如果想要进行检测完的图片的保存，利用r_image.save("img.jpg")即可保存，直接在predict.py里进行修改即可。 
3、如果想要获得预测框的坐标，可以进入yolo.detect_image函数，在绘图部分读取top，left，bottom，right这四个值。
4、如果想要利用预测框截取下目标，可以进入yolo.detect_image函数，在绘图部分利用获取到的top，left，bottom，right这四个值
在原图上利用矩阵的方式进行截取。
5、如果想要在预测图上写额外的字，比如检测到的特定目标的数量，可以进入yolo.detect_image函数，在绘图部分对predicted_class进行判断，
比如判断if predicted_class == 'car': 即可判断当前目标是否为车，然后记录数量即可。利用draw.text即可写字。
'''
from PIL import Image
import json
from yolo import YOLO
import os
yolo = YOLO()
path = './dataHomework/test'
objectid = 1
resultDic = {}
with open("./test_result.json","w") as f:
    for file in os.listdir(path):
        file_path = os.path.join(path,file)
        #print(file_path)
        image = Image.open(file_path)
        object_list = yolo.detect_image(image)
        #print(image.size)
        if not isinstance(object_list, list):
            object_list = []
        #print(object_list)
        object_dict = {}
        for i in object_list:
            # print(type(i[2]))
            object_dict.update({str(objectid):{"category":str(i[0],encoding='utf-8'),"bbox":[int(i[2]),int(i[1]),int(i[4]),int(i[3])]}})
            objectid = objectid + 1

        resultDic.update({file:{"height":image.size[1],"width":image.size[0],"depth":3,"objects":object_dict}})
        # print(resultDic)
    json.dump(resultDic, f)
'''
while True:
    img = input('Input image filename:')
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        continue
    else:
        r_image,object_list = yolo.detect_image(image)
        print(object_list)
        r_image.show()
'''