# coding=utf-8

import os

import random
import json

import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
from PIL import Image

DIR = './dataHomework/'
# Read the json annotation file.
filedir = DIR + 'train/train.json'
annos = json.loads(open(filedir).read())# 将已编码的 JSON 字符串解码为 Python 对象
classDic = {}
count = 1


def classDicSize():
    return len(classDic)
isChangeLine  = 1
classContext = ''

for (key, value) in annos.items():
    for (key1, value1) in annos[key]['objects'].items():
        if (value1['category'] not in classDic.keys()):
            classDic.update({value1['category']: count})
            # fw.writelines(value1['category']+'\n')
            classContext += value1['category'] + '\n'
            count = count + 1

classContext = classContext.strip('\n')
with open("./model_data/homework_class.txt","w") as fw:
    fw.write(classContext)
#print(classDic)
resultContext = ''
for (key, value) in annos.items():
    picName = DIR + 'train/train/' + key
    tmpStr = picName + ' '
    for (key1, value1) in annos[key]['objects'].items():
        category = str(classDic[value1['category']])
        xmin = str(value1['bbox'][0])
        ymin = str(value1['bbox'][1])
        xmax = str(value1['bbox'][2])
        ymax = str(value1['bbox'][3])
        '''
        if value1['bbox'][0]<0 or value1['bbox'][1]<0 or value1['bbox'][2]>annos[key]['height'] or value1['bbox'][3]>annos[key]['width'] \
                or value1['bbox'][2]>annos[key]['width'] or value1['bbox'][3]>annos[key]['height']:
            print(xmin + ',' + ymin + ',' + xmax +',' + ymax +',' + category + ' ' + str(annos[key]['width'])+ ' '+str(annos[key]['height']))
            if value1['category'] in classDic:
                print('enter')
                classDic.pop(category)
        else:
        '''
        tmpStr += xmin + ',' + ymin + ',' + xmax + ',' + ymax + ',' + category + ' '
    tmpStr += '\n'
    resultContext += tmpStr

resultContext = resultContext.strip('\n')
with open("result.txt","w") as f:
        f.write(resultContext)

