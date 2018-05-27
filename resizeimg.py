import numpy as np
from PIL import Image
import argparse
import os

def mkdir(path):
    folder = os.path.exists(path)  
    if not folder:
        os.makedirs(path)

def resize(inputs,outputs,t,w,h):
    mkdir(outputs)
    pattern = "%d/%d (%.2f%%)"
    s = ""
    j = 0
    l = os.listdir(inputs)
    for i in l:
        j += 1
        s = pattern%(j,len(l),float(j)/float(len(l))*100)
        print(s)
        img = Image.open(inputs+"\\"+i)
        o = img.resize((w, h),Image.ANTIALIAS)
        o.save(outputs+"\\"+i, t)

def main():
    parser = argparse.ArgumentParser(prog='ImgResize',description='图片大小批量修改by lzy2002 site:lzy2002.com')
    parser.add_argument('-i','--inputs',help='输入文件所在目录',required=True)
    parser.add_argument('-o','--outputs',help='输出文件所在目录',default='$[inputs]\\resize')
    parser.add_argument('-t','--type',help='输出文件类型',default='jpeg')
    parser.add_argument('-W','--width',help='输出宽度',default=1920)
    parser.add_argument('-H','--height',help='输出高度',default=1080)
    args = parser.parse_args()
    resize(args.inputs,args.outputs.replace('$[inputs]',args.inputs),args.type,int(args.width),int(args.height))

if __name__ == '__main__':
    main()

