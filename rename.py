import numpy as np
from PIL import Image
import argparse
import os


def rename(path,l):
    i = 0
    filelist = os.listdir(path)  #该文件夹下所有的文件（包括文件夹）
    for files in filelist:  #遍历所有文件
        i = i + 1
        Olddir = os.path.join(path, files)
        if os.path.isdir(Olddir):
            continue
        filename = ("%0"+l+"d")%(int(os.path.splitext(files)[0]),)
        filetype = os.path.splitext(files)[1]
        Newdir = os.path.join(path,filename + filetype)
        print("%s==>%s"%(files,filename + filetype))
        os.rename(Olddir, Newdir)  #重命名

def main():
    parser = argparse.ArgumentParser(prog='ImgResize', description='图片名称批量修改by lzy2002 site:lzy2002.com')
    parser.add_argument('-i', '--inputs', help='输入文件所在目录', required=True)
    parser.add_argument('-l', '--len', help='补齐长度', default=3)
    args = parser.parse_args()
    rename(args.inputs,str(args.len))

if __name__ == '__main__':
    main()